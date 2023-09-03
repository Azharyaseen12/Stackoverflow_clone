from django.contrib import admin
from .models import *

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display=('user','content','date_created')
admin.site.register(Questions,QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display=('name','content','date_created')
admin.site.register(Answer,AnswerAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display=('user','city','phone')
admin.site.register(User_profile,profileAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','subject','date_created')
admin.site.register(Contact,ContactAdmin)

class ChatAdmin(admin.ModelAdmin):
    list_display=('user','message','date_created')
admin.site.register(Chat_Messages,ChatAdmin)

class PersonelChatAdmin(admin.ModelAdmin):
    list_display=('sender','receiver','timestamp')
admin.site.register(PersonelChat,PersonelChatAdmin)

admin.site.register(Message)
# admin.site.register(ChatRoom)

admin.site.site_header = "CodeExchange Admin"
admin.site.site_title = "CodeExchange Admin"
admin.site.index_title = "Welcome To CodeExchange"