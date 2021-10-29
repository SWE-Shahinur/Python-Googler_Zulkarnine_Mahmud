def is_even(numbr):
    if numbr % 2 == 0:
        return True
    else:
        return False


starting=0
while starting<10:
    if is_even(starting):
        print(starting," is even")
    else:
        print(starting," is odd")
    starting=starting+1

#listed and user input whie loop
even_number=[]
user_input=int(input("enter limit: "))
starting=0
while starting<user_input:
    if is_even(starting):
        even_number.append(starting)
    starting=starting+1
print("even number",even_number)

print("while program finised")

#for loop
user_inputs=int(input("enter integer number limit:"))
even_list=[]
for value_num in range(0,user_inputs):
    if is_even(value_num):
        even_list.append(value_num)
print(even_list)
print("for loop program finised")


#another for loop
grocery=["carrot","graps", "painapple"]
for item in grocery:
    print(item)
print("grocery list end")
#water print hbe na
grocry=["water","onion","potato"]
for items in grocry:
    if items=="water":
        continue

    print(items)
print("for loop continue end")

grocry_itm=["water","onion","potato","pasta"]
for items in grocry_itm:
    if items=="potato":
        break

    print(items)
print("for loop break end")

print("normal for loop")
for i in range(0,20,3):
    print(i)


print("flower list for loop")
flower=["waterlily","red flower","white flower"]
for i in range(0,len(flower)):
    print(flower[i])