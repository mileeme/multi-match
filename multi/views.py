from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView


from .models import Candidate, Question, Response

def index(request):
  candidate_list = Candidate.objects.all()
  question_list = Question.objects.all().order_by('number')
  response_list = Response.objects.all().order_by('response')
  description_list = Question.objects.all().order_by('description')
  template_name = 'multi/index.html'
  context = {
    'candidate_list': candidate_list,
    'question_list': question_list,
    'response_list': response_list,
    }
  return render(request, template_name, context)




