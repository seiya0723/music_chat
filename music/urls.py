from django.urls import path

#from .migrations import views
from .import views

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

app_name = 'music'


urlpatterns = [
    #path('', views.index_view, name='index'),
    #path('music/', views.ListMusicView.as_view()),
    #path('music/<int:pk>/detail/', views.DetailMusicView.as_view(),name='detail-music'),
    ##path('music/detail/', views.DetailMusicView.as_view()),
    #path('music/create/', views.CreateMusicView.as_view()),
    #path('music/<int:pk>/delete/', views.DeleteMusicView.as_view(), name='delete-music'),
    #path('music/<int:pk>/update/', views.UpdateMusicView.as_view(), name='update-music'),
    ##path('music/<int:music_id>/review/', views.CreateReviewView.as_View(),name='review'),
    ##path('accounts/', include('django.contrib.auth.urls'))
    #path('music/<int:pk>/list/', views.ListView.as_view(), name="teacher-music"),
    #path('music/mypage/', views.MypageView.as_view(), name="mypage"),
    ##path('music/list/. views.'ListMusicView.as_view()),
    ##path('music/create/', views.CreatePeopleView.as_view()),
    #path('music/<int:pk>/list/', views.ListView.as_view(), name="teacher-music"),
    #path('music/mypage/', views.MypageView.as_view(), name="mypage"),

    
    path('', views.index_view, name='index'),
    path('music/', views.ListMusicView.as_view()),
    path('music/<int:pk>/detail/', views.DetailMusicView.as_view(),name='detail-music'),
    path('music/<int:pk>/student/', views.DetailStudentView.as_view(),name='detail-student'),
    #path('music/detail/', views.DetailMusicViewSecond.as_view()),
    path('music/create/', views.CreateMusicView.as_view(), name="musci-create"),
    path('music/<int:pk>/delete/', views.DeleteMusicView.as_view(), name='delete-music'),
    path('music/<int:pk>/update/', views.UpdateMusicView.as_view(), name='update-music'),
    #path('music/<int:music_id>/review/', views.CreateReviewView.as_View(),name='review'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('music/<int:pk>/list/', views.ListView.as_view(), name="teacher-music"),
    path('music/mypage/', views.MypageView.as_view(), name="mypage"),
    path('logout/',views.logout_view,name='logout'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
