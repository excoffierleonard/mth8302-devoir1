import numpy as np
from scipy.stats import poisson


def main():
    # Frequences observees
    x_vals = np.array([0, 1, 2, 3, 4, 5])
    freqs = np.array([7, 14, 12, 13, 6, 3])

    n = freqs.sum()
    sum_xi = (x_vals * freqs).sum()

    # EMV de lambda
    lambda_hat = sum_xi / n

    # Estimation de P(X = 2)
    p_x2 = poisson.pmf(2, lambda_hat)

    output_lines = [
        f"n = {n}",
        f"sum(x_i) = {sum_xi}",
        f"lambda_hat (EMV) = {lambda_hat:.6f}",
        f"P(X = 2) estimee = {p_x2:.6f}",
    ]
    with open("output/3.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(output_lines) + "\n")


if __name__ == "__main__":
    main()
