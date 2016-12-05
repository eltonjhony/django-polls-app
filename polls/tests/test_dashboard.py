import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from polls.models import Question

def create_question(question_text, days):
        """
        Creates a question with the given `question_text` and published the
        given number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

class DashboardControllerTest(TestCase):

    def test_dashboard_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['dashboardVOs'], [])

    def test_dashboard_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        dashboard page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:dashboard"))
        self.assertQuerysetEqual(
            response.context['dashboardVOs'], ['<Question: Past question.>']
        )

    def test_dashboard_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the dashboard page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:dashboard"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['dashboardVOs'], [])

    def test_dashboard_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:dashboard"))
        self.assertQuerysetEqual(
            response.context['dashboardVOs'], ['<Question: Past question.>']
        )

    def test_dashboard_with_more_than_one_past_questions(self):
        """
        The questions dashboard page may display multiple questions.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Past question again.", days=-20)
        response = self.client.get(reverse("polls:dashboard"))
        self.assertQuerysetEqual(
            response.context['dashboardVOs'], 
                ['<Question: Past question again.>', 
                '<Question: Past question.>']
        )