Consider a list (list = []). You can perform the following commands:

insert i e : Insert integer e at position i
print : Print the list
remove e : Delete the first occurrence of integer e
append e : Insert integer e at the end of the list
sort : Sort the list
pop : Pop the last element from the list
reverse : Reverse the list
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format
The first line contains an integer, n, denoting the number of commands.

Each line i of the n subsequent lines contains one of the commands described above.

Constraints
The elements added to the list must be integers

Output Format
For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

==>if __name__ == '__main__':
    N = int(input())
    the_list = list()

    for _ in range(N):
        query = input().split()
        if query[0] == "print":
            print(the_list)
        elif query[0] == "insert":
            the_list.insert(int(query[1]), int(query[2]))
        elif query[0] == "remove":
            the_list.remove(int(query[1]))
        elif query[0] == "append":
            the_list.append(int(query[1]))
        elif query[0] == "sort":
            the_list = sorted(the_list)
        elif query[0] == "pop":
            the_list.pop()
        elif query[0] == "reverse":
            the_list.reverse()

==>1. The code reads an integer N, which represents the number of commands to execute.  
2. It initializes an empty list the_list and processes N commands one by one.  
3. Depending on the command (e.g., "insert", "remove", "append"), it modifies the_list accordingly.  
4. The "print" command outputs the current state of the_list.  
5. The list operations include sorting, popping the last element, and reversing the order. 
