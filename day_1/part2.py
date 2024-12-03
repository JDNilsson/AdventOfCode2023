with open("/home/danne/Git_Repos/AdventOfCode2024/day_1/input","r") as f:
   lines = f.read().split('\n')

def main():
    left = [int(l.split()[0]) for l in lines]
    right = [int(r.split()[1]) for r in lines]
    right_dict = {}
    for k in right:
        if k not in right_dict:
            right_dict[k] = 1
        else:
            right_dict[k] += 1
    result = sum([l*right_dict[l] if l in right_dict else 0 for l in left])
    print(result)

if __name__ == "__main__":
    main()