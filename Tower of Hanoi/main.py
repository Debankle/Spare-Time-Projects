"""Implementation of Tower of Hanoi problem in python"""

def hanoi(n,start,end,temp):
    """
    Solves the Tower of Hanoi problem recursively

    Parameters:
        n (int): Number of disks.
        start (str): The starting peg.
        end (str): The destination peg.
        temp (str): The temporary peg.

    Returns:
        None
    """
    if n == 1:
        # Base case of recursion: move last piece disk on a peg
        # to the destination peg
        print("Move disk 1 from " + start + " to " + end)
    else:
        # Clear the start peg so the last disk can be moved to the
        # bottom of the destination peg
        hanoi(n-1,start,temp,end)
        # Move the last disk from the start to the end
        print("Move disk " + str(n) + " from " + start + " to " + end)
        # Move n-1 disks from temp to end using start as auxiliary.
        hanoi(n-1,temp,end,start)

if __name__ == "__main__":
    print("Testing the function with 3 disks")
    hanoi(3,"A","B","C")
    print()

    print("Testing the function with 5 disks")
    hanoi(5,"A","B","C")
