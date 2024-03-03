m1 = open('matrix_1.txt', 'r')
m2 = open("matrix_2.txt", 'r')
m3 = open("matrix_3.txt", 'w')

print("введите размерность первой матрицы")
sz_1 = input().split()
print("введите размерность второй матрицы")
sz_2 = input().split()

if sz_1[1] == sz_2[0]:
    print("матрицы можно перемножить")
    print('размер получившейся матрицы: ' + str(sz_1[0]) + "x" + str(sz_2[1]) )

i=0
j=0
number = 0 
add_ch = 0
for k in range (int(sz_1[0])):
    add_string = ''
    for l in range (int(sz_2[1])):
        add_num = 0
        ost = number % 3 
        cel = number // 3
        for w in range (int(sz_1[1])):
            print(m1.read()[cel+add_ch:w+2+add_ch]),(m2.read()[w+add_ch:ost+1+add_ch])
            add_num += int(m1.read()[cel+add_ch:w+1+add_ch])*int(m2.read()[w+add_ch:ost+1+add_ch])
    m3.write(add_string +'\n')
    add_ch += 1
print(m1.read()[5:6])
 

