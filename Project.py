Vehicle_Number=[]
Vehicle_Type=[]
Vehicle_Name=[]
Owner_Name=[]
Hours=[]
Date=[]
Minutes=[]
Parked_time=[]
bikes=50
cars=50
while True:
    print("\n\n")
    print("                Parking Management System")
    print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    print("1.Vehicle Entry")
    print("2.Remove Entry" )
    print("3.View Parked Vehicle ")
    print("4.View Available Parking Space ")
    print("5.Parking charges ")
    print("6.Bill")
    print("7.Close Programme ")
    print("\n")
    opt=int(input())
     if opt==1:
        b=True
        while b==True:
            Vb=input("\tEnter vehicle number (XXXX-XX-XXXX) - ").upper()
            if Vb=="":
                print("###### Please enter Vehicle No. ######")
            elif Vb in Vehicle_Number:
                print("###### Vehicle Number Already Exists")
            elif Vb[4]!="-" or Vb[7]!="-":
                print("\t########Please Enter as given Format ########")
            elif len(Vb)==12:
                b=False
                Vehicle_Number.append(Vb)
            else:
                print("###### Enter Valid Vehicle Number ######")
        c=True
        while c==True:
            Vc=(input("\tEnter vehicle type(Bike=B/Car=C):")).lower()
            if Vc=="":
                print("Please enter vehicle type")
            elif Vc=="b":
                Vehicle_Type.append("Bike")
                bikes=bikes-1
                c=False
            elif Vc=="c":
                Vehicle_Type.append("Car")
                cars=cars-1
                c=False
            else:
                print("###### Please enter valid option ######")
        d=True
        while d==True:
            Vd=input("\tEnter vehicle name - ")
            if Vd=="":
                print("########Please Enter Vehicle Name ########")
            else:
                Vehicle_Name.append(Vd)
                d=False
        e=True
        while e==True:
            Ve=input("\tEnter owner's name - ")
            if Ve=="":
                print("###### Please enter Owner's name ######")
            else:
                Owner_Name.append(Ve)
                e=False
        g=True
        while g==True:
            Vg=datetime.datetime.now()
            hours = Vg.strftime("%H")
            minutes = Vg.strftime("%M")
            date = Vg.strftime("%D")
            Date.append(date)
            Hours.append(hours)
            Minutes.append(minutes)
            print("\tTime Of Entry : "+ hours +":"+minutes)
            g=False
        print("\n============== Record detail saved ==============\n")
        next_main=input("Press enter to got to the main menu")
