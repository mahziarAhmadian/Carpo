from django.views.decorators.csrf import csrf_exempt
import json
from Reminder.Views import result_creator
from Reminder.Serializers.UsersSerializer import UsersSerializer


@csrf_exempt
class UsersView:
    '''
        This class is used to get data from the serializer and send it to the client.
    '''
    @csrf_exempt
    def login_user(self, request):
        """

            param : ["token",""user_phone", "user_password"]

            request_method: Post


            return: 'token for logging in to the system'

        """

        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")
        fields = ["user_phone", "user_password"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        user_phone = input_data["user_phone"]
        user_password = input_data["user_password"]
        result, data = UsersSerializer.user_login_serializer(user_phone=user_phone, user_password=user_password)
        if result:
            return result_creator(data=data)

        else:
            return result_creator(status="failure", code=403, farsi_message="شماره همراه یا رمز عبور اشتباه است",
                                  english_message="Wrong phone number or password.")

    @csrf_exempt
    def admin_create_new_user(self, request):
        """

            param : ["token", "user_name", "user_lastname", "user_phone","other_information]

            request_method: Post


            return: 'Created user in database by admin'

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
        fields = ["user_name", "user_phone", "user_password", "user_lastname", "other_information"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        user_name = input_data["user_name"]
        user_lastname = input_data["user_lastname"]
        user_phone = input_data["user_phone"]
        user_password = input_data["user_password"]
        other_information = input_data["other_information"]
        result, data = UsersSerializer.admin_create_new_user_serializer(
            token=token, user_name=user_name, user_phone=user_phone, user_lastname=user_lastname,
            user_password=user_password, other_information=other_information)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def admin_get_all_users(self, request):
        """

        param : ["token","page", "count", "user_name", "user_lastname", "user_phone"]

        request_method: Post


        return: 'List of system User'

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
        fields = ["page", "count", "user_name", "user_lastname", "user_phone"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        page = input_data["page"]
        count = input_data["count"]
        user_name = input_data["user_name"]
        user_lastname = input_data["user_lastname"]
        user_phone = input_data["user_phone"]
        result, data = UsersSerializer.admin_get_all_users_serializer(
            token=token, page=page, count=count, user_name=user_name, user_lastname=user_lastname,
            user_phone=user_phone)

        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])
