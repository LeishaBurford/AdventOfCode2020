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
            bag_dict[matches[0].strip()].append(([matches[i + 1].strip()], int(matches[i].strip())))
    return bag_dict

bag_regulations = [rule.strip() for rule in open('Day7/bag_regulations.txt').readlines()]

direct_contents = build_bag_dict(bag_regulations)
all_contents = dict.fromkeys(direct_contents.keys(), [])


for colour,contents in direct_contents.items():
    q = deque(contents)
    while len(q) > 0:
        bag = q.popleft()
        all_contents[colour].append(bag)
        q.append(bag)

for bag in all_contents:
    print(bag)
# print(build_bag_dict(bag_regulations))