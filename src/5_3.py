import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def main():
    sns.set_theme()

    np.random.seed(42)

    num_trials = 500
    for n in [100, 1000, 10000]:
        X_tcl = np.random.binomial(1, 0.5, (num_trials, n))
        sample_means = np.mean(X_tcl, axis=1)

        plt.figure(figsize=(10, 5))
        plt.hist(
            sample_means,
            bins=20,
            density=True,
            alpha=0.6,
            color="g",
            edgecolor="black",
            label="Moyennes empiriques",
        )

        # Superposition d'une distribution normale
        mu, sigma = 0.5, np.sqrt(0.5 * 0.5 / n)
        x_vals = np.linspace(0.3, 0.7, 100)
        plt.plot(
            x_vals,
            stats.norm.pdf(x_vals, mu, sigma),
            color="red",
            lw=2,
            label="Densité normale",
        )

        plt.axvline(
            0.5, color="black", linestyle="dashed", label=r"$\mathbb{E}[X] = 0.5$"
        )
        plt.title(f"Théorème Central Limite : Distribution pour $n={n}$")
        plt.xlabel("Valeur de la moyenne empirique")
        plt.ylabel("Densité")
        plt.legend()
        plt.savefig(f"output/5_3_n{n}.png")


if __name__ == "__main__":
    main()
