from pathlib import Path
from copy import deepcopy

class Ferry:

    def __init__(self, seat_plan):
        self.seats = [['*' for i in range(0, len(seat_plan[0]))]
                      for j in range(0, len(seat_plan))]
        # self.seat_plan = seat_plan
        self.stable = False
        self.set_seats(seat_plan)

    def set_seats(self, seat_plan):
        for row in range(0, len(seat_plan)):
            for col in range(0, len(seat_plan[0])):
                up = seat_plan[row - 1][col] if row - 1 > 0 else '*'
                down = seat_plan[row + 1][col] if row + \
                    1 < len(seat_plan) else '*'

                left = seat_plan[row][col - 1] if col - 1 > 0 else '*'
                right = seat_plan[row][col + 1] if col + \
                    1 < len(seat_plan[0]) else '*'

                up_left = seat_plan[row - 1][col -
                                             1] if row - 1 > 0 and col - 1 > 0 else '*'
                up_right = seat_plan[row - 1][col + 1] if row - \
                    1 > 0 and col + 1 < len(seat_plan[0])else '*'

                down_left = seat_plan[row + 1][col - 1] if row + \
                    1 < len(seat_plan) and col - 1 > 0 else '*'
                down_right = seat_plan[row + 1][col + 1] if row + \
                    1 < len(seat_plan) and col + 1 < len(seat_plan[0]) else '*'

                self.seats[row][col] = Seat(
                    seat_plan[row][col], up, down, left, right, up_left, up_right, down_left, down_right)

    def do_seating_round(self):
        # its updating while looping, need to not

        self.stable = True
        seat_plan = [['*' for i in range(0, len(self.seats[0]))]
                      for j in range(0, len(self.seats))]
        old_seats = [[deepcopy(seat) for seat in seat_row] for seat_row in self.seats ]
        for row, seat_row in enumerate(old_seats):
            for col, seat in enumerate(seat_row):
                if self.seats[row][col].update():
                    self.stable = False
                seat_plan[row][col] = self.seats[row][col].state
        self.set_seats(seat_plan)

    def __repr__(self):
        return self

    def __str__(self):
        return '\n'.join([str(row) for row in self.seats])


class Seat:
    # * = wall
    # . = floor
    # # = occupied seat
    # L = empty seat
    def __init__(self, state, up, down, left, right, up_left, up_right, down_left, down_right):
        self.state = state

        self.up = up
        self.down = down

        self.left = left
        self.right = right

        self.up_left = up_left
        self.up_right = up_right

        self.down_left = down_left
        self.down_right = down_right

        self.adjacent_seats = [self.up, self.down, self.left, self.right,
                               self.up_left, self.up_right, self.down_left, self.down_right]

    def update(self):
        if self.should_occupy():
            return True
        if self.should_vacate():
            return True
        return False

    def should_occupy(self):
        if self.state == 'L' and len([seat for seat in self.adjacent_seats if seat == '#']) == 0:
            self.state = '#'
            return True
        return False

    def should_vacate(self):
        if self.state == '#' and len([seat for seat in self.adjacent_seats if seat == '#']) >= 4:
            self.state = 'L'
            return True
        return False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.state


ferry = Ferry([list(seat_row.strip())
               for seat_row in open('Day11/seat_plan.txt').readlines()])

# while(not ferry.stable):
#     ferry.do_seating_round()
print(ferry)

ferry.do_seating_round()
print(ferry)
print()
ferry.do_seating_round()
print(ferry)
print()

ferry.do_seating_round()
print(ferry)
print()

ferry.do_seating_round()
print(ferry)
print()

ferry.do_seating_round()
print(ferry)
not_occupied = 0
for seat_row in ferry.seats:
    for seat in seat_row:
        if seat.state == '#':
            not_occupied += 1
print("Part 1:", not_occupied)
