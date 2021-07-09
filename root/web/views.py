from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .constants import *
from . import models

def index(request):
    content = {
        'title' : 'TENIS',
    }
    return render(request, 'web/index.html', content)

def user_login(request):
    content = {
        'title' : 'Login',
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        content['user'] = user
        if user:
            login(request, user)
            return HttpResponseRedirect('/settings')
        else:
            content = {
                'error':'Invalid login'
            }
            return render(request, 'web/login.html', content)
    
    return render(request, 'web/login.html', content)

def user_settings(request):
    user = request.user
    profile = None
    try:
        profile = models.UserProfile.objects.get(user=user)
    except:
        profile = models.UserProfile(user=user, participating=False)
        profile.save()

    content = {
        'title':'Settings',
        'is_participating':False,
    }
    
    if request.method=='POST':
        is_participating = bool(request.POST.get('is_Participating'))
    
        if is_participating != profile.participating:
            profile.participating = is_participating
            profile.save(update_fields=['participating'])
        
    if profile.participating:
        content['is_participating'] = True
            
    return render(request, 'web/settings.html', content)

def match(request):
    content = {
        'title':'Match',
    }
    tmp = models.UserProfile.objects.all()
    profiles = []
    for i in tmp:
        if i.participating:
            profiles.append(i)
    
    n = len(profiles)
    half = n//2
    
    if n != NUM_USERS_ALLOWED_AT_TURNAMENT:
        content['error'] = True
        return render(request, 'web/match.html', content)
    
    matches = []
    for i in range(n-1):
        matches.append([])
    
    first = profiles[0].user.username
    profiles = profiles[1::]
    for d in range(n-1):

        matches[d].append((first, profiles[d].user.username))
        
        for i in range(1,half):
            a = (d+i)%(n-1)
            b = (d-i+(n-1))%(n-1)
        
            a = profiles[a].user.username
            b = profiles[b].user.username
        
            matches[d].append((a,b))
    
    content['matches'] = matches
    print(matches[0])
    return render(request, 'web/match.html', content)
        