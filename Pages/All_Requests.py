import geopandas as gpd
from Pages.Get_item import *
from Pages.Check_Item import *
from shapely.geometry import Point
from geopy.distance import geodesic
from Pages.Check_between_date import *


#************************************************************************************************************
def Function_Request_1():
    result_query = Get_query('''SELECT id , color from owners_car where color in ('blue', 'red')''')
    result = []
    for value in result_query:
        result.append("ID for color " + str(value[1]) + " is : " + str(value[0]))
    print(result)
    return result

#************************************************************************************************************
def Add_Owner_and_Car(H_name,H_national_code,H_Age,H_total_toll_paid,H_id,H_type,H_color,H_length,H_load_valume):
    try:
        conn = connection_to_db()
        cursor = conn.cursor()
        conn.autocommit = True
        list_of_get_data = Check_All_item_get_from_html(H_name,H_national_code,H_Age,H_total_toll_paid,H_id,H_type,H_color,H_length,H_load_valume)
        if -4 in list_of_get_data:
            return "Some field empty"
        elif -5 in list_of_get_data:
            return "Name Error"
        elif -7 in list_of_get_data:
            return "Age Error"
        elif -8 in list_of_get_data:
            return "Totall paid Error"
        elif -9 in list_of_get_data:
            return "ID Error"
        elif -10 in list_of_get_data:
            return "Type Error"
        elif -11 in list_of_get_data:
            return "Color Error"
        elif -12 in list_of_get_data:
            return "length Error"
        elif -13 in list_of_get_data:
            return "load volume Error"
        else:
            cursor.execute("SELECT * FROM owners_car WHERE national_code = %(code)s or id = %(id)s",
                           {"code": H_national_code ,"id": H_id})
            result_query = cursor.fetchall();
            if bool(result_query) is False:
                val1 = [(str(H_national_code), str(H_name), str(H_Age), str(H_total_toll_paid))]
                sql1 = "INSERT INTO owners(national_code, name, age,total_toll_paid) VALUES (%s, %s, %s, %s)"
                val2 = [(str(H_national_code), str(H_id), str(H_type), str(H_color), str(H_length),str(H_load_valume))]
                sql2 = "INSERT INTO owners_car(national_code, id, type, color , length, load_valume) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.executemany(sql1, val1)
                cursor.executemany(sql2, val2)
                conn.commit()
                conn.close()
                return "Done! , owner and car add!"
            conn.close()
            return "Value Error or Duplicate values"
    except ValueError:
        return "value Error"

#************************************************************************************************************
def Add_Car(H_national_code,H_id,H_type,H_color,H_length,H_load_valume):
    try:
        conn = connection_to_db()
        cursor = conn.cursor()
        conn.autocommit = True
        list_of_get_data=Check_Car_item_get_from_html(H_national_code,H_id,H_type,H_color,H_length,H_load_valume)
        if -4 in list_of_get_data:
            return "Some field empty"
        elif -9 in list_of_get_data:
            return "ID Error"
        elif -10 in list_of_get_data:
            return "Type Error"
        elif -11 in list_of_get_data:
            return "Color Error"
        elif -12 in list_of_get_data:
            return "length Error"
        elif -13 in list_of_get_data:
            return "load volume Error"
        else:
            if H_type == "big":
                cursor.execute("SELECT national_code from owners_car WHERE national_code = %(code)s and type = %(type)s",
                                {"code": H_national_code ,"type": H_type})
                result_query = cursor.fetchall();
                if bool(result_query) is False:
                    cursor.execute("SELECT national_code from owners_car WHERE id = %(id)s",
                                    {"id": H_id})
                    result_query = cursor.fetchall();
                    if bool(result_query) is False:  # empty
                        val1 = [(str(H_national_code), str(H_id), str(H_type), str(H_color), str(H_length), str(H_load_valume))]
                        sql1 = "INSERT INTO owners_car(national_code, id, type, color , length, load_valume) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.executemany(sql1, val1)
                        conn.commit()
                        conn.close()
                        return "Done! Car added"
                    else:
                        conn.close()
                        return "ID car Error"
                else:
                    conn.close()
                    return "Type car Error"
            elif H_type == "small":
                cursor.execute("SELECT national_code from owners_car WHERE national_code = %(code)s",
                                {"code": H_national_code})
                result_query = cursor.fetchall();
                if bool(result_query) is True:
                    cursor.execute("SELECT national_code FROM owners_car WHERE id = %(id)s",
                                    {"id": H_id})
                    result_query = cursor.fetchall();
                    if bool(result_query) is False:  # empty
                        val1 = [(str(H_national_code), str(H_id), str(H_type), str(H_color), str(H_length), str(H_load_valume))]
                        sql1 = "INSERT INTO owners_car(national_code, id, type, color , length, load_valume) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.executemany(sql1, val1)
                        conn.commit()
                        conn.close()
                        return "Done! Car added"
                    else:
                        conn.close()
                        return "Id car Error!"
                else:
                    conn.close()
                    return "Value Error or national code not found!"
            else:
                conn.close()
                return "Type car Error!"
    except ValueError:
        return "value Error"


#************************************************************************************************************
def Function_Request_3():
    result_query = Get_query(
        '''SELECT id from owners_car INNER JOIN owners ON owners_car.national_code=owners.national_code where age > 70;''')
    result = []
    for value in result_query:
        result.append("ID Car : "+str(value[0]))
    return result

