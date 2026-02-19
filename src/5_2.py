import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    sns.set_theme()

    np.random.seed(42)

    # LOI FORTE DES GRANDS NOMBRES: Trajectoires individuelles
    # Paramètres
    n = 1000  # Nombre d'échantillons
    num_trials_list = [1, 5, 10, 1000]  # Nombre de répétitions

    fig, axes = plt.subplots(1, len(num_trials_list), figsize=(18, 5), sharex=True)

    for ax, num_trials in zip(axes, num_trials_list):
        # Génération des variables de Bernoulli
        X = np.random.binomial(1, 0.5, (num_trials, n))

        # Calcul des moyennes cumulatives
        means = np.cumsum(X, axis=1) / np.arange(1, n + 1)

        for i in range(num_trials):  # Tracer les trajectoires différentes
            ax.plot(means[i, :], alpha=0.7)

        ax.axhline(0.5, color="red", linestyle="dashed", label=r"$\mathbb{E}[X] = 0.5$")
        ax.set_title(r"$N_{\mathrm{rep}} = %d$" % num_trials)
    axes[0].set_ylabel(r"Moyenne empirique $\overline{X}_n$")
    fig.supxlabel(r"Nombre d'échantillons $n$")
    fig.suptitle(r"Loi forte des grands nombres : trajectoires de $\overline{X}_n$")
    fig.tight_layout()
    plt.savefig("output/5_2.png")


if __name__ == "__main__":
    main()
