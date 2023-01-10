
def fibonacci_series(max):
    n0 = 0
    n1 = 1
    print("\t\t\tFibonaci series starts ...")
    for i in range(max):
        print(n0)
        n0, n1 = n1, n0+n1

fibonacci_series(int(input("\tEnter input limit to generate fibonacci serires ...")))

    
    
 
