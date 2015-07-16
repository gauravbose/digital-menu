from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Menu,Cuisine,Cart,Usertable,Kitchen,Bill
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
from random import randint
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
        d=Cart()
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
         username = None
         if request.user.is_authenticated():
            username = request.user
         n=Cart.objects.all().filter(item_name=a,user=username)
         if(len(n)==0):
           q=Menu.objects.filter(menu_item=a)
           for i in q:
              p=i.price
           m=Cart.objects.all().filter(item_name=a)
      
           x=Cart(item_name=a,price=p,user=username)
	   x.quantity=1
           x.save()
  
              #easygui.msgbox("already added to cart!",title="simple gui")
          #    for f in m:
          #       f.quantity+=1
          #       f.save()
              

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

def kitchen(request):
   t=loader.get_template('restaurant/kitchen.html')
   a=request.POST.get('tableno')
   user1=None
   if a is not None:
     u=Usertable.objects.all().filter(table_no=int(a))
     for i1 in u:
       user1=i1.user
     if user1 is not None:
       Bill.objects.all().filter(user=user1).delete()
       Usertable.objects.all().filter(table_no=int(a),user=user1).delete()
       Kitchen.objects.all().filter(table=int(a)).delete()
   b1=Kitchen.objects.all().order_by('-id')
   for s in b1:
       x=request.POST.get(s.orderid)
       if x is not None:
        if x=="Unavailable":
          item=s.menu_item
          tab=s.table
          us=Usertable.objects.filter(table_no=tab)
          for ta in us:
            ee=ta.user        
          Bill.objects.all().filter(user=ee,item_name=item).delete()

	if x!="Nochange":	
	       if(x!='Delivered'):
	         s.status=x
	         s.save()
	       else:
	         s.delete()
 
  

  #r=request.GET.get('table')
  
  #if r!=0:
  #      Kitchen.objects.all().filter(table=r).delete()
  #      Usertable.objects.all().filter(table_no=r).delete()
  #      #Bill.objects.all().filter(user=use).delete()
   b2=Kitchen.objects.all().order_by('-id')       
   
   c=RequestContext(request, {
         'latest_question_list':b2    })
   return HttpResponse(t.render(c))

'''
def kitchen1(request,question_id):
  t=loader.get_template('restaurant/kitchen.html')
  a=request.GET.get('tableno')
  b=request.GET.get('kitchen')
  
  u= None
  if request.user.is_authenticated():
            u=request.user
  if(b=="on"):
     m=Cart.objects.all().filter(user=u)
     for i in m:
       h=i.item_name
       p=i.quantity
       k=Kitchen(table=a,menu_item=h,quantity=p)
       k.save()
       q=Usertable(table_no=a,user=u)
       q.save()
  Cart.objects.all().filter(user=u).delete()
  b=Kitchen.objects.all()
  for j in b:
      z=(str(j.table)+"_"+(j.menu_item)).split()
      j.orderid=""
      o=0
      for o in range(len(z)):
       j.orderid+=z[o]
       
       j.save()
  b1=Kitchen.objects.all()
  for s in b1:
       x=request.GET.get(s.orderid)
       s.status=x
       s.save()

  c=RequestContext(request, {
         'table':a,'latest_question_list':b1
    })
  return HttpResponse(t.render(c))
'''
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

def bill(request,question_id):
  t=loader.get_template('restaurant/bill.html')
  u= None
  if request.user.is_authenticated():
            u=request.user
  x=Bill.objects.all().filter(user=u)
  total=0
  for i in x:
       total=total+((i.price)*(i.quantity))
   

  c=RequestContext(request, {
        'Total':total,'latest_question_list': x
    })

  return HttpResponse(t.render(c))


def bill1(request):
  t=loader.get_template('restaurant/bill.html')
  u= None
  if request.user.is_authenticated():
            u=request.user
  x=Bill.objects.all().filter(user=u)
  total=0
  for i in x:
       total=total+((i.price)*(i.quantity))
   

  c=RequestContext(request, {
        'Total':total,'latest_question_list': x
    })

  return HttpResponse(t.render(c))




