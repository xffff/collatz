from pylab import *
import random
import argparse

def collatz(n, k):    
    if n != 1:
        if n%2 == 0:
            n = n/2
            k.append(n)
            return collatz(n, k)
        else:
            n = n*3+1
            k.append(n)
            return collatz(n, k)
    else:
        k.append(n)
        return k

def main(j):
    for n in j:
        e = []
        plot(collatz(n, e))
    show();
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Graph a list of numbers using Collatz conjecture")
    parser.add_argument("numlist", 
                        nargs='*', 
                        type=int, 
                        help="List of numbers to send to Collatz")
    parser.add_argument("-r", "--random", 
                        type=int, 
                        nargs=2, 
                        help="Random mode takes 2 args: range of random numbers, number of numbers to generate")
    args = parser.parse_args()

    if args.random != None:
        tomain = [random.randint(2,args.random[0]) for r in xrange(args.random[1])]
    else:
        tomain = args.numlist

    main(tomain)
    
