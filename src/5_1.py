import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    sns.set_theme()

    np.random.seed(42)

    # Paramètres
    n_list = [50, 500, 5000]  # Nombre d'échantillons
    num_trials = 2000  # Nombre de répétitions

    fig, axes = plt.subplots(1, len(n_list), figsize=(15, 5), sharex=True)

    for ax, n in zip(axes, n_list):
        # Génération des variables de Bernoulli
        X = np.random.binomial(1, 0.5, (num_trials, n))

        # Calcul des moyennes cumulatives
        means = np.cumsum(X, axis=1) / np.arange(1, n + 1)

        final_means = means[:, -1]  # Moyenne

        ax.hist(final_means, bins=20, density=True, alpha=0.6, color="b", edgecolor="black")
        ax.axvline(0.5, color="red", linestyle="dashed", label=r"$\mathbb{E}[X] = 0.5$")
        ax.set_title(rf"$n = {n}$")

    axes[0].set_ylabel("Densité")
    fig.supxlabel("Valeur de la moyenne empirique")
    axes[-1].legend()
    fig.suptitle(r"Loi faible des grands nombres : distribution de $\overline{X}_n$")
    fig.tight_layout()
    plt.savefig("output/5_1.png")


if __name__ == "__main__":
    main()