def status1(request,question_id):
  t=loader.get_template('restaurant/status.html')
  b='off'
  qw=None
  b1=None
  tb="Waiting..."
  tb1="Waiting..."
  b=request.GET.get('kitchen')
  u= None
  if request.user.is_authenticated():
            u=request.user
  as0=Usertable.objects.all().exclude(table_no__gt=1000)#,user=u)
  as1=Usertable.objects.all().filter(table_no__gt=1000, user=u)
  as2=Usertable.objects.all().filter(user=u).exclude(table_no__gt=1000)
  as3= Usertable.objects.all().filter(table_no__gt=1000)
  if len(as0)<8 and len(as2)==0:#table nos. already available and user not in waiting
    a=randint(1,8)
    while 1: 
                 de=Usertable.objects.all().filter(table_no=a)
                 if len(de)!=0:
                       a=a+1
                       a=a%9
                       if(a==0):
                        a=a+1
                 else:
                    break
  
  if len(as0)>=8 and len(as2)==0:#puts user in waiting if table not available
    if len(as3)==0:
     a=1001
    else:
      ls= Usertable.objects.all().order_by('table_no')
      for i in ls:
        a=i.table_no
      a=a+1

  if len(as0)<8 and len(as3)>0:
      ls1=Usertable.objects.all().filter(table_no__gt=1000).order_by('-table_no')
      for i in ls1:
         a1=i.table_no
      u1=Usertable.objects.all().get(table_no=a1)
      a=randint(1,8)
      while 1: 
                 de=Usertable.objects.all().filter(table_no=a)
                 if len(de)!=0:
                       a=a+1
                       a=a%9
                       if(a==0):
                        a=a+1
                 else:
                    break
         		 
      k1=Kitchen.objects.all().filter(table=a1)
      for g in k1:
        g.table=a
        g.save()
      us=u1.user
      u1.delete()
      unew=Usertable(user=us,table_no=a)
      unew.save()

  if u is not None:
   aa=Usertable.objects.all().filter(user=u)
   for i in aa:
       a=i.table_no
       tb=a
       if tb>1000:
         tb1="Table Status :Waiting"
       else:
         tb1="Assigned table no. : "+str(a)
 ########  
  #if(b=="on"):
  m=Cart.objects.all().filter(user=u)
     
  for i in m:
          h=i.item_name
          p=i.quantity
          d=i.price
          k=Kitchen(table=a,menu_item=h,quantity=p,status="Received")
          k.save()
          bil=Bill(item_name=h,quantity=p,price=d,user=u)
          bil.save()
          q=Usertable(table_no=a,user=u)
          q.save()
  Cart.objects.all().filter(user=u).delete()
  ######
  b=Kitchen.objects.all()
  for j in b:
      z=(str(j.table)+"_"+(j.menu_item)).split()
      j.orderid=""
      o=0
      for o in range(len(z)):
       j.orderid+=z[o]
       j.save()
  ######
  w=Usertable.objects.all().filter(user=u)
  if w is not None: 
   for e in w:
    qw=e.table_no
   if qw is not None:
    b1=Kitchen.objects.all().filter(table=qw)
  c=RequestContext(request, {
        'latest_question_list': b1,'a':tb1
    })
    
  return HttpResponse(t.render(c))





def status(request):
  t=loader.get_template('restaurant/status.html')
  b='off'
  qw=None
  b1=None
  tb=None
  tb1=None
  b=request.GET.get('kitchen')
  u= None
  if request.user.is_authenticated():
            u=request.user
  as0=Usertable.objects.all().exclude(table_no__gt=1000)#,user=u)
  as1=Usertable.objects.all().filter(table_no__gt=1000, user=u)
  as2=Usertable.objects.all().filter(user=u).exclude(table_no__gt=1000)
  as3= Usertable.objects.all().filter(table_no__gt=1000)
  if len(as0)<8 and len(as2)==0:#table nos. already available and user not in waiting
    a=randint(1,8)
    while 1: 
                 de=Usertable.objects.all().filter(table_no=a)
                 if len(de)!=0:
                       a=a+1
                       a=a%9
                       if(a==0):
                        a=a+1
                 else:
                    break
  
  if len(as0)>=8 and len(as2)==0:#puts user in waiting if table not available
    if len(as3)==0:
     a=1001
    else:
      ls= Usertable.objects.all().order_by('table_no')
      for i in ls:
        a=i.table_no
      a=a+1

  if len(as0)<8 and len(as3)>0:
      ls1=Usertable.objects.all().filter(table_no__gt=1000).order_by('-table_no')
      for i in ls1:
         a1=i.table_no
      u1=Usertable.objects.all().get(table_no=a1)
      a=randint(1,8)
      while 1: 
                 de=Usertable.objects.all().filter(table_no=a)
                 if len(de)!=0:
                       a=a+1
                       a=a%9
                       if(a==0):
                        a=a+1
                 else:
                    break
         		 
      k1=Kitchen.objects.all().filter(table=a1)
      for g in k1:
        g.table=a
        g.save()
      us=u1.user
      u1.delete()
      unew=Usertable(user=us,table_no=a)
      unew.save()

  if u is not None:
   aa=Usertable.objects.all().filter(user=u)
   for i in aa:
       a=i.table_no
       tb=a
       if tb>1000:
         tb1="Table Status :Waiting"
       else:
         tb1="Assigned table no. : "+str(a)
 ########  
  #if(b=="on"):
  m=Cart.objects.all().filter(user=u)
     
  for i in m:
          h=i.item_name
          p=i.quantity
          d=i.price
          k=Kitchen(table=a,menu_item=h,quantity=p,status="Received")
          k.save()
          bil=Bill(item_name=h,quantity=p,price=d,user=u)
          bil.save()
          q=Usertable(table_no=a,user=u)
          q.save()
  Cart.objects.all().filter(user=u).delete()
  ######
  b=Kitchen.objects.all()
  for j in b:
      z=(str(j.table)+"_"+(j.menu_item)).split()
      j.orderid=""
      o=0
      for o in range(len(z)):
       j.orderid+=z[o]
       j.save()
  ######
  w=Usertable.objects.all().filter(user=u)
  if w is not None: 
   for e in w:
    qw=e.table_no
   if qw is not None:
    b1=Kitchen.objects.all().filter(table=qw)
  c=RequestContext(request, {
        'latest_question_list': b1,'a':tb1
    })
    
  return HttpResponse(t.render(c))






















