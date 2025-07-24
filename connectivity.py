import mysql.connector
# connect to MySQL
conn = mysql.connector.connect(host="localhost",user="root",password="2004",database="connective")
method=conn.cursor()
# table creation
# method.execute("""create table contacts(id int auto_increment primary key,
# name varchar(200),
# mobile_num varchar(15));""")
# function to insert a record
def insert_values(name,mobile_num):
    v1= "insert into contacts(name,mobile_num)values(%s,%s)"
    v2=(name,mobile_num)
    method.execute(v1,v2)
    conn.commit()

# function to view records
def view_values ():
    method.execute("select * from contacts;")
    rows= method.fetchall()
    print("\n---ALL CONTACT---")
    for row in rows:
        print("ID:",row[0],"| name: ",row[1],"| mobile number ",row[2])
        print("-----------------")
# update the record
def update_record(contactID,new_name,new_mobile_num):
    v1="update contacts set name=%s,mobile_num=%s where id=%s"
    v2=(new_name,new_mobile_num,contactID)
    method.execute(v1,v2)
    conn.commit()
    print(f"Update ID to {contactID} to name :{new_name},mobile{new_mobile_num}")
# delete the record
def delete_values(contact_id):
    v1="delete from contacts where id=%s"
    v2=(contact_id)
    method.execute(v1,v2)
    conn.commit()
# insert_values("Adhi","8774577646")
update_record(1,"Dinesh","485124545")

# delete_values([6])
view_values()
method.close()
conn.close()