from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.users_form,name='users_insert'),
    path('<int:id>/',views.users_form,name='users_update'),
    path('delete/<int:id>/',views.users_delete,name='users_delete'),
    path('list/',views.users_list,name='users_list')
]