from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Menu,Cuisine,Cart
from django.template import Context,loader,RequestContext
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django import template
from restaurant.forms import NameForm,UserForm
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import UserForm 
from django.db import connection
from django import forms
#import easygui
register = template.Library()

#@register.filter
#def split(s, splitter=" "):
#    return s.split(splitter)

# Create your views here.




def register_user(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':		
	   user_form = UserForm(data=request.POST)
	   if user_form.is_valid():
	     user = user_form.save()
	     user.set_password(user.password)
             user.save()
	     registered = True
           
        else:
             user_form = UserForm()

        return render_to_response(
            'restaurant/register.html',
            {'user_form': user_form, 'registered': registered},
            context)





#    if request.method=='POST':
#       form = UserCreateForm(request.POST)
#       if form.is_valid():
#           form.save()
#           return HttpResponseRedirect('/accounts/register_success')

#    else:  
#        form = UserCreateForm()

#    args={}
#    args.update(csrf(request))

#    args['forms'] = form
#    print args
    #return render_to_response('restaurant/register.html',args)


def register_success(request):
    return render_to_response('restaurant/register_success.html')


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('restaurant/login.html',c )

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request,user)
	return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('restaurant/loggedin.html',
			     {'full_name':request.user.username})
def invalid_login(request):
    return render_to_response('restaurant/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('restaurant/logout.html')











def index(request,question_id):
    output=Cuisine.objects.all()
    #y=Menu.objects.all()
    t=loader.get_template('restaurant/index.html')
    #dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def index1(request):
    output=Cuisine.objects.all()
    #y=Menu.objects.all()
    t=loader.get_template('restaurant/index.html')
    #dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

#def indian(request):
#    output=Cuisine.objects.all()
#    y=Menu.objects.all()
#    t=loader.get_template('restaurant/Indian.html')
#    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
#    #s="ASCII"
#    con=Context()
#    c=RequestContext(request, {
#        'latest_question_list': output,"l":y
#    })
#    #o=', '.join([p.cuisine_name for p in output])
#    return HttpResponse(t.render(c))
'''
def chinese(request):
    output=Menu.objects.all().filter(cuisine_name_id="Chinese")
    
    t=loader.get_template('restaurant/Chinese.html')
    #dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    #con=Context()
    c=RequestContext(request, {
        'latest_question_list': output
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def southindian(request):
    output=Menu.objects.all().filter(cuisine_name_id="South Indian")
    t=loader.get_template('restaurant/South.html')
    #dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    #con=Context()
    c=RequestContext(request, {
        'latest_question_list': output
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def chaat(request):
    output=Menu.objects.all().filter(cuisine_name_id="Chaat")
    t=loader.get_template('restaurant/Chaat.html')
    #dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    #con=Context()
    c=RequestContext(request, {
        'latest_question_list': output
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def beverages(request):
    output=Cuisine.objects.all()
    y=Menu.objects.all()
    t=loader.get_template('restaurant/Beverages.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def desserts(request):
    output=Menu.objects.all().filter(cuisine_name_id="Desserts")
    t=loader.get_template('restaurant/Desserts.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
#    con=Context()
 #   c=RequestContext(request, {
#        'latest_question_list': output
#    })
#    #o=', '.join([p.cuisine_name for p in output])
#    return HttpResponse(t.render(c))

'''

def italian(request,question_id):
    
    cuis=Cuisine.objects.all().filter(cuisine_id=question_id)
    for j in cuis:
        z=j.cuisine_name
        h=j.cuisine_id
    output=Menu.objects.all().filter(cuisine_id=h)
    #for j in output:
   #    j.menu_item=j.menu_item.replace(" ","_")
    t=loader.get_template('restaurant/Italian.html')
   # dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    a=request.POST.get('item')
    ms=" added in the cart"
    if a is not None:
         a=a.replace('_',' ') 
         q=Menu.objects.filter(menu_item=a)
         for i in q:
           p=i.price
         m=Cart.objects.all().filter(item_name=a)
         if len(m)==0:
              x=Cart(item_name=a,price=p)
	      x.quantity+=1
              x.save()
         else:
              #easygui.msgbox("already added to cart!",title="simple gui")
          #    for f in m:
          #       f.quantity+=1
          #       f.save()
              for f in m:
                 if (f.quantity==1):
                     ms=' already added in the cart'

    c=RequestContext(request, {
        'latest_question_list': output,'msg':ms,'cuisine':z,'id':question_id
    })
    return HttpResponse(t.render(c))


def desserts(request):
    output=Menu.objects.all().filter(cuisine_name_id="Desserts")
    #for j in output:
   #    j.menu_item=j.menu_item.replace(" ","_")
    t=loader.get_template('restaurant/Desserts.html')
   # dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    a=request.POST.get('item')
    ms=" added in the cart"
    if a is not None:
         a=a.replace('_',' ')
	 
         q=Menu.objects.filter(menu_item=a)
         for i in q:
           p=i.price
         m=Cart.objects.all().filter(item_name=a)
         if len(m)==0:
              x=Cart(item_name=a,price=p)
	      x.quantity+=1
              x.save()
         else:
              for f in m:
                 if (f.quantity==1):
                     ms=' already added in the cart'

              
    c=RequestContext(request, {
        'latest_question_list': output,'msg':ms
    })
    return HttpResponse(t.render(c))

def chinese(request):
    output=Menu.objects.all().filter(cuisine_name_id="Chinese")
  
    t=loader.get_template('restaurant/Chinese.html')
   # dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    a=request.POST.get('item')
    ms=" added in the cart"
    if a is not None:
         a=a.replace('_',' ')
	
         q=Menu.objects.filter(menu_item=a)
         for i in q:
           p=i.price
         m=Cart.objects.all().filter(item_name=a)
         if len(m)==0:
              x=Cart(item_name=a,price=p)
	      x.quantity+=1
              x.save()
         else:
              for f in m:
                 if (f.quantity==1):
                     ms=' already added in the cart'

    c=RequestContext(request, {
        'latest_question_list': output,'msg':ms
    })
    return HttpResponse(t.render(c))

def chaat(request):
    output=Menu.objects.all().filter(cuisine_name_id="Chaat")

    t=loader.get_template('restaurant/Chaat.html')
   # dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    a=request.POST.get('item')
    ms=" added in the cart"
    
    if a is not None:
         a=a.replace('_',' ')
	 q=Menu.objects.filter(menu_item=a)
         for i in q:
           p=i.price
         m=Cart.objects.all().filter(item_name=a)
         if len(m)==0:
              x=Cart(item_name=a,price=p)
	      x.quantity+=1
              x.save()
         
         else:
              for f in m:
                 if (f.quantity==1):
                     ms=' already added in the cart'
    c=RequestContext(request, {
        'latest_question_list': output, 'msg':ms
    })
    return HttpResponse(t.render(c))



def southindian(request):
    output=Menu.objects.all().filter(cuisine_name_id="South Indian")

    t=loader.get_template('restaurant/South.html')
   # dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    a=request.POST.get('item')
    ms=" added in the cart"
    if a is not None:
         a=a.replace('_',' ')
	 q=Menu.objects.filter(menu_item=a)
         for i in q:
           p=i.price
         ms=" already added in the cart"
         m=Cart.objects.all().filter(item_name=a)
         if len(m)==0:
              x=Cart(item_name=a,price=p)
	      x.quantity+=1
              x.save()
         
         else:
                     ms=' already added in the cart'
    c=RequestContext(request, {
        'latest_question_list': output, 'msg':ms
    })
    return HttpResponse(t.render(c))





def welcome(request):
    output=Menu.objects.all()
    #c = {}
    a=request.POST.get('item') # => [39]
  #  cursor=connection.cursor()
  #  cursor.execute("insert into restaurant_cart values(93,'"+a+"',2,3);") 
    #c.update(csrf(request))
    t=loader.get_template('restaurant/welcome.html')
    dict={"path":"restaurant/13.jpg"}
    total=0
    for i in output:
       total=total+(i.price)
    c=RequestContext(request, {
        'latest_question_list': output,'Total':total,'a':a
    })
    return HttpResponse(t.render(c))       
#return render_to_response("welcome.html", c)


def cart(request,question_id):
    
    t=loader.get_template('restaurant/cart.html')
    #dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    a=request.POST.get('delete')
    b=request.POST.get('add')
    c=request.POST.get('dec')
    if a is not None:
         a=a.replace('_',' ') 
         Cart.objects.all().filter(item_name=a).delete()
    if b is not None:
         b=b.replace('_',' ') 
         q=Cart.objects.all().filter(item_name=b)
         for te in q:
          te.quantity+=1
          te.save()
    if c is not None:
         c=c.replace('_',' ') 
         w=Cart.objects.all().filter(item_name=c)
         for de in w:
          if (de.quantity)!=1:
           de.quantity-=1
           de.save()
          else:
           Cart.objects.all().filter(item_name=c).delete()
    total=0
    output=Cart.objects.all()
    for i in output:
       total=total+((i.price)*(i.quantity))
    c=RequestContext(request, {
        'latest_question_list': output,'Total':total
    })
     
	
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))


