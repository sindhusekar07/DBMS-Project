import mysql.connector
from prettytable import PrettyTable
from validation import vaers_id, age, gender, vaccine_manufacturer, postal_code, route, v_admin, date, single_val, v_series, num_days, f_version, symptom, sym_version

def connection_test():
    '''
    Function to test the MySQL DB connection as root user
    '''
    global mysql_conn
    mysql_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prince@07",
        port=3306,
        database="covidVaccine_656")
    if mysql_conn.is_connected() == False:
        print("MySQL server is not connected")
    else:
        print("MySQL server is connected")

def admin_login(user, passwd):
    '''
    Function to Switch from root user to admin
    '''
    user_conn = mysql_conn.cmd_change_user(
        username=user,
        password=passwd,
        database="covidVaccine_656")
    cursor = mysql_conn.cursor()
    cursor.execute("SELECT CURRENT_USER")
    result = cursor.fetchone()
    cursor.close()
    if (result[0] == "admin@localhost"):
        return 1
    else:
        return 0


def doctor_login(user, passwd):
    '''
    Function to Switch from root user to doctor
    '''
    user_conn = mysql_conn.cmd_change_user(
        username=user,
        password=passwd,
        database="covidVaccine_656")
    cursor = mysql_conn.cursor()
    cursor.execute("SELECT CURRENT_USER")
    result = cursor.fetchone()
    cursor.close()
    if(result[0] == "doctor@localhost"):
        return 1
    else:
        return 0

def nurse_login(user, passwd):
    '''
    Function to Switch from root user to Nurse
    '''
    user_conn = mysql_conn.cmd_change_user(
        username=user,
        password=passwd,
        database="covidVaccine_656")
    cursor = mysql_conn.cursor()
    cursor.execute("SELECT CURRENT_USER")
    result = cursor.fetchone()
    cursor.close()
    if (result[0] == "nurse@localhost"):
        return 1
    else:
        return 0


def conn_exit():
    '''
    Funtion to test whether MySQL DB got disconnected when user want to exit
    '''
    mysql_conn.close()
    if mysql_conn.is_connected() == False:
        print("MySQL server connection is closed")

def set_null(tbl, col, vaersID):
    '''
    Funtion to SET the blanks(Empty input from user) into NULL in database
    :param tbl: Determines the table
    :param col: Determines the column
    :param vaersID: Determines the vaersID(of patient)
    :return: Update NULL in the places of Empty input
    '''
    sql = "UPDATE tbl SET col = NULL where vaersID= v_id"
    sql = sql.replace("tbl", tbl)
    sql = sql.replace("col", col)
    sql = sql.replace("v_id", vaersID)
    cursor = mysql_conn.cursor()
    cursor.execute(sql)
    mysql_conn.commit()
    cursor.close()


def table_Info():
    ''' This function displays the table names to the user and
    receives the table name as input from user and
    displays the respective attribute Info of the table
    with respect to the user's choice
    '''
    while(True):
        try:
            tbl_query = "show tables"
            cursor = mysql_conn.cursor()
            cursor.execute(tbl_query)
            tables = cursor.fetchall()
            x = PrettyTable()
            x.field_names = ["TableName"]
            x.add_rows(tables)
            print(x)
            cursor.close()
            tbl_name = input("Enter the table name: ")
            desc_query = "desc %s" % tbl_name
            cursor = mysql_conn.cursor()
            cursor.execute(desc_query)
            desc = cursor.fetchall()
            x = PrettyTable()
            x.field_names =["Field", "Type", "Null", "Key", "Default", "Extra"]
            x.add_rows(desc)
            print(x)
            cursor.close()
            return tbl_name
        except:
            print("Error:Enter valid table name")


