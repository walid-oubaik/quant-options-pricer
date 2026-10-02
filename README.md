# Simulateur d'options — Black-Scholes & Monte Carlo

Projet personnel de pricing d'options européennes, comparant la formule
fermée de Black-Scholes à une simulation Monte Carlo de l'équation
différentielle stochastique sous-jacente.

## Contexte

Ce projet s'inscrit dans mon objectif de carrière en quant trading et risk management. Il s'appuie sur des bases vues en prépa  — probabilités, équations différentielles, et analyse numérique — que j'ai approfondies par moi-même pour aborder des notions plus avancées non couvertes par le programme, comme le calcul stochastique (mouvement brownien, équations différentielles stochastiques) et la simulation Monte Carlo . Ce projet m'a permis de passer d'un modèle mathématique théorique à un outil de calcul concret et vérifiable, une démarche centrale dans ces métiers.

## Objectifs

- [ ] Implémenter le prix fermé de Black-Scholes (call/put)
- [ ] Implémenter les grecques (Delta, Gamma, Vega, Theta)
- [ ] Implémenter une simulation Monte Carlo du prix
- [ ] Comparer et faire converger les deux méthodes
- [ ] Documenter les résultats avec des graphiques

## Théorie

On suppose que le prix d'une action suit une équation différentielle stochastique (EDS) :

$$dS_t = r\,S_t\,dt + \sigma\,S_t\,dW_t$$

Cette équation dit que la variation du prix à chaque instant est composée de deux parties : une tendance déterministe ($r\,S_t\,dt$), et un terme aléatoire ($\sigma\,S_t\,dW_t$) dont l'intensité est contrôlée par la volatilité $\sigma$. Le terme $W_t$ est un mouvement brownien : une trajectoire aléatoire continue, dont les incréments suivent une loi normale.

En résolvant cette équation, on obtient une formule directe pour le prix à un instant futur $T$ :

$$S_T = S_0\,e^{(r-\sigma^2/2)T + \sigma\sqrt{T}\,Z}, \quad Z \sim \mathcal{N}(0,1)$$

Autrement dit, le prix futur est le prix actuel multiplié par une exponentielle contenant une dérive et un terme aléatoire gaussien. C'est cette formule qui permet de simuler des scénarios futurs plausibles pour Monte Carlo.

Le prix d'une option est l'espérance actualisée de son gain à l'échéance. En intégrant cette espérance analytiquement (en utilisant que $S_T$ suit une loi log-normale), on obtient une formule fermée, sans simulation :

$$C = S_0\,N(d_1) - K\,e^{-rT}\,N(d_2)$$

$$d_1 = \frac{\ln(S_0/K) + (r+\sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$

où $N(\cdot)$ est la fonction de répartition de la loi normale. C'est cette formule que j'ai implémentée dans `black_scholes.py`, vérifiée par comparaison avec une estimation par simulation Monte Carlo.

## Structure du projet

```
quant-options-pricer/
├── src/
│   ├── black_scholes.py    # Pricing fermé + grecques
│   └── monte_carlo.py      # Simulation Monte Carlo
├── tests/
│   └── test_convergence.py # Vérifie que MC converge vers Black-Scholes
├── figures/                 # Graphiques générés
├── notebooks/                # Explorations / brouillons
├── requirements.txt
└── README.md
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate   # sous Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Utilisation

<!-- TODO : une fois ton code écrit, explique comment le lancer. -->

## Résultats

<!-- TODO : insère tes graphiques ici une fois générés, avec un
     commentaire sur ce qu'ils montrent (convergence, précision,
     comportement des grecques...). -->

## Pistes d'extension

- [ ] Pricer une option path-dependent (asiatique, barrière)
- [ ] Résoudre l'EDP de Black-Scholes par différences finies
- [ ] Modèle avec volatilité stochastique (Heston)

## Auteur

<!-- Ton nom, éventuellement un lien vers ton profil / CV -->
