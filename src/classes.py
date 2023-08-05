#!/usr/bin/python
import random
from wonderwords import RandomWord
import names
import statistics

randomWord = RandomWord()

class Attribute:
    """Calls representing an attribute"""

    def __init__(self) -> None:
        self.name = randomWord.word()
        self.probability = random.random()
        self.count = 0  # Indicates how often this attributes is actually found in the population

    def __str__(self) -> str:
        return self.name + "(" + str(self.probability) + "/" + str(self.count) + ")"

    def __eq__(self, __value: object) -> bool:
        return (
            self.name == __value.name and
            self.probability == __value.probability
        )

class Individual:
    """Class representing an individual"""

    def __init__(self) -> None:
        self.name = names.get_full_name()
        self.attributes = []

    def add_attribute(self, new_attribute: Attribute) -> None:
        self.attributes.append(new_attribute)
        new_attribute.count = new_attribute.count + 1

    def __str__(self) -> str:
        return_str = self.name + ": "
        for attribute in self.attributes:
            return_str = return_str + str(attribute) + ", "
        if len(self.attributes) > 0:
            return_str = return_str[:-2]
        return return_str

    def __eq__(self, __value: object) -> bool:
        return (
            self.name == __value.name and
            self.attributes == __value.attributes
        )

    def get_diversity_quotient(self) -> float:
        # Other tries were
        # - max(map(lambda x: x.probability, self.attributes))
        # - min(map(lambda x: x.probability, self.attributes))
        # - sum(map(lambda y: y.probability, self.attributes))
        return statistics.mean(map(lambda y: y.probability, self.attributes))


