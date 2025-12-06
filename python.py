import circle, recta
x=input("Do you wanna find area and perimeter of shapes y/n ? : ")
while x=='y':
    ch=int(input("1. Area of circle \n2. circumference of circle \n3. Area of rectangle \n4. Perimeter of rectangle\n Enter your choice : "))
    if ch==1:
        a=circle.area_cir()
        print(a)
        b=input("Do you wanna continue y/n ?: ")
        if b=='y':
            pass
        else: 
            print("THANK YOU")
            break
    elif ch==2:
        a=circle.cir_c('r')
        print(a)
        b=input("Do you wanna continue y/n ? : ")
        if b=='y':
            pass
        else: 
            print("THANK YOU")
            break
    elif ch==3:
        a=recta.area_rect()   
        print(a) 
        b=input("Do you wanna continue y/n ?: ")
        if b=='y':
            pass
        else: 
            print("THANK YOU")
            break
    elif ch==4:
        a=recta.peri_rect()
        print(a)    
        b=input("Do you wanna continue y/n ?: ")
        if b=='y':
            pass
        else: 
            print("THANK YOU")
            break
    else:
        print("WRONG INPUT")    