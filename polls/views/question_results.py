from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from polls.views.utils.context_utils import ContextUtils
from polls.views.utils.loader_utils import Template
from polls.models import Question

class QuestionResultController:
    
    @staticmethod
    def show(request, question_id):
        return HttpResponse(Template.RESULT.render(request))



