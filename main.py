import numpy as np

def generate_daily_demand(lam, n_days):
    return np.random.poisson(lam=lam, size=n_days)

def calc_results(demand_array):
    mean_demand = np.mean(demand_array)
    std_demand = np.std(demand_array, ddof=1)
    p5 = np.percentile(demand_array, 5)
    p95 = np.percentile(demand_array, 95)
    return mean_demand, std_demand, p5, p95

def simulate_monthly_demand(lam, n_days, n_simulations):
    totals = []
    for _ in range(n_simulations):
        daily = generate_daily_demand(lam, n_days)
        totals.append(np.sum(daily))
    return np.array(totals)

def main():
    # Inputs (with correct casting)
    lam = float(input("Input the mean daily demand (λ): "))
    n_days = int(input("Input the number of days to simulate: "))

    # Daily stats
    daily = generate_daily_demand(lam, n_days)
    mean_demand, std_demand, p5, p95 = calc_results(daily)
    print("Daily demand:", daily)
    print(f"Mean daily demand: {mean_demand:.2f}")
    print(f"Standard deviation: {std_demand:.2f}")
    print(f"5th percentile: {p5}")
    print(f"95th percentile: {p95}")

    # Monthly simulation
    n_simulations = 1000
    service_input = float(input("Desired service level (e.g., 95 or 0.95): "))
    service_pct = service_input * 100 if service_input <= 1 else service_input

    monthly_totals = simulate_monthly_demand(lam, n_days=30, n_simulations=n_simulations)
    optimal_inventory = np.percentile(monthly_totals, service_pct)

    print(f"\nOptimal inventory level for {service_pct:.1f}% service level: {optimal_inventory:.0f} units")

if __name__ == "__main__":
    main()
