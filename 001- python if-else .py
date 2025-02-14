Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

==> n = int(input().strip())
if n % 2 == 1 or (6 <= n <= 20):
    print("Weird")
else:
    print("Not Weird")

==>How it works:
If n is odd or in the range 6 to 20, print "Weird".
Otherwise, print "Not Weird" (this covers even numbers 2-5 and >20).
