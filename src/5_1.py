import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    sns.set_theme()

    np.random.seed(42)

    # Paramètres
    n = 100  # Nombre d'échantillons
    num_trials = 2000  # Nombre de répétitions

    # Génération des variables de Bernoulli
    X = np.random.binomial(1, 0.5, (num_trials, n))

    # Calcul des moyennes cumulatives
    means = np.cumsum(X, axis=1) / np.arange(1, n + 1)

    final_means = means[:, -1]  # Moyenne

    plt.figure(figsize=(10, 5))
    plt.hist(
        final_means, bins=20, density=True, alpha=0.6, color="b", edgecolor="black"
    )
    plt.axvline(0.5, color="red", linestyle="dashed", label=r"$\mathbb{E}[X] = 0.5$")
    plt.title(r"Loi faible des grands nombres : distribution de $\overline{X}_n$")
    plt.xlabel("Valeur de la moyenne empirique")
    plt.ylabel("Densité")
    plt.legend()
    plt.savefig("output/5_1.png")


if __name__ == "__main__":
    main()
