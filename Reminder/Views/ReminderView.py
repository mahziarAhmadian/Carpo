from django.views.decorators.csrf import csrf_exempt
import json
from Reminder.Views import result_creator
from Reminder.Serializers.ReminderSerializer import ReminderSerializer


@csrf_exempt
class RemindersView:
    '''
        This class is used to get data from the serializer and send it to the client.
    '''

    @csrf_exempt
    def user_create_reminder_view(self, request):
        """

            param : ["token","reminder_title", "reminder_message", "reminder_showtime", "reminder_alarm_time"]
            hint: the 'reminder_alarm_time' value can be null at first.

            request_method: Post


            return: 'created a reminder in database for user'

        """
        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        fields = ["reminder_title", "reminder_message", "reminder_showtime", "reminder_alarm_time"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        reminder_title = input_data["reminder_title"]
        reminder_message = input_data["reminder_message"]
        reminder_showtime = input_data["reminder_showtime"]
        reminder_alarm_time = input_data["reminder_alarm_time"]
        result, data = ReminderSerializer.user_create_reminder_serializer(
            token=token, reminder_title=reminder_title, reminder_message=reminder_message,
            reminder_showtime=reminder_showtime,
            reminder_alarm_time=reminder_alarm_time)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def user_edit_reminder_view(self, request):
        """

            param : ["token",reminder_title", "reminder_message", "reminder_showtime", "reminder_alarm_time", "reminder_id"]
            hint: the 'reminder_alarm_time' can be set in this api .

            request_method: Post


            return: 'edit a user reminder .'

        """
        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        fields = ["reminder_title", "reminder_message", "reminder_showtime", "reminder_alarm_time", "reminder_id"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        reminder_title = input_data["reminder_title"]
        reminder_message = input_data["reminder_message"]
        reminder_showtime = input_data["reminder_showtime"]
        reminder_alarm_time = input_data["reminder_alarm_time"]
        reminder_id = input_data["reminder_id"]
        result, data = ReminderSerializer.user_edit_reminder_serializer(
            token=token, reminder_id=reminder_id, reminder_title=reminder_title, reminder_message=reminder_message,
            reminder_showtime=reminder_showtime,
            reminder_alarm_time=reminder_alarm_time)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def user_add_alarm_reminder_view(self, request):
        """

            param : ["token",reminder_title", "reminder_id", "reminder_alarm_time"]

            request_method: Post

            return: 'set alarm for user reminder in database'

        """
        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        fields = ["reminder_id", "reminder_alarm_time"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        reminder_alarm_time = input_data["reminder_alarm_time"]
        reminder_id = input_data["reminder_id"]
        result, data = ReminderSerializer.user_add_alarm_reminder_serializer(
            token=token, reminder_id=reminder_id, reminder_alarm_time=reminder_alarm_time)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def user_delete_reminder_view(self, request):
        """

            param : ["token",reminder_title", "reminder_id"]

            request_method: Post

            return: 'delete user reminder from database.'

        """
        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        if 'reminder_id' not in input_data:
            return result_creator(status="failure", code=406, farsi_message=".وارد نشده است reminder_id",
                                  english_message="reminder_id is Null.")
        reminder_id = input_data["reminder_id"]
        result, data = ReminderSerializer.user_delete_reminder_serializer(
            token=token, reminder_id=reminder_id)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def user_get_all_reminder_view(self, request):
        """

            param : ["token","reminder_title", "reminder_message", "reminder_showtime", "reminder_alarm_time"]
            hint: 'The values in the param can be null, then the list of all data will be returned, if any of
            the values is not null, it will search with that value.'

            request_method: Post

            return: 'list of user reminders in database.'

        """
        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        fields = ["reminder_title", "reminder_message", "reminder_showtime", "reminder_alarm_time"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        reminder_title = input_data["reminder_title"]
        reminder_message = input_data["reminder_message"]
        reminder_showtime = input_data["reminder_showtime"]
        reminder_alarm_time = input_data["reminder_alarm_time"]
        result, data = ReminderSerializer.user_get_all_reminder_serializer(
            token=token, reminder_title=reminder_title, reminder_message=reminder_message,
            reminder_showtime=reminder_showtime,
            reminder_alarm_time=reminder_alarm_time)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def user_get_one_reminder_view(self, request):
        """

            param : ["token","reminder_id"]

            request_method: Post

            return: 'The data of a specific reminder.'

        """
        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        if 'reminder_id' not in input_data:
            return result_creator(status="failure", code=406, farsi_message=".وارد نشده است reminder_id",
                                  english_message="reminder_id is Null.")
        reminder_id = input_data["reminder_id"]
        result, data = ReminderSerializer.user_get_one_reminder_serializer(
            token=token, reminder_id=reminder_id)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])
