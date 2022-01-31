def min_tem(table):
    mintemp = table[0][2]
    for i in range(0, len(table)):
        if table[i][2] < mintemp:
            mintemp = table[i][2]
        else:
            continue
    return mintemp

def max_tem(table):
    maxtemp = table[0][2]
    for i in range(1, len(table)):
        if table[i][2] > maxtemp:
            maxtemp = table[i][2]
        else:
            continue
    return maxtemp
    
infile = open( "temp.txt" )
table=[]
Sum_Temperature=0
for line in infile :
    line=line.split(",")
    line[2]=int(line[2])
    table.append(line)
    
print("The minimum temperature is",min_tem(table),"The maximum temperature is",max_tem(table))
    
