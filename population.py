from knight import Knight
import random
import heapq

class Population:
    def __init__(self,population_size):
        self.population_size=population_size
        self.generation=1
        self.knights = [Knight() for i in range(population_size)]

    def check_population(self):
        for k in self.knights:
            k.check_moves()

    def evaluate(self):
        bestKnight=None
        for i in self.knights:
            i.fitness=i.evaluate_fitness()
        bestKnight=max(self.knights, key=lambda knight: knight.fitness)
        return bestKnight.fitness,bestKnight
    
    def tournament_selection(self,size=3):

        selection = random.sample(range(0, self.population_size), size)
        selected_knights=[self.knights[i] for i in selection]

        two_highest = heapq.nlargest(2,selected_knights, key=lambda knight: knight.fitness)

        return two_highest.copy()
    
    def create_new_generation(self):
        new_population=[]
        while len(new_population) < self.population_size:
            parents=self.tournament_selection()
            p1= parents[0]
            p2= parents[1]
            offsprins=p1.chromosome.crossover(p2.chromosome)
            offsp1=offsprins[0].mutation()
            offsp2=offsprins[1].mutation()
            new_population.append(Knight(offsp1))
            new_population.append(Knight(offsp2))

        self.knights=new_population
        self.generation+=1



