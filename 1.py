with open("file.txt", "w") as file:
        data = input().split()
        dt = 0
        for i in data:
            file.write(i + "\n")



def check_if_file_contains_only_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    float(line.strip())
                except ValueError:
                    return False
    except FileNotFoundError:
        return False
    return True

file_path = 'file.txt'
if check_if_file_contains_only_numbers(file_path):
    print("Файл содержит только числа.")

    
    with open("file.txt", "r") as file:
        fl = file.readlines()
        #print(int(fl[0])+int(fl[1]))
        fl_int = [""] * len(fl)
        #print(len(fl_int))
        for i in range (len(fl)):
            fl_int[i] = int(fl[i])
        print(fl_int)
        maxx = max(fl_int)
        minn = min(fl_int)
        summ = sum(fl_int)
        print(maxx,minn,summ)
    
    with open("file.txt", "a") as file:
        file.write(str(maxx))
        file.write('\n')
        file.write(str(minn))
        file.write('\n')
        file.write(str(summ))
else:
    print("Файл содержит нечисловые значения.")





    