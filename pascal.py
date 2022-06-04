print("Enter the number of rows to print")
n = int(input())

def pascal(limit):
    print("\n*** Pascal Triangle ***\n")
    for row in range(0,limit):
        for column in range(0,row+1):
            print("* ",end="")
        print("")

pascal(n)

 