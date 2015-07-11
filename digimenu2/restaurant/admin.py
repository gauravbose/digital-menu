from django.contrib import admin

# Register your models here.
from .models import Usertable,Menu,Cuisine,Cart,Kitchen,Bill
admin.site.register(Bill)
admin.site.register(Menu)
#admin.site.register(Cuisine)
#admin.site.register(Table)
#admin.site.register(Userprofile)
#admin.site.register(Cartlist)
admin.site.register(Cart)
#admin.site.register(Cartitem)
admin.site.register(Kitchen) 
admin.site.register(Usertable)
