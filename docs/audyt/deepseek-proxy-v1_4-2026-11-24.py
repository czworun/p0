#!/usr/bin/env python3
# PROXY v1.4 (wersja 2, poprawiona) — MVP-02 rachunek zerowy, kroki 3-5 pod bind v1.4
# Autor: DeepSeek 2026-11-24. SHA-256 tego pliku: do nadania przez warsztat przy odbiorze (B3 receipt).
# Poprawki v1->v2: literowka TAU-MALE-NIER, n_steps=mult*4000 (krok zamrozony T_SK/4000),
#                  H_t z formuly zamknietej (nie hardcoded), sanity H_t na 20 cyfr.
# Wymagania: Python 3.10+, mpmath >= 1.3.
# Arytmetyka: mpmath dps=60, "zaokraglenia NA ZEWNATRZ" przez PAD=1e-55.

import mpmath as mp
import sys, time, math

mp.mp.dps = 60
PAD = mp.mpf('1e-55')
EPS_CROSS = mp.mpf('1e-55')
HALF = mp.mpf(1) / 2
THIRD = mp.mpf(1) / 3
TWOTHIRDS = mp.mpf(2) / 3

SQ5 = mp.sqrt(5)
OMEGA = [mp.sqrt(3 - SQ5), mp.sqrt(2), mp.sqrt(3), SQ5, mp.sqrt(3 + SQ5)]
SECTORS = [
    ('T1g', mp.mpf(3), 3 - SQ5,  SQ5),
    ('H_u', mp.mpf(5), mp.mpf(2), mp.mpf(1)),
    ('G_g', mp.mpf(4), mp.mpf(3), mp.mpf(0)),
    ('G_u', mp.mpf(4), mp.mpf(5), mp.mpf(-2)),
    ('T2g', mp.mpf(3), 3 + SQ5, -SQ5),
]
T_SK = 2 * mp.pi / OMEGA[0]

def u_d(theta, d):
    if d == 0: return mp.mpf(1)
    if d == 1: return theta / 3
    if d == 2: return (theta**2 - 3) / 6
    if d == 3: return (theta**3 - theta**2 - 5*theta + 3) / 6
    if d == 4: return (theta**4 - 2*theta**3 - 5*theta**2 + 8*theta) / 6
    if d == 5: return (theta**5 - 2*theta**4 - 7*theta**3 + 10*theta**2 + 10*theta - 6) / 6
    raise ValueError(f"invalid d={d}")

def g_surface(d):
    return [ (m_a / 19) * u_d(theta_a, d) for (_, m_a, _, theta_a) in SECTORS ]

def g_interior(d):
    g_srf = g_surface(d)
    return [ (19 * lambda_a / 60) * g_srf[a] for a, (_, _, lambda_a, _) in enumerate(SECTORS) ]

def g_vec(d, ch):
    return g_surface(d) if ch == 'surface' else g_interior(d)

def theta_cfg(d, ch, factor=HALF):
    g = g_vec(d, ch)
    return factor * sum(abs(g_a) for g_a in g)**2

def udzial(t, d, ch):
    g = g_vec(d, ch)
    return (sum(g[a] * mp.cos(OMEGA[a] * t) for a in range(5)))**2

def H_t_cfg(d, ch):
    g = g_vec(d, ch)
    A = sum(abs(g[a]) * OMEGA[a] for a in range(5))
    B = sum(abs(g[a]) for a in range(5))
    C = sum(abs(g[a]) * OMEGA[a]**2 for a in range(5))
    return 2*A**2 + 2*B*C

