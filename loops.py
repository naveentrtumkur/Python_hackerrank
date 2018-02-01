/*

Task 
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format

The first and only line contains the integer, .

Constraints



Output Format

Print  lines, one corresponding to each .

*/

if __name__ == '__main__':
    n = int(input())
    i =0
    while n>=0 and i < n:
        print(i**2)
        i = i+1