def add():
    '''
    Inserting a new record into a table
    Input: TableName
    :return: Row successfully inserted or not
    '''
    while(True):
        tbl_name = table_Info()
        if tbl_name == "patientDetails":
            while(True):
                try:
                    vaersID = vaers_id()
                    ageInYears = age()
                    if (int(ageInYears) <= 2):
                        cageInMonth = input("Enter the months of the children < 2 years: ")
                        cageInMonth = "0.00" if cageInMonth == "" else cageInMonth
                    else:
                        cageInMonth = "0.00"
                        #cageInMonth = "0.00" if cageInMonth == "" else cageInMonth
                    sex = gender()
                    insert_query = "INSERT INTO patientDetails(vaersID, ageInYears, cageInMonth, sex) values(%s,%s,%s,%s)"
                    cursor = mysql_conn.cursor()
                    args = vaersID, ageInYears, cageInMonth, sex
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully Inserted (", cursor.rowcount, ") row!")
                    cursor.close()
                    set_null(tbl_name, "cageInMonth", vaersID) if cageInMonth == "0.00" else cageInMonth
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return

        elif tbl_name == "vaccineDetails":
            while(True):
                try:
                    vaersID = vaers_id()
                    print("Enter vaccine manufacturer: ")
                    vaxManu = vaccine_manufacturer()
                    vaxLot = input("Enter vaccine lot: ")
                    print("Enter State: ")
                    state = postal_code()
                    vaxRoute = route()
                    print("Enter vaccine site: ")
                    vaxSite = postal_code()
                    print("Enter vaccine name: ")
                    vaxName = vaccine_manufacturer()
                    spltType = input("Enter the spltType: ")
                    vaxAdminBy = v_admin()
                    insert_query = "INSERT INTO vaccinedetails(vaersID, vaxManu, vaxLot, state, vaxRoute, vaxSite, vaxName, spltType, vaxAdminBy) "\
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor = mysql_conn.cursor()
                    args = vaersID, vaxManu, vaxLot, state, vaxRoute, vaxSite, vaxName, spltType, vaxAdminBy
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully Inserted (", cursor.rowcount, ") row!")
                    cursor.close()
                    set_null(tbl_name, "vaxLot", vaersID) if vaxLot == "" else vaxLot
                    set_null(tbl_name, "spltType", vaersID) if spltType == "" else spltType
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return
        elif tbl_name == "dateRecords":
            while (True):
                try:
                    vaersID = vaers_id()
                    print("Received Date:")
                    receivedDate = date()
                    receivedDate = "0000-00-00" if receivedDate == "" else receivedDate
                    print("Vaccination Date")
                    vaccineDate = date()
                    vaccineDate = "0000-00-00" if vaccineDate == "" else vaccineDate
                    print("Onset Date")
                    onsetDate = date()
                    onsetDate = "0000-00-00" if onsetDate == "" else onsetDate
                    insert_query = "INSERT INTO dateRecords(vaersID, receivedDate, vaccineDate, onsetDate) values(%s,%s,%s,%s)"
                    cursor = mysql_conn.cursor()
                    args = vaersID, receivedDate, vaccineDate, onsetDate
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully Inserted (", cursor.rowcount, ") row!")
                    cursor.close()
                    set_null(tbl_name, "receivedDate", vaersID) if receivedDate == "0000-00-00" else receivedDate
                    set_null(tbl_name, "vaccineDate", vaersID) if vaccineDate == "0000-00-00" else vaccineDate
                    set_null(tbl_name, "onsetDate", vaersID) if onsetDate == "0000-00-00" else onsetDate
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return

        elif tbl_name == "patientOutcomes":
            while (True):
                try:
                    vaersID = vaers_id()
                    print("Enter the threat if any(Y/N)")
                    lThreat = single_val()
                    print("Enter the Emergency visit if any(Y/N)")
                    erVisit = single_val()
                    print("Enter if hospitalized any(Y/N)")
                    hospital = single_val()
                    if (hospital.upper()=="Y"):
                        print("Enter the hospitalized days if hospitalized")
                        hospDays = num_days()
                        hospDays = "0" if hospDays == "" else hospDays
                    else:
                        hospDays = "0"
                    print("Enter prolonged hospitalization if any(Y/N)")
                    xStay = single_val()
                    print("Enter if the vaccine recipient was disabled(Y/N)")
                    disabled = single_val()
                    labData = input("Enter the labData if any: ")
                    print("Enter the office visit if any(Y/N)")
                    officeVisit = single_val()
                    print("Enter if any emergency/urgent visit(Y/N)")
                    eredVisit = single_val()
                    vaxDoseSeries = v_series()
                    symptomText = input("Enter the symptomText if any: ")
                    print("Enter Onset Interval")
                    numDays = num_days()
                    numDays = "0" if numDays == "" else numDays
                    formVersion = f_version()
                    formVersion = "0.00" if formVersion == "" else formVersion
                    allergies = input("Enter the allergies if any: ")
                    insert_query = "INSERT INTO patientOutcomes(vaersID, lThreat, erVisit, hospital, hospDays, xStay, "\
                            "disabled, labData, officeVisit, eredVisit, vaxDoseSeries, symptomText, numDays, formVersion, allergies) "\
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor = mysql_conn.cursor()
                    args = vaersID, lThreat, erVisit, hospital, hospDays, xStay, disabled, labData, officeVisit, eredVisit, vaxDoseSeries, symptomText, numDays, formVersion, allergies
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully Inserted (", cursor.rowcount, ") row!")
                    cursor.close()
                    set_null(tbl_name, "lThreat", vaersID) if lThreat == "" else lThreat
                    set_null(tbl_name, "erVisit", vaersID) if erVisit == "" else erVisit
                    set_null(tbl_name, "hospital", vaersID) if hospital == "0" else hospital
                    set_null(tbl_name, "hospDays", vaersID) if hospDays == "" else hospDays
                    set_null(tbl_name, "xStay", vaersID) if xStay == "" else xStay
                    set_null(tbl_name, "disabled", vaersID) if disabled == "" else disabled
                    set_null(tbl_name, "labData", vaersID) if labData == "" else labData
                    set_null(tbl_name, "officeVisit", vaersID) if officeVisit == "" else officeVisit
                    set_null(tbl_name, "eredVisit", vaersID) if eredVisit == "" else eredVisit
                    set_null(tbl_name, "symptomText", vaersID) if symptomText == "" else symptomText
                    set_null(tbl_name, "numDays", vaersID) if numDays == "0" else numDays
                    set_null(tbl_name, "formVersion", vaersID) if formVersion == "0.00" else formVersion
                    set_null(tbl_name, "allergies", vaersID) if allergies == "" else allergies
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return

        elif tbl_name == "patientResults":
            while(True):
                try:
                    vaersID = vaers_id()
                    print("Enter the recovered status(Y/N)")
                    recovered = single_val()
                    print("Enter the patient died or not(Y/N)")
                    died = single_val()
                    print("Enter the died date:")
                    if (died.upper()=="Y"):
                        dateOfDeath = date()
                        dateOfDeath = "0000-00-00" if dateOfDeath == "" else dateOfDeath
                    else:
                        dateOfDeath = "0000-00-00"
                    insert_query = "INSERT INTO patientResults(vaersID, recovered, died, dateOfDeath) values(%s,%s,%s,%s)"
                    cursor = mysql_conn.cursor()
                    args = vaersID, recovered, died, dateOfDeath
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully Inserted (", cursor.rowcount, ") row!")
                    cursor.close()
                    set_null(tbl_name, "recovered", vaersID) if recovered == "" else recovered
                    set_null(tbl_name, "died", vaersID) if died == "" else died
                    set_null(tbl_name, "dateOfDeath", vaersID) if dateOfDeath == "0000-00-00" else dateOfDeath
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return

        elif tbl_name == "preExistingConditions":
            while(True):
                try:
                    vaersID = vaers_id()
                    otherMeds = input("Enter other medications of the patient if any: ")
                    currentIllness = input("Enter current illness of the patient if any: ")
                    historyMeds = input("Enter medical history of the patient if any: ")
                    print("Enter if the patient has birth defect or not(Y/N)")
                    birthDefect = single_val()
                    priorVaccine = input("Enter the details of prior vaccination: ")
                    insert_query = "INSERT INTO preExistingConditions(vaersID, otherMeds, currentIllness, "\
                            "historyMeds, birthDefect, priorVaccine) values(%s,%s,%s,%s,%s,%s)"
                    cursor = mysql_conn.cursor()
                    args = vaersID, otherMeds, currentIllness, historyMeds, birthDefect, priorVaccine
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully Inserted (", cursor.rowcount, ") row!")
                    cursor.close()
                    set_null(tbl_name, "otherMeds", vaersID) if otherMeds == "" else otherMeds
                    set_null(tbl_name, "currentIllness", vaersID) if currentIllness == "" else currentIllness
                    set_null(tbl_name, "historyMeds", vaersID) if historyMeds == "" else historyMeds
                    set_null(tbl_name, "birthDefect", vaersID) if birthDefect == "" else birthDefect
                    set_null(tbl_name, "priorVaccine", vaersID) if priorVaccine == "" else priorVaccine
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return

        elif tbl_name == "symptomDetails":
            while(True):
                try:
                    vaersID = vaers_id()
                    symptom1 = symptom()
                    symptomVersion1 = sym_version()
                    symptomVersion1 = "0.0" if symptomVersion1 == "" else symptomVersion1
                    symptom2 = input("Enter symptom2: ")
                    symptomVersion2 = sym_version()
                    symptomVersion2 = "0.0" if symptomVersion2 == "" else symptomVersion2
                    symptom3 = input("Enter symptom3: ")
                    symptomVersion3 = sym_version()
                    symptomVersion3 = "0.0" if symptomVersion3 == "" else symptomVersion3
                    symptom4 = input("Enter symptom4: ")
                    symptomVersion4 = sym_version()
                    symptomVersion4 = "0.0" if symptomVersion4 == "" else symptomVersion4
                    symptom5 = input("Enter symptom5: ")
                    symptomVersion5 = sym_version()
                    symptomVersion5 = "0.0" if symptomVersion5 == "" else symptomVersion5
                    insert_query = "INSERT INTO symptomDetails(vaersID, symptom1, symptomVersion1, symptom2, symptomVersion2, "\
                            "symptom3, symptomVersion3, symptom4, symptomVersion4, symptom5, symptomVersion5) "\
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor = mysql_conn.cursor()
                    args = vaersID, symptom1, symptomVersion1, symptom2, symptomVersion2, symptom3, symptomVersion3, symptom4, symptomVersion4, symptom5, symptomVersion5
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully Inserted (", cursor.rowcount, ") row")
                    cursor.close()
                    set_null(tbl_name, "symptomVersion1", vaersID) if symptomVersion1 == "0.0" else symptomVersion1
                    set_null(tbl_name, "symptom2", vaersID) if symptom2 == "" else symptom2
                    set_null(tbl_name, "symptomVersion2", vaersID) if symptomVersion2 == "0.0" else symptomVersion2
                    set_null(tbl_name, "symptom3", vaersID) if symptom3 == "" else symptom3
                    set_null(tbl_name, "symptomVersion3", vaersID) if symptomVersion3 == "0.0" else symptomVersion3
                    set_null(tbl_name, "symptom4", vaersID) if symptom4 == "" else symptom4
                    set_null(tbl_name, "symptomVersion4", vaersID) if symptomVersion4 == "0.0" else symptomVersion4
                    set_null(tbl_name, "symptom5", vaersID) if symptom5 == "" else symptom5
                    set_null(tbl_name, "symptomVersion5", vaersID) if symptomVersion5 == "0.0" else symptomVersion5
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return
        else:
            print("Error:Incorrect table name")
            return
