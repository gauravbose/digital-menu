from django.contrib import admin
from django.db import models
from PIL import Image 
# Create your models here.

class Cuisine(models.Model):
    cuisine_name = models.CharField(primary_key = True , max_length=200)
    image_path= models.CharField(max_length=100)

    def __str__(self):
        return self.cuisine_name

class Image(models.Model):
	cuisine = models.ForeignKey(Cuisine)
	image =models.ImageField(upload_to='images',verbose_name='My Photo')

class InlineImage(admin.TabularInline):
      model=Image

class CuisineAdmin(admin.ModelAdmin):
	inlines=[InlineImage]

admin.site.register(Cuisine,CuisineAdmin)   
 
class Menu(models.Model):
    menu_item = models.CharField(primary_key = True , max_length =200)
    price = models.IntegerField()
    description = models.TextField()
    cuisine_name = models.ForeignKey(Cuisine)
    def __str__(self):
        return self.menu_item


class Table(models.Model):
    table_no = models.IntegerField(primary_key = True)
    def __str__(self):
        return "Table Number " + str(self.table_no)
        

class User(models.Model):
    name = models.CharField(max_length = 30)
    phone_no = models.IntegerField()
    table_no = models.ForeignKey(Table)
    password = models.CharField(primary_key = True ,max_length=7)
    bill_id = models.IntegerField()


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key = True)
    item_name = models.CharField(max_length = 200)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()

    
class Cartlist(models.Model):
    bill_id = models.ForeignKey(User)
    cart_id = models.ForeignKey(Cart)
   
