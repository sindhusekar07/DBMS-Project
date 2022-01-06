from datetime import datetime
import mysql.connector

def mysql_con(host, port, user, passwd, database):
    global conn
    conn = mysql.connector.connect(host=host,
                                   port=port,
                                   user=user,
                                   password=passwd,
                                   database=database)
    if conn.is_connected() == True:
        return 1
    else:
        return 0

def mysql_query(query):
    conn = mysql.connector.connect(host="localhost",
                           port=3306,
                           user="doctor",
                           password="doctor123",
                           database="covidVaccine_656")

    cursor = conn.cursor()
    # get the number
    cursor.execute(query)
    version = cursor.fetchone()
    # commit and close everything
    conn.commit()
    cursor.close()
    conn.close()
    res = version[0]
    return res


def vaers_id(d):
    if ((d.isdigit()) and (len(d) == 6)):
        return 1

def age(age):
    if ((age.isdigit()) and (len(age) <= 2) and ((age > "0") and (age <= "99"))):
        return 1
def date(d):
    format = "%Y-%m-%d"
    res = True
    res = bool(datetime.strptime(d, format))
    if (res == True):
        return 1
def single_val(input_val):
    if ((input_val.upper() == "Y") or (input_val.upper() == "N") or (input_val=="")):
        return 1

def test_method():
    assert vaers_id("123456") == 1

def test_method1():
    assert age("34") == 1

def test_method2():
    assert date("2020-12-02") == 1
def test_method3():
    assert single_val("Y") == 1
    assert single_val("N") == 1
    #assert single_val("U") == 1

def test_query_method():
    query = "SELECT VERSION()"
    assert mysql_query(query) == "8.0.27"

def test_mysql_conn():
    assert mysql_con("localhost", 3306, "doctor", "doctor123", "covidVaccine_656") == 1