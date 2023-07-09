from switch_float import switch
import constants as c
import random
import math
import numpy as np
import sys
import pickle

class INDIVIDUAL:
    def __init__(self, i, j):
        self.N = 30
        self.genome1 = np.round(np.random.uniform(1, 10, size=self.N), decimals=1)
        self.genome2 = np.random.randint(low=0, high=self.N)
        while self.genome2 == 27 or self.genome2 == 3:
            self.genome2 = np.random.randint(low=0, high=self.N)
        self.genome3 = np.random.randint(low=0, high=self.N)
        while self.genome3 == self.genome2 or self.genome3 == 27 or self.genome3 == 3:
            self.genome3 = np.random.randint(low=0, high=self.N)
        self.fitness = 0
        self.gains = np.zeros(4)
        self.ID = i
        self.species = j
    
    def Compute_Fitness(self, show=False):
        # wait for the simulation to end and get the fitness
        results = switch.evaluate(self.genome1, self.genome2, self.genome3)
        self.fitness = results[0]
        self.gains = np.array(results[1:5])
        if show:
            print("fitness is:")
            print(self.fitness)
        return self.fitness
    
    def Mutate(self):
        type = random.random()
        if type < 0.75:
            # choose one particle randomly
            particle = np.random.randint(low=0, high=self.N)
            variation = np.random.normal(loc=0.0, scale=0.1)
            candidate = np.round(self.genome1[particle] + variation, decimals=1)
            if candidate<1:
                candidate = 1
            elif candidate>10:
                candidate = 10
            newGenome = np.array(self.genome1)
            newGenome[particle] = candidate
            while np.all(newGenome == self.genome1):
                particle = np.random.randint(low=0, high=self.N)
                variation = np.random.normal(loc=0.0, scale=0.1)
                candidate = np.round(self.genome1[particle] + variation, decimals=1)
                if candidate<1:
                    candidate = 1
                elif candidate>10:
                    candidate = 10
                newGenome[particle] = candidate

            self.genome1 = newGenome

        else:
            type2 = random.random()
            if type2 < 0.5:
                newGenome = np.random.randint(low=0, high=self.N)
                while newGenome == self.genome2 or newGenome == self.genome3 or newGenome == 27 or newGenome == 3:
                    newGenome = np.random.randint(low=0, high=self.N)
                self.genome2 = newGenome
            else:
                newGenome = np.random.randint(low=0, high=self.N)
                while newGenome == self.genome2 or newGenome == self.genome3 or newGenome == 27 or newGenome == 3:
                    newGenome = np.random.randint(low=0, high=self.N)
                self.genome3 = newGenome
        
    
    def Print(self):
        print('[', self.ID, self.fitness, ']', end=' ')
        
    
    def Save(self):
        f = open('savedFitnessSeed.dat', 'ab')
        pickle.dump(self.fitness , f)
        f.close()
    
    def SaveBest(self):
        f = open('savedBestsSeed.dat', 'ab')
        pickle.dump([self.genome1, self.genome2, self.genome3] , f)
        f.close()