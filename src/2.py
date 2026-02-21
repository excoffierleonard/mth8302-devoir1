import numpy as np
import matplotlib.pyplot as plt

# Parametres
A = np.array([[4.0, 1.0], [1.0, 3.0]])
b = np.array([1.0, 2.0])
mu = 0.1


def f(x):
    x1, x2 = x[0], x[1]
    quad = 0.5 * x @ A @ x - b @ x
    barrier = -mu * (np.log(x1) + np.log(x2))
    return quad + barrier


def grad_f(x):
    g = A @ x - b - mu * np.array([1.0 / x[0], 1.0 / x[1]])
    return g


def H_f(x):
    H = A + mu * np.diag([1.0 / x[0] ** 2, 1.0 / x[1] ** 2])
    return H


def backtracking_to_stay_positive(x, step, alpha0=1.0):
    alpha = alpha0
    while np.any(x + alpha * step <= 0):
        alpha *= 0.5
    return alpha


def run_gd(x0, eta=0.05, tol=1e-6, max_iter=2000):
    x = x0.astype(float).copy()
    hist = [x.copy()]
    for _ in range(max_iter):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            break
        step = -eta * g
        alpha = backtracking_to_stay_positive(x, step)
        x = x + alpha * step
        hist.append(x.copy())
    return np.array(hist)


def run_newton(x0, tol=1e-6, max_iter=100):
    x = x0.astype(float).copy()
    hist = [x.copy()]
    for _ in range(max_iter):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            break
        H = H_f(x)
        p = np.linalg.solve(H, -g)
        alpha = backtracking_to_stay_positive(x, p)
        x = x + alpha * p
        hist.append(x.copy())
    return np.array(hist)


def spectral_analysis(H):
    eigvals, eigvecs = np.linalg.eigh(H)
    lam_min, lam_max = eigvals[0], eigvals[-1]
    v_min, v_max = eigvecs[:, 0], eigvecs[:, -1]
    return lam_min, v_min, lam_max, v_max, eigvals, eigvecs


def main():
    x0 = np.array([1.0, 1.0])
    hist_gd = run_gd(x0, eta=0.05)
    hist_nt = run_newton(x0)

    # Grille pour contours
    x1 = np.linspace(0.1, 3.0, 200)
    x2 = np.linspace(0.1, 3.0, 200)
    X1, X2 = np.meshgrid(x1, x2)
    Z = np.zeros_like(X1)
    for i in range(X1.shape[0]):
        for j in range(X1.shape[1]):
            Z[i, j] = f(np.array([X1[i, j], X2[i, j]]))

    # Figure 1: Courbes de niveau et trajectoires
    plt.figure(figsize=(7, 6))
    plt.contour(X1, X2, Z, levels=25)
    plt.plot(hist_gd[:, 0], hist_gd[:, 1], marker="o", markersize=2, label="GD")
    plt.plot(hist_nt[:, 0], hist_nt[:, 1], marker="o", markersize=2, label="Newton")
    plt.scatter([x0[0]], [x0[1]], s=60, label="x0")
    plt.xlabel(r"$x_1$")
    plt.ylabel(r"$x_2$")
    plt.legend()
    plt.title("Courbes de niveau et trajectoires")
    plt.tight_layout()
    plt.savefig("output/2_contour.png", dpi=200)
    plt.close()

    # Figure 2: Norme du gradient
    plt.figure(figsize=(7, 4))
    plt.plot([np.linalg.norm(grad_f(x)) for x in hist_gd], label="GD")
    plt.plot([np.linalg.norm(grad_f(x)) for x in hist_nt], label="Newton")
    plt.yscale("log")
    plt.xlabel(r"it\'eration $k$")
    plt.ylabel(r"$\|\nabla f(x_k)\|$")
    plt.legend()
    plt.title("Evolution de la norme du gradient")
    plt.tight_layout()
    plt.savefig("output/2_gradient.png", dpi=200)
    plt.close()

    # Sortie texte
    lines = []
    lines.append(f"Descente de gradient: {len(hist_gd)-1} iterations")
    lines.append(f"  x* = [{hist_gd[-1, 0]:.6f}, {hist_gd[-1, 1]:.6f}]")
    lines.append(f"  f(x*) = {f(hist_gd[-1]):.6f}")
    lines.append(f"  ||grad|| = {np.linalg.norm(grad_f(hist_gd[-1])):.2e}")
    lines.append(f"Newton: {len(hist_nt)-1} iterations")
    lines.append(f"  x* = [{hist_nt[-1, 0]:.6f}, {hist_nt[-1, 1]:.6f}]")
    lines.append(f"  f(x*) = {f(hist_nt[-1]):.6f}")
    lines.append(f"  ||grad|| = {np.linalg.norm(grad_f(hist_nt[-1])):.2e}")

    # Analyse spectrale
    pts = [("x^(1) = (1,1)", np.array([1.0, 1.0])), ("x^(2) = (0.2,0.2)", np.array([0.2, 0.2]))]
    for name, xp in pts:
        H = H_f(xp)
        lam_min, v_min, lam_max, v_max, _, _ = spectral_analysis(H)
        kappa = lam_max / lam_min
        lines.append("=" * 60)
        lines.append(f"Point {name}")
        lines.append(f"H(x) =\n{H}")
        lines.append(f"lambda_min = {lam_min:.6f}, v_min = {v_min}")
        lines.append(f"lambda_max = {lam_max:.6f}, v_max = {v_max}")
        lines.append(f"kappa = {kappa:.6f}")

    with open("output/2.txt", "w", encoding="utf-8") as fout:
        fout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
