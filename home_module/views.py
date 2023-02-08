import queue

from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from .models import User, Post
from django.urls import reverse
from .linkedlistCode import LinkedList
from collections import deque


# used data strucrures : list - linkedlist - dictionary(map) - queue


# Create your views here.

def login_page(request):
    response = 'null'
    if request.method == 'POST':
        try:
            user_form = UserForm(request.POST)
            if user_form.is_valid():

                new_user = User(first_name=user_form.cleaned_data['first_name'],
                                last_name=user_form.cleaned_data['last_name'],
                                username=user_form.cleaned_data['username'],
                                email=user_form.cleaned_data['email'],
                                password=user_form.cleaned_data['password'])

                try:
                    new_user.save()
                    response = 'signed_in'

                except:
                    response = 'used_username'

                return render(request, 'home_module/signup.html', {'user_form': UserForm,
                                                                   'response': response,
                                                                   'login_form': LoginForm})
        except:
            pass

        try:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                try:
                    user_loged_in = User.objects.all().get(username=username, password=password)
                    return redirect(reverse('home_page', args=[user_loged_in.username]))
                except:
                    response = 'invalid_user_pass'
        except:
            pass

    context = {'user_form': UserForm,
               'login_form': LoginForm,
               'response': response}

    return render(request, 'home_module/signup.html', context=context)


# queue
def home_page(request, username_loged_in):
    if request.method == 'POST':

        text = request.POST['text']
        try:
            image = request.FILES['image']
        except:
            image = None
        author_username = request.POST['author_username']
        author_profile_picture_address = request.POST['author_profile_picture_address']
        user = User.objects.get(username=username_loged_in)
        post = Post(text=text, image=image, author=user)
        post.save()
    else:
        pass

    posts = []
    user = User.objects.get(username=username_loged_in)
    self_posts = Post.objects.filter(author__username=username_loged_in)
    posts.extend(self_posts)
    for username in User.objects.all().get(username=username_loged_in).followings_usernames.split(','):
        try:
            user = User.objects.get(username=username)
            user_posts = Post.objects.filter(author__username=username)
            posts.extend(user_posts)
        except:
            print(username)

    user_loged_in = User.objects.get(username=username_loged_in)

    return render(request, 'home_module/home_page.html', context={
        'user_loged_in': user_loged_in,
        'suggestion_pages': suggestion_usernames(username_loged_in),
        'posts': posts

    })


def profile_page(request, username, username_loged_in):
    followed = False
    user = User.objects.all().get(username=username)
    user_loged_in = User.objects.get(username=username_loged_in)
    if str(user_loged_in.username) in user.followers_usernames.split(','):
        followed = True
    posts = Post.objects.all().filter(author__username=username).order_by('-created_time')
    self_profile = False
    if user.username == user_loged_in.username: self_profile = True
    context = {'user': user,
               'user_loged_in': user_loged_in,
               'followed': followed,
               'posts': posts,
               'self_profile': self_profile,
               }
    print(followed)
    return render(request, 'home_module/profile_page.html', context=context)


# linkedlist
def followers_page(request, username, username_loged_in):
    user = User.objects.all().get(username=username)
    user_loged_in = User.objects.get(username=username_loged_in)

    followed = False
    if str(user_loged_in.username) in user.followers_usernames.split(','):
        followed = True

    followers = LinkedList()
    followers_usernames = User.objects.all().get(username=username).followers_usernames.split(',')
    for username in followers_usernames:
        try:
            followers.add_last(User.objects.all().get(username=username))
        except:
            pass
    self_profile = False
    if user.username == user_loged_in.username: self_profile = True
    context = {'user': user,
               'user_loged_in': User.objects.all().get(username=username_loged_in),
               'followed': followed,
               'followers': followers,
               'self_profile': self_profile}

    return render(request, 'home_module/followers_page.html', context=context)


# linkedlist
def followings_page(request, username, username_loged_in):
    followed = False
    user = User.objects.all().get(username=username)
    user_loged_in = User.objects.get(username=username_loged_in)
    if str(user_loged_in.username) in user.followers_usernames.split(','):
        followed = True

    followings = LinkedList()
    followings_usernames = User.objects.all().get(username=username).followings_usernames.split(',')
    for username in followings_usernames:
        try:
            followings.add_last(User.objects.all().get(username=username))
        except:
            pass
    self_profile = False
    if user.username == user_loged_in.username: self_profile = True

    context = {'user': user,
               'user_loged_in': User.objects.all().get(username=username_loged_in),
               'followed': followed,
               'followings': followings,
               'self_profile': self_profile}

    return render(request, 'home_module/followings_page.html', context=context)


