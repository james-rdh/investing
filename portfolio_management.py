class Portfolio:
    def __init__(self):
        self.cash_balance = 0
        self.positions = {}
    
    def add_cash(self, amount):
        self.cash_balance += amount
    
    def remove_cash(self, amount):
        self.cash_balance -= amount
    
    def add_position(self, symbol, quantity, purchase_price):
        if symbol in self.positions:
            self.positions[symbol]["quantity"] += quantity
        else:
            self.positions[symbol] = {
                "quantity": quantity,
                "average_price": purchase_price
            }
        self.cash_balance -= quantity * purchase_price
    
    def remove_position(self, symbol, quantity):
        try:
            if symbol not in self.positions:
                raise ValueError(f"Position {symbol} not found in portfolio.")
            current_quantity = self.positions[symbol]["quantity"]
            if quantity > current_quantity:
                raise ValueError(f"Cannot remove {quantity} shares of {symbol}. Only {current_quantity} shares are held.")
            if quantity == current_quantity:
                del self.positions[symbol]
            else:
                self.positions[symbol]["quantity"] -= quantity
                # Here, you'll likely need to adjust the 'purchase_data' 
                # to reflect the shares being sold. The specific logic will 
                # depend on your accounting method (e.g., FIFO, LIFO).

            # Update cash balance (assuming a sell transaction at current market price)
            current_price = self.get_current_price(symbol)  # You'll need to implement this method
            self.cash_balance += quantity * current_price
        except ValueError as e:
            print(e)
        finally:
            print("Position removed successfully.")

    def get_total_value(self):
        total_value = self.cash_balance
        for symbol in self.positions:
            total_value += symbol.quantity * symbol.purchase_data.priceposition()
        return total_value
    
# class PortfolioOptimiser:
#   def __init__(self, portfolio, risk_reward):
#     self.portfolio = portfolio
#     self.risk_reward = risk_reward

#   def optimise_weights(self):
#     # Perform portfolio optimisation here
#     # Access portfolio attributes and risk model for optimisation
#     # Example placeholder code
#     optimal_weights = [0.25, 0.25, 0.25, 0.25]  # Placeholder example weights
#     return optimal_weights