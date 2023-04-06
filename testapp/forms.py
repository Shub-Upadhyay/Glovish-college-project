from django import forms
from testapp import models
import re



class Login_form (forms.Form):
    Username = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)
    



def password_valid(value):
    uppercase = False
    lowercase = False
    num = False
    symbol = False
    for i in value:
        if i.islower():
            lowercase=True
        if i.isupper():
            uppercase = True
        regex = regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(regex.search(i)):
            symbol=True
        if(i.isnumeric()):
            num = True
    if (uppercase and lowercase and num and symbol):
        return True
    else :
        raise forms.ValidationError('Password Should Contain Special Char , Upper Case , Lower Case , Numbers')
        

class Signup_from(forms.ModelForm):
    password = forms.CharField(validators=[password_valid])
    class Meta:
        model = models.Login
        fields = '__all__'


# class Order_form(forms.ModelForm):
#     class Meta:
#         model = models.Test
#         exclude = ('print_status' , 'date' 'time' , 'payment')


    

class Check_form(forms.ModelForm):
   
    class Meta:
        model= models.Trying
        exclude = ('print_status' , 'date' 'time' , 'payment')
        
class Admin_forms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

