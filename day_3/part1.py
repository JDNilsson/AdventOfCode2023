import re

with open("/home/danne/Git_Repos/AdventOfCode2024/day_3/input","r") as f:
   muls = re.findall("mul\((\d+),(\d+)\)",f.read())

def main():
    result = 0
    for a,b in muls:
        result += int(a)*int(b)
    print(result)
    


if __name__ == "__main__":
    main()