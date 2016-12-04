from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from polls.views.utils.context_utils import ContextUtils
from polls.views.utils.loader_utils import Template
from polls.models import Question

class DashboardController(object):
    
    @staticmethod
    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')
        return HttpResponse(Template.DASHBOARD.render(
            ContextUtils.put_context(dashboardVOs=latest_question_list), 
            request))



