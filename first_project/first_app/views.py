from importlib.resources import contents
from django.http import  HttpResponse
from django.shortcuts import render,redirect

# from .models import PersonalData
# from .forms import ContactForm
from .forms import RegistrationForm, EmpDetailsForm
from .models import EmpDetails
#
# name_ip_for_finding="AAAA"
# update_city_id="Nagpur"
#
# database_data = [
#     {"Name":"AAAA","City":"Pune"},
#     {"Name":"BBBB","City":"Nagpur"},
#     {"Name":"CCCC","City":"Delhi"},
#     {"Name":"DDDD","City":"Mumbai"},
#     {"Name":"EEEE","City":"Goa"},
#     {"Name":"GGGG","City":"Pune"},
#     {"Name": "HHHH", "City": "Pune"},
#     {"Name": "IIII", "City": "Pune"},
#     {"Name": "JJJJ", "City": "Pune"},
#     {"Name": "KKKK", "City": "Pune"},
#     {"Name": "LLLL", "City": "Pune"},
#
# ]

# select * from PersonalData
#
# database_data = PersonalData.objects.all()




def home(request):
    # data="My first django App."
    # return render("<center><h1>" + data + "</h1><center>")
    # context ={"data":database_data}
    return render(request,"home.html")

def show_data(request,name):
    if name:
        if request.method == 'POST':
            name = request.POST['fname']

        if name:
            single_data = PersonalData.objects.filter(person_name=name)
            context = {"data": single_data}
            return redirect('show')

    context ={"data":database_data}
    return redirect('show', context)

def add_data(request):
    # new_database_data = database_data
    if request.method == 'POST':
        name =request.POST["fname"]
        city =request.POST["city"]
        # new_database_data.append({"Name": name, "City": city})
        #data.delete()
        d=PersonalData(person_name=name,person_city=city )
        d.save()
        database_data = PersonalData.objects.all()




    context ={"data":database_data}
    return render(request,"show.html",context)


#Delete method:-
def delete_op(request,name):
    # print("\n\n")
    # print("Name",name)
    # print("\n\n")
    # delete_database_data = []
    # for i in database_data:
    #     if name not in i["name"]:
    #         delete_database_data.append(i)


    # delete_database_data= [i for i in database_data if i["Name"] !=name]
   data= PersonalData.objects.filter(person_name=name)
   for d in data:
       d.delete()
   # data.delete()
   database_data = PersonalData.objects.all()
   context = {"data":database_data}
   return render(request,"show.html",context)

#search method:-
def search_by_name(request,name):
   if request.method == 'POST':
       name = request.POST['fname']

   if name:
        single_data =PersonalData.objects.filter(person_name=name)
        context = {"data": single_data}
        return redirect('show',context)

   database_data = PersonalData.objects.all()
   context = {"data":database_data}
   return render(request,"show.html",context)



def inance_home(request):
    return render(request,'index_INANCE.html')



def inance_about(request):
    return render(request,'about.html')


def inance_services(request):
    return render(request,'services.html')

# def contact_view(request):
#
#     if request.method=='POST':
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print('\n\n\n')
#             print(name,email,message)
#             print('\n\n\n')
#     form = ContactForm()
#     return render(request,"contact1.html",{"form" : form})

def registration_view(request):
    if request.method == 'POST':
        print("\n\n")
        print("registration_view")
        print("\n\n")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            print("\n\n")
            print(username,email,password,confirm_password)
            print("\n\n")
            return render(request,"sucsses.html")
    else:
        form = RegistrationForm()
    return render(request, "contact1.html", {"form": form})

def add_emp_form_view(request):
        if request.method == 'POST':
            form = EmpDetailsForm(request.POST)
            if form.is_valid():
                form.save()  # Saves the form data to the database
                return render(request, 'sucsses.html')
        else:
            form = EmpDetailsForm()
            return render(request, 'emp_details.html', {'form': form})












