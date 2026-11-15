#!/usr/bin/env python3
"""P0-Estrada gates C4-H. PROXY v2. DeepSeek 2026-11-15.
PROXY: code and analysis = DeepSeek; execution = Leszek; stdout verbatim.
numpy only. Deterministic LCG seed=42 (§2.2 DOP-1).

Changes v1 -> v2 (three, see wklejka v4 §2, B3 hygiene):
  1. wgap(): raw |x[i]-x[j]| instead of chord to great circle (DOP-2).
     Affects D1, D2, D5.
  2. D5 aggregation: per-image min over 6 pairs, then min/max over
     window n in [100,300] and 4 starts (DOP-3). v1 flattened per-pair.
  3. E1: normalize z to sum_k |z_k|^2 = 1 before Gram matrix.
     v1 used unnormalized z. Assertion unaffected (post-assert).
All other lines identical to v1 (sha256 0c119cae)."""

import numpy as np, time

t_start = time.time()
print("P0-Estrada gates C4-H — PROXY v2 execution")
print("Code+analysis: DeepSeek; executor: Leszek; stdout verbatim")
print("numpy:", np.__version__, "| start:", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

# ---- Setup (§2.1) ----
def M_i(i):
    m = np.eye(4); m[i,:] = 0.25; return m
def build_W(order):
    W = np.eye(4)
    for i in order: W = M_i(i) @ W
    return W
W_nat = build_W([0,1,2,3])
W_mir = build_W([0,1,3,2])
P_c = np.eye(4) - np.ones((4,4))/4
B4 = P_c @ W_nat
B4m = P_c @ W_mir

ONE = np.ones(4)
def nrm(x): return x/np.linalg.norm(x)
v_hats = [nrm(np.eye(4)[i]-ONE/4) for i in range(4)]
pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
m_hats = [nrm(v_hats[i]+v_hats[j]) for (i,j) in pairs]

# V_cyc orthonormal basis (3x4)
V_basis = []
for v in [v_hats[0], v_hats[1], v_hats[2]]:
    u = v.copy()
    for b in V_basis: u -= (u@b)*b
    V_basis.append(u/np.linalg.norm(u))
V_basis = np.array(V_basis)
def from_V(c): return c @ V_basis
def to_V(x): return (x - np.mean(x)*ONE) @ V_basis.T

# ---- Delta (§2.2) ----
def delta(x):
    p = 1.0
    for (i,j) in pairs: p *= (x[i]-x[j])
    return p

# ---- Spectral (§3, Krylov) ----
eigs = np.linalg.eigvals(B4)
lr = sorted([e.real for e in eigs if abs(e.imag)<1e-10])[-1]
lc = [e for e in eigs if e.imag>1e-10][0]
y = np.array([0.37,-0.52,0.81,-0.23])

def restrict(B,u,v):
    U = np.column_stack([u,v])
    M,_,_,_ = np.linalg.lstsq(U, B@U, rcond=None)
    return M

u0 = B4 @ (B4 - lr*np.eye(4)) @ y; v0 = B4 @ u0
M2 = restrict(B4,u0,v0); _, V2 = np.linalg.eig(M2)
idx = np.argmin(np.abs(np.linalg.eigvals(M2) - lc))
z = (V2[0,idx]*u0 + V2[1,idx]*v0).astype(complex)
assert np.linalg.norm(B4@z - lc*z)/np.linalg.norm(z) < 1e-10, "z resid"

u0L = B4.T @ (B4.T - lr*np.eye(4)) @ y; v0L = B4.T @ u0L
M2L = restrict(B4.T,u0L,v0L); _, V2L = np.linalg.eig(M2L)
idxL = np.argmin(np.abs(np.linalg.eigvals(M2L) - lc))
w = (V2L[0,idxL]*u0L + V2L[1,idxL]*v0L).astype(complex)
w /= np.linalg.norm(w)
w *= np.exp(-1j*np.angle(w @ v_hats[0]))

q = (B4@B4 - 2*lc.real*B4 + abs(lc)**2*np.eye(4)) @ y
u_hat = P_c @ q; u_hat /= np.linalg.norm(u_hat)
if u_hat[np.argmax(np.abs(u_hat))] < 0: u_hat = -u_hat

def phase(x):
    p = np.degrees(np.angle(w @ x))
    while p > 180: p -= 360
    while p <= -180: p += 360
    return p

# ---- Curve (§2.2) — CHANGE 3: normalize z before Gram ----
z /= np.sqrt(np.sum(np.abs(z)**2))
zr, zi = z.real, z.imag
G_curve = np.array([[zr@zr, zr@zi],[zr@zi, zi@zi]])
eig_Gc = np.linalg.eigvalsh(G_curve)
axes = np.sqrt(np.sort(eig_Gc)[::-1])
def curve_pt(t):
    p = np.cos(t)*zr + np.sin(t)*zi
    return p/np.linalg.norm(p)
def angle_to_E(x):
    c = np.linalg.solve(G_curve, [zr@x, zi@x])
    p = c[0]*zr + c[1]*zi
    return np.degrees(np.arccos(np.clip(np.linalg.norm(p)/np.linalg.norm(x),-1,1)))

# ---- Results ----
R = []
def add(name, exp, act, tol, note=""):
    if isinstance(exp,(int,float)) and isinstance(act,(int,float)):
        dev = abs(act-exp)
        status = "OK" if (tol is None or dev <= tol) else "FAIL"
    else:
        dev, status = "N/A", "CUSTOM"
    R.append((name, exp, act, dev, tol, status, note))

# ---- C1-C3: order fits (LCG directions) ----
class LCG:
    def __init__(s, seed=42): s.s, s.m, s.a, s.c = seed, 2**31, 1103515245, 12345
    def next(s):
        s.s = (s.a*s.s + s.c) % s.m
        return s.s / 2**30 - 1
lcg = LCG()
def rand_dir(x):
    r = np.array([lcg.next() for _ in range(4)])
    r = r - np.mean(r)*ONE
    r = r - (r@x)*x
    return r/np.linalg.norm(r)

def order_fit(base, d, ts):
    vals = [abs(delta(nrm(base+t*d))) for t in ts]
    A = np.column_stack([np.log(ts), np.ones(len(ts))])
    c,_,_,_ = np.linalg.lstsq(A, np.log(vals), rcond=None)
    return c[0]

ts = np.logspace(-4,-2,10)
C1 = np.mean([order_fit(m_hats[0], rand_dir(m_hats[0]), ts) for _ in range(3)])
C2 = np.mean([order_fit(v_hats[0], rand_dir(v_hats[0]), ts) for _ in range(3)])
gen = nrm(np.array([1.,1.,2.,-4.]))
C3 = np.mean([order_fit(gen, rand_dir(gen), ts) for _ in range(3)])
add("C1 order near m_hat_ij", 2.000, C1, 0.01, "3 LCG dirs")
add("C2 order near v_hat_i", 3.000, C2, 0.01, "3 LCG dirs")
add("C3 order generic wall", 1.000, C3, 0.02, "3 LCG dirs")

# ---- C4: max |Delta| (grid + coordinate descent) ----
best_val, best_coef = 0.0, None
for i in range(500):
    th = np.pi*i/499
    for j in range(1000):
        ph = 2*np.pi*j/1000
        c = np.array([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th)])
        v = abs(delta(from_V(c)))
        if v > best_val: best_val, best_coef = v, c.copy()
