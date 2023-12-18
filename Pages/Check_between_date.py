#start_date="2023-02-03"
#current_date="2023-02-04"
#end_date="2023-02-06"
#start_time="10"
#current_time="02"
#end_time="06"
def Check_between_date(start_date,end_date,start_time,end_time,datetime_in_all_node):
    if start_time!="00":
        start_time = start_time.lstrip("0")
    if end_time !="00":
        end_time = end_time.lstrip("0")
    datetime_in_all_node = datetime_in_all_node.split("T")
    #print("datetime_in_all_node",datetime_in_all_node)
    date_current = datetime_in_all_node[0]
    Time_current = datetime_in_all_node[1][:5]
    Time_current = Time_current.split(":")
    Time_current = str(Time_current[0][1:])
    start_date = start_date.split("-")
    date_current = date_current.split("-")
    end_date = end_date.split("-")
    if int(start_date[0]) <= int(date_current[0]) <= int(end_date[0]):
        if int(start_date[1]) <= int(date_current[1]) <= int(end_date[1]):
            if int(start_date[2]) <= int(date_current[2]) <= int(end_date[2]):
                if int(start_time) <= int(Time_current) <= int(end_time):
                    return True



