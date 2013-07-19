# Create your views here.
from .models import Container, Linker
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from utils.createXml import createXmlTree
from utils.decorators import ajaxWrapper
#from django.contrib.auth.forms import AuthenticationForm

def home(request):
    '''
    show the index page of this website depending on whether the user is logged in or not
    '''
    user = request.user
    if user.is_authenticated():
        container_list = user.container_set.order_by('id')
        return render(request, 'linker/home.html', {'container_list': container_list})
    return render(request, 'linker/home.html')


@login_required(login_url = '/')
@csrf_exempt
@ajaxWrapper('container', 'link', 'tip', 'name')
def ajaxAddUrl(request):
    '''
    use ajax to respond to user's adding new bookmarks' request
    '''
    to_return = {'result': 'failed'}
    if request.method == 'POST':
        post = request.POST.copy()
        user = request.user
        try:
            newContainer = Container.objects.get(name=post['container'])
        except:
            newContainer = Container(user=user, name=post['container'])
            newContainer.save()
             
        post['link'] = post['link'].strip('/')
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
                newLinker.opinion = post['tip']
                newLinker.save()
                to_return['result'] = 'success'
    
    return to_return


@login_required(login_url = '/')
@csrf_exempt
@ajaxWrapper('link_container', 'link_url')
def ajaxDelUrl(request):
    '''
    use ajax to respond to user's deleting old bookmarks' request. 
    Be cautious: data is not actually deleted from database, I just mark it as "deleted" using one field 
    '''
    to_return = {'result': 'failed'}
    if request.method == 'POST':
        post = request.POST.copy()
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
    
    return to_return

@login_required(login_url = '/')
@csrf_exempt
@ajaxWrapper('term')
def autoComplete(request):
    '''
    jquery-ui's auto-complete function which must return JSON
    '''
    to_return = {}
    if request.method == 'GET':
        term = request.GET['term']
        containers = Container.objects.filter(name__startswith=term).distinct()
        count = 0
        for one in containers:
            count += 1
            to_return["choice"+str(count)] = one.name
    return to_return


                
@login_required(login_url = '/')
def downloadXml(request):
    '''
    create an xml file containing user's all data and make downloadable for users
    '''         

    xmlstr = createXmlTree(request.user)
    response = HttpResponse(xmlstr,mimetype='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' %  request.user.username + '.xml'
    
    return response
    

@login_required(login_url = '/')
@csrf_exempt
@ajaxWrapper('container', 'link', 'tips')
def ajaxUpdateTips(request):
    '''
    update user's urls' opinion
    '''
    
    to_return = {'result': 'failed'}
    if request.method == 'POST':
        post = request.POST.copy()
        try:
            container = request.user.container_set.get(name=post['container'])
            link = container.linker_set.get(link=post['link'])
        except:
            pass
        else:
            link.opinion = post['tips']
            link.save()
            to_return['result'] = 'success'
            
    return to_return


@login_required(login_url = '/')
@csrf_exempt
@ajaxWrapper('container', 'link', 'votes')
def ajaxUpdateVotes(request):
    '''
    update user's urls' votes
    '''
    
    to_return = {'result': 'failed'}
    if request.method == 'POST':
        post = request.POST.copy()
        try:
            container = request.user.container_set.get(name=post['container'])
            link = container.linker_set.get(link=post['link'])
        except:
            pass
        else:
            link.votes = post['votes'].strip()
            link.save()
            to_return['result'] = 'success'            
    return to_return
    
    
    
    
    
    
    
    
    
    
    
    
    
