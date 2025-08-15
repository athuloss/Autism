"""
URL configuration for autism project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('sign/', views.signup,name='sig'),
    path('checksignin/', views.checksignin,name='checksignin'),
    path('logins/', views.loginviews,name='logins'),
    path('logouts/', views.logoutviews,name='logouts'),
    path('forum/', views.forum, name='forum'),
    path('upload/', views.uploadpost, name='uploadpost'),
    path('gamecontrol/', views.gamecontrol, name='gamecontrol'),
    path('chat_bot/', views.chat_bot, name='chat_bot'),
    path('delete/<pk>', views.delete_view,name='delete'),

    path('comment/<int:pk>/', views.add_comment, name='add_comment'),
    # path('Reply/', views.replay,name='replay'),
    path('parentDashboard/', views.parentDashboard,name='parentDashboard'),
    path('adminDashboard/', views.adminDashboard,name='adminDashboard'),
    
    path('ImageGame/', views.ImageGame,name='ImageGame'),
    path('ImageTileGame/', views.ImageTileGame,name='ImageTileGame'),
    # path('shuffel/', views.shuffel,name='shuffel'),
    path('puzzle/', views.puzzle,name='puzzle'),
    path('number/', views.number,name='number'),
    path('faq/', views.faq,name='faq'),
    path('replay_loop/', views.replay_loop,name='replay_loop'),
    path('replay_loop/', views.replay_loop,name='replay_loop'),
    # path('comment/', views.comment,name='comment'),
    # path('reply/<pk>', views.replay,name='replay'),
    path("update_game_count/", views.update_game_count, name="update_game_count"),
    path('gameResult/', views.game_result, name='game_result'),
    path("blogs/", views.blog_view, name="blogview"),
    path("imagepuzzlegame_gameresult/", views.imagepuzzlegame_gameresult, name="imagepuzzlegame_gameresult"),
    path("imagetile_gameresult/", views.imagetile_gameresult, name="imagetile_gameresult"),
    path("animalgame_gameresult/", views.animalgame_gameresult, name="animalgame_gameresult"),
    path("get_game_stats/", views.get_game_stats, name="get_game_stats"),
    path('update-post/', views.update_post, name='update-post'),
    path('update-comment/', views.update_comment, name='update_comment'),
    path('update_comment_replay/', views.update_comment_replay, name='update_comment_replay'),
    path('get-user-game-data/<int:user_id>/', views.get_user_game_stats, name='get_user_game_data'),
    path('update-doctor/', views.doctorview, name='doctorview'),

    path('start_gaze/', views.start_gaze, name='start_gaze'),
    path('stop_gaze/', views.stop_gaze, name='stop_gaze'),
    path('deletecmt/<pk>', views.deletecmt, name='deletecmt'),
    path('feedtest/', views.feedtest, name='feedtest'),
    path('data_feedback/', views.data_feedback, name='data_feedback'),


    path('verifing/<pk>', views.verifing, name='verifing'),
    path('verifingimage/<pk>', views.verifingimage, name='verifingimage'),
    path('verifingnumber/<pk>', views.verifingnumber, name='verifingnumber'),
    path('verifingident/<pk>', views.verifingident, name='verifingident'),
    path('disverifing/<pk>', views.disverifing, name='disverifing'),
    path('disverifingimage/<pk>', views.disverifingimage, name='disverifingimage'),
    path('disverifingident/<pk>', views.disverifingident, name='disverifingident'),
    path('disverifingnumber/<pk>', views.disverifingnumber, name='disverifingnumber'),
    path('videosection', views.videosection, name='videosection'),


    path('updatedata/', views.updatedata, name='updatedata'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)