c = best_coef; th, ph = np.arccos(np.clip(c[2],-1,1)), np.arctan2(c[1],c[0])
step = np.pi/500
for _ in range(5000):
    improved = False
    for dt in [-step, 0, step]:
        for dp in [-step, 0, step]:
            if dt==0 and dp==0: continue
            c = np.array([np.sin(th+dt)*np.cos(ph+dp), np.sin(th+dt)*np.sin(ph+dp), np.cos(th+dt)])
            v = abs(delta(from_V(c)))
            if v > best_val:
                best_val, best_coef = v, c.copy()
                th, ph, improved = th+dt, ph+dp, True
    if not improved:
        step /= 2
        if step < 1e-13: break
x_argmax = from_V(best_coef)
add("C4 max |D| on V_cyc", 1/(6*np.sqrt(3)), best_val, 1e-9, "grid + coord descent")

# ---- C5: argmax type ----
a_sorted = np.sort(np.abs(x_argmax))[::-1]
a_est = (a_sorted[0]+a_sorted[1])/2
r_est = (a_sorted[2]+a_sorted[3])/2 / a_est
r_exp = np.sqrt(5 - 2*np.sqrt(6))
C5_ok = abs(r_est - r_exp) < 1e-3 and abs(a_sorted[0]-a_sorted[1])/a_est < 1e-3
R.append(("C5 argmax type", f"(1,{r_exp:.6f},-r,-1)",
          f"r={r_est:.6f}", "N/A", None, "OK" if C5_ok else "FAIL",
          "typological check"))

