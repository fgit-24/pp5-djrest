from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article
from django.utils import timezone

class ArticleModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.article = Article.objects.create(
            title='Test Article',
            description='A description for the test article',
            slug='test-article',
            author=self.user
        )
    
    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test Article')
    
    def test_article_fields(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.description, 'A description for the test article')
        self.assertEqual(self.article.slug, 'test-article')
        self.assertEqual(self.article.author, self.user)
        self.assertTrue(isinstance(self.article.published, timezone.datetime))
