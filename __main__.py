from population import Population
from display import draw

def main():
    population_size = 50
    # Create the initial population
    population = Population(population_size)

    while True:
        # Check the validity of the current population
        population.check_population()
        
        # Evaluate the current generation and get the best knight with its fitness value
        maxFit, bestSolution = population.evaluate()
        print(bestSolution.fitness)
        
        if maxFit == 64:  # Solution found
            break
        
        # Generate the new population
        population.create_new_generation()
    
    print(bestSolution.path)
    
    # Initialize the Pygame interface only after finding the solution
    knight_position = (0, 0)
    draw(knight_position, bestSolution.path)

if __name__ == "__main__":
    main()
