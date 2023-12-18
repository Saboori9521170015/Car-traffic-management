def Check_float(string):
    try:
        string = string.replace(" ", "")
        float(string)
        string = string.lstrip(" ")
        string = string.strip(" ")
        return string
    except ValueError:
        return -1

def Check_name(Name):
    Name1 =Name.replace(" ", "")
    if Name1.isalpha() == True:
        Name = Name.lstrip(" ")
        Name = Name.strip(" ")
        return Name
    else:
        return -2
def Check_Number(Number):
    Number = Number.lstrip(" ")
    Number = Number.strip(" ")
    if Number.isdecimal() == True:
        return Number
    else:
        return -3

def Check_empty(Value):
    Value1 = Value.replace(" ","")
    if len(Value1)==0:
        #print("Empty!")
        return -4
    else:
        Value = Value.lstrip(" ")
        Value = Value.strip(" ")
        return Value

def Check_All_item_get_from_html(H_name,H_national_code,H_Age,H_total_toll_paid,H_id,H_type,H_color,H_length,H_load_valume):
    list_of_get_data=[]
    name=Check_empty(H_name)
    if name != -4:
        name=Check_name(H_name)
    elif name == -1:
        name = -5
    list_of_get_data.append(name)
    #***********************************************************
    national_code=Check_empty(H_national_code)
    if national_code != -4:
        national_code=Check_Number(H_national_code)
    elif national_code ==-3:
        national_code=-6
    list_of_get_data.append(national_code)
    #***********************************************************
    age = Check_empty(H_Age)
    if  age != -4:
        age=Check_Number(H_Age)
    elif age == -3:
        age=-7
    list_of_get_data.append(age)
    #***********************************************************
    total_toll_paid = Check_empty(H_total_toll_paid)
    if  total_toll_paid != -4:
        if Check_Number(H_total_toll_paid) != -3 or Check_float(H_total_toll_paid)!=-1:
            total_toll_paid=H_total_toll_paid
        else:
            total_toll_paid=-8
    list_of_get_data.append(total_toll_paid)
    #***********************************************************
    ID = Check_empty(H_id)
    if  ID != -4:
        ID=Check_Number(H_id)
    elif ID==-3:
        ID=-9
    list_of_get_data.append(ID)
    #***********************************************************
    Ctype = Check_empty(H_type)
    if  Ctype != -4:
        if Check_name(H_type)!= -2:
            if H_type=="small" or H_type=="big":
                Ctype=H_type
        else:
            Ctype = -10
    list_of_get_data.append(Ctype)
    #***********************************************************
    Color = Check_empty(H_color)
    if Color != -4:
        Color = Check_name(H_color)
    elif Color == -2:
        Color = -11
    list_of_get_data.append(Color)
    #***********************************************************
    length = Check_empty(H_length)
    if length != -4:
        if Check_Number(H_length) != -3 or Check_float(H_length) != -1:
            length = H_length
        else:
            length = -12
    list_of_get_data.append(length)
    #***********************************************************
    load_valume = Check_empty(H_load_valume)
    if load_valume != -4:
        if Check_Number(H_load_valume) != -3 or Check_float(H_load_valume) !=-1:
            load_valume=H_load_valume
        else:
            load_valume=-13
    list_of_get_data.append(load_valume)
    return  list_of_get_data

def Check_Car_item_get_from_html(H_national_code,H_id,H_type,H_color,H_length,H_load_valume):
    list_of_get_data=[]
    #***********************************************************
    national_code=Check_empty(H_national_code)
    if national_code != -4:
        national_code=Check_Number(H_national_code)
    elif national_code ==-3:
        national_code=-6
    list_of_get_data.append(national_code)
    #***********************************************************
    ID = Check_empty(H_id)
    if  ID != -4:
        ID=Check_Number(H_id)
    elif ID==-3:
        ID=-9
    list_of_get_data.append(ID)
    #***********************************************************
    Ctype = Check_empty(H_type)
    if  Ctype != -4:
        if Check_name(H_type)!= -2:
            if H_type=="small" or H_type=="big":
                Ctype=H_type
        else:
            Ctype = -10
    list_of_get_data.append(Ctype)
    #***********************************************************
    Color = Check_empty(H_color)
    if Color != -4:
        Color = Check_name(H_color)
    elif Color == -2:
        Color = -11
    list_of_get_data.append(Color)
    #***********************************************************
    length = Check_empty(H_length)
    if length != -4:
        if Check_Number(H_length) != -3 or Check_float(H_length) != -1:
            length = H_length
        else:
            length = -12
    list_of_get_data.append(length)
    #***********************************************************
    load_valume = Check_empty(H_load_valume)
    if load_valume != -4:
        if Check_Number(H_load_valume) != -3 or Check_float(H_load_valume) !=-1:
            load_valume=H_load_valume
        else:
            load_valume=-13
    list_of_get_data.append(load_valume)
    return  list_of_get_data