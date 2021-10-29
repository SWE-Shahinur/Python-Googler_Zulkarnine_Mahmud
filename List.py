grosery_list=["potato","egg"]
print(grosery_list)
grosery_list.append("water")
print(grosery_list)

l2=list()
print(l2)
l2.append(4)
print(l2)
l2.append("computer")
print(l2)

#-second item found
find_item=grosery_list[1]
print(find_item)
print(grosery_list[-1])

#-shorting
grosery_list.sort()
print(grosery_list)
number=[3,1,8,2,5,0]
number.sort()
print(number)

#or,sorting
num=[2,8,1,5,0]
num_sort=sorted(num)
print(num)
print(num_sort)