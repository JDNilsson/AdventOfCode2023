with open("/home/danne/Git_Repos/AdventOfCode2024/day_2/input","r") as f:
   lines = f.read().split('\n')

def safety_check(line):
   
   dir = line[0]-line[1]
   safe = 1
   if (abs(dir) > 3 or dir == 0):
      return 0
   for i in range(1,len(line)-1):
      diff = line[i]-line[i+1]
      if ((diff == 0) or (abs(diff) > 3) or (dir < 0 and diff > 0) or (dir > 0 and diff < 0)):
         return 0
   return 1

def main():
   safety_mask = []
   for line in lines:
      line = [int(n) for n in line.split()]
      if (safety_check(line) == 0):
         cringe = 0
         for i in range(len(line)):
            if(safety_check(line[:i]+line[i+1:len(line)])==1):
               safety_mask.append(1)
               cringe = 1
               break
         if cringe == 0:
            safety_mask.append(0)
      else:
         safety_mask.append(1)
   print(sum(safety_mask))

if __name__ == "__main__":
    main()