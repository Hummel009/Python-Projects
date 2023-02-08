import math


def launch():
    x = 0.6
    while x < 1.1:
        x = round(x, 1)
        n = 10
        while n <= 15:
            mySum = 0
            k = 1
            while k <= n:
                termR1 = math.exp(1.2 * k)
                termR2 = (k - 10) / (k + 30)
                termR3 = math.sqrt(k * math.exp(math.log(n + 5) / 3))
                termR4 = math.log(math.sqrt(n * x))
                numerator = math.exp(math.log(termR1 + termR2) / k)
                denominator = termR3 + termR4;
                mySum += numerator / denominator;
                k += 1
            termL1 = math.exp(n * x) / 2
            termL2 = math.exp(math.log(n * x) / 3)
            f = mySum + math.exp(math.log(termL1 + termL2) / 3)
            print("X = ", x, "N = ", n, "F = ", f)
            n += 1
        x += 0.1;    
  
