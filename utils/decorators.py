'''
Created on 2013-7-19

@author: siwei
'''

from django.http.response import HttpResponse
from django.utils import simplejson
import functools

def ajaxWrapper(*args):
    '''
        wrap ajax reply views 
        args: parameters that are the keys in the dictionary data to validate the json data from the client
    '''
    def my_decorator(func):

        @functools.wraps(func)
        def wrapper(request):
            if request.method == 'POST':
                data = request.POST.copy
            else:
                data = request.GET.copy
            temp = (lambda x: True if x in data else False for x in args)
            if any(temp):
                to_return = func(request)
            else:
                to_return = {'result': "failed"}
            serialized = simplejson.dumps(to_return)
            return HttpResponse(serialized, mimetype="application/json")
                
        return wrapper
    return my_decorator
    
    
if __name__ == '__main__':
    pass