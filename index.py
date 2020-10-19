from flying import Cardinal, Eagle, Osprey, Sandpiper, Swan
from swimming import BlueWhale, Flounder, Salmon, Shark, Tuna
from walking import Capybara, Cheetah, Elephant, RedFox, Tiger
from habitats import PettingZoo

varmint_village = PettingZoo("Varmint Village")

carlos = Capybara("Carlos", "Capybara", "morning", "cat food")
frank = Flounder("Frank", "Flounder", "algae")

varmint_village.animals.append(carlos)
varmint_village.animals.append(frank)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')