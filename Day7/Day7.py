from pathlib import Path
from re import compile
from collections import deque

def build_bag_dict( rules):
    bag_rules_regex = compile(r'([\w| ]+)bags contain (?:(\d+|no other)([\w| ]+)bags*)[, ]*(?:(\d+|no other)([\w| ]+)bags*)*')
    bag_dict = {}
    for rule in rules:
        matches = [match for match in bag_rules_regex.findall(rule)[0] if match and match != ' ']
        bag_dict[matches[0].strip()] = []
        for i in range(1, len(matches) - 1, 2):
            bag_dict[matches[0].strip()].append((matches[i + 1].strip(), int(matches[i].strip())))
    return bag_dict

def get_all_contained_bags(bag_to_search, bag_dict):
    if len(bag_dict[bag_to_search]) == 0:
        return []
    # all_bags = []
    # for bag in bag_dict[bag_to_search]:
    #     contained_bags = get_all_contained_bags(bag[0][0], bag_dict)
    #     for contained_bag in contained_bags:
    #         if contained_bag not in all_bags:
    #             all_bags.append(contained_bag)
    all_bags = [get_all_contained_bags(bag[0], bag_dict) for bag in bag_dict[bag_to_search]]
    # bags_in_this_bag = bag_dict[bag_to_search]
    return bag_dict[bag_to_search] + [item for sublist in all_bags for item in sublist]

bag_regulations = [rule.strip() for rule in open('Day7/bag_regulations.txt').readlines()]

direct_contents = build_bag_dict(bag_regulations)
all_contents = dict.fromkeys(direct_contents.keys(), [])
for colour, contents in direct_contents.items():
    all_contents[colour] = list(set([colour for colour, count in get_all_contained_bags(colour, direct_contents)]))


for colour, contents in all_contents.items():
    print(colour, contents)

bag_count = len([colour for colour, contents in all_contents.items() if 'shiny gold' in contents  ])

print("Part 1:", bag_count)

# test = list(set([colour for colour, count in get_all_contained_bags('light red', direct_contents)]))
# print(test)
# for colour,contents in direct_contents.items():
#     q = deque(contents)
#     while len(q) > 0:
#         bag = q.popleft()
#         all_contents[colour].append(bag)
#         q.append(bag)


# for bag in test:
#     print(bag)
# print(build_bag_dict(bag_regulations))
