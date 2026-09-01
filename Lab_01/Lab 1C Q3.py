def MtoKm(a):
    return a/1000
def KmtoM(a):
    return a*1000
def CmtoM(a):
    return a/100
def CmtoMm(a):
    return a * 10
def menu():
    user_input = 0
    while user_input != 5:
        print("1. Meter to Km\n2. Km to Meter\n3. Centimetre to Meter\n4. Centime to Millimetre\n5. Quit\n")
        user_input = int(input("Enter your choice:"))
        if user_input == 1:
            a = float(input("Enter value in meters:"))
            print(MtoKm(a))
        if user_input == 2:
            a = float(input("Enter value in Km :"))
            print(KmtoM(a))
        if user_input == 3:
            a = float(input("Enter value in Cm :"))
            print(CmtoM(a))
        if user_input == 4:
            a = float(input("Enter value in Cm :"))
            print(CmtoMm(a))
        if user_input == 5:
            return


