#!/usr/bin/env python3
"""TAU-10-Z1: Pair K4 Jacobian replication. PROXY v1.
DeepSeek 2026-11-16. Code+analysis: DeepSeek; execution proxy: Leszek; stdout verbatim.
numpy + scipy only. Deterministic (seed=42). No values from §4 except sanity check column."""

import numpy as np
from scipy.linalg import expm
import time

t_start = time.time()
print("TAU-10-Z1 — Pair K4 Jacobian — PROXY v1 execution")
print("Code+analysis: DeepSeek; executor: Leszek; stdout verbatim")
print(f"numpy: {np.__version__} | start: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")

# === Core ===
def build_L(D, edges, n_verts):
    L = np.zeros((n_verts, n_verts))
    for e, (i, j) in enumerate(edges):
        w = np.exp(-abs(D[e]))
        L[i, i] += w; L[j, j] += w
        L[i, j] -= w; L[j, i] -= w
    return L

def build_F(D, edges, n_verts, pairs, t):
    K = expm(-t * build_L(D, edges, n_verts))
    return np.array([K[i,i] + K[j,j] - 2*K[i,j] for (i,j) in pairs])

def jac_fd(D, edges, n_verts, pairs, t, eps=1e-6):
    J = np.zeros((len(pairs), len(edges)))
    for e in range(len(edges)):
        Dp = D.copy(); Dp[e] += eps
        Dm = D.copy(); Dm[e] -= eps
        J[:, e] = (build_F(Dp, edges, n_verts, pairs, t) -
                   build_F(Dm, edges, n_verts, pairs, t)) / (2*eps)
    return J

def jac_frechet(D, edges, n_verts, pairs, t):
    L = build_L(D, edges, n_verts)
    A = -t * L
    n = n_verts
    J = np.zeros((len(pairs), len(edges)))
    for e, (i, j) in enumerate(edges):
        s = float(np.sign(D[e])) if abs(D[e]) > 1e-20 else 0.0
        dw = -np.exp(-abs(D[e])) * s
        dL = np.zeros((n, n))
        dL[i, i] = dw; dL[j, j] = dw
        dL[i, j] = -dw; dL[j, i] = -dw
        dA = -t * dL
        M = np.zeros((2*n, 2*n))
        M[:n, :n] = A; M[n:, n:] = A; M[:n, n:] = dA
        dK = expm(M)[:n, n:]
        for k, (p, q) in enumerate(pairs):
            J[k, e] = dK[p, p] + dK[q, q] - 2*dK[p, q]
    return J

def sector_bases(edges, n_verts):
    M = np.zeros((len(edges), n_verts))
    for e, (i, j) in enumerate(edges):
        M[e, i] = 1; M[e, j] = -1
    U, S, _ = np.linalg.svd(M, full_matrices=True)
    rank = int(np.sum(S > 1e-10))
    return U[:, :rank], U[:, rank:]

def sector_ranks(J, U_imd, U_ker, tol=1e-10):
    P_imd = U_imd @ U_imd.T
    P_ker = U_ker @ U_ker.T
    return (np.linalg.matrix_rank(J @ P_imd, tol=tol),
            np.linalg.matrix_rank(J @ P_ker, tol=tol))

# === PART A: K4 gate ===
print("\n" + "="*78)
print("PART A: K4 gate (D=1, t=1). Checkpoint §21: SVs (.6756526, .3378263×3, .1689132×2), rank 6, sectors 3/3")
print("="*78)
K4_edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
K4_pairs = K4_edges[:]
D_K4 = np.ones(6)
J_fr = jac_frechet(D_K4, K4_edges, 4, K4_pairs, 1.0)
J_fd = jac_fd(D_K4, K4_edges, 4, K4_pairs, 1.0)
rel_dev_K4 = np.max(np.abs(J_fd - J_fr)) / np.max(np.abs(J_fr))
sv_fr = np.sort(np.linalg.svd(J_fr, compute_uv=False))[::-1]
sv_fd = np.sort(np.linalg.svd(J_fd, compute_uv=False))[::-1]
U_imd_K4, U_ker_K4 = sector_bases(K4_edges, 4)
sec_K4 = sector_ranks(J_fr, U_imd_K4, U_ker_K4)
expected_sv = np.array([.6756526, .3378263, .3378263, .3378263, .1689132, .1689132])
sv_err = np.max(np.abs(sv_fr - expected_sv))
print(f"SVs Frechet (desc): {['%.7g' % v for v in sv_fr]}")
print(f"SVs FD (desc):      {['%.7g' % v for v in sv_fd]}")
print(f"Max |SV(Frechet) - checkpoint§21|: {sv_err:.3e}  (threshold 1e-6)")
print(f"Max |SV(FD) - SV(Frechet)|:        {np.max(np.abs(sv_fd-sv_fr)):.3e}")
print(f"Rank (Frechet, tol 1e-10): {np.linalg.matrix_rank(J_fr, tol=1e-10)}  (expect 6)")
print(f"Sectors: Im(d)={sec_K4[0]}/3, ker_δ={sec_K4[1]}/3  (expect 3/3)")
print(f"Max rel dev (FD vs Frechet): {rel_dev_K4:.3e}")
for tt in [0.1, 2.0]:
    r = np.linalg.matrix_rank(jac_frechet(D_K4, K4_edges, 4, K4_pairs, tt), tol=1e-10)
    print(f"Rank at t={tt}: {r}  (expect 6)")

