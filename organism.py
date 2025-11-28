# organism.py
import random

class Organism:
    def __init__(self, speed=5.0, vision=5.0, metabolism=5.0, energy=100.0):
        self.speed = speed
        self.vision = vision
        self.metabolism = metabolism
        self.energy = energy

    def mutate(self, rate=0.1):
        def mutate_trait(x):
            return max(0.1, x + random.uniform(-rate, rate))

        self.speed = mutate_trait(self.speed)
        self.vision = mutate_trait(self.vision)
        self.metabolism = mutate_trait(self.metabolism)