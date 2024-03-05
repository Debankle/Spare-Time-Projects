

def Hanoi(n,start,end,temp):
    if n == 1:
        print("Move disk 1 from " + start + " to " + end)
    else:
        Hanoi(n-1,start,temp,end)
        print("Move disk " + str(n) + " from " + start + " to " + end)
        Hanoi(n-1,temp,end,start)

if __name__ == "__main__":
    Hanoi(3,"A","B","C")
    print()
    Hanoi(5,"A","B","C")