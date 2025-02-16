Problem
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

==>def swap_case(s):
    swapped = ""

    for c in s:
        if c.islower():
            swapped = swapped + c.upper()
        elif c.isupper():
            swapped = swapped + c.lower()
        else:
            swapped = swapped + c

    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

==>1. The function `swap_case(s)` initializes an empty string `swapped`.  
2. It loops through each character `c` in the input string `s`.  
3. If `c` is lowercase, it converts it to uppercase; if uppercase, it converts it to lowercase; otherwise, it remains unchanged.  
4. The modified characters are concatenated into `swapped`, which is then returned.  
5. The main part of the program takes user input, calls `swap_case()`, and prints the result.
