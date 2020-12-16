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

def has_a_chance(adapters):
    # for i in range(0, len(adapters)):
    #     for j in range(i + 1, len(adapters) - 1):
    #         if abs(adapters[j] - adapters[i]) > 3 or abs(adapters[j] - adapters[i] < 1):
    #             return False
    for i,j in zip(range(0, len(adapters)), range(1, len(adapters) - 1)):
        if abs(adapters[j] - adapters[i]) > 3 or abs(adapters[j] - adapters[i] < 1):
                return False
    return True

# def powerset(iterable):
#     s = list(iterable)
#     valid_arrangements = []
#     for r in range(1, len(s) + 1):
#         arrangements = list(combinations(s, r))
#         for combination in arrangements:
#             if has_a_chance(list(combination)):
#                 valid_arrangements.append(list(combination))
#     return valid_arrangements
    # return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1) if has_a_chance(list(combinations(s, r))))
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

diff_dict = get_joltage_diffs(adapters)
print("Part 1:", diff_dict[1] * diff_dict[3])




# memo = {0: 1}
# for r in adapters:
#     memo[r] = memo.get(r-3,0) \
#           + memo.get(r-2,0) \
#           + memo.get(r-1,0)
#     print(r, memo)
# print(memo[adapters[-1]])


built_in_adapter = max(adapters)
# adapters.remove(max(adapters))
adapters.append(0)
adapters.sort()
required_adapters = dict.fromkeys(adapters, False)
required_adapters[built_in_adapter] = True
required_adapters[0] = True

for index in range(1, len(adapters) - 1):
    if abs(adapters[index - 1] - adapters[index]) >= 3 or abs(adapters[index + 1] - adapters[index]) >= 3:
        required_adapters[adapters[index]] = True

powerset_not_required = [list(combo) for combo in list(powerset([adapter for adapter,is_required in required_adapters.items() if not is_required]))]
print(len(powerset_not_required))
# print(required_adapters)
# adapter_powerset = [list(arrangement) for arrangement in list(powerset(adapters))]
# # print(len(adapter_powerset))
# valid_arrangements = 0
# for arrangement in adapter_powerset:
#     arrangement.append(built_in_adapter)
#     if(get_joltage_diffs(arrangement) != -1):
#         valid_arrangements += 1

# print("Part 2:", valid_arrangements)
# print(adapter_powerset)
