from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Blog, Feedback, Anketa, Comment
from app.forms import FeedbackForm, AnketaForm, CommentForm, BootstrapAuthenticationForm, BlogForm
from datetime import datetime

class FeedbackFormTest(TestCase):
    def test_feedback_form_valid(self):
        form = FeedbackForm(data={
            'name': "Test User",
            'email': "test@example.com",
            'message': "Test message",
            'agree_to_news': True
        })
        self.assertTrue(form.is_valid())

    def test_feedback_form_invalid(self):
        form = FeedbackForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Name, email and message are required

class AnketaFormTest(TestCase):
    def test_anketa_form_valid(self):
        form = AnketaForm(data={
            'second_name': "Дмитриев",
            'first_name': "Алексей",
            'reservation': '5',
            'city': "Псков",
            'job': "Студент",
            'work': '5',
            'back': '1',
            'email': "aleksej.75144@hotmail.com",
            'message': "Test feedback",
            'notice': True
        })
        self.assertTrue(form.is_valid())

    def test_anketa_form_invalid(self):
        form = AnketaForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 9)  # All fields are required

class CommentFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="commentuser", password="12345")
        self.blog = Blog.objects.create(
            title="Comment Blog",
            description="Short description",
            content="Full content",
            posted=datetime.now(),
            author=self.user,
            image="comment.jpg"
        )

    def test_comment_form_valid(self):
        form = CommentForm(data={'text': "Test comment"})
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Text is required


class BootstrapAuthenticationFormTest(TestCase):
    def test_authentication_form_valid(self):
        form = BootstrapAuthenticationForm(data={
            'username': "Testing_User",
            'password': "G6Hdj+zfh!"
        })
        self.assertFalse(form.is_valid())

    def test_authentication_form_invalid(self):
        form = BootstrapAuthenticationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # Username and password are required

class BlogFormTest(TestCase):
    def test_blog_form_valid(self):
        form = BlogForm(data={
            'title': "Test Blog",
            'description': "Short description",
            'content': "Full content",
            'image': "test.jpg"
        })
        self.assertTrue(form.is_valid())

    def test_blog_form_invalid(self):
        form = BlogForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Title, description, and content are required