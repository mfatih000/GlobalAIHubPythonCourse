#User Login Application

nm0 = (input("Enter Your Nickname(For Login):"))
pw0 = (input("Enter Your Password(For Login):"))

keys ={"nick_name": nm0 , "password": pw0 }
pass_counter=5
while True:
    nm = (input("Enter Your Nickname(For SignIn) :"))
    pw = (input("Enter Your Password(For SignIn):"))


    if(nm==keys["nick_name"]):
        if(pw==keys["password"]):
            print("Welcome")
            break



    elif (pass_counter>0 and nm!= "nickname"):
        print("LOGİN FAİLED")
        pass_counter -= 1
        print("Left:",pass_counter)


    elif(pass_counter==0):
        print("Your Account Is Deleted")