def view():
    try:
        vaersID = vaers_id()
        tbl_name = input("Enter table name: ")
        sql = "SELECT * from tbl where vaersID=v_id"
        sql = sql.replace("tbl", tbl_name)
        sql = sql.replace("v_id", vaersID)
        cursor = mysql_conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        if (tbl_name == "patientDetails"):
            x = PrettyTable()
            x.field_names = ["vaersID", "ageInYears", "cageInMonth", "sex"]
            x.add_row(result)
            print(x)
            cursor.close()
        elif (tbl_name == "vaccineDetails"):
            x = PrettyTable()
            x.field_names = ["vaersID", "vaxManu", "vaxLot", "state", "vaxRoute", "vaxSite", "vaxName", "spltType", "vaxFundBY"]
            x.add_row(result)
            print(x)
            cursor.close()
        elif (tbl_name == "dateRecords"):
            x = PrettyTable()
            x.field_names = ["vaersID", "receivedDate", "vaccineDate", "onsetDate"]
            x.add_row(result)
            print(x)
            cursor.close()
        elif (tbl_name == "symptomDetails"):
            x = PrettyTable()
            x.field_names = ["vaersID", "symptom1", "symptomVersion1", "symptom2", "symptomVersion2",
                             "symptom3", "symptomVersion3", "symptom4", "symptomVersion4", "symptom5", "symptomVersion5"]
            x.add_row(result)
            print(x)
            cursor.close()
        elif (tbl_name == "patientOutcomes"):
            x = PrettyTable()
            x.field_names = ["vaersID", "lThreat", "erVisist", "hospital", "hospDays", "xStay",
                             "disabled", "labData", "officeVisit", "eredVisit", "vaxDoseSeries", "symptomText", "numDays", "formVersion", "allergies"]
            x.add_row(result)
            print(x)
            cursor.close()
        elif (tbl_name == "patientResults"):
            x = PrettyTable()
            x.field_names = ["vaersID", "recovered", "died", "dateOfDeath"]
            x.add_row(result)
            print(x)
            cursor.close()
        elif (tbl_name == "preExistingConditions"):
            x = PrettyTable()
            x.field_names = ["vaersID", "otherMeds", "currentIllness", "historyMeds", "birthDefect", "priorVaccine"]
            x.add_row(result)
            print(x)
            cursor.close()
        else:
            print("Error:Invalid Table name")
    except mysql.connector.Error as e:
        print("======================================")
        print("Something went wrong: {}".format(e))
        print("======================================")
        return
    except TypeError:
        print("=============================================")
        print("Error:vaersID doesn't exist in the database")
        print("=============================================")
        return



