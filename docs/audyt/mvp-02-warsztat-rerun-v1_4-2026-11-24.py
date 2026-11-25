#!/usr/bin/env python3
# MVP-02: FORMALNY RERUN warsztatu na bindzie v1.4 (erraty (ap) i (aq)).
# Metoda (zgodna z v1.3 warsztatu,abinet quick-close + certyfikaty mpmath):
#   - skan zewnętrzny: float64, okno 8·T_sk, krok T_sk/4000 ZAMROŻONY, bufor 1e-9 konserwatywny
#   - certyfikaty przedziałowe (aq): g = max(F_a,F_b) + H_t·w^2/8 (+PAD 1e-45 NA ZEWNĄTRZ), mpmath dps 60
#   - (ak) lewostronność, (ap) absorpcja strefy, (al) zaokrąglenia NA ZEWNĄTRZ, (ao) U_b przedziałowo + half-up2
import numpy as np, mpmath as mp, json, time, os

mp.mp.dps = 60
PAD = mp.mpf('1e-45')
BUF = 1e-9

SQ5 = mp.sqrt(5)
OMEGA_mp = [mp.sqrt(3-SQ5), mp.sqrt(2), mp.sqrt(3), SQ5, mp.sqrt(3+SQ5)]
OMEGA_f = [float(x) for x in OMEGA_mp]
T_SK = 2*mp.pi/OMEGA_mp[0]
T_SK_f = float(T_SK)

SECTORS = [  # (m_a, lambda_a, theta_a)
    (mp.mpf(3), 3-SQ5,  SQ5),
    (mp.mpf(5), mp.mpf(2), mp.mpf(1)),
    (mp.mpf(4), mp.mpf(3), mp.mpf(0)),
    (mp.mpf(4), mp.mpf(5), mp.mpf(-2)),
    (mp.mpf(3), 3+SQ5, -SQ5),
]

def u_d(t, d):
    if d == 0: return mp.mpf(1)
    if d == 1: return t/3
    if d == 2: return (t**2-3)/6
    if d == 3: return (t**3-t**2-5*t+3)/6
    if d == 4: return (t**4-2*t**3-5*t**2+8*t)/6
    if d == 5: return (t**5-2*t**4-7*t**3+10*t**2+10*t-6)/6
    raise ValueError

def g_srf(d):
    return [(m/19)*u_d(th, d) for (m, _, th) in SECTORS]

def g_int(d):
    return [(19*lam/60)*g_srf(d)[a] for a, (_, lam, _) in enumerate(SECTORS)]

def cfg(d, ch):
    g = g_srf(d) if ch == 'srf' else g_int(d)
    sup = sum(abs(x) for x in g)**2
    A = sum(abs(g[a])*OMEGA_mp[a] for a in range(5))
    B = sum(abs(g[a]) for a in range(5))
    C = sum(abs(g[a])*OMEGA_mp[a]**2 for a in range(5))
    Ht = 2*A**2 + 2*B*C
    return g, sup, Ht

def F_np(t, g_f, om_f):
    s = np.zeros_like(t)
    for a in range(5):
        s += g_f[a]*np.cos(om_f[a]*t)
    return s*s

def F_mp(t, g):
    s = sum(g[a]*mp.cos(OMEGA_mp[a]*t) for a in range(5))
    return s*s

def half_up2_mp(x):
    if x == 0: return mp.mpf(0)
    e = int(mp.floor(mp.log10(abs(x))))
    sc = mp.mpf(10)**(e-1)
    return mp.nint(x/sc)*sc

DT = T_SK_f/4000.0
N_NODES = 8*4000 + 1

