# CMPS 2200 Assignment 5
## Answers

**Name:**__Shayne Shelton________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**
  import math
  global coins = []
  def coin_convert(N):
    if N <= 2:
      return N
    else:
      n = int(math.log(N,2))
      power = math.pow(2,n)
      coins.append(power)
      return coin_convert(N - power)

- **1b.**
  W(n) = W(n/2) + 1 => O(logn)
  S(n) = S(n/2) + 1 => O(logn)

- **2a.**
  Breaking $10 into change using $6, $5, and $2. A greedy algoritm would choose $6, then $2,
  then $2 again. This results in 3 denominations. Picking $5 twice results in the same answer except
  only 2 or picked.
  
- **2b.**
  Intialize a dicionary to store values and their optimal picking combinations (memoization). Recursively solve
  the problem by doing recursive calls with the differnce between the denomination and the total. The base
  case should return the depth. The else statement outside of the base case should return the minimum of 
  all of the recursive calls.
  
  W => O(n)
  S => O(n)