def modify():
    '''
    This function update/modify a record in a table based on the table name & vaersID(of the patient) given by user
    :return: Row updated successfully or not
    '''
    while(True):
        print("Please select the details to be updated:\n "
              "(1) Update patient's age\n "
              "(2) Update Vaccine Info\n "
              "(3) Update the Symptom Details\n "
              "(4) Update patient's results\n "
              "(5) Update Vaccine dose series\n ")
        val = input("Enter the input: ")
        if(val == "1"):
            while (True):
                try:
                    print("Enter the vaersID of the patient that you need to update")
                    vaersID = vaers_id()
                    ageInYears = age()
                    insert_query = "UPDATE patientDetails SET ageInYears = %s where vaersID=%s"
                    cursor = mysql_conn.cursor()
                    args = ageInYears, vaersID
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully updated (", cursor.rowcount, ") row!")
                    cursor.close()
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return
        elif(val == "2"):
            while (True):
                try:
                    print("Enter the vaersID of the patient that you need to update")
                    vaersID = vaers_id()
                    vaxRoute = route()
                    vaxName = vaccine_manufacturer()
                    vaxAdminBy = v_admin()
                    insert_query = "UPDATE vaccineDetails SET vaxRoute = %s, vaxName = %s, vaxAdminBy = %s where vaersID=%s"
                    cursor = mysql_conn.cursor()
                    args = vaxRoute, vaxName, vaxAdminBy, vaersID
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully updated (", cursor.rowcount, ") row!")
                    cursor.close()
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return

        elif(val == "3"):
            while (True):
                try:
                    print("Enter the vaersID of the patient that you need to update")
                    vaersID = vaers_id()
                    symptom2 = input("Enter symptom2: ")
                    symptom3 = input("Enter symptom3: ")
                    symptom4 = input("Enter symptom4: ")
                    symptom5 = input("Enter symptom5: ")
                    insert_query = "UPDATE symptomDetails SET symptom2 = %s, symptom3 = %s, "\
                            "symptom4 = %s, symptom5 = %s where vaersID=%s"
                    cursor = mysql_conn.cursor()
                    args = symptom2, symptom3, symptom4, symptom5, vaersID
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully updated (", cursor.rowcount, ") row!")
                    cursor.close()
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return
        elif(val == "4"):
            while (True):
                try:
                    print("Enter the vaersID of the patient that you need to update")
                    vaersID = vaers_id()
                    print("Enter the recovered status(Y/N)")
                    recovered = single_val()
                    print("Enter the patient died or not(Y/N)")
                    died = single_val()
                    insert_query = "UPDATE patientResults SET recovered = %s, died = %s where vaersID=%s"
                    cursor = mysql_conn.cursor()
                    args = recovered, died, vaersID
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully updated (", cursor.rowcount, ") row!")
                    cursor.close()
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return

        elif(val == "5"):
            while (True):
                try:
                    print("Enter the vaersID of the patient that you need to update")
                    vaersID = vaers_id()
                    vaxDoseSeries = v_series()
                    insert_query = "UPDATE patientOutcomes SET vaxDoseSeries = %s where vaersID=%s"
                    cursor = mysql_conn.cursor()
                    args = vaxDoseSeries, vaersID
                    cursor.execute(insert_query, args)
                    mysql_conn.commit()
                    print("Successfully updated (", cursor.rowcount, ") row!")
                    cursor.close()
                    return
                except mysql.connector.Error as e:
                    print("Something went wrong: {}".format(e))
                    return
        else:
            print("Error:Invalid Operation")

