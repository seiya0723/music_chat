from .serializers import DirectMessageSerializer
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView, DetailView
from .models import Teacher,DirectMessage
from django.views import View
from .serializers import DirectMessageSerializer
from accounts.models import User
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .forms import TeacherForm, DirectMessageForm #TODO: DirectMessageFormをimportしておく。

from django.db.models import Q

def logout_view(request):
    logout(request)
    return redirect('music:index')

class ListMusicView(ListView):
    template_name = 'music_list.html'
    model = Teacher
    #model = music 


#旧DetailMusicView
# class DetailMusicView(DetailView):
#   template_name = 'music/music_detail.html'
#   model = Teacher

class DetailMusicView(View):
    def get(self, request, pk, *args, **kwargs):

        context = {}
        context["teacher"]  = Teacher.objects.filter(id=pk).first()

        #TODO:編集用のフォームを作る
        context["form"]     = TeacherForm(instance=context["teacher"])

        # 自分が送ったメッセージと自分宛のメッセージをすべて表示


        # 自分が送ったメッセージ
        context["sender_messages"]      = DirectMessage.objects.filter( sender=request.user.id )

        # 自分が受け取ったメッセージ
        context["receiver_messages"]    = DirectMessage.objects.filter( receiver=request.user.id )

        # 生徒のユーザーモデルを取り出す。
        context["students"]             = User.objects.filter(is_musician=False)


        """
        # ↓送信も受信も一緒にまとめて出てくる

        # .filter()での条件式が、 sender=request.user.id もしくは receiver=request.user.id のOR検索になるので、クエリビルダを使用する。
        #  OR検索の方法: https://noauto-nolife.com/post/django-or-and-search/

        # 冒頭に from django.db.models import Q を書いておく。

        # ↓のように|とQ() を使用してOR検索を行う。
        context["messages"] = DirectMessage.objects.filter( Q(sender=request.user.id) | Q(receiver=request.user.id) )
        """


        return render(request,"music/music_detail.html" ,context)

    # このpkはTeacherのid。 Userのidではない
    def post(self, request, pk, *args, **kwargs):
    
        #TODO:ここでダイレクトメッセージの保存処理を書いていく。

        copied              = request.POST.copy()
        copied["sender"]    = request.user.id 


        #生徒→先生の場合、receiverを指定する
        if not request.user.is_musician:
            # 一旦Teacherを特定する。teacherからUserのidを取り出して記録する
            teacher             = Teacher.objects.filter(id=pk).first()
            copied["receiver"]  = teacher.user_id


        # これでsender message receiverの3つが揃ったので、バリデーションして保存する。
        form    = DirectMessageForm(copied)
        
        # sender message receiverの3つ の値が正常であれば form.is_valid()はTrue
        if form.is_valid():
            print("バリデーションOK")

            # DBにデータを保存する
            form.save()




        """
        teacher             = Teacher.objects.filter(id=pk).first()
        copied["receiver"]  = teacher.user_id

        # 書き換えたデータをバリデーションする。
        form    = DirectMessageForm(copied)
        
        if form.is_valid():
            print("バリデーションOK")
            form.save()

        """
        return redirect("music:detail-music", pk)    

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


#class DeleteMusicView(View):
    #template_name = 'music/music_confirm_delete.html'
    #model = Teacher
    #success_url = '/music/'

    

class DeleteMusicView(View):
    
    def get(self, request, pk, *args, **kwargs):
        teacher = Teacher.objects.filter(id=pk).first()

        #teacherの存在確認(存在しない場合はリダイレクト)
        if not teacher:
            return  redirect("music:index")

        #ここで存在しないteacherの.user_idを参照するとエラーになる
        if teacher.user_id == request.user:

            #TODO:ここで削除対象のUserモデルのデータを特定する。その上で.delete()を実行する。
            user    = User.objects.filter(id=request.user.id).first()
            user.delete()

        # トップページへリダイレクト
        return redirect("music:index")
 



# ここがトップページ( http://127.0.0.1:8000/ )にアクセスした時実行される
def index_view(request):

    #TODO: 未ログインユーザーの場合、ログインページへリダイレクトするように仕立てる
    # .is_authenticated属性を参照し、未ログインであればFalseが帰ってくる
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    #ここで先生かどうかを判定する。未ログイン状態ではis_musicianは参照できない。
    if request.user.is_musician:
        #TODO:ここにDetailMusicViewSecondのnameを書く
        teacher = Teacher.objects.filter(user_id=request.user.id).first()
        return redirect("music:detail-music" , teacher.id )


    #アクセスした人が先生ではない場合、先生の一覧を表示する

    object_list = Teacher.objects.all()
    return render(request, 'music/index.html',{'object_list': object_list})




#def index_view(request):
#    object_list = Teacher.objects.all()
#    return render(request, 'music/index.html',{'object_list': object_list})

class UpdateMusicView(UpdateView): 
    model = Teacher
    fields = ("movie","fee","academic","experience","certificate","reputation","message","oneword","lang","year","revel","pic","user_id")
    template_name = 'music/music_update.html'
    success_url = '/music/' 

    ## DetailMusicView から直接 編集処理をしたい場合は POSTを
    ## DetailMusicView から UpdateMusicViewへ移動して編集処理をしたい場合は、GETを

    #TODO:現状、自分以外のユーザーも編集ができてしまう。
    #対策1: UpdateViewではなくViewを継承してpostメソッドを作る。
    #対策2: pkを元にTeacherで検索。teacher.user_id と request.user が一致していれば編集許可
    # 削除の前にやった処理と同じ



class MypageView(View):
    def get(self, request, *args, **kwargs):

        print(request.user.id)

        context = {}
        context["teacher"] = Teacher.objects.filter(user_id=request.user.id).first()

        return render(request, "music/mypage.html",context)

    def post(self, request, *args, **kwargs):



        return redirect("mypage") 


"""
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
"""       



#class CreateReviewView(CreateView):
#    model = Review
#    fields = ('teacher', 'title' , 'text' , 'rate')
#    template_name = 'teacher/review_form.html'     

#context_object_name = 'object_list'
#context_object_name = 'object_list'

