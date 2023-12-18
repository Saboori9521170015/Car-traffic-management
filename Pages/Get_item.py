from shapely.geometry import LineString
from operator import itemgetter
import psycopg2
import json

def connection_to_db():
    File = open("./Setup_db_connection.json", "r")
    db = json.load(File)
    conn = psycopg2.connect(
        database=db["database"], user=db["user"], password=db["password"], host=db["host"], port=db["port"]
    )
    return conn

def Get_query(query):
    conn = connection_to_db()
    cursor = conn.cursor()
    cursor.execute(query)
    result_query = cursor.fetchall()
    conn.close()
    return result_query

def Get_File_tollStations():
    TollStations_file=open("Pages/Files/tollStations.json", "r")
    List_of_Toll_Station=json.load(TollStations_file)
    return List_of_Toll_Station
def Get_File_all_nodes():
    All_nodes_file=open("Pages/Files/all_nodes.json", "r")
    List_of_All_nodes=json.load(All_nodes_file)
    return List_of_All_nodes
def Get_File_owners():
    owners_file=open("Pages/Files/owners.json", "r")
    List_of_owners=json.load(owners_file)
    return List_of_owners

def Get_File_roads():
    roads_file=open("Pages/Files/roads.json", "r",encoding="utf8")
    List_of_roads=json.load(roads_file)
    return List_of_roads

def Get_File_tollStations_Request_6():
    TollStations_file=open("Pages/Files/tollStations.json", "r",encoding="utf8")
    List_of_Toll_Station=json.load(TollStations_file)
    return List_of_Toll_Station

def Get_list_of_name_owner():
    return list(map(itemgetter('name'), Get_File_owners()))

def Get_list_of_national_code():
    return list(map(itemgetter('national_code'), Get_File_owners()))

def Get_list_of_age():
    return list(map(itemgetter('age'), Get_File_owners()))
def Get_list_of_total_toll_paid():
    return list(map(itemgetter('total_toll_paid'), Get_File_owners()))

def Get_list_of_All_node_location():
    return list(map(itemgetter('location'), Get_File_all_nodes()))
def Get_list_of_ownerCar():
    return list(map(itemgetter('ownerCar'), Get_File_owners()))

def Get_list_of_CarID_in_all_node():
    return list(map(itemgetter('car'), Get_File_all_nodes()))
def Get_list_of_datetime_in_all_node():
    return list(map(itemgetter('date'), Get_File_all_nodes()))

def Get_list_of_location_in_all_node():
    return list(map(itemgetter('location'), Get_File_all_nodes()))

def Get_list_of_location_Stations_in_tollStations():
    return list(map(itemgetter('location'), Get_File_tollStations()))
def Get_list_of_toll_per_cross_Stations_in_tollStations():
    return list(map(itemgetter('toll_per_cross'), Get_File_tollStations()))

def Get_list_of_name_roads():
    return list(map(itemgetter('name'), Get_File_roads()))

def Get_list_of_width_roads():
    return list(map(itemgetter('width'), Get_File_roads()))

def Get_list_of_geom_roads():
    return list(map(itemgetter('geom'), Get_File_roads()))
def Get_list_owener_ID_Car():
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_Car_ID = []
    i=0
    while i<len(list_of_ownerCar):
        for d1,d2 in enumerate(list_of_ownerCar[i]):
            list_of_Car_ID.append(d2.get('id',None))
        i+=1
    return list_of_Car_ID

def Get_list_owener_ID_Car_by_nation_code(index_nation_code):
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_Car_ID=[]
    for d1,d2 in enumerate(list_of_ownerCar[index_nation_code]):
        list_of_Car_ID.append(d2.get('id',None))
    return list_of_Car_ID


def Get_list_owener_total_toll_paid_by_nation_code(index_nation_code):
    list_of_ownerCar=Get_File_owners()
    list_of_total_toll_paid=0
    if list_of_ownerCar[index_nation_code].get('total_toll_paid', None) == None:
            list_of_total_toll_paid=(0.0)
    else:
        list_of_total_toll_paid=list_of_ownerCar[index_nation_code].get('total_toll_paid', None)

    return list_of_total_toll_paid


def Get_list_owener_load_valume_Car_by_nation_code(index_nation_code):
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_load_valume=[]
    for d1,d2 in enumerate(list_of_ownerCar[index_nation_code]):
        if d2.get('load_valume', None) == None:
            list_of_load_valume.append(0.0)
        else:
            list_of_load_valume.append(d2.get('load_valume', None))
    return list_of_load_valume

def swap_long_to_lat(location):
    location = location.replace(",", '')
    location=location.replace(" ",'S')
    location=location.split("S")
    y=location[0]
    x=location[1]
    xy=x+","+y
    return xy

def Get_list_owener_type_Car():
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_Car_type = []
    i=0
    while i<len(list_of_ownerCar):
        for d1,d2 in enumerate(list_of_ownerCar[i]):
            list_of_Car_type.append(d2.get('type',None))
        i+=1
    return list_of_Car_type

def Get_list_owener_color_Car():
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_Car_color = []
    i=0
    while i<len(list_of_ownerCar):
        for d1,d2 in enumerate(list_of_ownerCar[i]):
            list_of_Car_color.append(d2.get('color',None))
        i+=1
    return list_of_Car_color

def Get_list_owener_load_valume_Car():
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_Car_load_valume = []
    i=0
    while i<len(list_of_ownerCar):
        for d1,d2 in enumerate(list_of_ownerCar[i]):
            list_of_Car_load_valume.append(d2.get('load_valume',None))
        i+=1
    return list_of_Car_load_valume

def Get_list_of_ID_big_car():
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_IDbig_car=[]
    for d1,d2 in enumerate(list_of_ownerCar):
        if d2.get("type",None) == 'big':
            list_of_IDbig_car.append(d2.get("id",None))
    return list_of_IDbig_car



def Get_list_of_ID_big_car():
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_IDbig_car = []
    i=0
    while i<len(list_of_ownerCar):
        for d1,d2 in enumerate(list_of_ownerCar[i]):
            if d2.get('type',None) == 'big':
                list_of_IDbig_car.append(d2.get('id',None))
        i+=1
    return list_of_IDbig_car

def Get_list_of_ID_small_car():
    list_of_ownerCar=Get_list_of_ownerCar()
    list_of_IDbig_car = []
    i=0
    while i<len(list_of_ownerCar):
        for d1,d2 in enumerate(list_of_ownerCar[i]):
            if d2.get('type',None) == 'small':
                list_of_IDbig_car.append(d2.get('id',None))
        i+=1
    return list_of_IDbig_car


def Get_Close_distance(geom, point):
    def closest_dis(lines, point):
        distance_list = [line.distance(point) for line in line_string_list]
        shortest_distance = min(distance_list)
        return shortest_distance

    String_of_geom_roads = geom[28:-1]
    String_of_geom_roads = String_of_geom_roads.replace(")", "")
    String_of_geom_roads = String_of_geom_roads.replace(", ", ",")
    String_of_geom_roads = String_of_geom_roads.replace(" ", ",")
    list_of_xy_multistring = String_of_geom_roads.split(",")
    list_of_geom_x = list_of_xy_multistring[::2]
    list_of_geom_y = list_of_xy_multistring[1::2]
    ###########################################################
    list_line = []
    i = 0
    while i < len(list_of_geom_x) - 1:
        line_string_list = [
            LineString([(list_of_geom_y[i], list_of_geom_x[i]), (list_of_geom_y[i + 1], list_of_geom_x[i + 1])])]
        list_line.append(line_string_list)
        i += 1
    return closest_dis(list_line, point)