from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . import models
# Create your views here.

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
            print(username, password)
            #content['title'] = 'Settings'
            return HttpResponseRedirect('/settings')
            #return redirect('settings.html', )
        else:
            content = {
                'error':'Invalid login'
            }
            return render(request, 'web/login.html', content)
    return render(request, 'web/login.html', content)

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse(index))

#@login_required
def user_settings(request):
    user = request.user
    profile = models.UserProfile.objects.get(user=user)
    
    content = {
        'title':'Settings',
        'checked':'',
    }
    
    if request.method=='POST':
        flag = request.POST.get('checkbox')
        if flag:
            profile.participating = True
        else:
            profile.participating = False
        profile.save()

    if profile.participating:
        content['checked'] = 'checked'
            
    return render(request, 'web/settings.html', content)

def match(request):
    content = {
        'title':'Match',
    }
    tmp = list(models.UserProfile.objects.all())
    profiles = []
    for i in tmp:
        if i.participating:
            profiles.append(i)
    
    n = len(profiles)
    half = n//2
    
    if n != 4: #change to whatever number
        content['error'] = 'Wrong number of participantes'
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
        