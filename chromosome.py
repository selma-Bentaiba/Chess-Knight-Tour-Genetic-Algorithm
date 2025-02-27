import random

def flip(chromosome,gene):
    chromosome[gene] = random.choice([i for i in range(1, 9) if i != chromosome[gene]])


class Chromosome:

    def __init__(self,genes=None):
        if genes==None:
            self.genes=[random.randint(1,8) for i in range(63)]
        else:
            self.genes=genes



    def crossover(self,partner):
        point=random.randint(1,62)
        
        o1=Chromosome(self.genes[:point]+partner.genes[point:])
        o2=Chromosome(partner.genes[:point]+self.genes[point:])

        return [o1,o2]
    

    
    def mutation(self,mutationProb=0.001):
        
        for gene in range(len(self.genes)):
            prob_mutate=random.random()
            if prob_mutate<=mutationProb:
                flip(self.genes,gene)