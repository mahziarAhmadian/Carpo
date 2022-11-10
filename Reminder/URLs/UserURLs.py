from django.urls import path
from Reminder.Views.UsersView import UsersView

user_view = UsersView()

urlpatterns = [
    path('user/login', user_view.login_user),
    path('admin/creat/user', user_view.admin_create_new_user),
    path('admin/getAllUsers', user_view.admin_get_all_users),
]
