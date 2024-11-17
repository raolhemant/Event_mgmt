from django.test import TestCase
from feedback.models import Feedback
# Create your tests here.
class Feedback_TestCase(TestCase):
    def setUp(self):
        self.model = Feedback.objects.create(rating = '5')
        self.model = Feedback.objects.create(comment = 'nice')
        self.model = Feedback.objects.create()
        self.model = Feedback.objects.create(submitted_at = '')

    def test_model_rating(self):
        self.assertEqual(self.model.rating , '5')