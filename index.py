from flying import Cardinal, Eagle, Osprey, Sandpiper, Swan
from swimming import BlueWhale, Flounder, Salmon, Shark, Tuna
from walking import Capybara, Cheetah, Elephant, RedFox, Tiger
from habitats import Aviary, Pasture, PettingZoo

christy = Cardinal("Christy", "Cardinal", "seeds")

varmint_village = PettingZoo("Varmint Village", "A fun place to see all types of cute animals!")
cow_wow = Pasture("Cow Wow!", "A super fun place to see cows and horses!")

carlos = Capybara("Carlos", "Capybara", "morning", "cat food")
frank = Flounder("Frank", "Flounder", "algae")

eric = Elephant("Eric", "Elephant", "evening", "dog food")
chester = Cheetah("Chester", "Cheetah", "morning", "cheetos")

varmint_village.add_animals(carlos)
varmint_village.add_animals(frank)

cow_wow.add_animals(eric)
cow_wow.add_animals(chester)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in cow_wow.animals:
    print(f'You can find {animal.name} the {animal.species} in {cow_wow.attraction_name}')