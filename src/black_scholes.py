"""
black_scholes.py
----------------
Pricing d'options européennes par la formule fermée de Black-Scholes.
Calcule le prix (call/put) et les grecques (Delta, Gamma, Vega, Theta, Rho).
"""

import numpy as np
from scipy.stats import norm


def d1_d2(S0, K, r, sigma, T):
   d1=(np.log(S0/K)+(r+(sigma**2)/2)*T)/(sigma*np.sqrt(T))
   d2=d1-sigma*np.sqrt(T)
   return d1, d2
def bs_price(S0,K,r,sigma,T,option_type="call"):
   d1, d2 = d1_d2(S0, K, r, sigma, T)
   if option_type=="call" :
      prix=(S0*norm.cdf(d1))-(K*np.exp(-r*T)*norm.cdf(d2))
   else :
         prix=(K*np.exp(-r*T)*norm.cdf(-d2))-(S0*norm.cdf(-d1))
   return prix



    



