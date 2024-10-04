# class PerformanceAnalyser:
#     def __init__(self, portfolio):
#         self.portfolio = portfolio
    
#     def calculate_cumulative_returns(self):
#         cumulative_returns = (1 + self.returns).cumprod() - 1
#         return cumulative_returns
    
#     def calculate_annualized_returns(self):
#         total_returns = self.returns.sum()
#         num_periods = len(self.returns)
#         annualized_returns = (1 + total_returns) ** (252 / num_periods) - 1
#         return annualized_returns
    
#     def calculate_volatility(self):
#         volatility = self.returns.std() * (252 ** 0.5)
#         return volatility
    
#     def calculate_sharpe_ratio(self, risk_free_rate):
#         excess_returns = self.returns - risk_free_rate
#         sharpe_ratio = excess_returns.mean() / excess_returns.std() * (252 ** 0.5)
#         return sharpe_ratio

# class RiskAnalyser:
#     def __init__(self, portfolio):
#         self.portfolio = portfolio

#     def calculate_volatility(self):
#         volatility = np.std(self.returns) * np.sqrt(252)
#         return volatility

#     def calculate_beta(self, benchmark_returns):
#         covariance = np.cov(self.returns, benchmark_returns)[0][1]
#         benchmark_variance = np.var(benchmark_returns)
#         beta = covariance / benchmark_variance
#         return beta