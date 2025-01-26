LIST=[1,2,3,4,5,6,7,8,7,9,0,4,7]
duplicates=[]
for dup in LIST:
    if LIST.count(dup)>1:
        if dup not in duplicates:
            duplicates.append(dup)
print(duplicates)