def cart1(request):
    
    t=loader.get_template('restaurant/cart.html')
    #dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    a=request.POST.get('delete')
    b=request.POST.get('add')
    c=request.POST.get('dec')
    if a is not None:
         a=a.replace('_',' ') 
         Cart.objects.all().filter(item_name=a).delete()
    if b is not None:
         b=b.replace('_',' ') 
         q=Cart.objects.all().filter(item_name=b)
         for te in q:
          te.quantity+=1
          te.save()
    if c is not None:
         c=c.replace('_',' ') 
         w=Cart.objects.all().filter(item_name=c)
         for de in w:
          if (de.quantity)!=1:
           de.quantity-=1
           de.save()
          else:
           Cart.objects.all().filter(item_name=c).delete()
    total=0
    output=Cart.objects.all()
    for i in output:
       total=total+((i.price)*(i.quantity))
    c=RequestContext(request, {
        'latest_question_list': output,'Total':total
    })
     
	
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))






'''
def main(request):
     i = get_object_or_404(Image, pk=1)
     return render_to_response('polls/main.html', {'image': i}, context_instance=RequestContext(request))

def detail(request):
    i = get_object_or_404(Cuisine, pk=1)
    return render_to_response('restaurant/detail.html', {'album':album})

def post_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            #created_at = form.cleaned_data['created_at']
            post = m.Post.objects.create(content=content)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))
 
    return render(request, 'post/post_form_upload.html', {
        'form': form,
    })

'''

