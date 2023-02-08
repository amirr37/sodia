from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('home/<str:username_loged_in>', views.home_page, name='home_page'),
    path('profile/<str:username>/<str:username_loged_in>', views.profile_page, name='profile_page'),
    path('profile/<str:username>/followers/<str:username_loged_in>', views.followers_page,
         name='followers_page'),
    path('profile/<str:username>/followings/<str:username_loged_in>', views.followings_page,
         name='followings_page'),
    path('edit-profile/<str:username>', views.edit_profile, name='edit_profile_page'),
    path('follow-url/<username>/<username_loged_in>', views.follow, name='follow'),
    path('unfollow-url/<username>/<username_loged_in>', views.unfollow, name='unfollow'),
    path('delete-post/<int:post_id>/<username_loged_in>' , views.delete_post, name='delete_post'),
    path('all_users/<username_loged_in>' , views.all_users , name='all_users')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, )