# ---- Dynamics (Phi^n, n=0..300, 4 starts) ----
def Phi(x): return B4@x/np.linalg.norm(B4@x)
N = 300
traj = []
for i in range(4):
    t = [v_hats[i].copy()]
    for n in range(N): t.append(Phi(t[-1]))
    traj.append(np.array(t))

# ---- CHANGE 1: wgap() = raw |x_a - x_b| (DOP-2) ----
def wgap(x):
    return np.array([abs(x[i]-x[j]) for (i,j) in pairs])

add("D1 min wall gap (1r)", 0.096787, min(min(wgap(traj[i][1])) for i in range(4)), 1e-4)
for i in range(4):
    add(f"D2 start{i} gap", [0.104302,0.264164,0.096787,0.350760][i], min(wgap(traj[i][1])), 1e-4)
for i in range(4):
    add(f"D3 start{i} |D|1r", [0.004660,0.075436,0.028878,0.087756][i], abs(delta(traj[i][1])), 1e-4)

dA = [abs(delta(traj[i][n])) for i in range(4) for n in range(100,301)]
add("D4 |D| asympt min", 9.86e-5, min(dA), 1e-3)
add("D4 |D| asympt max", 0.094072, max(dA), 1e-3)

# ---- CHANGE 2: D5 per-image min over 6 pairs, then min/max over window (DOP-3) ----
per_image_min = [float(min(wgap(traj[i][n]))) for i in range(4) for n in range(100,301)]
add("D5 gap asympt min", 3.64e-4, min(per_image_min), 3.64e-4*0.05)
add("D5 gap asympt max", 0.419665, max(per_image_min), 1e-3)

pd = []
for n in range(100,301):
    P = [traj[i][n] for i in range(4)]
    for i in range(4):
        for j in range(i+1,4): pd.append(np.linalg.norm(P[i]-P[j]))
add("D6 pair dist min", 0.717518, min(pd), 1e-3)
add("D6 pair dist max", 1.985113, max(pd), 1e-3)

dg = [np.linalg.norm(traj[0][n]-traj[2][n]) for n in range(100,301)] + \
     [np.linalg.norm(traj[1][n]-traj[3][n]) for n in range(100,301)]
add("D7 diag pair min", 1.814063, min(dg), 1e-3)
add("D7 diag pair max", 1.985113, max(dg), 1e-3)

th_exp = 25.772093727472
d_ph = []
for i in range(4):
    phs = [phase(traj[i][n]) for n in range(N+1)]
    unw = [phs[0]]
    for k in range(1,len(phs)):
        dd = phs[k] - phs[k-1]
        while dd > 180: dd -= 360
        while dd < -180: dd += 360
        unw.append(unw[-1]+dd)
    d_ph.append((unw[-1]-unw[0])/N)
add("D8 phase/round", th_exp, np.mean(d_ph), 1e-9, f"per-start {[f'{p:.4f}' for p in d_ph]}")

prec = [np.linalg.norm(traj[i][n+14]-traj[i][n]) for i in range(4) for n in range(100,287)]
add("D9 precession avg", 0.014118, np.mean(prec), 2e-3)
add("D9 precession max", 0.022046, max(prec), 2e-3)

for k, m in enumerate(m_hats):
    add(f"D10 m_hat_{pairs[k]}", [1.945753,1.982096,1.898857,1.898857,1.982096,1.945753][k],
        np.linalg.norm(Phi(m)+m), 1e-3)

Rn = []
for n in range(100,201):
    P = np.array([traj[i][n] for i in range(4)]); c = np.mean(P,axis=0)
    Rn.append(np.mean([np.linalg.norm(p-c) for p in P]))
