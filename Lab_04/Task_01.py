fever = False
Pain_in_Abdomen = False
vomiting = False
TlC_high = False
DLC_high = False
N_high = False
ESR_high = False
cough = False
Red_Enlarged_Tonsils = False
Pain_in_chest = False
Pus_in_tonsil = False
selection_ccompleted = False
acute_appendicitis = False
Pneumonia = False
Acute_Tonsil = False
pneumonia_patch = False

def menu2():
    global TlC_high, DLC_high, ESR_high, pneumonia_patch, Red_Enlarged_Tonsils, Pus_in_tonsil
    if(acute_appendicitis):
        print("Test : Blood CP with ESR")
        ans = input("Is TLC High?   Y/N: ")
        if ans == "Y":
            TlC_high = True
        ans = input("Is DLC High?   Y/N: ")
        if ans == "Y":
            DLC_high = True
        ans = input("Is ESR High?   Y/N: ")
        if ans == "Y":
            ESR_high = True
        if(TlC_high and DLC_high and ESR_high):
            print("You have Acute Appendicitis\nTreatment: Surgery")
        else:
            print("You dont have Acute Appendicitis")
        return
    if(Pneumonia):
        print("Test : Blood CP with ESR and Chest X-Ray")
        ans = input("Is TLC High?   Y/N: ")
        if ans == "Y":
            TlC_high = True
        ans = input("Is DLC High?   Y/N: ")
        if ans == "Y":
            DLC_high = True
        ans = input("Is ESR High?   Y/N: ")
        if ans == "Y":
            ESR_high = True
        ans = input("Does X-Ray reveal Pneumonia patch?   Y/N: ")
        if ans == "Y":
            pneumonia_patch = True
        if(TlC_high and DLC_high and ESR_high and pneumonia_patch):
            print("You have Pneumonia\nTreatment: Antibiotics")
        else:
            print("You dont have Pneumonia")
        return
    if(Acute_Tonsil):
        print("Test : Examine Throat")
        ans = input("Red enlarged tonsils?   Y/N: ")
        if ans == "Y":
            Red_Enlarged_Tonsils = True
        ans = input("Pus in tonsils?   Y/N: ")
        if ans == "Y":
            Pus_in_tonsil = True
        if(Pus_in_tonsil and Red_Enlarged_Tonsils):
            print("You have Acute Tonsillitis\nTreatment: Antibiotics orally and if not gone add antibiotics IV")
        else:
            print("You dont have Acute Tonsillitis")
        return

def menu1():
    global fever, Pain_in_Abdomen, vomiting, cough, Pain_in_chest, selection_ccompleted
    while selection_ccompleted == False:
        print("Select Symptoms:")
        print("1. Fever")
        print("2. Pain_in_Abdomen (ILIAC FOSSA)")
        print("3. Vomiting")
        print("4. Cough (with Sputum)")
        print("5. Pain in chest")
        print("6. All Selected")
        user_input = input()
        if user_input == "1":
            fever = True
        if user_input == "2":
            Pain_in_Abdomen = True
        if user_input == "3":
            vomiting = True
        if user_input == "4":
            cough = True
        if user_input == "5":
            Pain_in_chest = True
        if user_input == "6":
            selection_ccompleted = True

menu1()

if (fever and Pain_in_Abdomen and vomiting):
    acute_appendicitis = True
    menu2()
    exit()
elif (fever and cough and Pain_in_chest):
    Pneumonia = True
    menu2()
    exit()
elif (fever and cough):
    Acute_Tonsil = True
    menu2()
    exit()
else:
    print("No matching disease profile for entered symptoms.")