# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from models import Container, Linker

def home(request):
    return render(request, 'linker/index.html')

@login_required(login_url = '/')
@csrf_exempt
def ajaxAddUrl(request):
    to_return = {'result': 'failed'}
    if request.method == 'POST':
        post = request.POST.copy()
        if post.has_key('container') and post.has_key('link') and \
        post.has_key('tip') and post.has_key('name'):
            user = request.user
            try:
                newContainer = Container.objects.get(name=post['container'])
            except:
                newContainer = Container(user=user, name=post['container'])
                newContainer.save()
            try:
                newLinker = Linker.objects.get(link=post['link'])
            except:
                newLinker = Linker(container=newContainer, name=post['name'], 
                                   link=post['link'], opinion=post['tip'],
                                   date = datetime.now())
                newLinker.save()
                to_return['result'] = 'success'
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")
            
