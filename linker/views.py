# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from .models import Container, Linker

def home(request):
    user = request.user
    if user.is_authenticated():
        container_list = user.container_set.all()
        return render(request, 'linker/index.html', {'container_list': container_list})
    return render(request, 'linker/index.html')

@login_required(login_url = '/')
@csrf_exempt
def ajaxAddUrl(request):
    to_return = {'result': 'failed'}
    if request.method == 'POST':
        post = request.POST.copy()
        if 'container' in post and 'link' in post and \
        'tip' in post and 'name' in post:
            user = request.user
            try:
                newContainer = Container.objects.get(name=post['container'])
            except:
                newContainer = Container(user=user, name=post['container'])
                newContainer.save()
            if not post['link'].startswith("http"): #http://www.ifeng.com/
                post['link'] = 'http://' + post['link']
            try:
                newLinker = Linker.objects.get(link=post['link'])
            except:
                newLinker = Linker(container=newContainer, name=post['name'], 
                                   link=post['link'], opinion=post['tip'],
                                   date = datetime.now())
                newLinker.save()
                to_return['result'] = 'success'
            else:
                if newLinker.deleted == True:
                    newLinker.deleted = False
                    newLinker.save()
                    to_return['result'] = 'success'
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")

@login_required(login_url = '/')
@csrf_exempt
def ajaxDelUrl(request):
    to_return = {'result': 'failed'}
    if request.method == 'POST':
        post = request.POST.copy()
        if 'link_url' in post and 'link_container' in post:
            user = request.user
            try:
                container = user.container_set.get(name=post['link_container'])
                link = container.linker_set.get(link=post['link_url'])
            except:
                pass
            else:
                link.deleted = True
                link.save()
                to_return['result'] = 'success'
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")

@login_required(login_url = '/')
@csrf_exempt
def autoComplete(request):
    to_return = {}
    if request.method == 'GET':
        if 'term' in request.GET:
            term = request.GET['term']
            containers = Container.objects.filter(name__startswith=term)
            count = 0
            for one in containers:
                count += 1
                to_return["choice"+str(count)] = one.name
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")
                
            