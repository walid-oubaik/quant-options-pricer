"""
test_convergence.py
-------------------
Vérifie que le prix Monte Carlo converge vers le prix exact de Black-Scholes :
l'écart doit être inférieur à l'intervalle de confiance à 95%.
"""

import sys
import os

# Permet d'importer les modules du dossier src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from black_scholes import bs_price
from monte_carlo import mc_price

# Paramètres de test
S0, K, r, sigma, T = 100, 100, 0.05, 0.20, 1.0

# Prix exact et estimation Monte Carlo
prix_bs = bs_price(S0, K, r, sigma, T, "call")
prix_mc, ic95 = mc_price(S0, K, r, sigma, T, 100_000, "call")

# Vérification : l'écart doit rester dans l'intervalle de confiance
assert abs(prix_mc - prix_bs) < ic95, "Monte Carlo ne converge pas vers Black-Scholes"

print(f"Test réussi : BS = {prix_bs:.4f}, MC = {prix_mc:.4f} ± {ic95:.4f}")