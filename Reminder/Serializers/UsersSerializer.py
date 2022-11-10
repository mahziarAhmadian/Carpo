from Reminder.Serializers import status_success_result, wrong_token_result, wrong_data_result, wrong_result
from Reminder.Serializers.AdminsSerializer import AdminsSerializer
from Reminder.models import Users, Admins
from Reminder.TokenManager import user_id_to_token, token_to_user_id
from Reminder.PasswordManager import Hashing
import re


class UsersSerializer():

    @staticmethod
    def admin_get_all_users_serializer(token, page, count, user_phone, user_name, user_lastname):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'User'):
                fields = {
                    "page": (page, int),
                    "count": (count, int),
                }
                field_result = wrong_result(fields)
                if field_result == None:
                    offset = int((page - 1) * count)
                    limit = int(count)
                    filters = {
                        "user_phone": user_phone,
                        "user_name": user_name,
                        "user_lastname": user_lastname,
                    }
                    filters = {k: v for k, v in filters.items() if v is not None}
                    all_users = Users.objects.filter(**filters)
                    all_users_pagination = all_users.order_by(
                        '-user_create_date')[offset:offset + limit]
                    all_users_result = [user.as_dict() for user in all_users_pagination]
                    return True, all_users_result
                else:
                    return field_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result

    @staticmethod
    def user_login_serializer(user_phone, user_password):
        try:
            fields = {
                'user_phone': (user_phone, str),
                'user_password': (user_password, str)
            }
            field_result = wrong_result(fields)
            if field_result == None:
                password_hashing = Hashing()
                password_hashing = password_hashing.get_password_string(user_password)
                try:
                    user = Users.objects.get(user_phone=user_phone, user_password=password_hashing)
                    user_id = str(user.user_id)
                    token = user_id_to_token(user_id, True, token_level="User")
                except:
                    wrong_data_result["farsi_message"] = "شماره همراه یا رمز عبور اشتباه است"
                    wrong_data_result[
                        "english_message"] = "phone number or password is incorrect"
                    return False, wrong_data_result
                result = {
                    "token": token,
                }
                return True, result
            else:
                return field_result
        except:
            return False

    @staticmethod
    def admin_create_new_user_serializer(token, user_name, user_phone, user_lastname, user_password, other_information):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'User'):
                admin = Admins.objects.get(admin_id=admin_id)
                if len(user_phone) > 11 or len(user_phone) < 11:
                    wrong_data_result["farsi_message"] = "لطفا یازده رقم وارد کنید "
                    wrong_data_result["english_message"] = "Please enter eleven digits"
                    return False, wrong_data_result
                if len(user_phone) == 11:
                    phone_number_register = bool(re.search("^(\\+98|0)?9\\d{9}$", user_phone))
                    if phone_number_register:
                        password_hashing = Hashing()
                        password_hashing = password_hashing.get_password_string(user_password)
                        try:
                            user = Users()
                            user.user_admin = admin
                            user.user_name = user_name
                            user.user_lastname = user_lastname
                            user.user_phone = user_phone
                            user.user_password = password_hashing
                            user.other_information = other_information
                            user.save()
                        except:
                            wrong_data_result["farsi_message"] = "شماره همراه در سیستم وجود د ارد . "
                            wrong_data_result[
                                "english_message"] = "phone number already exist."
                            return False, wrong_data_result
                        return True, status_success_result
                    else:
                        wrong_data_result["farsi_message"] = "شماره موبایل صحیح نیست "
                        wrong_data_result["english_message"] = "phone number not valid."
                        return False, wrong_data_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result
