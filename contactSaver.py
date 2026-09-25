# mysql-connector-python (package)
# pip (pip install packageName)

from mysql import connector

conn1=connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="augbatch2"
)
print("Connection successfull...!")

cursor=conn1.cursor()
# cursor.execute('''
# create table contacts(
# id int primary key,
# name varchar(30) not null,
# phone char(10) not null unique
# );
# ''')

# cursor.execute("SELECT * FROM contacts")
# res=cursor.fetchall()
# print(res)

# try:
#     cursor.execute("INSERT INTo contacts (id,name,phone) VALUES (%s,%s,%s)",(1,"Ken","6556455412"))
#     conn1.commit()
# except connector.errors.IntegrityError:
#     print("duplicate entry")
# except Exception:
#     print("Something went wrong...!")

# print("Data Created...!")



while True:
    inp=int(input("0 --> Exist\n1 --> View Contacts\n2 --> Add Contact\n3 --> Update a Contact\44 --> Delete a Contact\nChoose an option: "))

    if inp==0:
        break
    elif inp==1:
        try:
            cursor.execute("SELECT * from contacts")
            res=cursor.fetchall()
            for id,name,phone in res:
                print(f"Name: {name} Phone: {phone}")
        except Exception:
            print("Something went wrong...!")
    elif inp==2:
        pass
    elif inp==3:
        pass
    elif inp==4:
        pass
    else:
        print("Wrong Option")
    print()
    print()
    print()
    