"""
main.py
----------------
Script de comparaison entre le prix Black-Scholes (exact) et son estimation
par Monte Carlo, pour une gamme de strikes, avec génération d'un graphique.
"""
import numpy as np
import matplotlib.pyplot as plt

from black_scholes import bs_price
from monte_carlo import mc_price

# Paramètres fixes
S0, r, sigma, T = 100, 0.05, 0.20, 1.0

# On fait varier le strike K
strikes = np.linspace(70, 130, 20)

prix_bs = []
prix_mc = []
ic_mc = []

for K in strikes:
    prix_bs.append(bs_price(S0, K, r, sigma, T, "call"))
    p, ic = mc_price(S0, K, r, sigma, T, 100000, "call")
    prix_mc.append(p)
    ic_mc.append(ic)

# Graphique
plt.figure(figsize=(8, 5))
plt.plot(strikes, prix_bs, label="Black-Scholes (exact)", linewidth=2)
plt.errorbar(strikes, prix_mc, yerr=ic_mc, fmt="o", label="Monte Carlo (avec IC95%)", color="orange")
plt.xlabel("Strike (K)")
plt.ylabel("Prix de l'option (call)")
plt.title("Comparaison Black-Scholes vs Monte Carlo")
plt.legend()
plt.grid(True)
plt.savefig("figures/comparaison_bs_mc.png", dpi=150)
plt.show()

print("Graphique sauvegardé dans figures/comparaison_bs_mc.png")