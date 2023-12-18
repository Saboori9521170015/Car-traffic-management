from Pages.Get_item import *

#Create table

def Create_table_owners():
    print("Starting...")
    print("Creating owners table... please wait!")
    conn = connection_to_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS owners")
    sql ='''CREATE TABLE owners(
        national_code BIGINT PRIMARY KEY,
        name NAME NOT NULL,
        age INT,
        total_toll_paid INT
    )'''
    cursor.execute(sql)
    conn.commit()
    print("Table created successfully!")
    conn.close()
#************************************************************************************************************
def Create_table_owners_car():
    print("Creating owners_car table... please wait!")
    conn = connection_to_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS owners_car")
    sql ='''CREATE TABLE owners_car(
        national_code BIGINT NOT NULL,
        id INT PRIMARY KEY,
        type Name NOT NULL,
        color Name,
        length CHAR(5),
        load_valume CHAR(5)
    )'''
    cursor.execute(sql)
    conn.commit()
    print("Table created successfully........")
    conn.close()

#************************************************************************************************************
def Create_table_tollStation():
    print("Creating tollStation table... please wait!")
    conn = connection_to_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS tollStation")
    sql ='''CREATE TABLE tollStation(
        name Name PRIMARY KEY,
        toll_per_cross INT NOT NULL,
        location_lat CHAR(30) NOT NULL,
        location_long CHAR(30) NOT NULL
    )'''
    cursor.execute(sql)
    conn.commit()
    print("Table created successfully........")
    conn.close()

#************************************************************************************************************
def Create_table_all_node():
    print("Creating all_node table... please wait!")
    conn = connection_to_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS all_node")
    sql ='''CREATE TABLE all_node(
        car INT NOT NULL,
        location_lat CHAR(30) NOT NULL,
        location_long CHAR(30) NOT NULL,
        point Name NOT NULL,
        date date,
        time time  
    )'''
    cursor.execute(sql)
    conn.commit()
    print("Table created successfully........")
    conn.close()

#************************************************************************************************************
def Create_table_roads():
    print("Creating roads table... please wait!")
    conn = connection_to_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS roads")
    sql ='''CREATE TABLE roads(
        name Name NOT NULL,
        width double precision,
        point Name NOT NULL
    )'''
    cursor.execute(sql)
    conn.commit()
    print("Table created successfully........")
    conn.close()

#************************************************************************************************************

#insert to table

def insert_owners():
    name=Get_list_of_name_owner()
    national_code=Get_list_of_national_code()
    age=Get_list_of_age()
    total_toll_paid=Get_list_of_total_toll_paid()
    conn = connection_to_db()
    conn.autocommit = True
    cursor = conn.cursor()
    for N1,N2 in enumerate(national_code):
        val=[(str(N2), str(name[N1]), str(age[N1]), str(total_toll_paid[N1]))]
        sql="INSERT INTO owners(national_code, name, age,total_toll_paid) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, val)
    conn.commit()
    print("Records owners inserted........")
    conn.close()
#************************************************************************************************************

def insert_owners_car():
    national_code=Get_list_of_national_code()
    ownerCar = Get_list_of_ownerCar()
    conn = connection_to_db()
    conn.autocommit = True
    cursor = conn.cursor()
    for N1, N2 in enumerate(national_code):
        for i in ownerCar[N1]:
            val = [(str(N2), str(i["id"]), str(i["type"]), str(i["color"]), str(i["length"]), str(i["load_valume"]))]
            sql = '''INSERT INTO owners_car(national_code, id, type, color , length, load_valume) VALUES (%s, %s, %s, %s, %s, %s)'''
            cursor.executemany(sql, val)
    conn.commit()
    print("Records owners_car inserted........")
    conn.close()

#************************************************************************************************************

def insert_tollStation():
    tollStations = Get_File_tollStations()
    conn = connection_to_db()
    conn.autocommit = True
    cursor = conn.cursor()
    for i in tollStations:
        point = i["location"][16:]
        point = point.replace("(", "")
        point = point.replace(")", "")
        point = point.split(" ")
        val = [(str(i["name"]), str(i["toll_per_cross"]), str(point[1]), str(point[0]))]
        sql = '''INSERT INTO tollStation(name, toll_per_cross, location_lat, location_long) VALUES (%s, %s, %s, %s)'''
        cursor.executemany(sql, val)
    conn.commit()
    print("Records tollStation inserted........")
    conn.close()

#************************************************************************************************************

def insert_all_node():
    all_nodes = Get_File_all_nodes()
    conn = connection_to_db()
    conn.autocommit = True
    cursor = conn.cursor()
    for i in all_nodes:
        point = i["location"][16:]
        point = point.replace("(", "")
        point1 = point.replace(")", "")
        point = point1.split(" ")
        Date = i["date"]
        Date = Date.split("T")
        val = [(str(i["car"]), str(point[1]), str(point[0]),str(point1),str(Date[0]),str(Date[1][:8]))]
        sql = '''INSERT INTO all_node(car, location_lat, location_long, point, date, time) VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.executemany(sql, val)
    conn.commit()
    print("Records all_node inserted........")
    conn.close()

#************************************************************************************************************

def insert_roads():
    roads = Get_File_roads()
    conn = connection_to_db()
    conn.autocommit = True
    cursor = conn.cursor()
    for i in roads:
        MULTILINESTRING = i["geom"][28:]
        MULTILINESTRING = MULTILINESTRING.replace("))", "")
        MULTILINESTRING = MULTILINESTRING.split(",")
        for j in MULTILINESTRING:
            j = j.lstrip(" ")
            val = [(str(i["name"]), str(i["width"]), str(j))]
            sql = '''INSERT INTO roads(name, width, point) VALUES (%s, %s, %s)'''
            cursor.executemany(sql, val)
    conn.commit()
    print("Records roads inserted........")
    conn.close()
    print("All Done! End")
