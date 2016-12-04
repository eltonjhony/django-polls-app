from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from polls.views.utils.context_utils import ContextUtils
from polls.views.utils.loader_utils import Template
from polls.models import Question

class QuestionDetailsController(object):

    @staticmethod
    def show(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return HttpResponse(Template.DETAILS.render(
            ContextUtils.put_context(question=question), 
            request))



