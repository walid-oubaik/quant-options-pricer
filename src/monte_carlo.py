"""
monte_carlo.py
----------------
Pricing d'options européennes par simulation Monte Carlo.

Principe général : au lieu de résoudre l'équation de Black-Scholes analytiquement,
on simule un grand nombre de trajectoires possibles du prix de l'actif, on calcule
le gain (payoff) de l'option pour chaque scénario, puis on moyenne ces gains
actualisés. D'après la loi des grands nombres, cette moyenne converge vers le
prix théorique quand le nombre de simulations augmente,avec un intervalle de confiance à 95%.
"""
import numpy as np


def mc_price(S0, K, r, sigma, T, n_sims, option_type="call"):
    Z = np.random.default_rng().standard_normal(n_sims)
    S_T = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)

    if option_type == "call":
        payoffs = np.maximum(S_T - K, 0)
    else:
        payoffs = np.maximum(K - S_T, 0)

    discounted = np.exp(-r*T) * payoffs    
    prix = discounted.mean()                
    ic95 = 1.96 * discounted.std(ddof=1) / np.sqrt(n_sims)   

    return prix, ic95 
