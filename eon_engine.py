# eon_engine.py
import random
from organism import Organism

def generate_population(size=50):
    return [Organism() for _ in range(size)]

def evaluate_fitness(org, food_level=1.0, danger_level=1.0):
    score = (
        org.speed * 0.4 +
        org.vision * 0.3 +
        (10 - org.metabolism) * 0.2 +
        org.energy * 0.1
    )
    score *= food_level
    score *= (2 - danger_level)
    return max(0.1, score)

def evolve_population(pop, food_level=1.0, danger_level=1.0, mutation_rate=0.1):
    fitness_scores = [evaluate_fitness(o, food_level, danger_level) for o in pop]
    ranked = sorted(list(zip(pop, fitness_scores)), key=lambda x: x[1], reverse=True)
    
    survivors = [o for o,_ in ranked[:len(ranked)//2]]
    
    new_pop = survivors.copy()
    while len(new_pop) < len(pop):
        baby = Organism(
            speed=random.choice(survivors).speed,
            vision=random.choice(survivors).vision,
            metabolism=random.choice(survivors).metabolism,
            energy=100
        )
        baby.mutate(rate=mutation_rate)
        new_pop.append(baby)
    
    return new_pop, max(fitness_scores), sum(fitness_scores)/len(fitness_scores)