add("D11 R_n min", 0.962485, min(Rn), 1e-4)
add("D11 R_n max", 0.987304, max(Rn), 1e-4)

for i in range(4):
    add(f"D12 ||B4 v_{i}||", [0.172981,0.153673,0.139809,0.205750][i], np.linalg.norm(B4@v_hats[i]), 1e-5)

# ---- E (E1 already fixed by z normalization; axes here now correct) ----
add("E1 axis1", 0.842008, axes[0], 1e-4)
add("E1 axis2", 0.539466, axes[1], 1e-4)

NC = 10000
t_e = np.linspace(0, 2*np.pi, NC, endpoint=False)
crv = np.array([curve_pt(t) for t in t_e])
for (i,j) in pairs:
    dd = crv[:,i]-crv[:,j]; s = np.sign(dd)
    ch = int(np.sum(s[:-1]!=s[1:])) + int(s[-1]!=s[0])
    add(f"E2 signchange {i}{j}", 2, ch, 0)

for k, m in enumerate(m_hats):
    d = min(np.linalg.norm(crv[j]-m) for j in range(NC))
    add(f"E3 margin m_{pairs[k]}", [0.102727,1.067370,0.427859,0.427859,1.067370,0.102727][k], d, 1e-3)

for i in range(4):
    d = min(min(np.linalg.norm(crv[j]-v_hats[i]), np.linalg.norm(crv[j]+v_hats[i])) for j in range(NC))
    add(f"E4 margin +-v_{i}", [0.344211,0.221984,0.760304,0.927427][i], d, 1e-3)

alphas = [abs(w @ p) for p in crv]
add("E5 |a| min/max", 0.640689597602, min(alphas)/max(alphas), 1e-5)

d_u = min(min(np.linalg.norm(p-u_hat), np.linalg.norm(p+u_hat)) for p in crv)
add("E6 dist to +-u_hat", 0.693692, d_u, 1e-3)

b4n = [np.linalg.norm(B4@p) for p in crv]
add("E7 ||B4 p|| min", 0.139597, min(b4n), 1e-4)
add("E7 ||B4 p|| max", 0.207722, max(b4n), 1e-4)

add("E8 max |D| on curve", 0.094072, max(abs(delta(p)) for p in crv), 1e-3)

# ---- F ----
for k in range(4):
    add(f"F1 |u_{k}|", [0.7116,0.6090,0.1911,0.2936][k], abs(u_hat[k]), 1e-4,
        f"sign={int(np.sign(u_hat[k])):+d}")

for k, m in enumerate(m_hats):
    ang = np.degrees(np.arccos(np.clip(abs(u_hat@m), -1, 1)))
    add(f"F2 angle u to +-m_{pairs[k]}", [84.11,25.49,65.29,65.29,25.49,84.11][k], ang, 0.05)

for k, v in enumerate(v_hats):
    ang = np.degrees(np.arccos(np.clip(abs(u_hat@v), -1, 1)))
    add(f"F3 angle u to +-v_{k}", [34.75,45.31,77.26,70.18][k], ang, 0.05)

add("F4 angle u to E", 40.589057, angle_to_E(u_hat), 0.005)
add("F5 |w.u_hat|", 0, abs(w @ u_hat), 1e-15)

eigs_m = np.linalg.eigvals(B4m)
lr_m = sorted([e.real for e in eigs_m if abs(e.imag)<1e-10])[-1]
lc_m = [e for e in eigs_m if e.imag>1e-10][0]
q_m = (B4m@B4m - 2*lc_m.real*B4m + abs(lc_m)**2*np.eye(4)) @ y
u_m = P_c @ q_m; u_m /= np.linalg.norm(u_m)
if u_m[np.argmax(np.abs(u_m))] < 0: u_m = -u_m
add("F6 angle u_nat to u_mir", 40.087, np.degrees(np.arccos(np.clip(abs(u_hat@u_m),-1,1))), 0.05)

# ---- G ----
B4_V = V_basis @ B4 @ V_basis.T
sv = np.sort(np.linalg.svd(B4_V, compute_uv=False))[::-1]
for k in range(3):
    add(f"G1 sv{k+1}", [0.226568,0.145690,0.118340][k], sv[k], 1e-5)

