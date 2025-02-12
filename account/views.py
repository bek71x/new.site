from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from account.forms import ProfileForm


class UserLoginview(View):
    def get(self,request):
        login_form =LoginForm()
        return render(request,'registration/login.html',context={'form':login_form})

    def post(self,request):
        login_form = LoginForm(request.POST)
        print(login_form)
        # username = request.POST['username']
        # password = request.POST['password']

        return HttpResponse('login boldingiz')

class ProfileView(View):
    def get(self,request):

        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        context = {
            'username':username,
            'first_name':first_name,
            'last_name':last_name,
            'email':email
        }
        return render(request,'registration/profile.html',context)


class EditProfileView(View):
    def get(self,request):
        userform = ProfileForm(instance=request.user)
        return render(request,'registration/edit_profile.html',{'form':userform})

    def post(self,request):
         userform= ProfileForm(request.POST,instance=request.user)
         if userform.is_valid():
             userform.save()
             return redirect("profile")
         return render(request, 'registration/edit_profile.html', {'form': userform})