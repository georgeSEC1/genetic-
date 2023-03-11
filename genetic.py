import random
import string

# Define the target string that we want to evolve
TARGET_STRING = "this is a test sentnece"
with open("questions.conf", encoding='ISO-8859-1') as f:
	questions = f.readlines()
BASE_STRING = random.choice(questions)


# Define the size of the population, number of generations, and mutation rate
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.1

# Define the fitness function, which measures the similarity between a candidate string and the target string
def fitness(candidate):
    score = 0
    for i in range(len(TARGET_STRING)):
        if candidate[i] == TARGET_STRING[i]:
            score += 1
    return score

# Define the crossover function, which combines two candidate strings to create a new one
def crossover(parent1, parent2):
    split_point = random.randint(0, len(parent1) - 1)
    child = parent1[:split_point] + parent2[split_point:]
    return child

# Define the mutation function, which randomly modifies a candidate string
def mutate(candidate):
    mutated = ""
    for i in range(len(candidate)):
        if random.random() < MUTATION_RATE:
            mutated += random.choice(string.ascii_uppercase)
        else:
            mutated += candidate[i]
    return mutated

while(True):
	TARGET_STRING = input("USER: ")
# Generate an initial population of random candidate strings
	population = []
	for i in range(POPULATION_SIZE):
  	  candidate = ""
  	  for j in range(len(TARGET_STRING)):
  	      candidate += random.choice(BASE_STRING)
  	  population.append(candidate)

	# Evolve the population over multiple generations
	for generation in range(NUM_GENERATIONS):
  	  # Evaluate the fitness of each candidate string
  	  fitness_scores = [fitness(candidate) for candidate in population]
  	  # Select the best candidates for reproduction
  	  parents = [population[i] for i in sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i], reverse=True)[:10]]
  	  # Create offspring through crossover and mutation
  	  offspring = []
  	  while len(offspring) < POPULATION_SIZE - len(parents):
  	      parent1 = random.choice(parents)
  	      parent2 = random.choice(parents)
  	      child = crossover(parent1, parent2)
  	      mutated_child = mutate(child)
  	      offspring.append(mutated_child)
  	  # Replace the old population with the new one 
  	  population = parents + offspring

# Select the best candidate string as the result
	result = max(population, key=fitness)

# Print the result
	print(result)
