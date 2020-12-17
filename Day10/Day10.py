from pathlib import Path
from itertools import chain, combinations

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

# Stolen from reddit :'(
adapter_combo_dict = {0: 1}
for adapter in adapters:
    adapter_combo_dict[adapter] = adapter_combo_dict.get(adapter-3,0) + adapter_combo_dict.get(adapter-2,0) + adapter_combo_dict.get(adapter-1,0)

print("Part 2:", adapter_combo_dict[adapters[-1]])
