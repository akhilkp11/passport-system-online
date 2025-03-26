from django.contrib.auth.tokens import PasswordResetTokenGenerator

class CustomTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, employee, timestamp):
        return f'{employee.pk}{timestamp}{employee.official_email}'

custom_token_generator = CustomTokenGenerator()
