import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    sns.set_theme()

    np.random.seed(42)

    # LOI FORTE DES GRANDS NOMBRES: Trajectoires individuelles
    # Paramètres
    n = 10  # Nombre d'échantillons
    num_trials = 5  # Nombre de répétitions

    # Génération des variables de Bernoulli
    X = np.random.binomial(1, 0.5, (num_trials, n))

    # Calcul des moyennes cumulatives
    means = np.cumsum(X, axis=1) / np.arange(1, n + 1)

    plt.figure(figsize=(10, 5))
    for i in range(5):  # Tracer 5 trajectoires différentes
        plt.plot(means[i, :], alpha=0.7, label=f"Trajectoire {i+1}")

    plt.axhline(0.5, color="red", linestyle="dashed", label=r"$\mathbb{E}[X] = 0.5$")
    plt.title(r"Loi forte des grands nombres : trajectoires de $\overline{X}_n$")
    plt.xlabel(r"Nombre d'échantillons $n$")
    plt.ylabel(r"Moyenne empirique $\overline{X}_n$")
    plt.legend()
    plt.savefig("output/5_2.png")


if __name__ == "__main__":
    main()
