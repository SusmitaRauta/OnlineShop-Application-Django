from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name='ShopHome'),
    path("about/",views.about, name='AbouUs'),
    path("contact/",views.contact, name='ContactUs'),
    path("tracker",views.tracker, name='trackingStatus'),
    path("search",views.search, name='Search'),
    path("products/<int:myid>",views.productview, name='ProductView'),
    path("checkout",views.checkout, name='checkout')
]
