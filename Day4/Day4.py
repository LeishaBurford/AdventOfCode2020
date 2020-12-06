from pathlib import Path
from itertools import groupby, chain
from re import compile
import pprint

class Passport:
	def __init__(self, pass_data):
		pass_info = dict.fromkeys({'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'})
		for item in pass_data:
			(key, value) = item.split(':')
			pass_info[key] = value
		self.pass_info = pass_info
	def is_valid_2(self):
		missing_fields = {x:y for x,y in self.pass_info.items() if y == None}
		if len(missing_fields) > 1:
			return False
		if len(missing_fields) == 1 and list(missing_fields.keys())[0] != 'cid':
			return False
		if int(self.pass_info['byr']) < 1920 or int(self.pass_info['byr']) > 2002:
			return False
		if int(self.pass_info['iyr']) < 2010 or int(self.pass_info['iyr']) > 2020:
			return False
		if int(self.pass_info['eyr']) < 2020 or int(self.pass_info['eyr']) > 2030:
			return False
		if self.pass_info['hgt'][-2:] != 'in' and self.pass_info['hgt'][-2:] != 'cm':
			return False
		if self.pass_info['hgt'][-2:] == 'in':
			if int(self.pass_info['hgt'][:-2]) < 59 or int(self.pass_info['hgt'][:-2]) > 76:
				return False
		if self.pass_info['hgt'][-2:] == 'cm':
			if int(self.pass_info['hgt'][:-2]) < 150 or int(self.pass_info['hgt'][:-2]) > 193:
				return False
		hair_colour = compile(r"^(#[0-9a-f]{6})$")
		if not hair_colour.match(self.pass_info['hcl']):
			return False
		eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if len(self.pass_info['ecl']) != 3 or self.pass_info['ecl'] not in eye_colours:
			return False
		nine_digit = compile(r"^(\d{9})$")
		if not nine_digit.match(self.pass_info['pid']):
			return False
		return True

	def is_valid(self):
		missing_fields = {x:y for x,y in self.pass_info.items() if y == None}
		if len(missing_fields) > 1:
			return False
		if len(missing_fields) == 0 or 'cid' in missing_fields:
			return True
		return False
	def __str__(self):
		return "\n".join([str(x) + ":" + str(y) for x,y in self.pass_info.items()]) 
	def __repr__(self):
		return str(self)
def split_list(list, char):
	results = []
	temp = []
	for item in list:
		if item == char:
			results += temp
			temp = []
		else:
			temp += item
	return results

passports = [Passport(p.replace('\n', ' ').split(' ')) for p in open('Day4/batch.txt').read().split('\n\n')]

valid_passports = [passport for passport in passports if passport.is_valid()]
print("Part 1:", len(valid_passports))

valid_passports_2 = [passport for passport in passports if passport.is_valid_2()]
print("Part 2:", len(valid_passports_2))