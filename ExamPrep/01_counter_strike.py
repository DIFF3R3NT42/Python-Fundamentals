initial_energy = int(input())
won_battles = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
        break
    energy_required = int(command)
    if won_battles % 3 == 0:
        if won_battles > 1:
            initial_energy += won_battles
    initial_energy -= energy_required
    if initial_energy < 0:
        initial_energy = 0
        break
    won_battles += 1

if initial_energy <= 0:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
