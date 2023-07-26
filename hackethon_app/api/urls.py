from django.urls import path
from hackethon_app.api import views

urlpatterns = [
    path('list/', views.HackethonList.as_view(), name='hackethon-list'),
    path('create/', views.HackethonCreate.as_view(), name='hackethon-create'),
    path('registrationlist/', views.HackethonRegistrationList.as_view(), name='regitration-list'),
    path('<int:pk>/registrationcreate/', views.HackethonRegistrationCreate.as_view(), name='registration-create'),
    path('submissionlist/', views.HackethonSubmissionList.as_view(), name='submission-list'),
    path('<int:pk>/submissioncreate/', views.HackethonSubmissionCreate.as_view(), name='submission-create')
]
