from mon_app.views import UserCreateView, UserListView, UserRetrieveView, UserUpdateView, UserDelateView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create' ,UserCreateView.as_view() , name='User'),
    path('user/list' , UserListView.as_view() , name='list_users'),
    path('user/update/<int:pk>' , UserUpdateView.as_view() , name='user_update') ,
    path('user/delete/<int:pk>' ,UserDelateView.as_view() , name='user_delete' )
]
