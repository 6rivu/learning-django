from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist():
            raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def result(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)