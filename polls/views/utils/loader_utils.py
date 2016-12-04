from django.template import loader

class Template:
    DASHBOARD = loader.get_template('polls/dashboard.html')
    DETAILS = loader.get_template('polls/details.html')
    RESULT = loader.get_template('polls/result.html')