from django.conf.urls import url
from . import views

urlpatterns += static_files_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^$',views.welcome,name='welcome'),
    url(r'^$',views.index_italian,name='index_italian'),
    url(r'^$',views.cart,name='cart'),
]
