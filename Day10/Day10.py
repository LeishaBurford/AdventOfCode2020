from pathlib import Path
from itertools import permutations

adapters = [int(number.strip()) for number in open('Day10/joltage_output.txt').readlines()]

adapters.append(max(adapters) + 3)

# outlet_joltage = 0
# adapters.sort()
# diff_dict = {1: 0, 2:0, 3:0}
# for adapter in adapters:
#     diff_dict[abs(outlet_joltage - adapter)] += 1
#     outlet_joltage = adapter

def get_joltage_diffs(adapters):
    outlet_joltage = 0
    adapters.sort()
    diff_dict = {1: 0, 2:0, 3:0}
    for adapter in adapters:
        joltage_diff = abs(outlet_joltage - adapter)
        if joltage_diff > 3 or joltage_diff < 1:
            return -1
        diff_dict[abs(outlet_joltage - adapter)] += 1
        outlet_joltage = adapter
    return diff_dict

diff_dict = get_joltage_diffs(adapters)
print("Part 1:", diff_dict[1] * diff_dict[3])

built_in_adapter = max(adapters)
adapters.remove(max(adapters))

adapter_permutations = list(permutations(adapters))
valid_arrangements = 0
for permutation in adapter_permutations:
    permutation.append(built_in_adapter)
    if(get_joltage_diffs(permutation) != -1):
        valid_arrangements += 1

print("Part 2:", valid_arrangements)
