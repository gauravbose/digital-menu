from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu,Cuisine,Image
from django.template import Context,loader,RequestContext
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django import template
register = template.Library()

@register.filter
def split(s, splitter=" "):
    return s.split(splitter)

# Create your views here.
def index(request):
    output=Cuisine.objects.all()
    y=Menu.objects.all()
    t=loader.get_template('restaurant/index.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def indian(request):
    output=Cuisine.objects.all()
    y=Menu.objects.all()
    t=loader.get_template('restaurant/index_indian.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def chinese(request):
    output=Cuisine.objects.all()
    y=Menu.objects.all()
    t=loader.get_template('restaurant/Chinese.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def southindian(request):
    output=Cuisine.objects.all()
    y=Menu.objects.all()
    t=loader.get_template('restaurant/Southindian.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def chaat(request):
    output=Cuisine.objects.all()
    y=Menu.objects.all()
    t=loader.get_template('restaurant/Chaat.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
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
    output=Cuisine.objects.all()
    y=Menu.objects.all()
    t=loader.get_template('restaurant/Desserts.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def italian(request):
    output=Menu.objects.all().filter(cuisine_name_id="Italian")
    t=loader.get_template('restaurant/Italian.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output
    })
    #o=', '.join([p.cuisine_name for p in output])
    return HttpResponse(t.render(c))

def welcome(request):
    c = {}
    c.update(csrf(request))
    t=loader.get_template('restaurant/welcome.html')
    dict={"path":"restaurant/13.jpg"}
    return HttpResponse(t.render(dict))       
#return render_to_response("welcome.html", c)


def cart(request):
    #output=Menu.objects.all()
    t=loader.get_template('restaurant/cart.html')
    #c=Context({'menu': Menu,})
    return HttpResponse(t.render())

def main(request):
     i = get_object_or_404(Image, pk=1)
     return render_to_response('polls/main.html', {'image': i}, context_instance=RequestContext(request))

def detail(request):
    i = get_object_or_404(Cuisine, pk=1)
    return render_to_response('restaurant/detail.html', {'album':album})

