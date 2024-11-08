
from decimal import Decimal
import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name,user_name,user_password):
    connection=None
    try:
        connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_password)
        print("MYSQL Database connection successful")

    except Error as err:
        print(f"Error: '{err}'")
    return connection 

pw="1102"


def create_db_connection(host_name,user_name,user_password,db_name):
    connectioin=None
    try:
        connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_password,database=db_name)
        print("MySql database connection successfull ")

    except Error as err:
        print(f"Error:'{err}'")
    return connection

connection=create_db_connection("localhost","root",pw,"megamart")

def read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        connection.commit()
        result=cursor.fetchall()
        return result
    except Error as err:
        print(f"Error:'{err}'")

def read_query1(connection,query):
    cursor=connection.cursor()
    
    cursor.execute(query)
    # connection.commit()
    result=cursor.fetchall()
    
    for row in result:
        print(row)
        print("\n")
   
def read_query2(connection,query):
    cursor=connection.cursor()
    
    cursor.execute(query)
    result=cursor.fetchall()
    return result

def read_query3(connection,query):
    cursor=connection.cursor()
    
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result


def result_query(connection,query):
    z=read_query(connection,query)
    output = []
    for row in z:
        row_data = []
        for data in row:
            # if type(data) is Decimal:
                # row_data.append(float(data))
            # if:
                row_data.append(str(data))
        output.append(row_data)       
    for q in output:        
        print(q)
        print()

def read_query4(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        for _ in cursor.execute(query, multi=True): pass
        connection.commit()
        result=cursor.fetchall()
        return result
    except Error as err:
        print("")
        
connection=create_db_connection("localhost","root","1102","megamart")
q21="""SELECT Cart_Quantity FROM product WHERE product_id = 201;"""
present_qty=read_query3(connection,q21)
print(present_qty)