def delete():
    while(True):
        try:
            vaersID = vaers_id()
            del_query = "DELETE FROM preExistingConditions where vaersID=v_id"
            del_query = del_query.replace("v_id", vaersID)
            cursor = mysql_conn.cursor()
            cursor.execute(del_query)
            mysql_conn.commit()
            cursor.close()
            del_query = "DELETE FROM patientResults where vaersID=v_id"
            del_query = del_query.replace("v_id", vaersID)
            cursor = mysql_conn.cursor()
            cursor.execute(del_query)
            mysql_conn.commit()
            cursor.close()
            del_query = "DELETE FROM patientOutcomes where vaersID=v_id"
            del_query = del_query.replace("v_id", vaersID)
            cursor = mysql_conn.cursor()
            cursor.execute(del_query)
            mysql_conn.commit()
            cursor.close()
            del_query = "DELETE FROM symptomDetails where vaersID=v_id"
            del_query = del_query.replace("v_id", vaersID)
            cursor = mysql_conn.cursor()
            cursor.execute(del_query)
            mysql_conn.commit()
            cursor.close()
            del_query = "DELETE FROM vaccineDetails where vaersID=v_id"
            del_query = del_query.replace("v_id", vaersID)
            cursor = mysql_conn.cursor()
            cursor.execute(del_query)
            mysql_conn.commit()
            cursor.close()
            del_query = "DELETE FROM dateRecords where vaersID=v_id"
            del_query = del_query.replace("v_id", vaersID)
            cursor = mysql_conn.cursor()
            cursor.execute(del_query)
            mysql_conn.commit()
            cursor.close()
            del_query = "DELETE FROM patientDetails where vaersID=v_id"
            del_query = del_query.replace("v_id", vaersID)
            cursor = mysql_conn.cursor()
            cursor.execute(del_query)
            mysql_conn.commit()
            print("Successfully deleted (", cursor.rowcount, ") row!")
            cursor.close()
            return
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            return

