
from django.urls import path
from .import views
from med_store_api import views


urlpatterns = [
    
    path('available_med', views.available_med, name='available_med_api'),
    path('search_med', views.search_med, name='search_med'),
    path('<int:pk>/medicine_details', views.medicine_details.as_view()),
    path('add_medicine', views.add_medicine.as_view()),
    path('login', views.login, name='login_api'),
    path('signup',views.signup,name='signup_api')
 ]

  