#!/usr/bin/python
import random
from classes import Individual
from classes import Attribute

# random.seed(0)
NUM_ATTRIBUTES = 10
POPULATION_SIZE = 1000

# 1. Generate attributes
attributes = [Attribute() for i in range(NUM_ATTRIBUTES)]
# for attribute in attributes:
#     print(attribute.name + ": " + str(attribute.probability))

# 2. Distribute attributes to individuals
population = [Individual() for i in range(POPULATION_SIZE)]
for individual in population:
  for attribute in attributes:
      # Determine if they have the attribute
      if random.random() < attribute.probability:
         individual.add_attribute(attribute)

for attribute in attributes:
   print(str(attribute))

# 3. Select teams of certain size randomly from population

# 4. Calculate diversity score

# 5. Calculate probability of solving a problem with certain requirements
