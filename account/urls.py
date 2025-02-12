from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from account.views import ProfileView, EditProfileView

urlpatterns =[
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('profile/edit/', EditProfileView.as_view(), name = 'editprofile'),
]
