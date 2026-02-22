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
pdflatex -interaction=nonstopmode main.tex > /dev/null
pdflatex -interaction=nonstopmode main.tex > /dev/null
cp main.pdf ../output/main.pdf
echo "PDF written to output/main.pdf"
