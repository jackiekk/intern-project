from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
# Create your views here.



class IndexView(generic.ListView):
    template_name = 'data/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'data/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'data/results.html'


def vote(request, question_id):
    model = Question
    template_name = 'data/results.html'
