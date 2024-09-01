import random

def simulate_economy(steps):
    price = 100
    for step in range(steps):
        demand = random.uniform(0.9, 1.1)
        supply = random.uniform(0.9, 1.1)
        price = price * (demand / supply)
        print(f"Step {step + 1}: ${price:.2f} per unit")

simulate_economy(10)