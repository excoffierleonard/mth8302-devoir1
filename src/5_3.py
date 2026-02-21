import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def main():
    sns.set_theme()

    np.random.seed(42)

    num_trials = 500
    n_list = [100, 1000, 10000]

    fig, axes = plt.subplots(1, len(n_list), figsize=(15, 5), sharex=True)

    for ax, n in zip(axes, n_list):
        X_tcl = np.random.binomial(1, 0.5, (num_trials, n))
        sample_means = np.mean(X_tcl, axis=1)

        ax.hist(sample_means, bins=20, density=True, alpha=0.6, color="g", edgecolor="black", label="Moyennes empiriques")

        # Superposition d'une distribution normale
        mu, sigma = 0.5, np.sqrt(0.5 * 0.5 / n)
        x_vals = np.linspace(0.3, 0.7, 100)
        ax.plot(x_vals, stats.norm.pdf(x_vals, mu, sigma), color="red", lw=2, label="Densité normale")

        ax.axvline(0.5, color="black", linestyle="dashed", label=r"$\mathbb{E}[X] = 0.5$")
        ax.set_title(f"$n={n}$")

    axes[0].set_ylabel("Densité")
    fig.supxlabel("Valeur de la moyenne empirique")
    axes[-1].legend()
    fig.suptitle(r"Théorème Central Limite : distribution de $\overline{X}_n$")
    fig.tight_layout()
    plt.savefig("output/5_3.png")


if __name__ == "__main__":
    main()
