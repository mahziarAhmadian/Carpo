from django.views.decorators.csrf import csrf_exempt
import json
from Reminder.Serializers.AdminsSerializer import AdminsSerializer
from Reminder.Views import result_creator


@csrf_exempt
class AdminsView:
    '''
        This class is used to get data from the serializer and send it to the client.
    '''
    @csrf_exempt
    def login_admin(self, request):
        """

            param : ["token","admin_phone", "admin_password"]

            request_method: Post

            return: 'token for logging in to the system'

        """
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        admin_phone = input_data["admin_phone"]
        admin_password = input_data["admin_password"]
        result, data = AdminsSerializer.admin_login_serializer(admin_phone=admin_phone, admin_password=admin_password)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message="شماره موبایل و رمز عبور مطابقت ندارند.",
                                  english_message="Wrong phone number or password.")
