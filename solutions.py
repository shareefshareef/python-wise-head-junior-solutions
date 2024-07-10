rows = 7;cols = 7

for i in range(1,rows+1):
    for j in range(1,cols+1):

        print("*",end=' ')

    print()


# gb3
for i in range(1,rows+1):
    for j in range(1,cols+1):
        print("*",end='')

        if j<cols:
            print("_",end="")

    print()
print()

# gb4
for i in range(1,rows+1):
    for j in range(1,cols+1):
        print("*",end=" ")

    print()

    if i>2:
        print()



# looping problem A
for row in range(1,rows+1):
    for col in range(1,cols+1):
        print(f"{row}=={col}",end=" ")
    print()


# looping problem B
for row in range(1,rows+1):
    for col in range(1,cols+1):
        print(f"{row}!={col}",end=" ")
    print()

# looping problem C
for row in range(1,rows+1):
    for col in range(1,cols+1):

        print(f"{row}<={col}",end= ' ')
    print()

# looping problem D
for row in range(3,rows+1):
    for col in range(1,cols+1):
        print(f"{row}<{col}",end=' ')
    print()


# looping problem E
for row in range(1,rows+1):
    for col in range(1,cols+1):
        print(f"{row}>={col}",end=" ")
    print()

for row in range(1,rows+1):
    for col in range(1,cols+1):
        print(f"{row}>={row}",end=" ")
    print()



# looping problem F
for row in range(1,rows+1):
    if row<=5:
        for col in range(1,rows+1):
            print(f"{row}>={col}",end=" ")
        print()
    else:
        for col in range(cols,0,-1):
            print(f"{row}>={col}",end=" ")
        print()

# looping problem G
for row in range(1,rows):
    if row<=rows-5:
        for col in range(1,cols):
            if col%2 !=0:
                print(f"{row}!={col}",end=" ")

        print()
    else:
        for col in range(1,cols):
            if col%2 !=0:
                print(f"{rows-row}!={col}",end=' ')
        print()


# looping problem H
for row in range(2,4+1):
    for col in range(2,9,2):
        print(f"{row}>={col}",end=' ')
    print()

for row in range(1,rows+1):
    for cols in range(1,cols+1):
        if cols%2==0:
            print(f"{row}>={cols}",end=" ")
    print()


#ALPHABETS PROBLEMS 

rows = 5
cols = 5

for row in range(1,rows+1):
    for col in range(1,cols+1):
        if row == 1 or row == 3 or col == 1 or col == 5:
            print("*",end=" ")
        else:
            print(" ",end= ' ')
    print()
print()
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 5
        condition = condition or col == 2 or col == 5
        condition = condition or row == 5//2+1 and col>=2
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

print()
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 5 or col == 1
        
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

print()
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 5 or col == 2 or col == 5
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

print()

for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 5 or col == 2
        condition = condition or row == 5//2+1 and col>=2
        
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
print()
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or col == 2 
        condition = condition or row == 5//2+1 and col>=2
        
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
print()

for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 5 or col == 1
        condition = condition or row == 5//2+1 and col>=3
        condition = condition or col == 5 and row>=3
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

print()

for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or col == 3
        condition = condition or row == 5 and col<=3
        condition = condition or col == 1 and row>=4
        
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

rows = 5;cols = 5


# looping problem j and d

for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or col == 3 and row <= 4
        condition = condition or row == 5 and col == 2
        condition = condition or col == 1 and row>=3 and row<=4

        if condition:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print()

for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 and col<=4 or row == 5 and col<=4
        condition = condition or col == 2 or col == 5 and row >= 2 and row<=4

        if condition:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print()

# looping problem K
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 1 or row+col == 4 or row-col == 2

        if condition:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print()

# looping problem M
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 1 or col == 5 
        condition = condition or row == col and row<=2
        condition = condition or row+col == 6 and row<=3
        if condition:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()



# YBM1
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 1 or row == col and row<=3
        condition = condition or row + col == 6 and row>=3

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

# YMB2
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col ==1 or col == 5 or row == col or row+col == 6

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

# YBM3
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == col and col<=2 or row+col == 6 and row<=2 or row == col and col>=4 or row+col == 6 and row>=4

        if condition:
            print("0",end=" ")
        elif col == 3 and row>=3:
            print("00",end=' ')
        else:
            print(" ",end=' ')
    print()

