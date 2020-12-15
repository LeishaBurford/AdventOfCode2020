from pathlib import Path

class Console:
    def __init__(self, program):
        # self.progam = [(operation, argument) for operation, argument in command for command in program]
        self.program = []
        for command in program:
            operation, argument = command.split(' ')
            self.program.append((operation, Argument(argument)))
        self.accumulator = 0
        self.current_position = 0
        self.is_infinite = False
        self.is_complete = False
        self.commands_run = []
    
    def __str(self):
        return 'current position: ' + self.current_position + ' acc: ' + self.accumulator 
    def perform_current_operation(self, swap_at_index = -1):
        if self.current_position in self.commands_run:
            self.is_infinite = True
            return
        if self.current_position == len(self.program):
            self.is_complete = True
            return
        current_operation = self.program[self.current_position]
        command = current_operation[0]
        if self.current_position == swap_at_index:
            command = 'nop' if command == 'jmp' else 'jmp'
        self.commands_run.append(self.current_position)
        if(command == 'acc'):
            self.accumulator += current_operation[1].value
            self.current_position += 1
        elif(command == 'jmp'):
            self.current_position += current_operation[1].value
        elif(command == 'nop'):
            self.current_position += 1
        
        
class Argument:
    def __init__(self, arg):
        is_positive = arg[0] == '+'
        self.value = int(arg[1:]) if is_positive else int(arg[1:]) * -1
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self)


console_program = [command.strip() for command in open('Day8/program.txt').readlines()]
console = Console(console_program)
# print(console.program)

while(not console.is_infinite):
    console.perform_current_operation()
print("Part 1:", console.accumulator)

# for each nop or jmp
# switch it
accumulator = 0

for index in range(0, len(console_program)):
    if 'jmp' in console_program[index] or 'nop' in console_program[index]:
        # run until done or infinite
        console = Console(console_program)
        while(not console.is_infinite and not console.is_complete):
            console.perform_current_operation(index)
        if console.is_complete:
            accumulator = console.accumulator
            break

print("Part 2:", accumulator)