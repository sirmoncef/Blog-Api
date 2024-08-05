from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('delete/',views.delete,name='delete'),
    path('update/',views.update,name='update'),

]