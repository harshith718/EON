# run_eon_simulation.py
import os
import matplotlib.pyplot as plt
from eon_engine import generate_population, evolve_population

GENS = 60
POP_SIZE = 50

os.makedirs("../graphs", exist_ok=True)
os.makedirs("../logs", exist_ok=True)

population = generate_population(size=POP_SIZE)

max_scores = []
avg_scores = []

for gen in range(GENS):
    population, max_f, avg_f = evolve_population(
        population,
        food_level=1.0,
        danger_level=1.0,
        mutation_rate=0.15
    )
    max_scores.append(max_f)
    avg_scores.append(avg_f)

plt.figure(figsize=(7,4))
plt.plot(max_scores, label="Max Fitness")
plt.plot(avg_scores, label="Avg Fitness")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("EON Population Fitness Over Time")
plt.legend()
plt.tight_layout()
plt.savefig("../graphs/eon_fitness_curve.png")
plt.close()

print("EON simulation complete. Graph saved to ../graphs/eon_fitness_curve.png")
