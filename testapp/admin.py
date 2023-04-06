from django.contrib import admin
from testapp import models
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ['username' , 'password']

class TryingAdmin(admin.ModelAdmin):
    list_display =[ 'username' ,  'usn' , 'file' ,'print' , 'bindings' , 'print_type' , 'total_pages' , 'date' , 'time' , 'print_status' , 'amount' , 'payment' ]


# myModels = [models.Order , models.Login]

# admin.site.register(myModels)
admin.site.register(models.Trying , TryingAdmin)
admin.site.register(models.Login , LoginAdmin)

