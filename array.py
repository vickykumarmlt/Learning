from array import array

val = array('i', [12, 45, 74, 67, 4])
# val.append(34)
# val.reverse()
# val.append(34)
#print(val[3])

newArr = array(val.typecode, (a for a in val))
for e in newArr:
    print(e)


