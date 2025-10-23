from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_contributor/', views.add_contributor, name='add_contributor'),
    path('add_task/', views.add_task, name='add_task'),
    path('list_tasks/', views.list_tasks, name='list_tasks'),
    path('contributor_list/', views.contributor_list, name='contributor_list'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('display_contributors/', views.display_contributors, name='display_contributors'),
]
