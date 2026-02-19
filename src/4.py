import numpy as np
from scipy.stats import f
import matplotlib.pyplot as plt


def main():
    # Donnees
    group_a = np.array([72, 75, 78, 69, 82, 77, 71, 74, 80, 73], dtype=float)
    group_b = np.array([78, 81, 85, 79, 88, 84, 82, 80, 86, 83], dtype=float)

    n_a = len(group_a)
    n_b = len(group_b)
    df1 = n_a - 1
    df2 = n_b - 1
    alpha = 0.05

    var_a = group_a.var(ddof=1)
    var_b = group_b.var(ddof=1)
    f_stat = var_a / var_b

    f_lower = f.ppf(alpha / 2, df1, df2)
    f_upper = f.ppf(1 - alpha / 2, df1, df2)

    p_value = 2 * min(f.cdf(f_stat, df1, df2), 1 - f.cdf(f_stat, df1, df2))

    ci_lower = f_stat / f_upper
    ci_upper = f_stat / f_lower

    print(f"Variance A (s^2_A) = {var_a:.6f}")
    print(f"Variance B (s^2_B) = {var_b:.6f}")
    print(f"F_stat = {f_stat:.6f}")
    print(f"F_0.025 = {f_lower:.6f}")
    print(f"F_0.975 = {f_upper:.6f}")
    print(f"p-value = {p_value:.6f}")
    print(f"IC 95% du ratio (sigma_A^2 / sigma_B^2) = [{ci_lower:.6f}, {ci_upper:.6f}]")

    # Trace de la distribution F et region critique
    x_max = max(8.0, f_upper * 1.2)
    x = np.linspace(0.001, x_max, 1000)
    y = f.pdf(x, df1, df2)

    plt.figure(figsize=(8, 4.5))
    plt.plot(x, y, color="navy", lw=2, label=f"F({df1}, {df2})")
    plt.fill_between(x, y, where=(x <= f_lower), color="red", alpha=0.3, label="Zone critique (\u03b1/2)")
    plt.fill_between(x, y, where=(x >= f_upper), color="red", alpha=0.3)
    plt.axvline(f_stat, color="black", linestyle="--", lw=1.5, label=f"Fstat = {f_stat:.3f}")
    plt.axvline(f_lower, color="red", linestyle=":", lw=1.2, label=f"F0.025 = {f_lower:.3f}")
    plt.axvline(f_upper, color="red", linestyle=":", lw=1.2, label=f"F0.975 = {f_upper:.3f}")
    plt.title("Test F de Fisher : region critique et statistique observee")
    plt.xlabel("Valeur de F")
    plt.ylabel("Densite")
    plt.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig("output/4.png", dpi=200)
    plt.close()


if __name__ == "__main__":
    main()
