# src/var/var_estimators.py

import numpy as np
from scipy.stats import norm

def historical_var(portfolio_returns, confidence_level=0.95):
    """
    Computes Historical Simulation VaR from return series.
    """
    return np.percentile(portfolio_returns, (1 - confidence_level) * 100)

def parametric_var(portfolio_mean, portfolio_std, confidence_level=0.95):
    """
    Computes Parametric Normal VaR.
    """
    z_score = norm.ppf(1 - confidence_level)
    return portfolio_mean + z_score * portfolio_std

def monte_carlo_var(mean_return, cov_matrix, weights, num_simulations=100000, confidence_level=0.95, horizon_days=1):
    """
    Computes Monte Carlo Simulated VaR for multi-asset portfolio.

    Parameters:
    - mean_return: vector of asset means
    - cov_matrix: covariance matrix of returns
    - weights: portfolio weights
    - horizon_days: holding period
    """
    port_mean = np.dot(weights, mean_return) * horizon_days
    port_cov = cov_matrix * horizon_days

    simulated_returns = np.random.multivariate_normal(mean_return, cov_matrix, size=num_simulations)
    simulated_portfolio = simulated_returns @ weights
    return np.percentile(simulated_portfolio, (1 - confidence_level) * 100)
