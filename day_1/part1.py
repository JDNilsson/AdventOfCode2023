with open("/home/danne/Git_Repos/AdventOfCode2024/day_1/input","r") as f:
   lines = f.read().split('\n')

def main():
    left = [int(l.split()[0]) for l in lines]
    right = [int(r.split()[1]) for r in lines]
    left.sort()
    right.sort()

    mul = [abs(a-b) for a,b in zip(left,right)]
    print(sum(mul))

if __name__ == "__main__":
    main()