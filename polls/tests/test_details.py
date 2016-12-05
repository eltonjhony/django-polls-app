from django.test import TestCase
from django.urls import reverse

from polls.models import Question
from tests_utils import TestsUtils

class QuestionDetailsControllerTests(TestCase):

    def test_details_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = TestsUtils.create_question(question_text="Future question", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)