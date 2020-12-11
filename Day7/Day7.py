from pathlib import Path
from re import compile
from collections import deque

# def build_bag_dict( rules):
#     bag_rules_regex = compile(r'([\w| ]+)bags contain (?:(\d+|no other)([\w| ]+)bags*)[, ]*(?:(\d+|no other)([\w| ]+)bags*)*')
#     bag_dict = {}
#     for rule in rules:
#         matches = [match for match in bag_rules_regex.findall(rule)[0] if match and match != ' ']
#         bag_dict[matches[0].strip()] = {}
#         for i in range(1, len(matches) - 1, 2):
#             bag_dict[matches[0].strip()][matches[i + 1].strip()] = int(matches[i].strip())
#     return bag_dict

def build_bag_dict( rules):
    outer_bag_regex = compile(r'([\w| ]+)bags contain ')
    inner_bag_regex = compile(r'(?:(\d+|no other)([\w| ]+)bags*)')
    bag_dict = {}
    for rule in rules:
        # all_matches = bag_rules_regex.findall(rule)[0]
        # matches = [match for match in all_matches if match != '' and match != ' ']
        outer_bag = outer_bag_regex.findall(rule)[0].strip()
        inner_bag_rule = rule[rule.find('contain')+ len('contain'):]
        matches = inner_bag_regex.findall(inner_bag_rule)
        for match in matches:
            inner_bag = match[1].strip()
            if match[0] == 'no other':
                continue
            count = int(match[0].strip())
            if inner_bag not in bag_dict:
                bag_dict[inner_bag] = [outer_bag]
            else:
                bag_dict[inner_bag].append(outer_bag)
    return bag_dict

# def get_all_contained_bags(bag_to_search, bag_dict):
#     if len(bag_dict[bag_to_search]) == 0:
#         return {}
#     all_bags = [get_all_contained_bags(bag, bag_dict) for bag, count in bag_dict[bag_to_search].items()]
#     result = bag_dict[bag_to_search]
#     for inner_bag_dict in all_bags:
#         for bag, count in inner_bag_dict.items():
#             if bag not in result:
#                 result[bag] = count
#     return result

def get_all_outer_bags(bag_to_search, bag_dict):
    # TODO stopping condition
    if bag_to_search not in bag_dict.keys():
        return []
    result = set(bag_dict[bag_to_search])
    for outer_bag in bag_dict[bag_to_search]:
        for outer_outer_bag in get_all_outer_bags(outer_bag, bag_dict):
            result.add(outer_outer_bag)
    return result


bag_regulations = [rule.strip() for rule in open('Day7/bag_regulations.txt').readlines()]

bag_dict = build_bag_dict(bag_regulations)
print(bag_dict)
outer_bags = get_all_outer_bags('shiny gold', bag_dict)
print(outer_bags)
print("Part 1:", len(outer_bags))
# for inner_bag, outer_bags in bag_dict.items():
#     print(inner_bag, outer_bags)


# all_contents = dict.fromkeys(direct_contents.keys(), [])

# for colour, contents in direct_contents.items():
#     all_contents[colour] = get_all_contained_bags(colour, direct_contents)

# for colour,contents in all_contents.items():
#     print(colour, contents)

# bag_count = len([colour for colour, contents in all_contents.items() if 'shiny gold' in contents  ])

# print("Part 1:", bag_count)
