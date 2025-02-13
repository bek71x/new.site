from django.contrib.auth.views import (LoginView, LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,
                                       PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)
from django.urls import path


from account.views import ProfileView, EditProfileView

urlpatterns =[
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('profile/edit/', EditProfileView.as_view(), name = 'editprofile'),
    path('profile/password/edit/', PasswordChangeView.as_view(), name = 'editpassword'),
    path('profile/password/change_done/', PasswordChangeDoneView.as_view(), name = 'password_change_done'),


    path('password/reset/', PasswordResetView.as_view(), name = 'password_reset'),
    path('password/reset/done', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password/reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password/resetcomplete', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
]
