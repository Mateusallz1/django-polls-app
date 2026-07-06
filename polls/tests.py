from django.test import TestCase
from django.urls import reverse
from .models import Question, Choice
import datetime
from django.utils import timezone

class VoteViewTests(TestCase):
    def setUp(self):
        self.q = Question.objects.create(question_text="Q?", pub_date=timezone.now())
        self.c = Choice.objects.create(question=self.q, choice_text="A", votes=0)

    def test_vote_valid_choice_redirects_to_results(self):
        resp = self.client.post(reverse('polls:vote', args=(self.q.id,)), {'choice': self.c.id})
        self.assertRedirects(resp, reverse('polls:results', args=(self.q.id,)))
        self.c.refresh_from_db()
        self.assertEqual(self.c.votes, 1)

    def test_vote_no_choice_shows_error(self):
        resp = self.client.post(reverse('polls:vote', args=(self.q.id,)), {})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "You MUST select a choice.")