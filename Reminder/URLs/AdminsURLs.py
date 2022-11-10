from django.urls import path
from Reminder.Views.AdminsView import AdminsView

admins_view = AdminsView()

urlpatterns = [
    path('admin/login', admins_view.login_admin),
]
