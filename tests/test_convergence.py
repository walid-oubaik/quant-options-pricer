import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from black_scholes import bs_price
from monte_carlo import mc_price

S0, K, r, sigma, T = 100, 100, 0.05, 0.20, 1.0

prix_bs = bs_price(S0, K, r, sigma, T, "call")
prix_mc, ic95 = mc_price(S0, K, r, sigma, T, 100_000, "call")

assert abs(prix_mc - prix_bs) < ic95, "Monte Carlo ne converge pas vers Black-Scholes"

print(f"Test réussi : BS = {prix_bs:.4f}, MC = {prix_mc:.4f} ± {ic95:.4f}")