#************************************************************************************************************
def Function_Request_4():
    result_query = Get_query(
        '''SELECT id from all_node INNER JOIN roads ON all_node.point=roads.point  INNER JOIN owners_car ON all_node.car=owners_car.id where (width < 20) and (owners_car.type in ('big'));''')
    result = []
    for i in result_query:
        result.append(i[0])
    result = sorted([*set(result)])
    return result

#************************************************************************************************************
def Function_Request_5(H_nation_code,H_start_date,H_end_date,H_start_time,H_end_time):
    try:
        list_of_national_code = Get_list_of_national_code()
        for pars_nation_code1,pars_nation_code2 in enumerate(list_of_national_code):
            if int(H_nation_code) == pars_nation_code2:
                list_of_CarID_for_this_H_nation_code = Get_list_owener_ID_Car_by_nation_code(pars_nation_code1)
                list_of_load_valume_Car_for_this_H_nation_code = Get_list_owener_load_valume_Car_by_nation_code(pars_nation_code1)
                list_of_toll_per_cross_Stations_in_tollStations = Get_list_of_toll_per_cross_Stations_in_tollStations()
                list_of_CarID_in_all_node = Get_list_of_CarID_in_all_node()
                list_of_datetime_in_all_node = Get_list_of_datetime_in_all_node()
                list_of_location_in_all_node = Get_list_of_location_in_all_node()
                list_of_location_of_stations = Get_list_of_location_Stations_in_tollStations()
                Total_toll_ownerCar = 0
                list_total_toll_ownerCar = []
                list_toll_IDCar = []
                total_toll_paid_owner = Get_list_owener_total_toll_paid_by_nation_code(pars_nation_code1)

                for CarID_owner_index,CarID_owner in enumerate(list_of_CarID_for_this_H_nation_code):
                    for CarID_all_node_index,CarID_node in enumerate(list_of_CarID_in_all_node):
                        if CarID_owner == CarID_node:
                            if Check_between_date(H_start_date, H_end_date, H_start_time, H_end_time, list_of_datetime_in_all_node[CarID_all_node_index]) == True:
                                for Station_index,Station_location in enumerate(list_of_location_of_stations):
                                    if geodesic(list_of_location_in_all_node[CarID_all_node_index][17:-1], Station_location[17:-1]).meters <= 100:
                                        Toll_ID = (300*list_of_load_valume_Car_for_this_H_nation_code[CarID_owner_index])+list_of_toll_per_cross_Stations_in_tollStations[Station_index]
                                        Total_toll_ownerCar += Toll_ID
                    total_toll_paid_owner += Total_toll_ownerCar
                    list_total_toll_ownerCar.append("Totall toll for ID "+str(CarID_owner)+" : "+str(Total_toll_ownerCar))
                    Total_toll_ownerCar = 0
                list_total_toll_ownerCar.append("Totall toll for nation code "+H_nation_code+" is : "+str(total_toll_paid_owner))
                return list_total_toll_ownerCar
    except ValueError:
        return "value Error"
    except TypeError:
        return "Type Error"

#************************************************************************************************************
def Function_Request_6_1():
    result_query = Get_query(
        '''SELECT location_lat , location_long from all_node INNER JOIN owners_car ON all_node.car=owners_car.id where all_node.time = now()::time and owners_car.type in ('small');''')
    result = []
    df_places = gpd.read_file('Pages/Files/Teh.geojson')
    for location in result_query:
        lat = location[0].replace(" ", "")
        long = location[1].replace(" ", "")
        P = Point(long, lat)
        Check_Tehran = str(P.within(df_places))
        Check_Tehran = Check_Tehran[18:25].replace(" ", "")
        if Check_Tehran == "True":
            if (geodesic((lat, long), (35.68687562520049, 51.40340611555077)).meters) < 600:
                result.append("Location : (" + str(lat) + " , " + str(long) + ")")
    if bool(result_query) is False:
        return "Not Found!"
    else:
        return result

#************************************************************************************************************
def Function_Request_6_2():
    result_query = Get_query(
        '''SELECT location_lat , location_long  from all_node INNER JOIN owners_car ON all_node.car=owners_car.id where owners_car.type in ('small');''')
    result = []
    df_places = gpd.read_file('Pages/Files/Teh.geojson')
    for location in result_query:
        lat = location[0].replace(" ", "")
        long = location[1].replace(" ", "")
        P = Point(long, lat)
        Check_Tehran = str(P.within(df_places))
        Check_Tehran = Check_Tehran[18:25].replace(" ", "")
        if Check_Tehran == "True":
            if (geodesic((lat, long), (35.68687562520049, 51.40340611555077)).meters) < 600:
                #print("Location : (" + str(lat) + " , " + str(long) + ")")
                result.append("Location : (" + str(lat) + " , " + str(long) + ")")
    if bool(result_query) is False:
        return "Not Found!"
    else:
        return result

#************************************************************************************************************
def Function_Request_7():
    result_query = Get_query('''SELECT name,national_code,total_toll_paid from owners order by total_toll_paid DESC ''')
    result = []
    for value in result_query:
        result.append(
            "Total toll paid for name " + str(value[0]) + " wtih national_code " + str(value[1]) + " is : " + str(
                value[2]))
    return result



