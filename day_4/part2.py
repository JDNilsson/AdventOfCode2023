import re

#with open("/home/danne/Git_Repos/AdventOfCode2024/day_4/test","r") as f:
with open("/home/danne/Git_Repos/AdventOfCode2024/day_4/input","r") as f:
    lines = f.read().split('\n')

m = len(lines)
n = len(lines[0])

def find_X_MAS(i,j):
    return ((((lines[i-1][j-1] == 'M') and
             (lines[i+1][j+1] == 'S')) or
            ((lines[i-1][j-1] == 'S') and 
             (lines[i+1][j+1] == 'M'))) and
             (((lines[i+1][j-1] == 'M') and
             (lines[i-1][j+1] == 'S')) or
            ((lines[i+1][j-1] == 'S') and 
             (lines[i-1][j+1] == 'M'))))

def main():
    count = 0
    for i in range(m):
        for j in range(n):
            if (lines[i][j] == 'A'):
                if ((i > 0) and 
                    (i < len(lines)-1) and
                    (j > 0) and
                    (j < len(lines[0])-1)):
                        count += find_X_MAS(i,j)
                        print(f"Found A and Got cross: \n{lines[i-1][j-1]} {lines[i-1][j+1]}\n A \n{lines[i+1][j-1]} {lines[i+1][j+1]}")
    print(count)




if __name__ == "__main__":
    main()