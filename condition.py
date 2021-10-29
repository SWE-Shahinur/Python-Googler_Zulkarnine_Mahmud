marks=int(input("inter your marks: "))
def show_grad(grad):
    print("your grad:",grad)
if marks>=80:
    show_grad("A+")
elif marks<80 and marks>=70:
    show_grad("A")
elif marks<70 and marks>=60:
    show_grad("A-")
elif marks<60 and marks>=50:
    show_grad("A-")
elif marks>=33:
    show_grad("pass")
else:
    show_grad("fail")
print("finised")

#or
mark=int(input("enter your mark: "))
if mark>80 or mark<30:
    print("you are good or bad")
    if mark>80:
        print("excellent")
    else:
        print("not so good")
else:
    print("you are oky")


#true/false
the_user_is_good=80>60
print(the_user_is_good)
#user inpput true or false
e_number=int(input("give a number: "))
user_number=e_number>80
print(user_number)