# === PART B: Pair K4 (BLIND) ===
print("\n" + "="*78)
print("PART B: Pair K4, D=1, t in {0.1, 1, 2}. J shape: 10 pairs x 9 edges. BLIND.")
print("="*78)
P_edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(4,1),(4,2),(4,3)]
P_pairs = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
D_P = np.ones(9)
U_imd_P, U_ker_P = sector_bases(P_edges, 5)
for tt in [0.1, 1.0, 2.0]:
    J = jac_frechet(D_P, P_edges, 5, P_pairs, tt)
    J_fd_tt = jac_fd(D_P, P_edges, 5, P_pairs, tt)
    rel = np.max(np.abs(J_fd_tt - J)) / np.max(np.abs(J))
    svs = np.sort(np.linalg.svd(J, compute_uv=False))[::-1]
    rank = np.linalg.matrix_rank(J, tol=1e-10)
    sec = sector_ranks(J, U_imd_P, U_ker_P)
    print(f"\n-- t={tt} --")
    print(f"SVs (desc, 6 sig): {['%.6g' % v for v in svs]}")
    print(f"Rank: {rank}/9")
    print(f"κ = σ_min/σ_max (spec): {svs[-1]/svs[0]:.6g}   |   κ_std = σ_max/σ_min: {svs[0]/svs[-1]:.6g}")
    print(f"Sectors: Im(d)={sec[0]}/4, ker_δ={sec[1]}/5")
    print(f"Max rel dev (FD vs Fr): {rel:.3e}")

# === PART C: 720 random ===
print("\n" + "="*78)
print("PART C: 720 Jacobians (240 states × 3 t), seed=42, U(-2,2)^9, |D_e|>=1e-3")
print("="*78)
rng = np.random.default_rng(42)
N_STATES = 240
T_VALS = [0.1, 1.0, 2.0]
res = {tt: {'rank': [], 'smin': [], 'kappa': []} for tt in T_VALS}
acc, rej = 0, 0
while acc < N_STATES:
    D = rng.uniform(-2, 2, 9)
    if np.min(np.abs(D)) < 1e-3:
        rej += 1; continue
    acc += 1
    for tt in T_VALS:
        J = jac_frechet(D, P_edges, 5, P_pairs, tt)
        svs = np.sort(np.linalg.svd(J, compute_uv=False))[::-1]
        res[tt]['rank'].append(np.linalg.matrix_rank(J, tol=1e-10))
        res[tt]['smin'].append(svs[-1])
        res[tt]['kappa'].append(svs[-1]/svs[0])
print(f"Accepted: {acc}, rejected: {rej}")
for tt in T_VALS:
    ranks = np.array(res[tt]['rank'])
    smin = np.array(res[tt]['smin'])
    kap = np.array(res[tt]['kappa'])
    full = int(np.sum(ranks == 9))
    near = int(np.sum(smin < 1e-3))
    print(f"\n-- t={tt} -- full-rank {full}/{acc}; σ_min: min={smin.min():.4g}, med={np.median(smin):.4g}; κ=σ_min/σ_max: max={kap.max():.4g}, med={np.median(kap):.4g}; near-loss(σ_min<1e-3): {near}")

# === PART H1: peak-pair row (0,4) ===
print("\n" + "="*78)
print("PART H1: row for pair (0,4) in J at D=1 (BLIND). Orbits: A=(0,1),(0,2),(0,3); F=(1,2),(1,3),(2,3); B=(4,1),(4,2),(4,3)")
print("="*78)
for tt in [0.1, 1.0, 2.0]:
    J = jac_frechet(D_P, P_edges, 5, P_pairs, tt)
    row = J[3, :]  # pair (0,4) is index 3 in P_pairs
    print(f"\n-- t={tt} --")
    for k, (i, j) in enumerate(P_edges):
        print(f"  (0,4) x edge ({i},{j}): {row[k]:+.8f}")
    print(f"  Orbit A avg (edges (0,1),(0,2),(0,3)): {np.mean(row[0:3]):+.8f}")
    print(f"  Orbit F avg (edges (1,2),(1,3),(2,3)): {np.mean(row[3:6]):+.8f}")
    print(f"  Orbit B avg (edges (4,1),(4,2),(4,3)): {np.mean(row[6:9]):+.8f}")

print("\n" + "="*78)
print(f"Elapsed: {time.time()-t_start:.1f}s")
print("Attribution: code and analysis = DeepSeek; proxy execution = Leszek; stdout verbatim.")