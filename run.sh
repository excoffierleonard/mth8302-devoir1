#!/bin/bash

set -e

cd "$(dirname "$0")"

for script in src/2.py src/3.py src/4.py src/5_1.py src/5_2.py src/5_3.py; do
    echo "Running $script..."
    uv run "$script"
done

echo "All scripts completed."

echo "Compiling LaTeX..."
cd report
TEX_NAME="MTH8302_ExcoffierLeonard_2085276_Devoir1"
pdflatex -interaction=nonstopmode "$TEX_NAME.tex" > /dev/null
pdflatex -interaction=nonstopmode "$TEX_NAME.tex" > /dev/null
cp "$TEX_NAME.pdf" "../$TEX_NAME.pdf"
echo "PDF written to $TEX_NAME.pdf"
