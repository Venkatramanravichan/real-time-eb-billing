import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="final",
    auth_plugin='mysql_native_password'
)
n = int(input("1.newcustomer 2.existingcustomer 3.viewdetails"))
if (n == 1):

    name = input("enter your name")
    mobilenumber = int(input("enter mobile number"))
    address = input("enter your address")
    ebnumber = int(input("enter eb number"))
    month = input("entrer billed month and year")
    meterreading=int(input("enter your meter reading"))
    amount = 0
    mycursor = mydb.cursor()
    sql = "insert into last(name,mobilenumber,address,ebnumber,month,meterreading,amount)values(%s,%s,%s,%s,%s,%s,%s)"
    val = (name, mobilenumber, address, ebnumber, month,meterreading,amount)
    mycursor.execute(sql, val)
    mydb.commit()
    previousreading=0
    mycursor=mydb.cursor()
    sql = "insert into elast(ebnumber,month,meterreading,previousreading,unitsused,amount)values(%s,%s,%s,%s,%s,%s)"
    val = ( ebnumber, month, previousreading,meterreading,meterreading, amount)
    mycursor.execute(sql, val)
    mydb.commit()


    mycursor = mydb.cursor()
    sql = "select meterreading from last where ebnumber='{}'".format(ebnumber)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    for x in myresult:
        mreading = x

        unitsrunned = mreading
        if (unitsrunned >= 300):
            newunit = unitsrunned - 100
            ebamount = newunit * 20

        elif (unitsrunned <= 100):
            ebamount = 0
        elif (unitsrunned >= 101) and (unitsrunned <= 199):
            newunit = unitsrunned - 100
            ebamount = newunit * 5
        elif (unitsrunned >= 200) and (unitsrunned <= 299):
            newunit = unitsrunned - 100
            newunit2 = newunit - 100
            newunit3 = newunit - newunit2
            am1 = newunit2 * 15
            am2 = newunit3 * 5
            ebamount = am1 + am2
        mycursor = mydb.cursor()


        sql = "update last set amount='{}'where ebnumber='{}'".format(ebamount,ebnumber)
        mycursor.execute(sql)
        mydb.commit()
        sql = "select amount from last where ebnumber ='{}'".format(ebnumber)
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        for s in myresult:
            amount = s
        mycursor=mydb.cursor()
        sql = "update elast set amount='{}'where ebnumber='{}'".format(amount, ebnumber)
        mycursor.execute(sql)
        mydb.commit()


elif(n==2):

    ebnumber=int(input("enter your eb number"))
    billedmonth = input("enter billed date")
    thismonthreading = int(input("enter your this month reading"))




    mycursor = mydb.cursor()
    sql = "select meterreading from last where ebnumber='{}'".format(ebnumber)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    for j in myresult:
        mreading = j

    if(thismonthreading>mreading):
        s=thismonthreading-mreading
        unitsrunned=s


        if (unitsrunned >= 300):
            newunit = unitsrunned - 100
            ebamount = newunit * 20

        elif (unitsrunned <= 100):
            ebamount = 0
        elif (unitsrunned >= 101) and (unitsrunned <= 199):
            newunit = unitsrunned - 100
            ebamount = newunit * 5
        elif (unitsrunned >= 200) and (unitsrunned <= 299):
            newunit = unitsrunned - 100
            newunit2 = newunit - 100
            newunit3 = newunit - newunit2
            am1 = newunit2 * 15
            am2 = newunit3 * 5
            ebamount = am1 + am2
    else:
        exit()
    mycursor = mydb.cursor()
    sql = "update last set meterreading ='{}'where ebnumber='{}'".format(thismonthreading, ebnumber)
    mycursor.execute(sql)
    mydb.commit()






    mycursor=mydb.cursor()
    sql="insert into elast(ebnumber,month,meterreading,previousreading,unitsused,amount)values(%s,%s,%s,%s,%s,%s)"
    val=(ebnumber,billedmonth,mreading,thismonthreading,unitsrunned,ebamount)
    mycursor.execute(sql,val)
    mydb.commit()
elif(n==3):
    ebnumber=int(input("enter your ebnumber"))
    mycursor=mydb.cursor()
    sql="select * from elast where ebnumber='{}'".format(ebnumber)
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    print("ebnumber\tbilleddate\tpreviousmonthreading thismonthreading toatlreading amount")
    for z in myresult:
        print(z[0],"\t\t",z[1],"\t\t",z[2],"\t\t\t\t",z[3],"\t\t\t",z[4],"\t\t",z[5])

