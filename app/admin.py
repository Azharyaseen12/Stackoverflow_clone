from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Questions)
admin.site.register(Comment)
admin.site.register(User_profile)
admin.site.register(Contact)
admin.site.register(Chat_Messages)