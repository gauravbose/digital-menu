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
    t=loader.get_template('restaurant/index2.html')
    dict={"one":"first","two":"second","three":"third","path":'{% static "restaurant/1.jpg" %}'}
    #s="ASCII"
    con=Context()
    c=RequestContext(request, {
        'latest_question_list': output,"l":y
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

def index_italian(request):
    #output=Menu.objects.all()
    t=loader.get_template('restaurant/index_italian.html')
    #c=Context({'menu': Menu,})
    return HttpResponse(t.render())

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
