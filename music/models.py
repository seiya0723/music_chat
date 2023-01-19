from django.db import models
from django.conf import settings
from accounts.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.translation import gettext as _
#from .consts import MAX_RATE

#RATE_CHOICES = [(x, str(x))for x in range(0, MAX_RATE +1)]

class instrument(models.Model):
    inst_name = models.CharField(max_length=50)
    #inst_image = models.ImageField(blank=True, null=True)
    #inst_category = models.CharField(max_length=20)
    #TODO:AUTH_USER_MODELにカスタムユーザーモデルの在り処が書いてあるので、settingsから呼び出し、1対多を組む
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="ユーザー", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.inst_name

class language(models.Model):
    language_name =  models.CharField(max_length=20)

    def __str__(self):
        return self.language_name

#class teaching_inst(models.Model):
    #teaching_inst   = models.ForeignKey(instrument, related_name="teaching_inst" ,  on_delete=models.CASCADE, null=True, blank=True) 
    #teaching_inst1  = models.ForeignKey(instrument, related_name="teaching_inst1",  on_delete=models.CASCADE, null=True, blank=True)
    #teaching_inst2  = models.ForeignKey(instrument, related_name="teaching_inst2",  on_delete=models.CASCADE, null=True, blank=True)
    #teaching_inst3  = models.ForeignKey(instrument, related_name="teaching_inst3",  on_delete=models.CASCADE, null=True, blank=True)
    #year = models.IntegerField(null=True, blank=True)
    #revel = models.IntegerField(null=True, blank=True)
#class teaching_langage(models.Model):    
#    teaching_lang = models.ForeignKey(language, on_delete=models.CASCADE) 

class teacher_picture(models.Model): 
    image = models.ImageField(_('image'), blank=True, null=True)    

class  Teacher(models.Model):
    movie = models.URLField(max_length=200, null=True, blank=True)
    #fee = models.IntegerField()
    #fee = models.IntegerField()
    #この場合、feeには0から3までの数値だけ入力が許される。
    fee = models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(100)] , null=True, blank=True)
    academic = models.TextField(max_length=500)
    experience = models.TextField(max_length=500)
    certificate = models.TextField(max_length=500)
    reputation = models.TextField(max_length=500, null=True, blank=True)
    message = models.TextField(max_length=500)
    oneword = models.TextField(max_length=500)
    lang = models.ManyToManyField(language, blank=True)
    #lang = models.ForeignKey(language, on_delete=models.CASCADE, null=True, blank=True)
    #lang2 = models.ForeignKey(language, on_delete=models.CASCADE, null=True, blank=True)
    #inst = models.ForeignKey(teaching_inst, on_delete=models.CASCADE, null=True, blank=True)
    pic = models.ForeignKey(teacher_picture, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='email',default="9999")
    #contributer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    teaching_inst   = models.ForeignKey(instrument, related_name="teaching_inst", on_delete=models.CASCADE, null=True, blank=True) 
    year = models.IntegerField(null=True, blank=True)
    revel = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return str(self.user_id)

class DirectMessage(models.Model):
        
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sender',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='receiver',
        on_delete=models.CASCADE
    )
    message = models.CharField(verbose_name="メッセージ", max_length=200)
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    def __str__(self):
        return str(self.sender) + ' --- send to ---> ' + str(self.receiver)        
   

                
#class Review (models .Model):
    #teacher = models.CharField('名前', max_length=39)
    #title = models.CharField(max_length=100)
    #text = models.TextField()
    #rate = models.IntegerField(choices=RATE_CHOICES)
    #user = models.ForeignKey(auth.User , on_delete=models.CASCADE)

    #ef __str__(self):
     #   return self.title
