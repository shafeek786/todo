from . import views
from django.urls import path
app_name='todoapp'
urlpatterns=[
    path("",views.add,name='add'),

    path('updat/<int:id>/',views.updat,name='update'),
    path("cbvhome/",views.TaskListview.as_view(),name='cbvhome'),
    path("details/<int:pk>/",views.TaskDetailview.as_view(),name='details'),
    path('update/<int:pk>/',views.TaskUpdateview.as_view(),name='update'),
    path('delete/<int:pk>/',views.TaskDeleteView.as_view(),name='delete')


]