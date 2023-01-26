from django import forms
from .models import Teacher,DirectMessage

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        #fields = ["movie","fee","academic","experience","certificate","reputation","message","oneword","lang","inst","year","revel","pic"]
        fields = ["movie","fee","academic","experience","certificate","reputation","message","oneword","lang","year","revel","pic"]
        #TODO: ここにTeacherのバリデーション対象のフィールドを書く



#TODO:ダイレクトメッセージのフォームクラスを作る。
class DirectMessageForm(forms.ModelForm):

    class Meta:
        model   = DirectMessage
        fields  = ["sender","receiver","message"]


    


