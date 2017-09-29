def extractdata():
    fp = open("file.txt", "w")
    while True:
        data = input()
        if(data == "EndOfInput"):
            break
        fp.write(str(data.split("~")) + '\n')


    fp.close()

    feature = 0
    datalist = []
    fp = open("file.txt", "r")
    data = fp.readlines()
    for line in data:
        a = line.strip('\n').strip('[').strip(']').split(',')
        for i in range(len(a)):
            a [i] = a[i].lstrip(" ' ").rstrip(" ' ")

        
        if(feature == 1 and a[0]!="Students" and a[0]!= "Grades"):
            a.insert(0,"c")
        if(feature == 2 and a[0]!="Courses" and a[0]!= "Grades"):
            a.insert(0,"s")
        if(feature == 3 and a[0]!="Courses" and a[0]!= "Students"):
            a.insert(0,"g")
        if(a[0] == "Courses"):
            feature = 1
        if(a[0] == "Students"):
            feature = 2
        if(a[0] == "Grades"):
            feature = 3
        datalist.append(a)
        #print(a)

    for i in range(len(datalist)):
        if datalist[i][0] == 's':
            grades = []
            for j in range(len(datalist)):
                if datalist[j][0] == 'g' and datalist[j][4] == datalist[i][1]:
                    grades.append(datalist[j][5])
            datalist[i].append(grades)
            datalist[i].append(len(datalist[i][3]))
    #print(datalist)

    final_students = []
    for k in range(len(datalist)):
        if datalist[k][0] == 's':
            final_students.append(datalist[k])

    for i in range(len(final_students)):
        for j in range(len(final_students[i][3])):
            if final_students[i][3][j] == 'A':
                final_students[i][3][j] = 10
            if final_students[i][3][j] == 'AB':
                final_students[i][3][j] = 9            
            if final_students[i][3][j] == 'B':
                final_students[i][3][j] = 8
            if final_students[i][3][j] == 'BC':
                final_students[i][3][j] = 7
            if final_students[i][3][j] == 'C':
                final_students[i][3][j] = 6
            if final_students[i][3][j] == 'CD':
                final_students[i][3][j] = 5
            if final_students[i][3][j] == 'D':
                final_students[i][3][j] = 4

    for i in range(len(final_students)):
        if(final_students[i][4] > 0):
            result = sum(final_students[i][3])/final_students[i][4]
            final_students[i].append(result)
        else:
            final_students[i].append(final_students[i][4])
    #print(final_students)

    fp = open("solutionfile.txt", "w")
    solution_list = final_students[:]
    for i in range(len(solution_list)):
        solution_list[i].pop(0)
        solution_list[i].pop(2)
        solution_list[i].pop(2)
        round(solution_list[i][2], 2)
        solution_list[i] = str(solution_list[i]).lstrip('[').rstrip(']').split(',')
        solution_list[i] = solution_list[i][0] + '~' + solution_list[i][1] + '~' + solution_list[i][2]
        fp.write(solution_list[i] + '\n')
    fp.close()
    #return(solution_list)
extractdata()

"""
SUBMITTED CODE FOR ASSIGNMENT WITH SMALLER STRING ADJUSTMENTS TO MATCH OUTPUT:

def extractdata():
    data = []
    while True:
        io = input()
        if(io == "EndOfInput"):
            break
        data.append(io.split("~"))
    #print(data)

    feature = 0
    datalist = []
    for line in data:
        a = line
        
        if(feature == 1 and a[0]!="Students" and a[0]!= "Grades"):
            a.insert(0,"c")
        if(feature == 2 and a[0]!="Courses" and a[0]!= "Grades"):
            a.insert(0,"s")
        if(feature == 3 and a[0]!="Courses" and a[0]!= "Students"):
            a.insert(0,"g")
        if(a[0] == "Courses"):
            feature = 1
        if(a[0] == "Students"):
            feature = 2
        if(a[0] == "Grades"):
            feature = 3
        datalist.append(a)
        #print(a)

    for i in range(len(datalist)):
        if datalist[i][0] == 's':
            grades = []
            for j in range(len(datalist)):
                if datalist[j][0] == 'g' and datalist[j][4] == datalist[i][1]:
                    grades.append(datalist[j][5])
            datalist[i].append(grades)
            datalist[i].append(len(datalist[i][3]))
    #print(datalist)

    final_students = []
    for k in range(len(datalist)):
        if datalist[k][0] == 's':
            final_students.append(datalist[k])

    for i in range(len(final_students)):
        for j in range(len(final_students[i][3])):
            if final_students[i][3][j] == 'A':
                final_students[i][3][j] = 10
            if final_students[i][3][j] == 'AB':
                final_students[i][3][j] = 9            
            if final_students[i][3][j] == 'B':
                final_students[i][3][j] = 8
            if final_students[i][3][j] == 'BC':
                final_students[i][3][j] = 7
            if final_students[i][3][j] == 'C':
                final_students[i][3][j] = 6
            if final_students[i][3][j] == 'CD':
                final_students[i][3][j] = 5
            if final_students[i][3][j] == 'D':
                final_students[i][3][j] = 4

    for i in range(len(final_students)):
        if(final_students[i][4] > 0):
            result = sum(final_students[i][3])/final_students[i][4]
            final_students[i].append(result)
        else:
            final_students[i].append(final_students[i][4])
    #print(final_students)
    solution_list = final_students[:]
    solution_list.sort(key=lambda x: x[1])
    #k = final_students[1]
    #solution_list = sorted(final_students, key = k)
    #print(solution_list)
    for i in range(len(solution_list)):
        solution_list[i].pop(0)
        solution_list[i].pop(2)
        solution_list[i].pop(2)
        round(solution_list[i][2], 2)
        solution_list[i] = str(solution_list[i]).lstrip('[').rstrip(']').split(',')
        result = str(solution_list[i][0].strip(" ' ") + '~' + solution_list[i][1].strip(" ' ") + '~' + solution_list[i][2].strip(" ' "))
        print(result)
    return(solution_list)
extractdata()
   
"""
    
