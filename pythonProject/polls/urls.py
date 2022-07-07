from django.urls import path

from . import views

urlpatterns = [
    # login page
    path('', views.index, name='index'),

    # login
    path('loginProcess', views.login, name='login'),

    # register
    path('registerProcess', views.register, name='login'),

    # login redirect
    path('loginRedirect', views.login_redirect, name='login'),

    # register redirect
    path('registerRedirect', views.register_redirect, name='register'),

    # logout redirect
    path('logoutRedirect', views.logout_redirect, name='logout'),

    # quiz redirect
    path('quizRedirect', views.quiz_redirect, name='quiz'),

    # start quiz
    path('takeTest', views.take_test, name='test'),

    # user menu
    path('userMenu', views.user_menu, name='test'),

]