def certify_interval(d, ch, t_a, t_b, F_a, F_b, th, ht, max_levels=5):
    """Returns: ('CERT_NONE',None)|('CROSS',t)|('UNCERTAIN',(lo,hi))|
                 ('UNCERTAIN_NO_CROSS',(lo,hi))|('ABSORB_CROSS',(zone_lo, t_cross))"""
    w = t_b - t_a
    if F_a >= th + EPS_CROSS: return ('CROSS', t_a)
    if F_b >= th + EPS_CROSS: return ('CROSS', t_b)
    ub = max(F_a, F_b) + ht * w**2 / 8 + PAD
    if ub < th - EPS_CROSS: return ('CERT_NONE', None)
    if max_levels <= 0: return ('UNCERTAIN', (t_a, t_b))
    t_m = (t_a + t_b) / 2
    F_m = udzial(t_m, d, ch)
    left = certify_interval(d, ch, t_a, t_m, F_a, F_m, th, ht, max_levels - 1)
    if left[0] == 'CROSS': return left
    if left[0] == 'UNCERTAIN':
        right = certify_interval(d, ch, t_m, t_b, F_m, F_b, th, ht, max_levels - 1)
        if right[0] == 'CROSS': return ('ABSORB_CROSS', (left[1][0], right[1]))
        if right[0] == 'UNCERTAIN': return ('UNCERTAIN', (t_a, t_b))
        return ('UNCERTAIN_NO_CROSS', (t_a, t_b))
    return certify_interval(d, ch, t_m, t_b, F_m, F_b, th, ht, max_levels - 1)

def run_a4_window(d, ch, mult, factor=HALF, max_bisek=100):
    """Skan cale okno [0, mult*T_SK] z krokiem T_SK/4000 ZAMROZONYM (per errata (x)).
       Uwaga: re-skan poprzednich okien (nieefektywne, ale poprawne).
       Certyfikaty z poprzednich okien NIE SA re-uzywane (uproszczenie implementacji)."""
    th = theta_cfg(d, ch, factor)
    ht = H_t_cfg(d, ch)
    dt = T_SK / 4000
    n_steps = mult * 4000  # krok zamrozony, liczba krokow rosnie z oknem
    ts = [i * dt for i in range(n_steps + 1)]
    Fs = [udzial(t, d, ch) for t in ts]

    last_certified = ts[0]
    zone_start = None
    crossing_time = None

    for k in range(n_steps):
        t_a, t_b = ts[k], ts[k+1]
        F_a, F_b = Fs[k], Fs[k+1]
        w = t_b - t_a

        ub = max(F_a, F_b) + ht * w**2 / 8 + PAD
        if ub < th - EPS_CROSS:
            last_certified = t_b
            continue

        res = certify_interval(d, ch, t_a, t_b, F_a, F_b, th, ht, 5)
        if res[0] == 'CERT_NONE':
            last_certified = t_b
            continue
        if res[0] == 'CROSS':
            crossing_time = res[1]
            break
        if res[0] in ('UNCERTAIN', 'UNCERTAIN_NO_CROSS'):
            if zone_start is None:
                zone_start = t_a
            continue
        if res[0] == 'ABSORB_CROSS':
            lo_zone, tc = res[1]
            if zone_start is None:
                zone_start = lo_zone
            crossing_time = tc
            break

    if crossing_time is None:
        return {'status': 'PRAWO-OCENZUROWANE', 'tau_lo': None, 'tau_hi': None,
                'flags': ['PRAWO-OCENZUROWANE'], 'mult': mult, 'last_certified': last_certified}

    lo = zone_start if zone_start is not None else last_certified
    hi = crossing_time
    converged = False

    for _ in range(max_bisek):
        if (hi - lo) < mp.mpf('1e-4'):
            converged = True; break
        t_m = (lo + hi) / 2
        F_lo = udzial(lo, d, ch); F_m = udzial(t_m, d, ch)
        res = certify_interval(d, ch, lo, t_m, F_lo, F_m, th, ht, 5)
        if res[0] == 'CERT_NONE': lo = t_m
        elif res[0] == 'CROSS': hi = t_m
        elif res[0] == 'ABSORB_CROSS': hi = res[1][1]
        else: break

    if not converged or (hi - lo) >= mp.mpf('1e-4'):
        return {'status': 'NIEROZSTRZYGALNY-PARCJALNY', 'tau_lo': lo, 'tau_hi': hi,
                'flags': ['BISEKCJA-UNCERTAIN'], 'mult': mult}

    def half_up2(x):
        if x == 0: return mp.mpf(0)
        e = int(mp.floor(mp.log10(abs(x))))
        sc = mp.mpf(10)**(e - 1)
        return mp.nint(x / sc) * sc
    lu, hu = half_up2(lo), half_up2(hi)
    flags = []
    if lu != hu: flags.append('NIEROZSTRZYGNIETY-ROUNDING')
    if hi < mp.mpf('0.01'): flags.append('TAU-MALE')
    elif lo < mp.mpf('0.01') <= hi: flags.append('TAU-MALE-NIER')
    return {'status': 'RESOLVED', 'tau_lo': lo, 'tau_hi': hi, 'width': hi - lo,
            'half_up': (lu, hu), 'flags': flags, 'mult': mult}

