import numpy as np
import matplotlib.pyplot as plt

# Define parameters
initial_population = 100  # Initial population size
initial_resources = 1000  # Initial amount of resources (e.g., food)
population_growth_rate = 0.05  # Annual population growth rate
resource_growth_rate = 0.03  # Annual resource growth rate
resource_consumption_per_capita = 5  # Amount of resources consumed per capita

# Simulation settings
num_years = 100  # Number of years to simulate

# Initialize arrays to store population and resource data
population = np.zeros(num_years)
resources = np.zeros(num_years)

# Set initial values
population[0] = initial_population
resources[0] = initial_resources

# Simulate the Malthusian model
for year in range(1, num_years):
    population[year] = population[year - 1] * (1 + population_growth_rate)
    resources[year] = resources[year - 1] * (1 + resource_growth_rate) - population[year - 1] * resource_consumption_per_capita

    # Ensure resources cannot go negative
    if resources[year] < 0:
        resources[year] = 0

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(population, label='Population')
plt.plot(resources, label='Resources')
plt.xlabel('Years')
plt.ylabel('Amount')
plt.title('Malthusian Economics Simulation')
plt.legend()
plt.grid(True)
plt.show()
