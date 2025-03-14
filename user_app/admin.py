from django.contrib import admin
from user_app.models import PassportRegistration,PassportApplication,Payment
#   # Correct import

admin.site.register(PassportRegistration)
admin.site.register(PassportApplication)

admin.site.register(Payment)