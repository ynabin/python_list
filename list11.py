#Remove an item whem we code thislist.pop(1) which element lies in 1 index then remove this element which lies in this index.
thislist = [10, 20, 30, 40]
reverse_list=[]
length=len(list)-1
i=1
while i<=length:
    reverse_list.insert(0,list[i])
    i+=1
    print(reverse_list)
    # error in code