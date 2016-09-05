from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import question, choice
# Create your views here.

def index(request):
    return HttpResponse("Hiii, pollingsite welcomes you")

def detail(request,ques_id):
    try:
        ques = question.objects.get(pk=ques_id)
    except question.DoesNotExist:
        raise Http404("question Does not exist")
    return render(request, 'polls/details.html',{'ques':ques})

def results(request, ques_id):
    try:
        ques = question.objects.get(pk=ques_id)
    except question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request, "polls/results.html", {"ques":ques})

def vote(request, ques_id):
    try:
        ques = question.objects.get(pk=ques_id)
    except question.DoesNotExist:
        raise Http404("Question Does not exist")
    try:
        select_choice = ques.choice_set.get(pk = request.POST['choic'])
    except (KeyError, choice.DoesNotExist):
        return render(request, 'polls/details.html', {'ques':ques, 'error_message':'you did not select a choice'})

    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('results', args=(ques.id,)))

def indexing(request):
    latest_ques_list=question.objects.order_by('-pub_date')[:5]
    context = {'latest_ques_list': latest_ques_list}
    return render(request, 'polls/index.html', context)