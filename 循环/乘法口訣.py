# coding= utf-8
row = 1
while row <= 9:
    col=1
    while col <= row:
        values = col * row
        print(" %d * %d = %d" % (col, row, values), end="\t")
        col += 1
    #print("行號%d" %row)
    print("")
    row += 1