def vaccine_cause_death():
    '''
    Display the table info with vaersID, Patient's age, date of death, Vaccine Info of the died patients
     to identify the type of vaccine that caused death
    '''
    effects_query = "SELECT patientDetails.vaersID, patientDetails.ageInYears, patientResults.dateOfDeath, vaccineDetails.vaxManu FROM patientDetails "\
            "INNER JOIN patientResults ON patientDetails.vaersID = patientResults.vaersID INNER JOIN "\
            "vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID WHERE patientResults.died = 'Y'"
    cursor = mysql_conn.cursor()
    cursor.execute(effects_query)
    results = cursor.fetchall()
    x = PrettyTable()
    x.field_names = ["vaersID", "ageInYears", "dateOfDeath", "vaxManu"]
    x.add_rows(results)
    print(x)
    cursor.close()

def death_count():
    '''
    This function calculates and displays the count of the patients died
    '''
    count_query = "SELECT count(*) FROM patientDetails "\
            "INNER JOIN patientResults ON patientDetails.vaersID = patientResults.vaersID "\
            "INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID WHERE patientResults.died = 'Y'"
    cursor = mysql_conn.cursor()
    cursor.execute(count_query)
    results = cursor.fetchone()
    print("=======================================")
    print("Count of died patients: ", results[0])
    print("=======================================")
    cursor.close()

