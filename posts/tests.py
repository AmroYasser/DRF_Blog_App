from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        # create user
        test_user1 = User.objects.create_user(
            username="testuser1",
            password="abc123",
        )
        test_user1.save()

        # create blog post
        test_post = Post.objects.create(
            author=test_user1, title="post title", body="body content..."
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "testuser1")
        self.assertEqual(title, "post title")
        self.assertEqual(body, "body content...")
