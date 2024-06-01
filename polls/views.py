from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question

def detail(request, question_id):
    if(question_id ==1):
        return HttpResponse("Event 1")
    elif (question_id ==2):
        return HttpResponse("Event page 2")
    return HttpResponse("You are looking at events page" % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)