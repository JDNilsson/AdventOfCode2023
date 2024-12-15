#with open("/home/danne/Git_Repos/AdventOfCode2024/day_2/test","r") as f:
with open("/home/danne/Git_Repos/AdventOfCode2024/day_2/input","r") as f:
   lines = f.read().split('\n')

def safety_check(line):
   
   dir = line[0]-line[1]
   if (abs(dir) > 3 or dir == 0): return 0

   for i in range(1,len(line)-1):
      diff = line[i]-line[i+1]
      if ((diff == 0)            or 
          (abs(diff) > 3)        or 
          (dir < 0 and diff > 0) or 
          (dir > 0 and diff < 0)): return 0
   
   return 1



def main():
   res = 0
   
   for line in lines:
      line = [int(n) for n in line.split()]
      is_safe = safety_check(line)
      if not is_safe:
         for i in range(len(line)):
            is_safe = safety_check(line[:i]+line[i+1:len(line)])
            if is_safe: break

      res += is_safe
   
   print(res)

if __name__ == "__main__":
    main()