# YBM4
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == col or row+col == 6
        condition2 = row == 3 and col<=2 or row == 3 and col>=4
        condition2 = condition2 or col == 3 and row<=2 or col == 3 and row>=4


        if condition:
            print("$$",end="  ")
        elif condition2:
            print("0 ",end = "  ")
        else:
            print("  ",end="  ")
    print()
# YMB5
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 3 or col-row==2 or row+col == 8 or row-col == 2 or row+col == 12

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

# YBN
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 1 or col == 5 or col == 2 and row>=2 and row<=4 or col == 3 and row>=3 and row<=5 or col == 4 and row>=4 and row<=6

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

# YBP
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 2 or row == 1 and col>=2 or row == 3 and col>=2 or col == 5 and row<=3

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

# YBR
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 and col<=4 or col == 2 or col == 4 and row<=4 or row == 4 and col>=2 and col<=4 or row-col == 2 and col>=3

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

# YBS
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 6 or row == 7 or row == 4
        condition = condition or col == 1 and row<=4 or col == 2 and row<=4 or col == 5 and row>=4

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()


# TASK Y
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 1 and row<=2 or col == 5 and row<=2
        condition = condition or col == 2 and row>=2 and row<=3
        condition = condition or col == 4 and row>=2 and row<=3

        condition2 = row == 3 and col == 3
        condition3 = row == 4 and col == 3
        condition4 = col == 3 and row>=5

        if condition:
            print("xx",end="  ")
        elif condition2:
            print("xxx",end=" ")
        elif condition3:
            print(r"\\// ",end="  ")
        elif condition4:
            print(" or",end="  ")
        else:
            print("  ",end="  ")
    print()

# TASK 9
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row+col == 9 or col == 5 and row>=2 and row<=4 or row == 4 and col>=3 or row == 1 and col>=3 and col<=4 or col == 2 and row>=2 and row<=3

        if condition:
            print("99",end="  ")
        else:
            print("  ",end='  ')
    print()

# TASK 5
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 3 and col<=3 or col == 1 and row<=4 or col ==2 and row<=3 or row == 7 and col<=3 or col ==4 and row>=4 and row<=6

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

# TASK8
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 1 and row<=3 or col == 2 and row>=5 or col == 5 and row<=3 or col == 4  and row<=1 or col == 4 and row>=5
        condition2 = row == 4 and col<=2 or row == 4 and col>=4
        condition3 = col == 1 and row>=5 or col == 2 and row<=3 or col == 5 and row>=5 or col == 4 and row>=2 and row<=3

        if condition:
            print("8",end="  ")
        elif condition2:
            print("@",end="  ")
        elif condition3:
            print("or",end=' ')
        else:
            print("  ",end='  ')
    print()

# TASK6
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 3 and col<=4 or row ==2 and col<=1 or col == 4 and row>=4 or col == 5 and row>=4 and row<=6 or row == 7 and col>=2 and col<=4 or row == 6 and col<=1

        if condition:
            print("5",end=" ")
        else:
            print(" ",end=' ')
    print()

# TASK6
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row+col == 5 or row == 3 and col>=2 and col<=3 or row == 4 and col<=4 or col == 1 and row>=4 and row<=6 or col == 4 and row>=4 and row<=6 or row == 7 and col>=2 and col<=3 

        if condition:
            print("6",end=" ")
        else:
            print(" ",end=' ')
    print()

# TASK7
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or col == 5

        if condition:
            print("7",end=" ")
        else:
            print(" ",end=' ')
    print()

# TASKLT
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row+col == 5 or row-col == 3 or row+col == 6 and col>=2 and col<=4 or row-col==2 and col>=2 and col<=4

        if condition:
            print("#",end=" ")
        else:
            print(" ",end=' ')
    print()

# TASK 2
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 7 or row+col == 4 or row+col == 9 or row == 2 and col>=2 or col == 5 and row>=2 and row<=4 or row == 1 and col == 4

        if condition:
            print("#",end=" ")
        else:
            print(" ",end=' ')
    print()

# TASK4
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 4 or row == 5 or row+col == 5 or row+col == 6 and col<=4

        if condition:
            print("#",end=" ")
        else:
            print(" ",end=' ')
    print()