def run_config(d, ch, factor=HALF):
    for mult in [1, 2, 4, 8]:
        res = run_a4_window(d, ch, mult, factor)
        if res['status'] in ('RESOLVED', 'NIEROZSTRZYGALNY-PARCJALNY'):
            return res
    return res

def compute_U_b(results):
    U = {}
    for d in [1,2,3,4,5]:
        rs = results.get((d,'surface')); ri = results.get((d,'interior'))
        if not rs or not ri or rs['status'] != 'RESOLVED' or ri['status'] != 'RESOLVED':
            U[d] = None; continue
        s_lo, s_hi = rs['tau_lo'], rs['tau_hi']
        i_lo, i_hi = ri['tau_lo'], ri['tau_hi']
        if i_lo <= 0: U[d] = None; continue
        U[d] = (s_lo / i_hi, s_hi / i_lo)
    return U

def classify_kill(U, tol=mp.mpf('0.01')):
    if U.get(5) is None: return 'NIEROZSTRZYGALNY-PARCJALNY'
    null_vals = [U[d] for d in [1,2,3,4] if U[d] is not None]
    if not null_vals: return 'NIEROZSTRZYGALNY-PARCJALNY'
    max_hi = max(v[1] for v in null_vals); min_lo = min(v[0] for v in null_vals)
    d5_lo, d5_hi = U[5]
    wsp = d5_lo > max_hi * (1 + tol)
    nsp = d5_hi < min_lo * (1 - tol)
    if wsp and not nsp: return 'WSPARTE'
    if nsp and not wsp: return 'NIESPRAWIEDLIWIONE'
    if wsp and nsp: return 'NIEROZSTRZYGALNY-PARCJALNY'
    return 'WYNIK TYPOWY'

def compute_F_r(results):
    null_vals = []
    for d in [1,2,3,4]:
        for ch in ['surface','interior']:
            r = results.get((d, ch))
            if r and r['status'] == 'RESOLVED':
                null_vals.append((r['tau_lo'], r['tau_hi']))
    d5_vals = []
    for ch in ['surface','interior']:
        r = results.get((5, ch))
        if r and r['status'] == 'RESOLVED':
            d5_vals.append((r['tau_lo'], r['tau_hi']))
    null_mid = sorted([(lo+hi)/2 for lo,hi in null_vals])
    if len(null_mid) < 1: return None
    q3_idx = int(math.floor(0.75 * (len(null_mid) - 1)))
    q3 = null_mid[q3_idx]
    count_above = 0; total = 0
    for lo,hi in d5_vals:
        total += 1
        if lo > q3: count_above += 1
    return {'F_r': count_above / max(total,1), 'Q3': q3, 'M': total, 'null_size': len(null_vals)}

REG = {
    (1,'surface'):  (mp.mpf('2.43215'),  mp.mpf('2.43221')),
    (1,'interior'): (mp.mpf('1.11414'),  mp.mpf('1.1142')),
    (2,'surface'):  (mp.mpf('3.66457'),  mp.mpf('3.66463')),
    (2,'interior'): (mp.mpf('3.7245'),   mp.mpf('3.72455')),
    (3,'interior'): (mp.mpf('26.9368'),  mp.mpf('26.9368')),
    (4,'surface'):  (mp.mpf('28.2693'),  mp.mpf('28.2693')),
    (5,'surface'):  (mp.mpf('30.8734'),  mp.mpf('30.8734')),
}

