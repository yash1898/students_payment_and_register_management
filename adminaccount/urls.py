from django.urls import path,include
from . import views
app_name= 'adminaccount'
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]