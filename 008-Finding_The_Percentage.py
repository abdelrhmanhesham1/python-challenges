You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format
The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Constraints
2 <= N <= 10 0 <= Marks <= 100

Output Format
Print one line : The average of the marks obtained by the particular student correct to 2 decimal places.

==>if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    def find_percentage(name):
        return f"{sum(student_marks[name]) / len(student_marks[name]):.2f}"

    print(find_percentage(query_name))
    
    ==>1. Reads the number of students (n).
2. Creates a dictionary (student_marks) where:
The key is the student's name.
The value is a list of their scores converted to float.
3. Reads the query name (the student whose average marks need to be calculated).
4. Defines find_percentage(name) function, which:
Retrieves the student's marks from the dictionary.
Computes the average and formats it to two decimal places.
5. Prints the calculated average for the queried student.
