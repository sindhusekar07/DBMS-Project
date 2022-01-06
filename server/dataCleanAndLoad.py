import mysql.connector
import sys


def createUser(filename):
    connection = mysql.connector.connect(host='localhost',
                                         database='sys',
                                         user='root',
                                         password='$indhu95R')
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    cursor = None
    for command in sqlCommands:
        try:
            cursor =connection.cursor(buffered=True)
            if command.strip() != '':
                cursor.execute(command)
                #myresult = cursor.fetchone()
                connection.commit()
                #print(myresult)
        except IOError:
            print ("Command skipped: ")
        finally:    
            if cursor :
                cursor.close()
    connection.close()

def createTables(user_input):
    connection = mysql.connector.connect(host='localhost',
                                         database='covidVaccine_656',
                                         user='admin',
                                         password='admin123')
    if(user_input == "1"):
        filename = "/Users/sindhumathiramalingam/Downloads/WaterlooAcademics/ECE656/Project/ece-656/server/tableCreation.sql"
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')
        cursor = None
        for command in sqlCommands:
            try:
                cursor =connection.cursor(buffered=True)
                if command.strip() != '':
                    cursor.execute(command)
                    #myresult = cursor.fetchone()
                    connection.commit()
                    #print(myresult)
            except IOError:
                print ("Command skipped: ")
            finally:    
                if cursor :
                    cursor.close()
    connection.close()

def dataPreprocessAndLoading(user_input):
    connection = mysql.connector.connect(host='localhost',
                                         database='covidVaccine_656',
                                         user='admin',
                                         password='admin123')
    if(user_input == "2"):
        filename = "/Users/sindhumathiramalingam/Downloads/WaterlooAcademics/ECE656/Project/ece-656/server/dataPreProcessing.sql"
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')
        cursor = None
        for command in sqlCommands:
            try:
                cursor =connection.cursor(buffered=True)
                if command.strip() != '':
                    cursor.execute(command)
                    #myresult = cursor.fetchone()
                    connection.commit()
                    #print(myresult)
            except IOError:
                print ("Command skipped: ")
            finally:    
                if cursor :
                    cursor.close()
    connection.close()

if __name__ == "__main__":
  
    createUser('/Users/sindhumathiramalingam/Downloads/WaterlooAcademics/ECE656/Project/ece-656/server/userCreation.sql')

    while True:
            print("Enter the choice:\n")
            print("1. Table Creation")
            print("2.Data Pre-processing and Data Loading data into tables")
            print("3. End")
            user_input = input()
            prev_choice = None;
            if(user_input == "1"):
                createTables(user_input)
                prev_choice = user_input
            elif (user_input == "2"):

                dataPreprocessAndLoading(user_input)
            elif (user_input == "3"):
                sys.exit(1)

