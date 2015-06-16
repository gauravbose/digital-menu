from django.contrib import admin

# Register your models here.
from .models import Menu,Cuisine,Table,User,Cartlist,Cart

admin.site.register(Menu)
admin.site.register(Cuisine)
admin.site.register(Table)
admin.site.register(User)
admin.site.register(Cartlist)
admin.site.register(Cart)
