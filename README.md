# Value-at-Risk (VaR) Estimation Model for Multi-Asset Portfolio

This project provides a comprehensive framework to compute Value-at-Risk (VaR) for a multi-asset portfolio using multiple techniques including Historical Simulation, Parametric Normal VaR, and Monte Carlo Simulation. It evaluates downside portfolio risk at various confidence levels and time horizons using only open-source tools.

---

## Objectives

- Estimate 1-day and 10-day VaR at 95% and 99% confidence levels
- Implement Historical Simulation, Parametric Gaussian VaR, and Monte Carlo Simulation
- Preserve asset correlation using covariance matrix or copulas
- Analyze portfolio volatility and tail losses under stress

---

## Supported Methods

| Method                | Description                                  |
|----------------------|----------------------------------------------|
| Historical Simulation | Direct sampling of historical return data   |
| Parametric Normal     | Closed-form solution using mean and std     |
| Monte Carlo Simulation| Random paths from multivariate distribution |

---

## Portfolio Coverage

This model supports any freely available market asset. Default example includes:

- SPY (S&P 500 ETF)
- GLD (Gold ETF)
- TLT (US Treasury Bonds ETF)
- BTC-USD (Bitcoin)

---

## Technology Stack

- Python (pandas, numpy, matplotlib)
- yfinance for free historical data
- scipy.stats for normal distribution
- seaborn for optional visualization

---

## Run Instructions

```bash
git clone https://github.com/AdityaKanthManne/Value-at-Risk-VaR-Estimation-Model-for-Multi-Asset-Portfolio.git
cd Value-at-Risk-VaR-Estimation-Model-for-Multi-Asset-Portfolio
pip install -r requirements.txt
python main.py
```

---

## Outputs

- 1-day and 10-day VaR values at 95% and 99% confidence levels
- Return distribution histograms and loss tails
- Stress scenarios and correlation matrices
- Exportable charts and CSVs

---

## License

MIT License © 2025 Aditya Kanth Manne  
https://github.com/AdityaKanthManne

---

## Contributions

Contributions are welcome. Extensions can include Conditional VaR, Cornish-Fisher VaR, and copula-based VaR modeling.
