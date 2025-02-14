Given the participants' score sheet for your University Sports Day, you are required to find the runner-up n score. You are given scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
2 <= n <= 10 -100 <= A[i] <= 100

Output Format
Print the runner-up score.

==>if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lst = list(arr)
    scores = list()
    for score in lst:
        if score not in scores:
            scores.append(score)
        else :
            continue
    ordr = sorted(scores, reverse=True)
    print(ordr[1])  

==>1. Read an integer `n` and a list of scores as input.  
2. Convert the input scores into a list (`lst`).  
3. Create a new list (`scores`) to store unique values from `lst`.  
4. Sort `scores` in descending order.  
5. Print the second-highest score (`ordr[1]`).
