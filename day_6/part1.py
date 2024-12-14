import re
#with open("/home/danne/Git_Repos/AdventOfCode2024/day_6/test","r") as f:
with open("/home/danne/Git_Repos/AdventOfCode2024/day_6/input","r") as f:
   lines = f.read().split('\n')

max_x = len(lines[0])-1
max_y = len(lines)-1

def main():
    guard_coords = [0,0]
    dir = [0,-1]
    res = 1
    for i,line in enumerate(lines):
        if '^' in line:
            guard_coords[1] = i
            guard_coords[0] = line.index('^')
            break
    
    while (guard_coords[0] in range(1,max_x) and
           guard_coords[1] in range(1,max_y)):
        while (lines[guard_coords[1] + dir[1]][guard_coords[0] + dir[0]] == '#'):
            if (dir[0] == 0):
                dir[0] = -dir[1]
                dir[1] = 0
            else:
                dir[1] = dir[0]
                dir[0] = 0
        update_string = list(lines[guard_coords[1]])
        update_string[guard_coords[0]] = 'X'
        lines[guard_coords[1]] = "".join(update_string)
        guard_coords[0] += dir[0]
        guard_coords[1] += dir[1]
    
    for line in lines:
        for c in line:
            res += c == 'X'
    
    print(res)
if __name__ == "__main__":
    main()