from pathlib import Path
from re import compile

class Bag:
    def __init__(self, regex, rule):
        matches = [match for match in regex.findall(rule)[0] if match and match != ' ']
        self.colour = matches[0].strip()
        self.contents = {}
        for i in range(1, len(matches) - 1, 2):
            self.contents[matches[i + 1].strip()] = int(matches[i].strip())

    def __str__(self):
        return self.colour + ": " + " ".join([a + "x " + str(b) for a,b in self.contents.items() if b != 'no other'])
    def __repr__(self):
        return str(self)
    def can_carry_bag(self, bag_colour):
        return bag_colour in self.contents
bag_regulations = [rule.strip() for rule in open('Day7/bag_regulations.txt').readlines()]
bag_rules_regex = compile(r'([\w| ]+)bags contain (?:(\d+|no other)([\w| ]+)bags*)[, ]*(?:(\d+|no other)([\w| ]+)bags*)*')
bags = [Bag(bag_rules_regex, rule) for rule in bag_regulations]
can_carry = [bag for bag in bags if bag.can_carry_bag('shiny gold')]

keep_checking = True
while(keep_checking):
    keep_checking = False
    for bag in bags:
        for innerbag in bag.contents.keys():
            can_carry_colours = [carry.colour for carry in can_carry]
            if innerbag in can_carry_colours:
                can_carry.append(bag)
                keep_checking = True
                continue
for bag in can_carry:
    print(bag)