def locate(d, ch, factor, g, sup, Ht, window_iters=1):
    """Zwraca slownik statusu pierwszego przekroczenia wg A.4 v1.4."""
    theta = factor*sup
    theta_f = float(theta); Ht_f = float(Ht)
    g_f = [float(x) for x in g]
    leak0 = F_mp(0, g)  # udzial(0), B4
    if factor != mp.mpf(1)/2:
        leak_pass = leak0 >= theta  # tylko deskryptywnie raportowane
    else:
        leak_pass = False
    if leak0 >= theta:
        return {'status': 'PRZECIEK-B4a', 'tau': 0, 'udzial0': leak0, 'theta': theta}
    # skan float64: okna 1,2,4,8·T_sk, krok ZAMROŻONY T_sk/4000
    for mult in [1, 2, 4, 8]:
        t = np.arange(mult*4000+1)*DT
        F = F_np(t, g_f, OMEGA_f)
        j = np.argmax(F >= theta_f - BUF) if (F >= theta_f - BUF).any() else -1
        if j >= 1:
            break
    if j < 1:
        return {'status': 'PRAWO-OCENZUROWANE', 'maxF_window': float(F.max())}
    # strefa: pierwsza nlekertyfikowalna komorka przed wezlem j (indeksy przedzialow)
    ub_grid = np.maximum(F[:-1], F[1:]) + (Ht_f*DT*DT/8.0)
    nonfree = np.where(ub_grid >= theta_f - BUF)[0]
    zs = int(nonfree[0]) if len(nonfree) > 0 and nonfree[0] <= j-1 else j-1
    lo0 = mp.mpf(zs)*mp.mpf(DT)
    hi = mp.mpf(int(j))*mp.mpf(DT)
    lo = lo0
    F_lo = F_mp(lo, g); F_hi = mp.mpf(F[int(j)])
    assert float(F_hi) >= theta_f - BUF
    iters = 0; stuck = 0
    while (hi - lo) > mp.mpf('1e-4') and iters < 400:
        iters += 1
        t_m = (lo + hi)/2
        F_m = F_mp(t_m, g)
        if F_m >= theta + PAD:
            hi = t_m; F_hi = F_m; stuck = 0
            continue
        ub = max(F_lo, F_m) + Ht*(t_m-lo)**2/8 + PAD
        if ub < theta - PAD:
            lo = t_m; F_lo = F_m; stuck = 0
            continue
        # lewa czescniej certifikowalna: sonduj wewnatz [lo, t_m] (32 podwezlow)
        tt = [lo + (t_m-lo)*mp.mpf(k)/32 for k in range(1, 32)]
        FF = [F_mp(x, g) for x in tt]
        hit = next((idx for idx, fv in enumerate(FF) if fv >= theta + PAD), None)
        if hit is not None:
            hi = tt[hit]; F_hi = FF[hit]; stuck = 0
            continue
        # brak wezla przekraczajacego w lewej: certyfikuj po kolei od lo mala krokami
        moved = False
        for k in range(1, 32):
            cand = lo + (t_m-lo)*mp.mpf(k)/32
            F_c = FF[k-1]
            ubc = max(F_lo, F_c) + Ht*(cand-lo)**2/8 + PAD
            if ubc < theta - PAD:
                lo = cand; F_lo = F_c; moved = True
            else:
                # strefa: absorpcja (ap): lo zostaje, zawezamy od gory przez hi
                last = cand; break
        if not moved:
            stuck += 1
            if stuck > 3:
                break
    width = hi - lo
    hu_lo, hu_hi = half_up2_mp(lo), half_up2_mp(hi)
    flags = []
    if hu_lo != hu_hi: flags.append('NIEROZSTRZYGNIETY-ROUNDING')
    if hi < mp.mpf('0.01'): flags.append('TAU-MALE')
    elif lo < mp.mpf('0.01') <= hi: flags.append('TAU-MALE-NIEROZSTRZYGNIETY')
    res = {
        'status': 'RESOLVED' if width < mp.mpf('1e-4') else 'NIEROZSTRZYGALNY-PARCJALNY',
        'mult': mult if (j >= 1) else None,
        'tau_lo': lo, 'tau_hi': hi, 'width': width,
        'F_hi_cert': F_hi >= theta,  # hi = oceniony wezel przekraczajacy
        'half_up': (hu_lo, hu_hi), 'flags': flags, 'iters': iters,
    }
    res['absorb_zone_lo0'] = lo0
    return res

