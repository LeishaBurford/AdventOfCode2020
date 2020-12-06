from pathlib import Path

def find_seat(seat_nums, seat_code):
    if len(seat_nums) == 1:
        return seat_nums[0]
    char = seat_code[0]
    if(char == 'F' or char == 'L'):
        return find_seat(seat_nums[:int(len(seat_nums)/2)], seat_code[1:])
    else:
        return find_seat(seat_nums[int(len(seat_nums)/2):], seat_code[1:])  

boarding_passes = [boarding_pass.strip() for boarding_pass in open('Day5/boarding_passes.txt').readlines()]

seat_ids = []
for boarding_pass in boarding_passes:
    row = find_seat([i for i in range(0,128)], boarding_pass[:7])
    col = find_seat([i for i in range(0,8)], boarding_pass[7:])
    seat_ids.append(row * 8 + col)

print("Part 1:", max(seat_ids))

possible_seats = []
seat_ids.sort()
for i in range(1, len(seat_ids) - 2):
    seat = seat_ids[i]
    if abs(seat_ids[i - 1] - seat) > 1:
        possible_seats.append(seat_ids[i] - 1)
    if abs(seat_ids[i + 1] - seat) > 1:
        possible_seats.append(seat_ids[i] + 1)

print("Part 2:", set(possible_seats))