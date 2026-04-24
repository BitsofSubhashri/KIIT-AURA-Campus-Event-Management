from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
    path('event/<int:id>/register/', views.register_event, name='register_event'),
    path('history/', views.history, name='history'),
    path('contact/', views.contact, name='contact'),  
    path('signup/', views.signup, name='signup'),
    path('feedback/', views.feedback, name='feedback'),
]
