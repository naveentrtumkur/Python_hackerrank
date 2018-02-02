// Average marks of students

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = {}
    #print(student_marks[query_name])
    sumVal =0
    val = student_marks[query_name]
    for i in range(len(student_marks[query_name])):
        sumVal += val[i]
        
    
    print('%.2f'%(sumVal/3))
        


