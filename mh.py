#Monty Hall Problem
import random
d1 = "Door 1"
d2 = "Door 2"
d3 = "Door 3"
options = [d1, d2, d3]
print(options)
new_list = [options.remove(random.choice(options))]  #removal
goats = [options[0], options[1]]
goat_opened = [random.choice(goats)]
new_list_2 = [goats.remove(goat_opened[0])]
other_goat = [goats[0]]
car = []
if "Door 1" not in options:
    car.append(d1)
elif "Door 2" not in options:
    car.append(d2)
else:
    car.append(d3)
options = [d1, d2, d3]
guess = input("Monty Hall: choose one of the three doors (Door 1, Door 2, Door 3): ")
if guess == "Door 1":
    print("\nYou picked Door 1")
elif guess == "Door 2":
    print("\nYou picked Door 2")
elif guess == "Door 3":
    print("\nYou picked Door 3")
else:
    print("Invalid answer. Remember you have to enter Door 1, Door 2 or Door 3")
    exit()
print(options)
if goat_opened[0] == guess:
    while goat_opened[0] == guess:
        options = [d1, d2, d3]
        options.remove(car[0])
        goats = [options[0], options[1]]
        goat_opened = [random.choice(goats)]
        new_list_2 = [goats.remove(goat_opened[0])]
        other_goat = [goats[0]]
print(f"\nMonty Hall: Before opening {guess}, I am going to open a door on which there is a goat")
print(f"I opened {goat_opened[0]}")
options = ["Door 1", "Door 2", "Door 3"]
print(options)
options_with_goat_opened = []
for door in options:
    if door == goat_opened[0]:
        options_with_goat_opened.append("Goat")
    else:
        options_with_goat_opened.append(door)
print(options_with_goat_opened)
final_options = []
for item1 in options:
    if item1 == car[0]:
        final_options.append("Car")
    else:
        final_options.append("Goat")
print("\nNow I am going to offer you to switch or stay:")
if guess == car[0]:
    second_statement = input(f"Monty Hall: do you want to stick to {car[0]} or switch to {other_goat[0]}?(switch, stick) ")
    if second_statement == "stick":
        print(f"You won the car! {car[0]} had the car!")
        print(final_options)
    elif second_statement == "switch":
        print(f"You lost... {car[0]} had the car.")
        print(final_options)
    else:
        print("Invalid answer. Remember you have to enter stick or switch.")
        exit()
elif guess != car[0]: #so that it equals other goat
    second_statement = input(f"Monty Hall: do you want to stick to {other_goat[0]} or switch to {car[0]}?(switch, stick) ")
    if second_statement == "stick":
        print(f"You lost... {car[0]} had the car.")
        print(final_options)
    elif second_statement == "switch":
        print(f"You won the car! {car[0]} had the car!")
        print(final_options)
    else:
        print("Invalid answer. Remember you have to enter stick or switch.")
        exit()
