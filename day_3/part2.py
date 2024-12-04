import re

with open("/home/danne/Git_Repos/AdventOfCode2024/day_3/input","r") as f:
    dont_blocks = re.split(r"don't\(\)",f.read())
    do_blocks = []
    do_blocks.append(dont_blocks[0])
    muls = []
    for block in dont_blocks:
        if len(re.findall(r"do\(\)",block)) > 0:
            do_blocks.append(re.split(r"do\(\)",block)[1])
    for block in do_blocks:
        muls.append(re.findall(r"mul\((\d+),(\d+)\)",block))
def main():
    result = 0
    for a,b in muls:
        result += int(a)*int(b)
    print(result)
    


if __name__ == "__main__":
    main()