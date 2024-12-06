import re

with open("/home/danne/Git_Repos/AdventOfCode2024/day_3/input","r") as f:
    dont_blocks = re.split(r"don't\(\)",f.read())
    do_blocks = []
    do_blocks.append(dont_blocks[0])
    muls = []
    for block in dont_blocks:
        do_indexes = re.findall(r"do\(\)",block)
        if len(do_indexes) > 0:
            do_index = re.search(r"do\(\)",block).start()
            do_blocks.append(block[do_index:])
    for block in do_blocks:
        muls += (re.findall(r"mul\((\d+),(\d+)\)",block))

def main():
    result = 0
    for a,b in muls:
        result += int(a)*int(b)
    print(result)
    
if __name__ == "__main__":
    main()