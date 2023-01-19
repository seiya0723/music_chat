from .serializers import DirectMessageSerializer
from django.shortcuts import render,redirect
#from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView,UpdateView,DetailView
from .models import Teacher,DirectMessage
from django.views import View
from .serializers import DirectMessageSerializer
from accounts.models import User
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

class ListMusicView(ListView):
    template_name = 'music_list.html'
    model = Teacher
    #model = music 


#旧DetailMusicView
# class DetailMusicView(DetailView):
#   template_name = 'music/music_detail.html'
#   model = Teacher

class DetailMusicView(View):
#ここにはis_musicianが使われてないから、全員出てきてしまうのでは？
    def get(self, request, pk, *args, **kwargs):

        #Teacher.objects.filter(id=pk).first()
        context = {}
        context["teacher"]  =Teacher.objects.filter(id=pk).first()

        return render(request,"music/music_detail.html" ,context)

class DetailStudentView(View):

    # このpkはUserモデルのid
    def get(self, request, pk, *args, **kwargs):

        #ここでrequest.user.is_teacherがfalseの場合に限り表示させる。
        #↑ request.userはリクエストを送信したユーザー自身の情報になる。pkが閲覧対象のユーザーのidなので、pkを使ってUserモデルからデータを取り出す。

        user    = User.objects.filter(id=pk).first()

        #存在しない場合リダイレクト
        if not user:
            return redirect("")


        #講師である場合もリダイレクト
        if user.is_musician:
            return redirect("")

        context = {"user":user}

        #生徒である場合レンダリング
        return render(request, "music/student_detail.html", context )


    










#生徒の個別ページを作りたい

#class DetailStudentView(View):
#    def get(self,request,pk,*args,**kwargs):
        #ここでrequest.user.is_teacherがfalseの場合に限り表示させる。


# #不具合のあるVeiw
# #class CreateMusicView(CreateView):    
#    template_name = 'music/music_create.html'
#    model = Teacher
    
#    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","teaching_inst","year","revel","pic","user_id")
#    success_url = '/music/'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['user_id'] = " User.objects.get()pk =self .kwargs['int:pk']"
#        return context

class CreateMusicView(CreateView):    
    template_name = 'music/music_create.html'
    model = Teacher
    #fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","teaching_inst","year","revel","pic","user_id")
    fields = ("fee","academic","experience","certificate","reputation","message","oneword","lang","teaching_inst","year","revel")

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user_id = self.request.user
    
        object.save()

        return super().form_valid(form)

    success_url = '/music/'


    

#class CreatePeopleView(CreateView):    
#    template_name = 'music/music_people_create.html'
#    model = User
#    fields = ("first_name","last_name","","city","introduction")

#    success_url = '/music/'


class DeleteMusicView(DeleteView):
    template_name = 'music/music_confirm_delete.html'
    model = Teacher
    success_url = '/music/'



def index_view(request):

    #TODO: 未ログインユーザーの場合、ログインページへリダイレクトするように仕立てる .is_authenticated属性を参照し、未ログインであればFalseが帰ってくる
    """
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    """

    if request.user.is_musician:
        #TODO:ここにDetailMusicViewSecondのnameを書く
        return redirect("music:detail-music")


    object_list = Teacher.objects.all()
    return render(request, 'music/index.html',{'object_list': object_list})



#def index_view(request):
#    object_list = Teacher.objects.all()
#    return render(request, 'music/index.html',{'object_list': object_list})

class UpdateMusicView(UpdateView): 
    model = Teacher
    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","inst","year","revel","pic","user_id")
    template_name = 'music/music_update.html'
    success_url = '/music/' 

class MypageView(View):
    def get(self, request, *args, **kwargs):

        print(request.user.id)

        context = {}
        context["teacher"] = Teacher.objects.filter(user_id=request.user.id).first()

        return render(request, "music/mypage.html",context)

    def post(self, request, *args, **kwargs):

        return redirect("mypage") 

class DirectMessageViewSet(ModelViewSet):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'Delete DM is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class InboxListView(ReadOnlyModelViewSet):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
        return self.queryset.filter(receiver=self.request.user)



#class CreateReviewView(CreateView):
#    model = Review
#    fields = ('teacher', 'title' , 'text' , 'rate')
#    template_name = 'teacher/review_form.html'     

#context_object_name = 'object_list'
#context_object_name = 'object_list'
