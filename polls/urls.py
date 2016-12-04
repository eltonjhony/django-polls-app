from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', dashboard.index, name='dashboard'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', dashboard.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', dashboard.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', dashboard.vote, name='vote'),
]