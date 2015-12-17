"""
A Meep is a collection of diploid chromosomes, and a pair of gametes: an egg and a sperm.
"""

import collections
import webcolors
import random

Diploid = collections.namedtuple('Diploid', ('mother', 'father'))


class Meep(object):
    def __init__(self, genes):
        """

        :Type genes: list[Diploid]
        :return:
        """
        self.chromosomes = genes
        self.egg, self.sperm = meiosis(self.chromosomes)

    def express(self):
        print(self.chromosomes)

    def mate(self, father):
        """
        Mate self with a father and return their child.

        :type father: Meep
        :rtype: Meep
        """
        zygote = []
        for e, s in zip(self.egg, father.sperm):
            zygote.append(Diploid(e, s))
        return self.__class__(zygote)


class Moop(Meep):
    """
    A Moop is a monochrome Meep with a single chromosome that represents the color in HSV.
    """
    def express(self):
        """
        :rtype: String
        """
        phenotype = None
        for m, f in self.chromosomes:
            hm, sm, vm = m
            hf, sf, vf = f
            phenotype = (hm * hf, sm * sf, vm * vf)
        return webcolors.hsv_to_hex(phenotype)


def crossover(chromosome):
    """
    Possibly initiate genetic crossover.

    :param chromosome: Diploid
    :rtype: Diploid
    """
    daughter = []
    son = []
    for m, f in zip(chromosome.mother, chromosome.father):
        if not random.randint(0, 2):
            daughter.append(f)
            son.append(m)
        else:
            daughter.append(m)
            son.append(f)
    return Diploid(daughter, son)


def meiosis(chromosomes):
    """
    Randomly split the chromosome into egg and sperm.

    :type chromosomes: list[Diploid]
    :rtype: (list, list)
    """
    interphase = [crossover(ch) for ch in chromosomes]
    return [i.mother for i in interphase], [i.father for i in interphase]


def random_moop():
    """
    :rtype: Moop
    """
    mother = (random.random(), random.randint(40, 100) / 100.0, random.randint(40, 100) / 100.0)
    father = (random.random(), random.randint(40, 100) / 100.0, random.randint(40, 100) / 100.0)
    return Moop([Diploid(mother, father)])
