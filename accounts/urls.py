from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LogIn.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
]
