# hotel_app/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Blog, Feedback, Anketa, Comment
from app.forms import FeedbackForm, AnketaForm, CommentForm, BootstrapAuthenticationForm, BlogForm
from datetime import datetime

class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Testing_User", password="12345nfo23i@#f3")
        self.blog = Blog.objects.create(
            title="Тестовый заголовок",
            description="краткий текст поста",
            content="тут текст всего поста, текст текст тут текст",
            posted=datetime.now(),
            author=self.user,
            image="test.jpg"
        )

    

    def test_blog_meta(self):
        self.assertEqual(self.blog._meta.db_table, "Posts")
        self.assertEqual(self.blog._meta.verbose_name, "статья блога")
        self.assertEqual(self.blog._meta.verbose_name_plural, "статьи блога")

class FeedbackModelTest(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(
            name="Testing_User",
            email="aleksej.75144@hotmail.com",
            message="Тут пишу тестовое сообщение",
            agree_to_news=True
        )

    def test_feedback_creation(self):
        self.assertTrue(isinstance(self.feedback, Feedback))
        self.assertEqual(self.feedback.__str__(), self.feedback.name)

class AnketaModelTest(TestCase):
    def setUp(self):
        self.anketa = Anketa.objects.create(
            second_name="Дмитриев",
            first_name="Алексей",
            reservation='5',
            city="Псков",
            job="Студент",
            work='5',
            back='1',
            email="aleksej.75144@hotmail.com",
            message="Тут пишу сообщение",
            notice=True
        )

    def test_anketa_creation(self):
        self.assertTrue(isinstance(self.anketa, Anketa))
        self.assertEqual(self.anketa.__str__(), f'{self.anketa.first_name} {self.anketa.second_name}')

    def test_anketa_meta(self):
        self.assertEqual(self.anketa._meta.verbose_name, "Анкета")
        self.assertEqual(self.anketa._meta.verbose_name_plural, "Анкеты")

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="commentuser", password="12345")
        self.blog = Blog.objects.create(
            title="Комментарий для статьи блога",
            description="Сокращенный текст",
            content="Весь текст комментария тут",
            posted=datetime.now(),
            author=self.user,
            image="comment.jpg"
        )
        self.comment = Comment.objects.create(
            text="Test comment",
            date=datetime.now(),
            author=self.user,
            post=self.blog
        )

    def test_comment_creation(self):
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertEqual(self.comment.__str__(), f'Комментарий {self.comment.id} {self.comment.author} k {self.comment.post}')

    def test_comment_meta(self):
        self.assertEqual(self.comment._meta.db_table, "Comment")
        self.assertEqual(self.comment._meta.verbose_name, "Комментарии к статье блога")
        self.assertEqual(self.comment._meta.verbose_name_plural, "Комментарии к статье блога")

