
from django.urls import path
from . import views

app_name='bin'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('paste/',views.paste,name='paste'),
	    path('login/',views.user_login,name='user_login'),

]
