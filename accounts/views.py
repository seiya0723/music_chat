#from django.contrib.auth.models import User
#from django.urls import reverse_lazy
#from django.views.generic import CreateView

#from django.contrib.auth.models import User
#from django.urls import reverse_lazy
#from django.views.generic import CreateView

from .models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.shortcuts import render, redirect
from django.views import View
from .forms import SignupForm
from django.contrib.auth import login

#class SignupView(View):

#    def get(self,request,*args,**kwargs):
#        return render(request,"accounts/signup.html")

#    def post(self,request,*args,**kwargs):

#        form    = SignupForm(request.POST)

#        if form.is_valid():
#            form.save()

#        if request.POST["is_musician"]:
#            #TODO:音楽家であるにチェックが入っていた場合のリダイレクト先
#            return redirect()
#        else:
#            #TODO:音楽家であるにチェックが入ってなかった場合のリダイレクト先
#            return redirect()


#class SignupView(CreateView):
#    model = User
#    form_class = SignupForm
#    template_name = 'accounts/signup.html'
#
#    def get_success_url(self) -> str:
#        print(self.request.POST.get("is_musician",False))
#        print(self.request)
#        if self.request.POST.get("is_musician",False):
#            return reverse_lazy("music:musci-create")
#            #return reverse_lazy("accounts:user_create")
#        else:
#            print("---------")
#
#            return reverse_lazy("music:index")
#UserとTeacherの不具合のあるコード

#↓不具合改修コード
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self) -> str:
        print(self.request.POST.get("is_musician",False))
        print(self.request)
        if self.request.POST.get("is_musician",False):
            return reverse_lazy("music:musci-create")
            #return reverse_lazy("accounts:user_create")
        else:
            return reverse_lazy("music:index")
        
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result


# class CreatePeopleView(CreateView):    
#    success_url = reverse_lazy('index')
#    template_name='people/User_account.html'
#    model= User
#    fields = ("first_name","last_name","email","city","introduction","image","is_musician")


#class SignupView(CreateView):
#    model = User
#    form_class = SignupForm
#    template_name = 'accounts/signup.html'
#    success_url = "/music/music_create.html"

class CreatePeopleView(CreateView):    
    success_url = reverse_lazy('index')
    template_name='people/User_account.html'
    model= User
    fields = ("first_name","last_name","email","city","introduction","image","is_musician")

#def receive_checkbox(request):
#    model = User
#    check = request.POST["is_musician"]
#    template_name = 'accounts/signup.html'
#    success_url = "/music/create.html"
