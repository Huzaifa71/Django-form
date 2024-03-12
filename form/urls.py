from django.contrib import admin
# Importing for media or image/ file types
from django.conf import settings
from django.conf.urls.static import static 
from form_App import views

from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signUpPage,name='signup'),
    path('signin/',views.signInPage,name='signin'),
    path('home/',views.homePage,name='home'),
    path('logout/',views.logOutPage,name='logout')
]

