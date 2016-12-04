from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from polls.views.utils.context_utils import ContextUtils
from polls.views.utils.loader_utils import Template
from polls.models import Question, Choice

class VotingController(object):

    @staticmethod
    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, NameError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return HttpResponse(Template.DETAILS.render(
                ContextUtils.put_context(question=question, error_message="You didn't select a choice"), 
                request))
        else:
            selected_choice.votes +=1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



