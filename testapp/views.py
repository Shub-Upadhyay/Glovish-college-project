from django.shortcuts import render
from testapp import forms , models
from django.http import HttpResponse
# Create your views here.

def homepage_view(request):
    
    if request.method == 'GET':
        form = forms.Login_form()
        return render (request , 'testapp/index.html' , {'forms': form} )
    if request.method == 'POST':
        form = forms.Login_form(request.POST)
        if form.is_valid():
            print(' Verifying Email ')
            data = models.Login.objects.all()
            data_list = list(data)
            login = False
            password = False
            for i in range(len(data_list)):
                print ( 'username  = ' ,  data_list[i].username ," password = ", data_list[i].password )
                if (form.cleaned_data['Username'] == data_list[i].username ):
                    login = True
                    if(form.cleaned_data['Password'] == data_list[i].password):
                        password=True
                        break
            if login == True and password == False:
                login = False
                password = False
                return HttpResponse('<h1>Wrong Id and Password</h1>')
            elif login == False and password == False:
                return signup_view(request)
            else:
                request.method= 'GET'
                return render(request , 'testapp/login.html')
                
            
    

def signup_view(request):
    if request.method == 'GET':
        form = forms.Signup_from()
        return render (request , 'testapp/sign_up.html' , {'forms': form} )
    
    if request.method == 'POST':
        form = forms.Signup_from(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Data Saved IN Database")
        form = forms.Login_form()
        return render(request , 'testapp/signupthankyou.html')


    

def Check_view(request):
    print(request)
    if request.method == "GET":
        print("GET IS WORKING")
        data = forms.Check_form()
        return render(request , 'testapp/user_page.html' , {'data':data}) 


    if request.method =='POST':
        print("POST IS WORKING")
        
        data = forms.Check_form(request.POST , request.FILES)
        
        if data.is_valid():
            data.save(commit=True)
            print("data is saved")
        else:
            print("data is not saved" )
        
        return render(request , 'testapp/upi_section.html' ) 

def Admin_view(request):
    data = models.Trying.objects.all()
    return render(request , 'testapp/admin_page.html' , {'data':data})

def Admin_auth(request):
    if request.method == "GET":
        form = forms.Admin_forms()
        return render(request , 'testapp/adminlogin.html' , {'data':form})
    if request.method == 'POST':
        
        data = forms.Admin_forms(request.POST)
        print("POST IS WORKING")
        if data.is_valid():
            if(data.cleaned_data['username'] == 'admin@admin.com' and data.cleaned_data['password'] == 'Admin123@'):
                print("admin : " , data.cleaned_data['username'] )
                return Admin_view(request)

            else:
                return HttpResponse("<h1>Admin Login Failed</h1> <h3>Please Try Again From the Home Page </h3> ")
        return render(request , 'testapp/upi_section.html')
        # if data.is_valid():
        #     print("data is valid")
        #     if(data.cleaned_data['username'] == 'admin@admin.com' and data.cleaned_data['password'] == 'Admin123@' ):

        #         return Admin_view(request)
        #     else:
        #         HttpResponse ("Wrong ID and password")
        # else:
        #     HttpResponse ("Wrong ID and password")
        # HttpResponse ("Something went wrong")
        



   


    


    