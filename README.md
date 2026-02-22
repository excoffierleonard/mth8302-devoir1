# MTH8302 - Devoir 1: Rappel Mathématique

Devoir 1 du cours MTH8302 (Hiver 2026) - Polytechnique Montréal.

## Structure

```txt
src/           Scripts Python (2.py, 3.py, 4.py, 5_1.py, 5_2.py, 5_3.py)
report/        Source LaTeX (MTH8302_ExcoffierLeonard_2085276_Devoir1.tex)
output/        Sorties générées (figures, .txt)
lessons/       Diapositives du cours (référence)
run.sh         Script d'exécution complet
```

## Prérequis

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/) (gestionnaire de paquets Python)
- LaTeX (`pdflatex`) avec les paquets standards (`amsmath`, `babel`, `listings`, etc.)

## Installation

```bash
git clone https://github.com/excoffierleonard/mth8302-devoir1.git
cd mth8302-devoir1
uv sync
```

## Exécution

Tout en une commande :

```bash
./run.sh
```

Cela exécute tous les scripts Python (génère figures et fichiers texte dans `output/`), puis compile le rapport LaTeX. Le PDF final est généré à la racine du projet sous `MTH8302_ExcoffierLeonard_2085276_Devoir1.pdf`.

## Visualisation

Le rapport compilé se trouve dans [`MTH8302_ExcoffierLeonard_2085276_Devoir1.pdf`](MTH8302_ExcoffierLeonard_2085276_Devoir1.pdf) à la racine du projet après exécution de `run.sh`.
