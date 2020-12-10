from collections import defaultdict
import re


def part1_countouterbags(bag_rules):
    inverted_bag_rules = defaultdict(list)  ## Track parent of each color bag

    for outer_bag, inner_bags in bag_rules.items():
        for count, bag in inner_bags:
            inverted_bag_rules[bag].append(outer_bag)

    def _countouterbags(targetbag):
        seen = set()
        stack = [targetbag]
        while stack:
            bag = stack.pop()
            for parentbag in inverted_bag_rules[bag]:
                if parentbag not in seen:
                    seen.add(parentbag)
                    stack.append(parentbag)
        return len(seen)

    for key, value in inverted_bag_rules.items():
        print(key, value)
    return _countouterbags('shiny gold')


def part2_countinnerbags(bag_rules):
    def _countinnerbags(currentbag):
        return sum(int(count) + int(count) * _countinnerbags(bag) for count, bag in bag_rules[currentbag])

    return _countinnerbags('shiny gold')


def read_input(filename):
    with open(filename) as file:
        bag_rules = {}
        for line in file:
            # print(line)
            outer_bag, inner_bags = line.split(" bags contain")
            bag_rules[outer_bag] = re.findall(r'([0-9]+) ([a-z ]+) bag[s]?', inner_bags.strip())
    return bag_rules


if __name__ == '__main__':
    bag_rules = read_input('Day7/bag_regulations.txt')
    # bag_rules = read_input("day7_input.txt")
    part1_ans = part1_countouterbags(bag_rules)
    print("part1 answer", part1_ans)
    part2_ans = part2_countinnerbags(bag_rules)
    print("part2 answer", part2_ans)
