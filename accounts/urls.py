#from django.contrib.auth.views import LoginView, LogoutView
#from django.urls import path
#from .import views
#from .views import SignupView, CreatePeopleView

#app_name = 'accounts'

#urlpatterns = [
#    path('login/', LoginView.as_view(), name='login'),
#    path('logout/', LogoutView.as_view(), name='logout'),
#    path('signup/', SignupView.as_view(), name='signup'),
#    path('accounts/create/', views.CreatePeopleView.as_view()),


from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import SignupView, CreatePeopleView

from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    #path('create/', CreatePeopleView.as_view(), name="user_create"),
 
]