def vaccine_type():
    '''
    This Function calculates and returns the count of patient's died based on the chosen vaccine(PFIZERBIONTECH/MODERNA)
    '''
    print("Enter the type of vaccine that caused death\n1.PFIZERBIONTECH\n2.MODERNA")
    vaccine_name = input()
    if vaccine_name == "1":
        vacc_query = "SELECT count(*) from patientDetails "\
                "INNER JOIN patientResults ON patientDetails.vaersID = patientResults.vaersID "\
                "INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID "\
                "WHERE patientResults.died = 'Y' AND vaccineDetails.vaxManu = 'PFIZERBIONTECH'"
        cursor = mysql_conn.cursor()
        cursor.execute(vacc_query)
        results = cursor.fetchone()
        print("===========================================================")
        print("Count of died patients due to PFIZERBIONTECH: ", results[0])
        print("===========================================================")
        cursor.close()
    elif vaccine_name == "2":
        vacc_query = "SELECT count(*) FROM patientDetails "\
                "INNER JOIN patientResults ON patientDetails.vaersID = patientResults.vaersID "\
                "INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID "\
                "WHERE patientResults.died = 'Y' AND vaccineDetails.vaxManu = 'MODERNA'"
        cursor = mysql_conn.cursor()
        cursor.execute(vacc_query)
        results = cursor.fetchone()
        print("===========================================================")
        print("Count of died patients due to MODERNA: ", results[0])
        print("===========================================================")
        cursor.close()
    else:
        print("Error:Invalid vaccine type")

def adverse_effects():
    '''
    This Function shows the effects caused due to vaccination
    '''
    query = "SELECT patientDetails.vaersID, patientDetails.ageInYears, vaccineDetails.vaxManu, "\
            "symptomDetails.symptom1, symptomDetails.symptom2, symptomDetails.symptom3, symptomDetails.symptom4, "\
            "symptomDetails.symptom5 FROM patientDetails "\
            "INNER JOIN vaccineDetails ON vaccineDetails.vaersID = patientDetails.vaersID "\
            "INNER JOIN symptomDetails ON patientDetails.vaersID = symptomDetails.vaersID limit 10"
    cursor = mysql_conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    x = PrettyTable()
    x.field_names = ["vaersID", "ageInYears", "vaxManu", "symptom1", "symptom2", "symptom3", "symptom4", "symptom5"]
    x.add_rows(results)
    print(x)
    cursor.close()
