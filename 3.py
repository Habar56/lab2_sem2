with open("mesta.txt", "r") as dt:
    l = dt.readlines()
    print(l)
    data = [line.rstrip() for line in l]
    print(data)
    
    kolvo_nf = 0
    for i in data:
        for j in i:
            kolvo_nf += int(j)
    print("занято: ",kolvo_nf)
    
    kolvo_mest = 0
    for i in data:
        kolvo_mest += len(i)
    print("всего: ", kolvo_mest)
    
    print("свободно: ", kolvo_mest-kolvo_nf)

    nomer_ryada = 0
    for i in data:
        nomer_ryada += 1
        kolvo_v_ryadu = 0
        for j in i:
            kolvo_v_ryadu += int(j)
        kolvo_v_ryadu_svobodno = len(i) - kolvo_v_ryadu
        print ("свободно в " + str(nomer_ryada) + " ряду: " + str(kolvo_v_ryadu_svobodno))

    print("введите номер ряда и места")
    ryad = int(input())
    mesto = int(input())
    rd = data[ryad-1]
    mt = rd[mesto-1]
    if int(mt):
        print("занято")
    else:
        print("свободно")

        


