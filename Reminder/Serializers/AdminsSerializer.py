from Reminder.models import Admins
from Reminder.TokenManager import user_id_to_token
from Reminder.PasswordManager import Hashing


class AdminsSerializer:
    '''
        This class is used to login the admin in the system and check the access level of each admin.
    '''

    @staticmethod
    def admin_check_permission(admin_id, permission):
        admin = Admins.objects.get(admin_id=admin_id)
        if type(permission) == str:
            if permission in admin.admin_permissions:
                return True
            else:
                return False
        else:
            counter = len(permission)
            counter_checker = 0
            for per in permission:
                if per in admin.admin_permissions:
                    counter_checker += 1
                else:
                    pass
            if counter_checker == counter:
                return True
            else:
                return False

    @staticmethod
    def admin_login_serializer(admin_phone, admin_password):
        """
        In this function, because of  admin must be added to the system manually for the first time and the don't hashed
        password is entered, hashing of the input password is prevented.

        """

        # password_hashing = Hashing()
        # password_hashing = password_hashing.get_password_string(admin_password)
        try:
            admin = Admins.objects.get(admin_phone=admin_phone, admin_password=admin_password)
            admin_id = str(admin.admin_id)
            permissions = admin.admin_permissions
            token = user_id_to_token(admin_id, True, token_level="Admin")
            result = {
                "permissions": permissions,
                "token": token
            }
            return True, result
        except:
            return False, None
