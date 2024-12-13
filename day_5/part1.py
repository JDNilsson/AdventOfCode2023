#with open("/home/danne/Git_Repos/AdventOfCode2024/day_5/test","r") as f:
with open("/home/danne/Git_Repos/AdventOfCode2024/day_5/input","r") as f:
    lines = f.read().split('\n')

def main():
    rules = [(int(rule[0]),int(rule[1])) for rule in [line.split("|") for line in lines[:lines.index("")]]]
    updates = [[int(page) for page in update] for update in [line.split(",") for line in lines[lines.index("")+1:]]]
    correct_updates = []
    for update in updates:
        correct = True
        relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
        for rule in relevant_rules:
            if(update.index(rule[0]) > update.index(rule[1])):
                correct = False
                break
        if (correct):
            correct_updates.append(update)
    
    middles = [update[len(update)//2] for update in correct_updates]
    res = sum(middles)

    print(res)

if __name__ == "__main__":
    main()