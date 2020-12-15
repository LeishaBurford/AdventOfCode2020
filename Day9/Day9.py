from pathlib import Path

port_outputs = [int(number.strip()) for number in open('Day9/port_output.txt').readlines()]
preamble_size = 25

corrupted = -1
for i in range(preamble_size, len(port_outputs) - preamble_size):
    goal = port_outputs[i]
    found = False
    for x in range(i - preamble_size, i):
        for y in range(x + 1, i):
            if port_outputs[x] + port_outputs[y] == goal:
                found = True
                break
        if found:
            break
    if not found:
        corrupted = port_outputs[i]
        break

print('Part 1:', corrupted)

# find range that equals currupted
# add smallest and largest from the range

contiguous_set = []
for i in range(0, len(port_outputs)):
    for j in range(i + 1, len(port_outputs) - 1):
        if sum(port_outputs[i:j+1]) == corrupted:
            contiguous_set = port_outputs[i:j+1]
            break
    if contiguous_set != []:
        break

print("Part 2:", max(contiguous_set) + min(contiguous_set))
