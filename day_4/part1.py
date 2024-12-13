import re

#with open("/home/danne/Git_Repos/AdventOfCode2024/day_4/test","r") as f:
with open("/home/danne/Git_Repos/AdventOfCode2024/day_4/input","r") as f:
    lines = f.read().split('\n')

m = len(lines)
n = len(lines[0])

def find_XMAS(i,j,x,y):
    return ((lines[i+y][j+x] == 'M') and 
        (lines[i+2*y][j+2*x] == 'A') and 
        (lines[i+3*y][j+3*x] == 'S'))

def main():
    forwad_reg = 'XMAS'
    backward_reg = 'SAMX'
    count = 0
    
    for line in lines:
        count += len(re.findall(forwad_reg,line))
        count += len(re.findall(backward_reg,line))
    for i in range(m):
        for j in range(n):
            if (lines[i][j] == 'X'):
                if (i >= 3):
                    count += find_XMAS(i,j,0,-1)
                    if (j >= 3):
                        count += find_XMAS(i,j,-1,-1)
                    if (j <= len(lines[i])-4):
                        count += find_XMAS(i,j,1,-1)
                if (i <= len(lines)-4):
                    count += find_XMAS(i,j,0,1)
                    if (j >= 3):
                        count += find_XMAS(i,j,-1,1)
                    if (j <= len(lines[i])-4):
                        count += find_XMAS(i,j,1,1)
    print(count)




if __name__ == "__main__":
    main()