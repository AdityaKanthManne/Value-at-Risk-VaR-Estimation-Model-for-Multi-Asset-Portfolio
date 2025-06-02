# main.py

import numpy as np
import matplotlib.pyplot as plt
from src.data.market_loader import fetch_price_data, calculate_log_returns
from src.var.var_estimators import historical_var, parametric_var, monte_carlo_var

# Portfolio configuration
tickers = ['SPY', 'GLD', 'TLT', 'BTC-USD']
weights = np.array([0.3, 0.3, 0.2, 0.2])  # Should sum to 1
confidence_levels = [0.95, 0.99]
horizons = [1, 10]

# Fetch and process data
price_df = fetch_price_data(tickers, start_date="2018-01-01")
returns_df = calculate_log_returns(price_df)

# Portfolio returns
portfolio_returns = returns_df @ weights
mean_vector = returns_df.mean()
cov_matrix = returns_df.cov()
portfolio_mean = portfolio_returns.mean()
portfolio_std = portfolio_returns.std()

# Results table
print("Value-at-Risk (VaR) Estimates")
print("--------------------------------------")
for horizon in horizons:
    for cl in confidence_levels:
        hist_var = historical_var(portfolio_returns * np.sqrt(horizon), cl)
        param_var = parametric_var(portfolio_mean * horizon, portfolio_std * np.sqrt(horizon), cl)
        mc_var = monte_carlo_var(mean_vector, cov_matrix, weights, horizon_days=horizon, confidence_level=cl)

        print(f"Horizon: {horizon}d | CL: {int(cl*100)}%")
        print(f"  Historical VaR: {hist_var:.4f}")
        print(f"  Parametric VaR: {param_var:.4f}")