# TASKZ
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = row == 1 or row == 6
        condition2 = row == 2 and col<=4 or row == 5 or row+col == 6 and col<=4

        if condition:
            print("z",end=" ")
        elif condition2:
            print("#",end=' ')
        else:
            print(" ",end=' ')
    print()

# TASK 1
for row in range(1,rows+1):
    for col in range(1,cols+1):
        condition = col == 3 or row == 7 or row+col == 4

        if condition:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

n = 10
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = row == 1 or col == n or row==col
        if condition:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# PROBLEM1A
for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end=' ')
    print()   

# PROBLEM1B
for row in range(1,n+1):
    for col in range(1,(n+1)-row+1):
        print("*",end=' ')
    print()

for row in range(0,n+1):
    for col in range(1,n-row+1):
        print("*",end=' ')
    print()

for row in range(n,0,-1):
    for col in range(1,row+1):
        print("*",end=" ")
    print()

for row in range(n+1,1,-1):
    for col in range(row,1,-1):
        print("*",end=' ')
    print()


# PATTERN1C
for row in range(1,n+1):
    for col in range(1,n-row+1):
        print(" ",end=' ')
    for col in range(1,row+1):
        print("*",end=' ')
    print()

for row in range(1,n+1):
    for col in range(1,n+1):
        if col<=n-row:
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print()

for row in range(1,n+1):
    for col in range(1,n+1):
        if col>=n-row+1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

for row in range(n,0,-1):
    for col in range(1,n+1):
        if col>=row:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

for row in range(n,0,-1):
    for col in range(1,n+1):
        if col<row:
            print(' ',end=' ')
        else:
            print("*",end=' ')
    print()

for row in range(0,n+1):
    for col in range(1,row+1):
        print(" ",end=' ')
    for col in range(1,n+1-row+1):
        print("*",end=' ')
    print()

for row in range(1,n+1):
    for col in range(1,n+1):
        if col>=row:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

for row in range(1,n+1):
    for col in range(1,n+1):
        if col<row:
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print()

for row in range(n,0,-1):
    for col in range(n,0,-1):
        if row < col:
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print()


# PROBLEM1E
for row in range(1,n+1):
    for col in range(1,(n)+row):
        if col<=(n-row):
            print(" ",end=' ')
        else:
            print(col,end=' ')
    print()

for row in range(0,n):
    for col in range(0,n+row+1):
        if col>=n-row:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

for row in range(n,0,-1):
    for col in range(1,2*n-row+1):
        if col>=row:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


# PROBLEM1F
for row in range(1,n+1):
    for col in range(1,2*n+1-row):
        if col>=row:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

for row in range(n,0,-1):
    for col in range(1,n+row):
        if col>n-row:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


# PROBLEM1G
for row in range(1,2*n):
    if row<n:
        for col in range(1,row+1):
            print("*",end=' ')
    else:
        for col in range(1,(n+1)-(row-n)):
            print("*",end=' ')

    print()

for row in range(1,2*n):
    if row<=n:
        colmax = row
    else:
        colmax = 2*n-row
    for col in range(1,colmax+1):
        print("*",end=' ')
    print()
count = 0
for row in range(1,2*n):
    if row>n:
        count = count + 1

    for col in range(1,row-2*count+1):
        print("*",end=' ')
    print()


# PROBLEM1H
for row in range(1,2*n+1):
    if row<=n:
        for col in range(1,n+row):
            if col>n-row:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()

    else:
        for col in range(1,3*n-row+1):
            if col>=row-n:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
print()
for row in range(1,2*n):
    if row<=n:
        for col in range(1,n+row):
            if col>n-row:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
    else:
        for col in range(1,2*n-(row-n)):
            if col>=row-n+1:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()

count = 0
print()
for row in range(1,2*n):
    if row<=n:
        count = count +1
    else:
        count = count - 1
    for col in range(1,n+count):
        if col>=n-count+1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print()

colmin = 0;colmax = 0

for row in range(1,2*n):
    if row<=n:
        colmax = n+row
        colmin = n-row
    else:
        colmax = 2*n-(row-n)
        colmin = row-n
    for col in range(1,colmax):
        if col>colmin:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print()

spacemax = n
starmax = 1

for row in range(1,2*n+1):

    for sp in range(1,spacemax+1):
        print(" ",end=' ')

    for col in range(1,starmax+1):
        print("*",end=' ')

    print()

    if row<=n:
        spacemax = spacemax - 1
        starmax = starmax +2
    else:
        spacemax = spacemax + 1
        starmax = starmax-2


