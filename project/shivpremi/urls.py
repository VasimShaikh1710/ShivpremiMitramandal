from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name = 'home'),
    path('ganeshutsav', views.ganeshutsav, name = 'ganeshutsav'),
    path('shivjayanti', views.shivjayanti, name = 'shivjayanti'),
    path('navratri', views.navratri, name = 'navratri'),
    path('ganeshutsav', views.ganeshutsav, name = 'ganeshutsav')
]
