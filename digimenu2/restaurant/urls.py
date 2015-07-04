from django.conf.urls import url
from . import views

#urlpatterns += static_files_urlpatterns()
#urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


urlpatterns=[
   # url(r'^polls/', include('restaurant.urls', namespace="restaurant")),
   # url(r'^$',views.index,name='index'),
   # url(r'^$',views.welcome,name='welcome'),
   # url(r'^$',views.italian,name='italian'),
   # url(r'^$',views.chinese,name='chinese'),
    #url(r'^$',views.indian,name='indian'),
   # url(r'^$',views.desserts,name='desserts'),
    #url(r'^$',views.beverages,name='beverages'),
   # url(r'^$',views.southindian,name='southindian'),
   # url(r'^$',views.chaat,name='chaat'),
   # url(r'^$',views.cart,name='cart'),
    url(r'^index.?$','restaurant.views.index1'),
    url(r'^Chinese.*$','restaurant.views.chinese'),
    url(r'^Desserts.*$','restaurant.views.desserts'),
    url(r'^Chaat.+$','restaurant.views.chaat'),
    url(r'^restaurant/index/Italian.*$','restaurant.views.italian'),
    url(r'^South.*$','restaurant.views.southindian'),
   # url(r'^index/1.*$','restaurant.views.italian'),
    url(r'^welcome.*$','restaurant.views.welcome'),
    url(r'^cart.*$','restaurant.views.cart'),
    url(r'^restaurant/welcome/index.*$','restaurant.views.index'),
    url(r'^restaurant/index/welcome.*$','restaurant.views.welcome'),
    url(r'^index/index.*$','restaurant.views.index1'),
    url(r'^index/cart.*$','restaurant.views.cart1'),
   # url(r'^index/(?P<question_id>[0-9]+.*)$','restaurant.views.italian'),
    url(r'^index(/(?P<question_id>[0-9]+))+.?$','restaurant.views.italian'),
    url(r'^index(/(?P<question_id>[0-9]+))+/index.*$','restaurant.views.index'),
    url(r'^index(/(?P<question_id>[0-9]+))+/cart.*$','restaurant.views.cart'),
 
    ]
