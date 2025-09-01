import random

def fitness_function(x):
    return x**2

def initialize_population(size, x_min, x_max):   # fixed: 'sixe' → 'size'
    return [random.uniform(x_min, x_max) for _ in range(size)]

def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        return random.choice(population)
    pick = random.uniform(0, total_fitness)
    current = 0.0
    for individual, fitness in zip(population, fitnesses):  # fixed: added 'fitnesses'
        current += fitness
        if current >= pick:
            return individual
    return population[-1]   # fixed: moved outside loop

def crossover(parent1, parent2):
    alpha = random.random()
    return alpha * parent1 + (1 - alpha) * parent2

def mutate(individual, mutation_rate, x_min, x_max):
    if random.random() < mutation_rate:
        x = individual + random.uniform(-1, 1)
        return max(x_min, min(x, x_max))
    return individual

def genetic_algorithm(pop_size, x_min, x_max, mutation_rate, generations):
    population = initialize_population(pop_size, x_min, x_max)
    for gen in range(generations):
        fitnesses = [fitness_function(ind) for ind in population]
        best = population[fitnesses.index(max(fitnesses))]
        print(f"Generation {gen+1} : Best = {best:4f}, Fitness = {fitness_function(best):4f}")
        new_population = []

        for _ in range(pop_size):
            p1 = selection(population, fitnesses)
            p2 = selection(population, fitnesses)
            child = crossover(p1, p2)
            child = mutate(child, mutation_rate, x_min, x_max)
            new_population.append(child)

        population = new_population   # fixed: moved outside inner loop

    fitnesses = [fitness_function(ind) for ind in population]
    best = population[fitnesses.index(max(fitnesses))]
    return best

if __name__ == "__main__":
    pop_size = 10
    x_min, x_max = -10, 10
    mutation_rate = 0.1
    generations = 20

    best = genetic_algorithm(pop_size, x_min, x_max, mutation_rate, generations)
    print("\n Final Result")
    print(f"Best solution: {best}, Fitness : {fitness_function(best)}")