def edit_profile(request, username):
    user = User.objects.all().get(username=username)
    context = {'user': user,
               'user_loged_in': user,
               'is_edited': None}

    if request.method == 'POST':
        try:
            print(request.POST['delete_account'])
            followings = user.followings_usernames.split(',')
            for username in followings:
                try:
                    user_following = User.objects.all().get(username=username)
                    remove_list = user_following.followers_usernames.split(',')
                    remove_list.remove(user.username)
                    user_following.followers_usernames = ",".join(remove_list)
                    user_following.save()
                except:
                    print("Exception")

            posts = Post.objects.all().filter(author_username=user.username)
            for post in posts:
                print('hey')
                post.delete()
            user.delete()
            return redirect('login_page')
            # for post in Post
        except:
            pass
        try:
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            # user.username = request.POST['username']
            user.password = request.POST['password']
            user.email = request.POST['email']
            user.bio = request.POST['bio']
            user.location = request.POST['location']
            try:
                user.profile_picture = request.FILES['image']
            except:
                pass
            try:
                user.cover_picture = request.FILES['banner']
            except:
                pass
            user.save()
            context['is_edited'] = True

        except:
            context['is_edited'] = False

    return render(request, 'home_module/edit_profile.html', context)


def follow(request, username, username_loged_in):
    user = User.objects.get(username=username)
    user_loged_in = User.objects.get(username=username_loged_in)
    user.followers_usernames += f'{user_loged_in.username},'
    user_loged_in.followings_usernames += f'{user.username},'
    user.save()
    user_loged_in.save()
    return redirect('profile_page', username=username, username_loged_in=username_loged_in, )


def unfollow(request, username, username_loged_in):
    user = User.objects.get(username=username)
    user_loged_in = User.objects.get(username=username_loged_in)

    followings = user_loged_in.followings_usernames.split(',')
    followings.remove(username)
    followings = ','.join(followings)
    user_loged_in.followings_usernames = followings
    user_loged_in.save()

    followers = user.followers_usernames.split(',')
    followers.remove(username_loged_in)
    followers = ','.join(followers)
    user.followers_usernames = followers
    user.save()
    return redirect('profile_page', username=username, username_loged_in=username_loged_in, )


def delete_post(request, post_id, username_loged_in):
    post = Post.objects.all().get(id=post_id)
    post.delete()
    return redirect('home_page', username_loged_in=username_loged_in)


def all_users(request, username_loged_in):
    context = {
        'user_loged_in': User.objects.all().get(username=username_loged_in),
        'followings': User.objects.all(),
    }

    return render(request, 'home_module/all_users.html', context=context)


def suggestion_usernames(username):
    if len(User.objects.all().get(username=username).followings_usernames.split(',')) <= 2:

        if len(User.objects.all()) < 6:
            return User.objects.all()
        else:
            sg = User.objects.all()
            sg.reverse()
            sg = list(sg)
            return sg[-7:-1]
    #     ---------------------
    user = User.objects.all().get(username=username)
    user_followings = User.objects.all().get(username=username).followings_usernames.split(',')

    graph_followings = {}
    for user in User.objects.all():
        graph_followings[user.username] = user.followings_usernames.split(',')

    graph_commons = {}

    for user in User.objects.all():
        all = graph_followings[user.username]
        all.extend(user_followings)

        count_common = (len(all) - len(set(all)))

        try:
            graph_commons[user.username] = round(count_common / len(all), 4)
        except:
            print("error")

    graph_commons_reverse = {}
    graph_commons_keys_sorted = list(graph_commons.values())
    graph_commons_keys_sorted.sort()
    for key in graph_commons.keys():
        graph_commons_reverse[graph_commons[key]] = key
    #
    # graph_commons
    # graph_commons_reverse
    gs_keys = list(graph_commons_reverse.keys())
    gs_keys.sort()
    suggest = []
    try:

        for x in range(5):

            key = gs_keys[x]
            username = graph_commons_reverse[key]
            suggest.append(User.objects.all().get(username=username))
    except:
        pass
    return suggest
