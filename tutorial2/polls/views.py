from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Question, Choice                                  
from django.http import Http404

cheat_code = '4d4eadbb '
def index(request):
    latest_question_list =  Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html',{
        'latest_question_list': latest_question_list,
        'cheat_code':cheat_code})
# Create your views here.
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist')
#     return render(request,'polls/detail.html',{
#         'question': question,
#         'cheat_code':cheat_code})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{
        'question': question,
        'cheat_code':cheat_code})

def results(request,question_id):
    response="You are looking at the results of question %s." 
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s." % question_id)

def owner(request):
    return HttpResponse('Hello, world. 4d4eadbb is the polls index.')