from django.conf.urls import url
from . import views

urlpatterns += static_files_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


urlpatterns=[
    
    url(r'^$',views.index,name='index'),
    url(r'^$',views.welcome,name='welcome'),
    url(r'^$',views.italian,name='italian'),
    url(r'^$',views.chinese,name='chinese'),
    url(r'^$',views.indian,name='indian'),
    url(r'^$',views.desserts,name='desserts'),
    url(r'^$',views.beverages,name='beverages'),
    url(r'^$',views.southindian,name='southindian'),
    url(r'^$',views.chaat,name='chaat'),
    url(r'^$',views.cart,name='cart'),
]
