def pascalTriangle(num):
    ls = [
        [1],
        [1,1],
        [1,2,1]
    ]
    for j in range(num-3):
        nRow = [1]
        for i in range(len(ls[-1])):
            if i != len(ls[-2]):
                n = ls[-1][i] + ls[-1][i+1]
                nRow.append(n)
        nRow.append(1)
        ls.append(nRow)
        # nRow.clear()
    [print(i) for i in ls]

num = int(input("Enter the number of rows you want of pascal's triangle: "))
pascalTriangle(num)