# #output 1

for row in range(1,2*n+1):
    for col in range(1,2*n+1):
        condition = row == 1 or col == 1 or row == 2*n
        condition = condition or col == 2*n or row == col
        condition = condition or row+col == 2*n+1

        if condition:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print()
# #output2

for row in range(1,2*n+1):
    for col in range(1,2*n+1):
        condition = (row == 1 or row==2*n) and col<n-1 or (row == 1 or row==2*n) and col>n+2

        condition = condition or (col == 1 or col == 2*n) and row<n-1 or (col == 1 or col == 2*n) and row>n+2

        condition = condition or row==col or row+col == 2*n+1

        if condition:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print()

# #output3

for row in range(1,n+1):
    for col in range(1,n+1):
        condition = row == col
        if condition:
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print()

# #output4

for row in range(1,n+1):
    for col in range(1,n+1):
        condition = row == col
        if condition:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        
    print()

for row in range(1,4*n+1):
    if row<=2*n:
        for col in range(1,2*n+row+1):
            if col>2*n:
                print("*",end=' ')
            else:
                print(' ',end=' ')
        print()
    else:
        for col in range(1,2*n+1):
            if col>=row-2*n:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()


# #PROBLEMAA
for row in range(1,4*n+1):
    if row<=2*n:
        for col in range(1,2*n+row):
            if col>=2*n:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
    else:
        for col in range(1,2*n+1):
            if col>=row-2*n:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()

print()
# #PROBLEMBB
for row in range(1,4*n+1):
    if row<=2*n:
        for col in range(1,2*n+1):
            if col>=2*n-row+1:
                print("*",end=' ')
            else:
                print(' ',end=' ')
        print()
    else:
        for col in range(1,4*n-(row-2*n)+1):
            if col>=2*n:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()

for row in range(1,4*n):
    if row<=2*n:
        for col in range(1,2*n-row+1):
            print("*",end=' ') 
    else:
        for col in range(1,row-2*n+1):
            print("*",end=' ')
    print()

# #PATTERN DD
for row in range(1,4*n+1):
    if row<=2*n:
        for col in range(1,2*n+1):
            if col>=row:
                print("*",end=' ')
                
            else:
                print(" ",end=' ')
    else:
        for col in range(1,2*n+1):
            if col>2*n-(row-2*n):
                print("*",end=' ')
            else:
                print(" ",end=' ')
                
    print()
print()
# #PATTERN DD
for row in range(1,4*n):
    if row<=2*n:
        for col in range(1,2*n+1):
            if col<=2*n-row:
                print("*",end=' ')
            else:
                print(" ",end=' ') 
    else:
        for col in range(1,2*n+1):
            if col<=row-2*n:
                print("*",end=' ')
            else:
                print(' ',end=' ')
    print()


# #PROBLEM EE
for row in  range(1,2*n+1):
    for col in range(1,4*n):
        if col<=2*n-row:
            print("*",end=' ')
        elif col>=2*n+row:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
# #PROBLEMFF
for row in range(1,2*n+1):
    for col in range(1,4*n):
        if col<row:
            print("*",end=' ')
        elif col>4*n-row-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


# #PATTERNGG
for row in range(1,4*n):
    if row<=2*n:
        for col in range(1,2*n+1):
            if col>2*n-row:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
    else:
        for col in range(1,2*n+1):
            if col>=row-2*n+1:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
# #PATTERNHH
for row in range(1,4*n):
    if row<=2*n:
        for col in range(1,4*n):
            if col<=2*n-row:
                print("*",end=' ')
            elif col>=2*n+row:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
    else:
        for col in range(1,4*n):
            if col<=row-2*n:
                print("*",end=' ')
            elif col>=4*n-(row-2*n):
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()

#PATTERN II
def butterfly(n=5):

    for row in range(1,2*n+1):
        if row<=n:
            for col in range(1,2*n+1):
                if col<=row or col>2*n-row:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            
        else:
            for col in range(1,2*n+1):
                if col<=n-(row-n) or col>n+(row-n):
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
        print()
