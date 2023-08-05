#!/usr/bin/python
import random
import statistics
from classes import Individual
from classes import Attribute

# random.seed(0)
NUM_ATTRIBUTES = 10
POPULATION_SIZE = 100
MIN_ATTRIBUTES_PER_PERSON = 1

# 1. Generate attributes
attributes = [Attribute() for i in range(NUM_ATTRIBUTES)]
attributes.sort(key=lambda x: x.probability)
# for attribute in attributes:
#     print(str(attribute))

# 2. Distribute attributes to individuals
population = [Individual() for i in range(POPULATION_SIZE)]
for individual in population:
  while len(individual.attributes) < MIN_ATTRIBUTES_PER_PERSON:
    for attribute in attributes:
        # Determine if they have the attribute
        if random.random() < attribute.probability:
          individual.add_attribute(attribute)

# for individual in population:
#    print(str(individual))

population_sorted_by_most_obscure = sorted(population, key=lambda x: min(map(lambda y: y.probability, x.attributes)))

population_sorted_by_diversity = sorted(population, key=lambda x: x.get_diversity_quotient())
for individual in population_sorted_by_most_obscure:
   print(str(individual))

# 3. Select teams of certain size randomly from population

# 4. Calculate probability of solving a problem with certain requirements