H_T_REF = {
    (1,'surface'):  mp.mpf('2.7799256086419015599'),
    (1,'interior'): mp.mpf('4.4638931847741486532'),
    (2,'surface'):  mp.mpf('1.2627661133724648589'),
    (2,'interior'): mp.mpf('1.4077207528728531348'),
    (3,'surface'):  mp.mpf('1.2627661133724648589'),
    (3,'interior'): mp.mpf('1.4077207528728531348'),
    (4,'surface'):  mp.mpf('2.7799256086419015599'),
    (4,'interior'): mp.mpf('4.4638931847741486532'),
    (5,'surface'):  mp.mpf('12.142544504890295249'),
    (5,'interior'): mp.mpf('15.682603751680600089'),
}

def main():
    t0 = time.time()
    print("=" * 80)
    print("PROXY v1.4 (wersja 2) — MVP-02 rachunek zerowy — DeepSeek 2026-11-24")
    print(f"mpmath dps={mp.mp.dps}; start: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    print(f"T_SK = {mp.nstr(T_SK, 15)}")
    print("=" * 80)

    print("\n[A] Sanity H_t (referencyjne per (aq), 20 cyfr):")
    for k, ref in H_T_REF.items():
        comp = H_t_cfg(*k); dev = abs(comp - ref)
        ok = dev < mp.mpf('1e-15')
        print(f"  {k}: ref={mp.nstr(ref,22)} comp={mp.nstr(comp,22)} dev={mp.nstr(dev,3)} {'OK' if ok else 'FAIL'}")
        if not ok:
            print("STOP: H_t reference mismatch"); return 1

    print("\n[B] Regresja 7 bracketow STAB diag v1.1:")
    reg_results = {}
    for k, (blo, bhi) in REG.items():
        res = run_config(*k, factor=HALF)
        reg_results[k] = res
        if res['status'] != 'RESOLVED':
            print(f"  {k}: status={res['status']} FAIL (brak RESOLVED)"); print("STOP regresja"); return 1
        lo, hi = res['tau_lo'], res['tau_hi']
        tol = mp.mpf('1e-4')
        match = (lo >= blo - tol) and (hi <= bhi + tol) and (blo >= lo - tol) and (bhi <= hi + tol)
        status = 'OK' if match else 'MISMATCH'
        print(f"  {k}: computed=[{mp.nstr(lo,12)},{mp.nstr(hi,12)}] expected=[{mp.nstr(blo,10)},{mp.nstr(bhi,10)}] {status}")
        if not match:
            print("STOP: regresja mismatch"); return 1

    print("\n[C] Pelny A.4 wszystkie 10 config (half):")
    results = {}
    for d in [1,2,3,4,5]:
        for ch in ['surface','interior']:
            res = run_config(d, ch, factor=HALF)
            results[(d,ch)] = res
            lo = res.get('tau_lo'); hi = res.get('tau_hi')
            print(f"  d{d} {ch:8s}: {res['status']} mult={res.get('mult')} tau=[{mp.nstr(lo,14) if lo else 'None'}, {mp.nstr(hi,14) if hi else 'None'}] flags={res.get('flags',[])}")

    U = compute_U_b(results)
    print("\n[D] U_b interwaly per (ao):")
    for d in [1,2,3,4,5]:
        if U[d]: print(f"  U_b(d{d}) = [{mp.nstr(U[d][0],14)}, {mp.nstr(U[d][1],14)}]")
        else: print(f"  U_b(d{d}) = NIEROZSTRZYGALNE")
    kill = classify_kill(U)
    print(f"\n[KILL] = {kill}")

    F = compute_F_r(results)
    print(f"\n[F_r] = {F}")

    print("\n[E] Wrazliwosc theta'=sup/3, 2*sup/3 (deskryptywnie):")
    for factor, name in [(THIRD, 'third'), (TWOTHIRDS, 'twothirds')]:
        resv = {}
        for d in [1,2,3,4,5]:
            for ch in ['surface','interior']:
                resv[(d,ch)] = run_config(d, ch, factor=factor)
        Uv = compute_U_b(resv)
        killv = classify_kill(Uv)
        print(f"  factor={name}: kill = {killv}")

    print(f"\nEnd: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} | elapsed={time.time()-t0:.1f}s")
    print("Attribution: code and analysis = DeepSeek; proxy execution = warsztat.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