def main():
    t0 = time.time()
    out = {}
    print('=== WARSZTAT FORMALNY RERUN v1.4 (half wiezacy). T_sk =', mp.nstr(T_SK, 16), '===')
    # etap dokladny: bramki + H_t + theta
    gates = {}
    leaks_ok = True
    for d in [1,2,3,4,5]:
        gs = g_srf(d); gi = g_int(d)
        assert abs(sum(gs) + mp.mpf(1)/19) < mp.mpf('1e-50')
        if d == 1:
            leaks_ok &= abs(sum(gi) + mp.mpf(1)/3) < mp.mpf('1e-50')
        else:
            leaks_ok &= abs(sum(gi)) < mp.mpf('1e-50')
    assert abs(OMEGA_mp[4] - OMEGA_mp[0] - OMEGA_mp[1]) < mp.mpf('1e-50')
    print('bramki wyciekow i rezonans: PASS')
    cfgs = {}
    for d in [1,2,3,4,5]:
        for ch in ['srf', 'int']:
            g, sup, Ht = cfg(d, ch)
            cfgs[(d, ch)] = (g, sup, Ht)
            print(f'  d{d} {ch}: sup={mp.nstr(sup, 20)} theta_half={mp.nstr(sup/2, 16)} H_t={mp.nstr(Ht, 20)}')
    # A.4 half
    res_half = {}
    for d in [1,2,3,4,5]:
        for ch in ['srf', 'int']:
            g, sup, Ht = cfgs[(d, ch)]
            r = locate(d, ch, mp.mpf(1)/2, g, sup, Ht)
            res_half[(d, ch)] = r
            if r['status'] == 'RESOLVED':
                print(f"  d{d} {ch}: RESOLVED tau=[{mp.nstr(r['tau_lo'],14)}, {mp.nstr(r['tau_hi'],14)}] w={mp.nstr(r['width'],3)} hu={mp.nstr(r['half_up'][0],4)}/{mp.nstr(r['half_up'][1],4)} flags={r['flags']} it={r['iters']} hi_wezel_przek={r['F_hi_cert']}")
            else:
                print(f"  d{d} {ch}: {r['status']} {r.get('flags','')} {r.get('tau_lo','')}")
    # U_b + kill
    Ub = {}
    for d in [1,2,3,4,5]:
        rs = res_half[(d,'srf')]; ri = res_half[(d,'int')]
        if rs['status'] == 'RESOLVED' and ri['status'] == 'RESOLVED':
            Ub[d] = (rs['tau_lo']/ri['tau_hi'], rs['tau_hi']/ri['tau_lo'])
    print('\nU_b przedzialowe:')
    for d in [1,2,3,4,5]:
        if d in Ub:
            print(f"  U_b(d{d}) = [{mp.nstr(Ub[d][0],12)}, {mp.nstr(Ub[d][1],12)}]")
    # kill per (ao) half-up2 na calosci przedzialow
    lo5, hi5 = Ub[5][0], Ub[5][1]
    max_hi = max(Ub[d][1] for d in [1,2,3,4]); min_lo = min(Ub[d][0] for d in [1,2,3,4])
    wsp = half_up2_mp(lo5) > half_up2_mp(max_hi)
    nsp = half_up2_mp(hi5) < half_up2_mp(min_lo)
    kill = 'WSPARTE' if wsp else ('NIESPRAWIEDLIWIONE' if nsp else 'WYNIK TYPOWY')
    print(f"\nKILL (half-up2, calosc przedzialow): {kill} (wsp={wsp}, nsp={nsp})")
    print(f"  half-up2: lo5={mp.nstr(half_up2_mp(lo5),4)} hi5={mp.nstr(half_up2_mp(hi5),4)} max_hi_null={mp.nstr(half_up2_mp(max_hi),4)} min_lo_null={mp.nstr(half_up2_mp(min_lo),4)}")
    # F_r: ranga 270/360 z degeneracja 60x d1, 120x d2, 120x d3, 60x d4
    blocks = [(1,60),(2,120),(4,60),(3,120)]  # posortowane rosnaco wg U_b: d2 < d4 < d3 < d1
    def orbit_of_rank(r):
        s = 0
        for d, n in blocks:
            s += n
            if r <= s: return d
    # kryterium sortowania: porownanie srodkow przedzialow
    mids = {d: (Ub[d][0]+Ub[d][1])/2 for d in [1,2,3,4]}
    blocks_sorted = sorted(blocks, key=lambda x: mids[x[0]])
    d_Q3 = None; s = 0
    for d, n in blocks_sorted:
        s += n
        if 270 <= s: d_Q3 = d; break
    Q3 = Ub[d_Q3]
    Fr = '0/20' if hi5 < Q3[0] else ('20/20' if lo5 > Q3[1] else None)
    print(f"\nF_r diagnostyczne: bloki rosnaco {[(d,n) for d,n in blocks_sorted]}; ranga 270/360 => orbita d{d_Q3}; Q3 = [{mp.nstr(Q3[0],12)}, {mp.nstr(Q3[1],12)}]; caly U_b(d5) ponizej calego Q3: {hi5 < Q3[0]} => F_r = {Fr}")
    # wrazenie theta: third i twothirds (deskryptywnie)
    print('\nWrazliwosc (deskryptywnie):')
    sens = {}
    for fac, name in [(mp.mpf(1)/3, 'third'), (mp.mpf(2)/3, 'twothirds')]:
        st = {}
        for d in [1,2,3,4,5]:
            for ch in ['srf','int']:
                g, sup, Ht = cfgs[(d, ch)]
                r = locate(d, ch, fac, g, sup, Ht)
                st[(d,ch)] = {k: (str(v) if not isinstance(v, (list, tuple)) else [str(x) for x in v]) for k, v in r.items() if k in ('status','flags','tau_lo','tau_hi')}
        # kill deskryptywny: d5 vs null; przeciek => U_b inf
        Ubs = {}
        for d in [1,2,3,4,5]:
            rs, ri = st[(d,'srf')], st[(d,'int')]
            if rs['status']=='RESOLVED' and ri['status']=='RESOLVED':
                Ubs[d] = 'ok'
        sens[name] = {k[0]: v['status'] for k, v in st.items()}
        print(f"  {name}: " + ', '.join(f"d{d}{'s' if ch=='srf' else 'i'}:{st[(d,ch)]['status']}" for d in [1,2,3,4,5] for ch in ['srf','int']))
    # zapis JSON (skroty)
    def fl(x): return float(x) if not isinstance(x, str) else x
    save = {
      'T_sk': mp.nstr(T_SK, 20),
      'half': {f'{d}{ch}': {'status': r['status'],
                'tau_lo': mp.nstr(r['tau_lo'], 20), 'tau_hi': mp.nstr(r['tau_hi'], 20),
                'width': mp.nstr(r['width'], 8), 'flags': r.get('flags', [])} for (d, ch), r in res_half.items()},
      'Ub': {d: [mp.nstr(Ub[d][0], 16), mp.nstr(Ub[d][1], 16)] for d in Ub},
      'kill': kill, 'Fr': Fr, 'Q3': [mp.nstr(Q3[0], 12), mp.nstr(Q3[1], 12)], 'Q3_orbit': d_Q3,
      'sens': sens,
      'Ht': {f'{d}{ch}': mp.nstr(cfgs[(d,ch)][2], 20) for (d, ch) in cfgs},
      'sup': {f'{d}{ch}': mp.nstr(cfgs[(d,ch)][1], 20) for (d, ch) in cfgs},
      'elapsed': round(time.time()-t0, 1),
    }
    os.makedirs('/home/user/tool-results/data-analysis/mvp02-v14-rerun', exist_ok=True)
    with open('/home/user/tool-results/data-analysis/mvp02-v14-rerun/w14_result.json', 'w') as f:
        json.dump(save, f, indent=1)
    print('\n czas:', round(time.time()-t0,1), 's; wyniki w w14_result.json')

if __name__ == '__main__':
    main()
