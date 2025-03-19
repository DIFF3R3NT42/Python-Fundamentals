values = [int(x) for x in input().split()]
while True:
    command = input()
    if command == "end":
        break
    command_parts = command.split()
    action = command_parts[0]
    if len(command_parts) > 1:
        index1 = int(command_parts[1])
        index2 = int(command_parts[2])
    if action == 'swap':
        values[index1], values[index2] = values[index2], values[index1]

    if action == 'multiply':
        values[index1] = values[index1] * values[index2]

    if action == 'decrease':
        values = [value -1 for value in values]

print(", ".join(map(str, values)))
