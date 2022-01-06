from datetime import datetime
'''
This file contains the validation check for the attributes that validates before inserting into the table
and also, implemented the mandatory and optional attributes conditions
'''
def vaers_id():
    while(True):
        try:
            vaers_ID = input("Enter vaers_ID: ")
            if ((vaers_ID.isdigit()) and (len(vaers_ID) == 6)):
                return vaers_ID
            else:
                print("Error:Incorrect format. Please enter a valid input!")
        except:
            print("Error:Invalid format")

def age():
    while(True):
        try:
            age = input("Enter age in years: ")
            if ((age.isdigit()) and (len(age) <= 2) and ((age > "0") and (age <= "99"))):
                return age
            else:
                print("Error:Incorrect format. Please enter a valid input!")
        except:
            print("Error:Invalid format")

def gender():
    while(True):
        try:
            gen = input("Enter the sex: ")
            if gen.upper() == "M":
                return gen
            elif gen.upper() == "F":
                return gen
            else:
                print("Error:Incorrect format. Please enter F or M!")
        except:
            print("Error:Invalid format")

def vaccine_manufacturer():
    while(True):
        try:
            vcc_m = input()
            if ((vcc_m.isalpha()) and (len(vcc_m) <= 25) and (len(vcc_m) > 0)):
                return vcc_m
            else:
                print("Error:Incorrect format. Please enter a valid input")
        except:
            print("Error:Invalid format")

def postal_code():
    while(True):
        try:
            state = input()
            if ((state.isalpha()) and (len(state) == 2)):
                return state
            else:
                print("Error: Invalid format. Please enter a valid input")
        except:
            print("Error:Invalid format")

def route():
    while(True):
        try:
            print("Enter the vaccine route of administration\nUN-Unknown\nID-Intradermal\nIM-Intramuscular\nSC-Subcutaneous\nIN-Intranasal\nPO-Pre Oral\nSYR-Needleand syringe\nJET-Needle free jet injector device\nOT-Other")
            v_route = input("Enter vaccine route: ")
            r_list = ["UN", "ID", "IM", "SC", "IN", "PO", "SYR", "JET", "OT"]
            for i in r_list:
                if (i == v_route):
                    return v_route
                else:
                    pass
        except:
            print("Error:Invalid input")

def v_admin():
    while(True):
        try:
            v_adm = input("Enter the facility vaccine administered: ")
            if ((v_adm.isalpha()) and (len(v_adm) == 3)):
                return v_adm
            else:
                print("Error: Invalid format. Please enter a valid input")
        except:
            print("Error:Invalid format")

def date():
    while(True):
        try:
            d = input("Enter the date in the format yyyy-mm-dd: ")
            if (d == ""):
                return d
            else:
                format = "%Y-%m-%d"
                res = True
                res = bool(datetime.strptime(d, format))
                if (res == True):
                    return d
                else:
                    print("Error:Invalid format. Enter in the format yyyy-mm-dd")
        except:
            print("Error:Invalid input format")

def single_val():
    while(True):
        try:
            input_val = input()
            if ((input_val.upper() == "Y") or (input_val.upper() == "N") or (input_val=="")):
                return input_val
            else:
                print("Error:Invalid input. Please enter a valid input Y or N")
        except:
            print("Error:Invalid format")

def v_series():
    while(True):
        try:
            dose_series = input("Enter the vaccination dose series: ")
            if ((dose_series.isdigit()) and (len(dose_series)==1)):
                return dose_series
            else:
                print("Error:Invalid input. Please enter a valid dose series number")
        except:
            print("Error:Invalid format")

def num_days():
    while(True):
        try:
            days = input("Enter the number of days: ")
            if (days.isdigit()):
                return days
            elif(days == ""):
                return days
            else:
                print("Error:Invalid format. Please enter a valid input!")
        except:
            print("Error:Invalid format")

def f_version():
    while(True):
        try:
            version = input("Enter the form version: ")
            if (len(version.rsplit('.')[-1])==2):
                return version
            elif (version == ""):
                    return version
            else:
                print("Error:Invalid input. Please enter a valid form version")
        except:
            print("Error:Invalid format")

def symptom():
    while(True):
        try:
            symp = input("Enter symptom1: ")
            if ((len(symp) > 0) and (len(symp) <=255)):
                return symp
            else:
                print("Error:Invalid input. Please enter the symptom details")
        except:
            print("Error:Invalid format")


def sym_version():
    while(True):
        try:
            s_ver = input("Enter the symptom version: ")
            if ((len(s_ver.rsplit('.')[-1])==1)  or (s_ver == "")):
                return s_ver
            else:
                print("Error:Invalid input. Please enter a valid symptom version")
        except:
            print("Error:Invalid format")

