from Reminder.Serializers import status_success_result, wrong_token_result, wrong_data_result, wrong_result
from Reminder.Serializers.AdminsSerializer import AdminsSerializer
from Reminder.models import Users, Admins, Reminder
from Reminder.TokenManager import user_id_to_token, token_to_user_id


class ReminderSerializer():
    '''
        The reminder class is used to communicate with the database and receive information and send it to the view
    '''

    @staticmethod
    def user_create_reminder_serializer(token, reminder_title, reminder_message, reminder_showtime,
                                        reminder_alarm_time):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            user_id = token_result["data"]["user_id"]
            try:
                user = Users.objects.get(user_id=user_id)
                Reminder.objects.create(reminder_user=user, reminder_message=reminder_message,
                                        reminder_title=reminder_title, reminder_showtime=reminder_showtime,
                                        reminder_alarm_time=reminder_alarm_time)
            except:
                wrong_data_result["farsi_message"] = "عملیات ناموفق "
                wrong_data_result["english_message"] = "Operation failed"
                return False, wrong_data_result
            return True, status_success_result
        else:
            return False, wrong_token_result

    @staticmethod
    def user_edit_reminder_serializer(token, reminder_id, reminder_title, reminder_message, reminder_showtime,
                                      reminder_alarm_time):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            user_id = token_result["data"]["user_id"]
            try:
                reminder = Reminder.objects.filter(reminder_id=reminder_id, reminder_user__user_id=user_id)
                reminder.update(reminder_title=reminder_title, reminder_message=reminder_message,
                                reminder_showtime=reminder_showtime, reminder_alarm_time=reminder_alarm_time)
            except:
                wrong_data_result["farsi_message"] = "reminder_id اشتباه است "
                wrong_data_result["english_message"] = "reminder_id is wrong"
                return False, wrong_data_result
            return True, status_success_result
        else:
            return False, wrong_token_result

    @staticmethod
    def user_add_alarm_reminder_serializer(token, reminder_id, reminder_alarm_time):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            user_id = token_result["data"]["user_id"]
            try:
                reminder = Reminder.objects.filter(reminder_id=reminder_id, reminder_user__user_id=user_id)
                reminder.update(reminder_alarm_time=reminder_alarm_time)
            except:
                wrong_data_result["farsi_message"] = "reminder_id اشتباه است "
                wrong_data_result["english_message"] = "reminder_id is wrong"
                return False, wrong_data_result
            return True, status_success_result
        else:
            return False, wrong_token_result

    @staticmethod
    def user_delete_reminder_serializer(token, reminder_id):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            user_id = token_result["data"]["user_id"]
            try:

                deleted_reminder = Reminder.objects.filter(reminder_id=reminder_id)
                if deleted_reminder != 0:
                    deleted_reminder.delete()
                else:
                    wrong_data_result["farsi_message"] = "موردی یافت نشد "
                    wrong_data_result["english_message"] = "Nothing found"
                    return False, wrong_data_result
            except:
                wrong_data_result["farsi_message"] = "reminder_id اشتباه است "
                wrong_data_result["english_message"] = "reminder_id is wrong"
                return False, wrong_data_result
            return True, status_success_result
        else:
            return False, wrong_token_result

    @staticmethod
    def user_get_all_reminder_serializer(token, reminder_title, reminder_message, reminder_showtime,
                                         reminder_alarm_time):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            user_id = token_result["data"]["user_id"]
            filters = {
                "reminder_user__user_id": user_id,
                "reminder_title": reminder_title,
                "reminder_message": reminder_message,
                "reminder_showtime": reminder_showtime,
                "reminder_alarm_time": reminder_alarm_time,
            }
            filters = {k: v for k, v in filters.items() if v is not None}
            try:
                reminders = Reminder.objects.filter(**filters)
                reminder_results = [reminder.as_dict() for reminder in reminders]
            except:
                wrong_data_result["farsi_message"] = "داده های ورودی اشتباه است"
                wrong_data_result["english_message"] = "input data is incorrect"
                return False, wrong_data_result
            return True, reminder_results

        else:
            return False, wrong_token_result

    @staticmethod
    def user_get_one_reminder_serializer(token, reminder_id):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            try:
                reminder = Reminder.objects.get(reminder_id=reminder_id)
                reminder_result = reminder.as_dict()
            except:
                wrong_data_result["farsi_message"] = "reminder_id اشتباه است "
                wrong_data_result["english_message"] = "reminder_id is wrong"
                return False, wrong_data_result
            return True, reminder_result

        else:
            return False, wrong_token_result
