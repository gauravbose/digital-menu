from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu,Cuisine,Image,Cart
from django.template import Context,loader,RequestContext
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django import template
from restaurant.forms import NameForm
from django.db import connection
from django import forms
register = template.Library()

#@register.filter
#def split(s, splitter=" "):
#    return s.split(splitter)

# Create your views here.


def index(request):
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

def indian(request):
    output=Cuisine.objects.all()
    y=Menu.objects.all()
    t=loader.get_template('restaurant/Indian.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

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
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def italian(request):
    output=Menu.objects.all().filter(cuisine_name_id="Italian")
    t=loader.get_template('restaurant/Italian.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    a=request.POST.get('item') # => [39]
    if a is not None:
        cursor=connection.cursor()
        cursor.execute("insert into restaurant_cart values(DEFAULT,'"+a+"',2,3);")
    c=RequestContext(request, {
        'latest_question_list': output
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def welcome(request):
    output=Cart.objects.all()
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


def cart(request):
    output=Cart.objects.all()
    t=loader.get_template('restaurant/cart.html')
    #dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    total=0
    for i in output:
       total=total+((i.price)*(i.quantity))
    c=RequestContext(request, {
        'latest_question_list': output,'Total':total
    })
     
	
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

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



