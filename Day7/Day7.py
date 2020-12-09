from pathlib import Path
from re import compile

class Bag:
    def __init__(self, regex, rule):
        matches = [match for match in regex.findall(rule)[0] if match and match != ' ']
        self.colour = matches[0]
        self.contents = []
        for i in range(1, len(matches) - 1, 2):
            self.contents.append((int(matches[i].strip()), matches[i + 1].strip()))

    def __str__(self):
        return self.colour + ": " + " ".join([str(a) + "-" + b for a,b in self.contents if a != 'no other'])
    def __repr__(self):
        return str(self)
    def can_carry_bag(self, bag_colour):
        can_carry = [i for i, v in enumerate(self.contents) if v[1] == bag_colour and v[0] > 0]
        if len(can_carry) > 0:
            return True
        return False
bag_regulations = [rule.strip() for rule in open('Day7/bag_regulations.txt').readlines()]
bag_rules_regex = compile(r'([\w| ]+)bags contain (?:(\d+|no other)([\w| ]+)bags*)[, ]*(?:(\d+|no other)([\w| ]+)bags*)*')
bags = [Bag(bag_rules_regex, rule) for rule in bag_regulations]
can_carry = [bag for bag in bags if bag.can_carry_bag('shiny gold')]
for bag in can_carry:
    print(bag)
