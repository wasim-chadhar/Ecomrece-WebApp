"""Shop URL Configuration

"""

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index' ),
    path('about/', views.about, name='AboutUs' ),
    path('contact/', views.contact, name='ContactUs' ),
    path('tracker/', views.tracker, name='TrackingStatus' ),
    path('productView/<int:myid>', views.productView, name='ProductView' ),
    path('search/', views.search, name='Search' ),
    path('checkout/', views.checkout, name='Checkout' ),
    # path('', views.index, name='index' ),
    # path('', views.index, name='index' ),
]