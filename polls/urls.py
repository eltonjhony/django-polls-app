from django.conf.urls import url
from views.dashboard import DashboardController
from views.question_details import QuestionDetailsController
from views.question_results import QuestionResultController
from views.voting import VotingController

app_name = 'polls'
urlpatterns = [
    
    # ex: /polls/
    url(r'^$', DashboardController.index, name='dashboard'),
    
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', QuestionDetailsController.show, name='detail'),
    
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', QuestionResultController.show, name='results'),
    
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', VotingController.vote, name='vote'),
]