#PROBLEM GB SWITCH CASE
def gbSwithcase(n=5,borderStyle=0):
    for row in range(1,2*n+n//2+1):
        if borderStyle == 1:
            for col in range(1,4*n+n//2+2):
                #layer one 
                condition = (row+col == 2*n+n//2+1 and row<=n-1) or (col-row == 2*n+1 and row<=n-1) or ((col-row == n or row+col == 4*n-1) and row>=n and row<=2*n+n//2)

                condition = condition or (row == 2*n-n//2 and col>=5 and col<=4*n-1)

                condition = condition or ((row+col == 3*n-n//2 or col-row==2*n+1) and row>=2*n-1)

                condition = condition or row == 2*n+n//2 and (col<=n+n//2 or col>=3*n+n//2)

                if condition:
                    print("0",end=' ')
                else:
                    print(" ",end=' ')

        elif borderStyle == 2:
            for col in range(1,4*n+n//2+2):
                #including layer one part here 
                condition = (row+col == 2*n+n//2+1 and row<=n-1) or (col-row == 2*n+1 and row<=n-1) or ((col-row == n or row+col == 4*n-1) and row>=n and row<=2*n+n//2)

                condition = condition or (row == 2*n-n//2 and col>=5 and col<=4*n-1)

                condition = condition or ((row+col == 3*n-n//2 or col-row==2*n+1) and row>=2*n-1)

                condition = condition or row == 2*n+n//2 and (col<=n+n//2 or col>=3*n+n//2)
                #inner part of borderstyle2 #layer 2 (layertwo)
                condition = condition or ((row+col == 3*n-1 or col-row == 2*n) and (row>=n//2 and row<=n-1)) or (col-row == n+1 or row+col == 4*n-n//2) and (row>=n-1 and row<=n+1)

                condition = condition or ((col-row == n+1 or row+col == 4*n-n//2) and (row>=2*n-1 and row<=2*n+1)) or ((row+col == 3*n-1 or col-row == 2*n) and (row>=2*n-1 and row<=2*n+1))

                condition = condition or (row==2*n-1 and (col>=n and col<=2*n-1)) or (row==2*n-1 and (col>=3*n and col<=4*n-1))

                condition = condition or ((row == 2*n+1) and (col>=n//2+1 and col<=n+1)) or ((row == 2*n+1) and (col>=3*n+n//2 and col<=4*n+1))
                #layer two end here#############################################
                if condition:
                    print("0",end=' ')
                else:
                    print(" ",end= ' ')

        elif borderStyle == 0:
            for col in range(1,4*n+n//2+2):
                #including layer one part here 
                condition = (row+col == 2*n+n//2+1 and row<=n-1) or (col-row == 2*n+1 and row<=n-1) or ((col-row == n or row+col == 4*n-1) and row>=n and row<=2*n+n//2)

                condition = condition or (row == 2*n-n//2 and col>=5 and col<=4*n-1)

                condition = condition or ((row+col == 3*n-n//2 or col-row==2*n+1) and row>=2*n-1)

                condition = condition or row == 2*n+n//2 and (col<=n+n//2 or col>=3*n+n//2)
                #inner part of borderstyle2 #layer 2 (layertwo)
                condition = condition or ((row+col == 3*n-1 or col-row == 2*n) and (row>=n//2 and row<=n-1)) or (col-row == n+1 or row+col == 4*n-n//2) and (row>=n-1 and row<=n+1)

                condition = condition or ((col-row == n+1 or row+col == 4*n-n//2) and (row>=2*n-1 and row<=2*n+1)) or ((row+col == 3*n-1 or col-row == 2*n) and (row>=2*n-1 and row<=2*n+1))

                condition = condition or (row==2*n-1 and (col>=n and col<=2*n-1)) or (row==2*n-1 and (col>=3*n and col<=4*n-1))

                condition = condition or ((row == 2*n+1) and (col>=n//2+1 and col<=n+1)) or ((row == 2*n+1) and (col>=3*n+n//2 and col<=4*n+1))
                #layer two end here#############################################

                #third layer
                condition = condition or (col == 2*n+n//2 and row>=n//2+1 and row<=n) or (row == n-1 and col>=2*n+1 and col<=3*n-n//2) or (row == 2*n and col>=n and col<=n+n//2) or (row == 2*n and col>=3*n+1 and col<=4*n-1)
                #third layer end here#########################
                if condition:
                    print("0",end=' ')
                else:
                    print(" ",end=' ')

        else:
            print("AVAILABLE BORDERSTYLE 0,1,2\nCHECK THE BORDERSTYLE PARAMETER")

        print()
#PATTERN NUMBER1A I THINK 1B ALSO INCLUDED IN THIS FUNCTION
def a1(n=5):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(row,end=' ')
        print()

    print()

    for row in range(1,n+1):
        for sp in range(1,n-row+1):
            print(" ",end=' ')
        for col in range(1,row+1):
            print(row,end=' ')
        print()

    for row in range(1,n+1):
        for col in range(1,n-row+1):
            print(" ",end=' ')
        for num in range(row,0,-1):
            print(num,end=' ')

        print()

    for row in range(1,n+1):
        for col in range(n,0,-1):
            if col<=row:
                print(row,end=' ')
            else:
                print(" ",end=' ')
        print()
#PATTERN NUMBER1C
def c1(n=5):
    for row in range(1,n+1):
        for col in range(1,n-row+2):
            print(n-row+1,end=" ")
        print()

    for row in range(1,n+1):
        for col in range(1,n+1):
            upper_limit = (n+1-row)
            if col<=upper_limit:
                print(upper_limit,end= " ")
            
        print()

    for row in range(1,n+1):
        upper_limit=n+1-row
        for col in range(1,upper_limit+1):
            print(upper_limit,end=" ")
        print()

    for row in range(n,0,-1):
        for col in range(1,row+1):
            print(row,end=' ')
        print()
#PATTERN NUMBER 1D
def d1(n=5):
    for row in range(n,0,-1):
        for col in range(1,n-row+1):
            print(" ",end=" ")
        for num in range(1,row+1):
            print(row,end=" ")
        print()

    for row in range(1,n+1):
        for col in range(1,n+1):
            if col<row:
                print(" ",end=" ")
            else:
                print(n-row+1,end=" ")
        print()

    for row in range(n,0,-1):
        for col in range(1,n+1):
            if col<=n-row:
                print(" ",end=" ")
            else:
                print(row,end=" ")
        print()

    for row in range(n,0,-1):
        for col in range(n,0,-1):
            if col<=row:
                print(row,end=" ")
            else:
                print(" ",end=" ")
        print()
#PATTERN NUMBER 1E
def e1(n=5):
    for row in range(1,n+1):
        for col in range(1,n+row+1):
            if col<=n-row+1:
                print(" ",end=" ")
            else:
                print(row,end=" ")
        print()
    
    for row in range(1,n+1):
        for col in range(1,2*n):
            if col>=((n+1)-row) and (col<=n+row-1):
                print(row,end=" ")
            else:
                print(" ",end=" ")
        print()
#PATTERN NUMBER 1F
def f1(n=5):
    for row in range(1,n+1):
        for col in range(1,row+1):
            if row%2 == 0:
                print("0",end=" ")
            else:
                print("1",end=" ")
        print()

    for row in range(1,n+1):
        for col in range(1,row+1):
            if row%2==1:
                num = 1
            else:
                num = 0
            print(num,end=" ")
        print()
#NUMBER PATTERN AA
def aa(n=5):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(col,end=" ")
        print()
#NUMBER PATTERN BB
def bb(n=5):
    for row in range(1,n+1):
        for col in range(1,n-row+1):
            print(" ",end=" ")
        for num  in range(row,0,-1):
            print(num,end=" ")
        print()

    for row in range(1,n+1):
        for col in range(n,0,-1):
            if col<=row:
                print(col,end=" ")
            else:
                print(" ",end=" ")
        print()
#NUMBER PATTERN CC
def cc(n=5):
    for row in range(1,n+1):
        for col in range(1,n+1-row+1):
            print(col,end=" ")
        print()

    for row in range(1,n+1):
        for col in range(1,n+1):
            if col>=1 and col<=n+1-row:
                print(col,end=" ")
        print()

    for row in range(1,n+1):
        for col in range(1,n+1):
            if col<=n+1-row:
                print(col,end=" ")
        print()

    for row in range(0,n):
        for col in range(1,n+1):
            if col<=n-row:
                print(col,end=" ")
            else:
                print(" ",end=" ")
        print()
#NUMBER PATTERN DD
def dd(n=5):

    for row in range(n,0,-1):
        for col in range(n,0,-1):
            if col<=row:
                print(col,end=" ")
            else:
                print(" ",end=" ")
        print()

    for row in range(1,n+1):
        for col in range(n,0,-1):
            if col>=1 and col<=n+1-row:
                print(col,end=" ")
            else:
                print(" ",end=" ")
        print()

    for row in range(1,n+1):
        for col in range(n,0,-1):
            if  col<=n+1-row:
                print(col,end=" ")
            else:
                print(" ",end=" ")
        print()

    for row in range(0,n):
        for col in range(n,0,-1):
            if col<=n-row:
                print(col,end=' ')
            else:
                print(" ",end=" ")
        print()
#NUMBER PATTERN EE
def ee(n=5):
    for row in range(1,n+1):
        for col in range(1,n-row+1):
            print(" ",end=" ")
        for num in range(row,0,-1):
            print(num,end=" ")
        for nums in range(1,row+1):
            print(nums,end=" ")
        print()

    print()

    for row in range(1,n+1):
        num = row
        for col in range(1,2*n+1):
            if col>=n+1-row and col<=n+row-1:
                if col<n:
                    print(num,end=" ")
                    num = num - 1
                elif col>=n:
                    print(num,end=" ")
                    num = num + 1
            else:
                print(" ",end=" ")
        print()

    for row in range(1,n+1):
        for col in range(1,n+row):
            if col>n-row:
                print(col,end=" ")
            else:
                print(" ",end=" ")
        print()
#NUMBER PATTERN FF    
def ff(n=5):
    numset2 = 0
    for row in range(0,n):
        for col in range(1,2*n):
            ll_num = (n-1) if row == 0 else n-row
            ll_sp = 0 if row == 0 else (n-row+1)
            up_sp = -1 if row == 0 else (n+row-1)
            if col<=ll_num:
                numset1 = col
                print(numset1,end=" ")
                if col == ll_num:
                    numset2 = numset1
            elif col>= ll_sp and col<=up_sp:
                print(" ",end=" ")
            else:
                if row == 0 and col == n:
                    numset2 = n
                print(numset2,end=" ")
                numset2-=1
        print()
def abc(n=5):
    numset2 = 0
    for row in range(0,n):
        for col in range(1,2*n):
            ll_num = (n-1) if row == 0 else n-row
            ll_sp = 0 if row == 0 else (n-row+1)
            up_sp = -1 if row == 0 else (n+row-1)
            if col<=ll_num:
                numset1 = col
                print(chr(numset1-1+65),end=" ")
                if col == ll_num:
                    numset2 = numset1
            elif col>= ll_sp and col<=up_sp:
                print(" ",end=" ")
            else:
                if row == 0 and col == n:
                    numset2 = n
                print(chr(numset2-1+65),end=" ")
                numset2-=1
        print() 

n = 5;unicodeA = 65;unicodea= 97;unicode1 = 49;

def printPattern(param1,param2):
    numset1 = 0;numset2=0
    for row in range(0,param1):
        for col in range(1,2*param1):
            ll_lt_num = (param1-1) if row == 0 else (param1-row)
            ll_lt_spaces = 0 if row == 0 else (param1-row+1)
            up_lt_spaces = -1 if row == 0 else (param1+row-1)

            if col<=ll_lt_num:
                numset1 = col
                print(chr(numset1-1+param2),end=" ")
            elif col>= ll_lt_spaces and col<= up_lt_spaces:
                print(" ",end=" ")
            else:
                if row == 0 and col == param1:
                    numset2 = param1

                print(chr(numset2-1+param2),end=" ")
                numset2-=1
        print()

def aaa(n=5):
    for row in range(1,n+1):
        for col in range(row,2*row-1+1):
            print(col,end=" ")
        print()

    for row in range(1,n+1):
        for col in range(row,2*row-1+1):
            if col%2 == 1:
                print(col,end=" ")
            else:
                print(" ",end=" ")
        print()

    for row in range(1,n+1):
        for col in range(row,2*row-1+1):
            if col%2 == 0:
                print(col,end=" ")
            else:
                print(" ",end=" ")
        print()

def bbb(n=5):
    for row in range(1,n+1):
        for sp in range(1,n-row+1):
            print(" ",end=" ")
        for num in range(2*row-1,row-1,-1):
            print(num,end=" ")
        print()

    for row in range(1,n+1):
        num = 2*row-1
        for col in range(1,n+1):
            
            if col<=n-row:
                print(" ",end=" ")
            elif num>=row:
                print(num,end=" ")
                num -= 1
        print()

bbb()

