class Account:
    def __init__(self):
        self.positions = {}
    
    def add_position(self, position, quantity, price):
        if position in self.positions:
            current_quantity = self.positions[position]["quantity"]
            current_price = self.positions[position]["average_purchase_price"]
            self.positions[position]["quantity"] += current_quantity
        else:
            self.positions[position] = {
                "quantity": quantity,
            }
    
    def remove_position(self, position, quantity):
        try:
            if position not in self.positions:
                print(f"Position {position} not found in portfolio.")
            current_quantity = self.positions[position]["quantity"]
            if quantity > current_quantity:
                raise ValueError(f"Cannot remove {quantity} shares of {position}. Only {current_quantity} shares are held.")
            if quantity == current_quantity:
                del self.positions[position]
            else:
                self.positions[position]["quantity"] -= quantity
        except ValueError as e:
            print(e)
        finally:
            print(f"Position removed successfully. ( id : {position['id']} )")

    def get_total_value(self):
        total_value = 0
        for position in self.positions:
            total_value += position.quantity * position.price
        return total_value
    
# class AccountOptimiser:
#   def __init__(self, holdings, goals):
#     self.holdings = holding
#     self.risk_reward = goals.risk_reward

#   def optimise_weights(self):
#     # Perform account optimisation here
#     # Access account attributes and risk model for optimisation
#     # Example placeholder code
#     optimal_weights = [0.25, 0.25, 0.25, 0.25]  # Placeholder example weights
#     return optimal_weights