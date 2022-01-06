#!/usr/bin/python
#from functionalities import connection_test, add, modify, vaccine_cause_death, death_count, vaccine_type, adverse_effects, conn_exit, doctor_login, admin_login, nurse_login, view
from functionalities import *
from getpass import getpass
import os
def admin():
    '''
        Performing the operations based on user's preference and privileges applied to the respective user
        '''
    while (True):
        print("Select the operation to be performed:\n "
              "(1) Add a record\n "
              "(2) Modify a record\n "
              "(3) Delete a record\n "
              "(4) View a record\n "
              "(5) Logout and Return to main page to switch user\n "
              "(6) Exit\n ")
        val = input("Enter the input: ")
        os.system('cls')
        if val == "1":
            add()
        elif val == "2":
            modify()
        elif val == "3":
            delete()
        elif val == "4":
            view()
        elif val == "5":
            main()
        elif val == "6":
            conn_exit()
            print("Thank you!")
            quit()
        else:
            print("Invalid operation")

def doctor():
    '''
    Performing the operations based on user's preference and privileges applied to the respective user
    '''
    while (True):
        print("Select the operation to be performed:\n "
              "(1) Add a record\n "
              "(2) Modify a record\n "
              "(3) Vaccine details of died patients\n "
              "(4) Number of Deaths due to vaccine\n "
              "(5) Count of died patients with respect to vaccine type\n "
              "(6) Adverse Effect of different types of vaccine\n "
              "(7) View the record\n "
              "(8) Logout and Return to main page to switch user\n "
              "(9) Exit\n ")
        val = input("Enter the input: ")
        os.system('cls')
        if val == "1":
            add()
        elif val == "2":
            modify()
        elif val == "3":
            vaccine_cause_death()
        elif val == "4":
            death_count()
        elif val == "5":
            vaccine_type()
        elif val == "6":
            adverse_effects()
        elif val == "7":
            view()
        elif val == "8":
            main()
        elif val == "9":
            conn_exit()
            print("Thank you!")
            quit()
        else:
            print("Invalid operation")

def nurse():
    '''
    Performing the operations based on user's preference and privileges applied to the respective user
    '''
    while (True):
        print("Select the operation to be performed:\n "
              "(1) Vaccine details of died patients\n "
              "(2) Number of Deaths due to vaccine\n "
              "(3) Count of died patients with respect to vaccine type\n "
              "(4) Adverse Effect of different types of vaccine\n "
              "(5) View a record\n "
              "(6) Logout and Return to main page to switch user\n "
              "(7) Exit")
        val = input("Enter the input: ")
        os.system('cls')
        if val == "1":
            vaccine_cause_death()
        elif val == "2":
            death_count()
        elif val == "3":
            vaccine_type()
        elif val == "4":
            adverse_effects()
        elif val == "5":
            view()
        elif val == "6":
            main()
        elif val == "7":
            print("Thank you!")
            quit()
        else:
            print("Invalid operation")

def main():
    '''
    Checking the status of MySQL server
    '''
    print("Welcome to Vaccine Adverse Event Reporting System!\nMySQL server Status:")
    connection_test()
    while(True):
        '''
        Taking input from the user to login into MySQL server as Admin/Doctor/Nurse
        '''
        print("Press 1 to login as Admin\nPress 2 to login as Doctor\nPress 3 to login as Nurse")
        val = input()
        os.system('cls')

        if val == "1":
            user = input("Enter Username: ")
            passwd = getpass("Enter password: ")
            admin_login(user, passwd)
            if (admin_login(user, passwd) == 1):
                admin()

        if val == "2":
            user = input("Enter Username: ")
            passwd = getpass("Enter password: ")
            if(doctor_login(user, passwd) == 1):
                doctor()

        elif val == "3":
            user = input("Enter Username: ")
            passwd = getpass("Enter password: ")
            if (nurse_login(user, passwd) == 1):
                nurse()
        else:
            print("Error:Invalid user name")



if __name__ == '__main__':
    main()