'''
  t=loader.get_template('restaurant/status.html')
  a=request.GET.get('tableno')
  b='off'
  b=request.GET.get('kitchen')
  
  u= None
  if request.user.is_authenticated():
            u=request.user
  w=Usertable.objects.all().filter(user=u)
  
  if(b=="on"):
     m=Cart.objects.all().filter(user=u)
   
     for i in m:
       h=i.item_name
       p=i.quantity
       d=i.price
       k=Kitchen(table=a,menu_item=h,quantity=p,status="Received")
       k.save()
       bil=Bill(item_name=h,quantity=p,price=d,user=u)
       bil.save()
       q=Usertable(table_no=a,user=u)
       q.save()
  Cart.objects.all().filter(user=u).delete()
  ######
  b=Kitchen.objects.all()
  for j in b:
      z=(str(j.table)+"_"+(j.menu_item)).split()
      j.orderid=""
      o=0
      for o in range(len(z)):
       j.orderid+=z[o]
       j.save()
  ######
  for e in w:
    qw=e.table_no
  b1=Kitchen.objects.all().filter(table=qw)
  c=RequestContext(request, {
        'latest_question_list': b1
    })
    
  return HttpResponse(t.render(c))'''

def thankyou(request,question_id):
    t=loader.get_template('restaurant/thankyou.html')
    #a="off"
    q=None
    a=request.GET.get('item')
    u= None
    if request.user.is_authenticated():
            u=request.user
    w=Usertable.objects.all().filter(user=u)
    #if a=="on":
    for i in w:
        q=i.table_no
        i.delete()
    Kitchen.objects.all().filter(table=q).delete()
    Bill.objects.all().filter(user=u).delete()
     
    return HttpResponse(t.render()) 

def thankyou1(request):
    t=loader.get_template('restaurant/thankyou.html')
   # a="off"
    q=None
    a=request.GET.get('item')
    u= None
    if request.user.is_authenticated():
            u=request.user
    w=Usertable.objects.all().filter(user=u)
   # if a=="on":
    for i in w:
        q=i.table_no
        i.delete()
    Kitchen.objects.all().filter(table=q).delete()
    Bill.objects.all().filter(user=u).delete()
     
    return HttpResponse(t.render()) 
 



def welcome(request):
    output=Menu.objects.all()
    #c = {}
    a=request.POST.get('item') # => [39]
    b=Kitchen.objects.all()
    for j in b:
      z=(str(j.table)+"_"+(j.menu_item)).split()
      j.orderid=""
      o=0
      for o in range(len(z)):
       j.orderid+=z[o]
       
       j.save()
  
  #  cursor=connection.cursor()
  #  cursor.execute("insert into restaurant_cart values(93,'"+a+"',2,3);") 
    #c.update(csrf(request))
    t=loader.get_template('restaurant/welcome.html')
    dict={"path":"restaurant/13.jpg"}
    total=0
    for i in output:
       total=total+(i.price)
    c=RequestContext(request, {
        'latest_question_list': b,'Total':total,'a':a
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
    username = None
    if request.user.is_authenticated():
            username = request.user
    output=Cart.objects.all().filter(user=username)
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
    username = None
    if request.user.is_authenticated():
            username = request.user
    output=Cart.objects.all().filter(user=username)
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