Gm = np.linalg.inv(np.eye(3) - B4_V.T @ B4_V)
eig_Gm = np.sort(np.linalg.eigvalsh(Gm))[::-1]
for k in range(3):
    add(f"G2 eigG{k+1}", [1.054111,1.021686,1.014203][k], eig_Gm[k], 1e-4)

# ---- H ----
for i in range(4):
    add(f"H1 phi(v_{i}) nat", [0,-61.918,-146.782,96.443][i], phase(v_hats[i]), 0.02)

phs = sorted([phase(v_hats[i]) for i in range(4)])
gaps = np.diff(np.append(phs, phs[0]+360))
for k, v in enumerate(sorted(gaps)):
    add(f"H2 gap{k+1}", [61.918,84.864,96.443,116.774][k], v, 0.02)

def wrap_d(d):
    while d > 90: d -= 180
    while d <= -90: d += 180
    return d

for k, (i,j) in enumerate(pairs):
    ph_m = phase(m_hats[k]); ph_av = (phase(v_hats[i])+phase(v_hats[j]))/2
    add(f"H3 delta {pairs[k]}", [-9.321,-44.690,26.204,-1.224,44.656,-15.110][k],
        wrap_d(ph_m-ph_av), 0.02)

u0Lm = B4m.T @ (B4m.T - lr_m*np.eye(4)) @ y; v0Lm = B4m.T @ u0Lm
M2Lm = restrict(B4m.T, u0Lm, v0Lm); _, V2Lm = np.linalg.eig(M2Lm)
idxLm = np.argmin(np.abs(np.linalg.eigvals(M2Lm) - lc_m))
w_m = (V2Lm[0,idxLm]*u0Lm + V2Lm[1,idxLm]*v0Lm).astype(complex)
w_m /= np.linalg.norm(w_m)
w_m *= np.exp(-1j*np.angle(w_m @ v_hats[0]))
def phm(x):
    p = np.degrees(np.angle(w_m @ x))
    while p > 180: p -= 360
    while p <= -180: p += 360
    return p

for k, (i,j) in enumerate(pairs):
    ph_m = phm(m_hats[k]); ph_av = (phm(v_hats[i])+phm(v_hats[j]))/2
    add(f"H4 mirror delta {pairs[k]}", [-9.321,26.204,-44.690,44.656,-1.224,-15.110][k],
        wrap_d(ph_m-ph_av), 0.02)

for i in range(4):
    add(f"H5 mirror phi(v_{i})", [0,-61.918,96.443,-146.782][i], phm(v_hats[i]), 0.02)

# ---- Output ----
print("="*118)
print(f"{'Gate':<34} {'Expected':<22} {'Actual':<22} {'Dev':<11} {'Tol':<9} {'Stat':<5} Note")
print("-"*118)
for (n, e, a, d, t, s, note) in R:
    es = f"{e:.10g}" if isinstance(e,(int,float)) else str(e)
    as_ = f"{a:.10g}" if isinstance(a,(int,float)) else str(a)
    ds = f"{d:.2e}" if isinstance(d,(int,float)) else str(d)
    ts_ = f"{t:.1e}" if isinstance(t,(int,float)) else (str(t) if t is not None else "—")
    print(f"{n:<34} {es:<22} {as_:<22} {ds:<11} {ts_:<9} {s:<5} {note}")
n_ok = sum(1 for r in R if r[5]=="OK"); n_fail = sum(1 for r in R if r[5]=="FAIL")
print("-"*118)
print(f"Total: {len(R)}  OK: {n_ok}  FAIL: {n_fail}")
if n_fail:
    print("\nCANDIDATE ERRATA (§0 pkt 3 — STOP-rule):")
    for r in R:
        if r[5]=="FAIL": print(f"  {r[0]}: expected {r[1]}, got {r[2]}, dev {r[3]:.2e}" if isinstance(r[3],(int,float)) else f"  {r[0]}: expected {r[1]}, got {r[2]}")
print(f"\nEnd: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} | elapsed: {time.time()-t_start:.1f}s")
print("Attribution: code and analysis = DeepSeek; proxy execution = Leszek; stdout verbatim.")
