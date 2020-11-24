import pandas as pd
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=hkp;'
                      'Database=CONTACT_BOOK;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# cursor.execute('SELECT * FROM PEOPLE')
# for row in cursor:
#     print(row)
# sql_query = pd.read_sql_query('SELECT * FROM PEOPLE', conn)
# print(sql_query.iloc[0, 0])
# print(type(sql_query))


def menu():
    print("Hey You. Please choose : ")
    print("1. See all contacts")
    print("2. Find contacts")
    print("3. Add new contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6 or Above . Exit")


def See_all():
    sql_query = pd.read_sql_query('SELECT * FROM PEOPLE', conn)
    return sql_query


def Find_Contact(strF):
    strFind = "SELECT * FROM PEOPLE WHERE PEOPLE.name LIKE '%{f}%' OR PEOPLE.phone LIKE '%{f}%'".format(
        f=str(strF))
    sql_query = pd.read_sql_query(strFind, conn)
    return sql_query


def Check_Info(strName, strPhone, strAddress, strEmail):
    if strPhone == "":
        strAddress = "Unknown phone"
    if strName == "":
        strAddress = "Unknown name"
    if strAddress == "":
        strAddress = "Unknown address"
    if strEmail == "":
        strEmail = "Unknown email"


def Adding(strName, strPhone, strAddress, strEmail):
    Check_Info(strName, strPhone, strAddress, strEmail)
    check = Check_Duplicate(strName, strPhone)
    if check == 0:
        strAdd = "INSERT PEOPLE(name, address, phone, email) VALUES('{0}', '{1}', '{2}', '{3}')".format(
            strName, strAddress, strPhone, strEmail)
        cursor.execute(strAdd)
        conn.commit()
        return("Adding {} Complete".format(strName))
    else:
        return("Duplicate name or phone")


def Check_Duplicate(strName, strPhone):
    strCheckDup = "SELECT COUNT(*) FROM PEOPLE where PEOPLE.name='{0}' or PEOPLE.phone='{1}'".format(
        strName, strPhone)
    sql_query = pd.read_sql_query(strCheckDup, conn)
    return sql_query.iloc[0, 0]


def UpdateChosen():
    print("Please choose what to update...")
    print("0. Done")
    print("1. Name")
    print("2. Address")
    print("3. Phone")
    print("4. Email")
    result = eval(input())
    return result


def Update_Contact(iID):
    strShow = "SELECT * FROM PEOPLE WHERE PEOPLE.id={}".format(iID)
    print(pd.read_sql_query(strShow, conn))
    res = UpdateChosen()
    while(res != 0):
        if res == 1:
            print("Update Name")
            strName = input()
            strUpdate = "UPDATE PEOPLE SET PEOPLE.name = '{0}' WHERE id = {1}".format(
                strName, iID)
            cursor.execute(strUpdate)
            conn.commit()
        if res == 2:
            print("Update Address")
            strAddress = input()
            strUpdate = "UPDATE PEOPLE SET PEOPLE.address = '{0}' WHERE id = {1}".format(
                strAddress, iID)
            cursor.execute(strUpdate)
            conn.commit()
        if res == 3:
            print("Update Phone")
            strPhone = input()
            strUpdate = "UPDATE PEOPLE SET PEOPLE.phone = '{0}' WHERE id = {1}".format(
                strPhone, iID)
            cursor.execute(strUpdate)
            conn.commit()
        if res == 4:
            print("Update Email")
            strEmail = input()
            strUpdate = "UPDATE PEOPLE SET PEOPLE.email = '{0}' WHERE id = {1}".format(
                strEmail, iID)
            cursor.execute(strUpdate)
            conn.commit()
        strShow = "SELECT * FROM PEOPLE WHERE PEOPLE.id={}".format(iID)
        print(pd.read_sql_query(strShow, conn))
        res = UpdateChosen()


def Delete_Contact(iID):
    strDel = "DELETE FROM PEOPLE WHERE PEOPLE.id={0}".format(iID)
    cursor.execute(strDel)
    conn.commit()
    return "Delete Success"


def main():
    menu()
    choice = eval(input())
    while choice < 6 and choice > 0:
        if choice == 1:
            print("All Contacts")
            print(See_all())
        elif choice == 2:
            print("Find Contact")
            finding = str(input())
            print(Find_Contact(finding))
        elif choice == 3:
            print("Add New Contact")
            strName = str(input())
            strAddress = str(input())
            strPhone = str(input())
            strEmail = str(input())
            print(Adding(strName, strPhone, strAddress, strEmail))
        elif choice == 4:
            print("All Contacts")
            print(See_all())
            print("Update Contact")
            iID = eval(input())
            Update_Contact(iID)
        elif choice == 5:
            print("All Contacts")
            print(See_all())
            print("Delete Contact")
            iID = eval(input())
            print(Delete_Contact(iID))
        menu()
        choice = eval(input())
    print("Exit")


if __name__ == "__main__":
    main()
