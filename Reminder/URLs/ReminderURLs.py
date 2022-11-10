from django.urls import path
from Reminder.Views.ReminderView import RemindersView

reminder_view = RemindersView()

urlpatterns = [
    path('user/create', reminder_view.user_create_reminder_view),
    path('user/edit', reminder_view.user_edit_reminder_view),
    path('user/add/alarm', reminder_view.user_add_alarm_reminder_view),
    path('user/delete', reminder_view.user_delete_reminder_view),
    path('user/getAll', reminder_view.user_get_all_reminder_view),
    path('user/getOne', reminder_view.user_get_one_reminder_view),

]
