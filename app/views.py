from django.shortcuts import render

from app.form import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def topic(request):
    ETFO = TopicForm()
    d = {'ETFO': ETFO}

    if request.method =='POST':
        TFDO = TopicForm(request.POST)

        if TFDO.is_valid():
            topic_name = TFDO.cleaned_data['topic_name']

            LTO = Topic.objects.get_or_create(topic_name = topic_name)

            if LTO[1]:
                return HttpResponse('New topic is created')
            else:
                return HttpResponse('Tpoic is already present')
            
        else:
            return HttpResponse('Data is not valid')  
    return render (request, 'topicForm.html', d)



def webpage(request):

    EWFO = WebpageForm()

    d = {'EWFO' : EWFO}

    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)

        if WFDO.is_valid():
            topic_name = WFDO.cleaned_data['topic_name']
            name = WFDO.cleaned_data['name']
            url = WFDO.cleaned_data['url']
            email = WFDO.cleaned_data['email']

            LWO = Webpage.objects.get_or_create(topic_name=topic_name, name = name, urls = url, email = email)

            if LWO[1]:
                return HttpResponse('New web form is created')
            else:
                return HttpResponse('Web form is already present')
        else:
            return HttpResponse('Data is not valid')

    return render(request, 'web.html', d)