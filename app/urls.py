from django.contrib import admin
from django.urls import path
from .  import views

urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('questions/',views.questions,name='questions'),
    path('logout/',views.LogoutPage,name='logout'),
    path('ask_question/',views.ask_question,name='ask_question'),
    path("detail/<int:question_id>/", views.detail, name="detail"),
    path("like/<int:question_id>/", views.like, name="like"),
    path("answer/<int:question_id>/", views.answer, name="answer"),
    path("profile/<int:id>", views.profile, name="profile"),    
    path("liked_posts/<int:id>", views.liked_post, name="liked_post"),    
    path("posted_answers/<int:id>", views.posted_answers, name="posted_answers"),    
    path("createprofile/<int:id>", views.create_profile, name="createprofile"),
    path("update_profile/<int:id>", views.update_profile, name="update_profile"),
    path("user_posts/<int:id>", views.user_posts, name="user_posts"),
    path('search/',views.search,name='search'),
    path('delete_question/<int:id>',views.delete_question,name='delete_question'),
    path('contact/',views.contact,name='contact'),
    path('chat/',views.chat_home,name='chat'),
    path('personel_chat/',views.personel_chat,name='personel_chat'),

]
