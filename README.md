hacker rank certificate in python

Given an integer, n, perform the following conditional actions:
If  n is odd, print Weird
If  n is even and in the inclusive range of 2 to 5, print Not Weird
If  n is even and in the inclusive range of  6 to 20 , print Weird
If  n is even and greater than 20, print Not Weird
==>    n = int(input().strip())
==>    if n % 2 == 1 or (6 <= n <= 20):
==>        print("Weird")
==>    else:print("Not Weird")

The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer division. The second line should contain the result of float division.
==>a = int(input()); b = int(input())
==>print(a // b)  # Integer division
==>print(a / b)   # Float division

You are given a string s.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
==>    from itertools import permutations
==>     # Read input
==>     s, k = input().split()
==>     k = int(k)  # Convert k to an integer
==>    # Generate and print permutations
==>     for perm in sorted(permutations(s, k)):
==>        print("".join(perm))
