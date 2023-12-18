from django.shortcuts import render
from Pages.All_Requests import *


# Create your views here.
def index(request):
    #return HttpResponse('<h1>Hello Saeid </h1>')
    return render(request, 'index.html')

def Request1(request):
    value_of_request_1 = Function_Request_1()
    context = {
        'Values': value_of_request_1,
    }
    return render(request,'Request_1.html', context)
def about(request):
    context = {
        'firstname': 'Saeid Saboori',
    }
    #return HttpResponse('<h1>Hello Saeid </h1>')
    return render(request, 'about me.html',context)

def F(request):
    Saboori=["reza","mohsen","zahra","morteza"]
    context = {
        'firstname': Saboori,
    }
    #return HttpResponse('<h1>Hello Saeid </h1>')
    return render(request, 'My_item.html',context)

def form1(request):
    if 'message_frm' in request.POST:
    #if request.method == "POST":
        H_name = request.POST["F_name"]
        context = {
        'R': H_name,
        }
        return render(request,'form.html', context)
    return render(request,'form.html')

def Request2_1(request):
   if 'message_frm' in request.POST:
      H_name = request.POST["Name"]
      H_national_code = request.POST["national_code"]
      H_Age = request.POST["age"]
      H_total_toll_paid = request.POST["total_toll_paid"]
      H_id = request.POST["id"]
      H_type = request.POST["type"]
      H_color = request.POST["color"]
      H_length = request.POST["length"]
      H_load_valume = request.POST["load_valume"]
      Result_Add_owner = Add_Owner_and_Car(H_name,H_national_code,H_Age,H_total_toll_paid,H_id,H_type,H_color,H_length,H_load_valume)
      context = {
          'result': Result_Add_owner,
      }
      return render(request,'H_Add_owner.html', context)
   return render(request,'H_Add_owner.html')

def Request2_2(request):
   if 'message_frm' in request.POST:
      H_national_code = request.POST["national_code"]
      H_id = request.POST["id"]
      H_type = request.POST["type"]
      H_color = request.POST["color"]
      H_length = request.POST["length"]
      H_load_valume = request.POST["load_valume"]
      Result_Add_car=Add_Car(H_national_code, H_id, H_type, H_color, H_length, H_load_valume)
      context = {
          'result': Result_Add_car,
      }
      return render(request,'H_Add_car.html', context)
   return render(request,'H_Add_car.html')

def Request5(request):
   if 'message_frm' in request.POST:
      H_national_code = request.POST["national_code"]
      H_Start_date = request.POST["Start_date"]
      H_End_date = request.POST["End_date"]
      H_Start_time = request.POST["Start_time"]
      H_End_time = request.POST["End_time"]

      Result_Function_Request_5 = Function_Request_5(H_national_code,H_Start_date,H_End_date,H_Start_time,H_End_time)
      if Result_Function_Request_5 == "value Error":
          context = {
              'result': "value Error",
              'Values': "",
          }
          return render(request,'Request_5_2.html',context)
      elif Result_Function_Request_5 == "Type Error":
          context = {
              'result': "Type Error",
              'Values': "",
          }
          return render(request,'Request_5_2.html', context)
      else:
          context = {
              'result': " ",
              'Values': Result_Function_Request_5,
          }
          return render(request,'Request_5_2.html', context)
   return render(request,'Request_5.html')

def Request3(request):
    value_of_request_3 = Function_Request_3()
    context = {
        'Values': value_of_request_3,
    }
    return render(request,'Request_3.html', context)
def Request4(request):
    value_of_request_4 = Function_Request_4()
    context = {
        'Values': value_of_request_4,
        'result': "ID big car is : ",
    }
    return render(request,'Request_4.html',context)

def Request6_1(request):
    value_of_request_6_1 = Function_Request_6_1()
    if value_of_request_6_1 == "Not Found!":
        context = {
            'Values': " ",
            'result': "Not Found!",
        }
        return render(request,'Request_6_1.html', context)
    else:
        context = {
            'Values': value_of_request_6_1,
            'result': "Location : ",
        }
        return render(request,'Request_6_1.html', context)


def Request6_2(request):
    value_of_request_6_2 = Function_Request_6_2()
    context = {
        'Values': value_of_request_6_2,
        'result': "",
    }
    return render(request,'Request_6_2.html', context)

def Request7(request):
    value_of_request_7 = Function_Request_7()
    context = {
        'Values': value_of_request_7,
    }
    return render(request,'Request_7.html',context)