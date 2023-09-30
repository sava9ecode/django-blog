import datetime as dt

from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Blog, BlogAuthor, BlogComment


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create(username="testuser", password="12345")
        test_user1.save()
        blog_author = BlogAuthor.objects.create(
            user=test_user1,
            bio="Test bio",
        )
        Blog.objects.create(
            name="Test Blog 1",
            author=blog_author,
            description="Test Blog 1 Description",
        )

    def test_name_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field("name").max_length
        self.assertEqual(max_length, 200)

    def test_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_description_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_description_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field("description").max_length
        self.assertEqual(max_length, 2000)

    def test_description_help_text(self):
        blog = Blog.objects.get(id=1)
        help_text = blog._meta.get_field("description").help_text
        self.assertEqual(help_text, "Enter your blog text here.")

    def test_post_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("post_date").verbose_name
        self.assertEqual(field_label, "post date")

    def test_date(self):
        blog = Blog.objects.get(id=1)
        the_date = blog.post_date
        self.assertEqual(the_date, dt.date.today())

    def test_object_name(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = blog.name
        self.assertEqual(expected_object_name, str(blog))

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.get_absolute_url(), "/blog/blog/1")


class BlogCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create(username="testuser1", password="12345")
        test_user1.save()
        test_user2 = User.objects.create(username="testuser2", password="12345")
        test_user2.save()
        blog_author = BlogAuthor.objects.create(
            user=test_user1,
            bio="testbio",
        )
        blog_author.save()
        blog_test = Blog.objects.create(
            name="Test Blog 1",
            author=blog_author,
            description="Test Blog 1 Description",
        )
        BlogComment.objects.create(
            description="Test Blog 1 Comment 1 Description",
            author=test_user1,
            blog=blog_test,
        )

    def test_description_label(self):
        comment = BlogComment.objects.get(id=1)
        field_label = comment._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_description_max_length(self):
        comment = BlogComment.objects.get(id=1)
        max_length = comment._meta.get_field("description").max_length
        self.assertEqual(max_length, 1000)

    def test_description_help_text(self):
        comment = BlogComment.objects.get(id=1)
        help_text = comment._meta.get_field("description").help_text
        self.assertEqual(help_text, "Enter comment about the blog here.")

    def test_author_label(self):
        comment = BlogComment.objects.get(id=1)
        field_label = comment._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_post_date_label(self):
        comment = BlogComment.objects.get(id=1)
        field_label = comment._meta.get_field("post_date").verbose_name
        self.assertEqual(field_label, "post date")

    def test_blog_label(self):
        comment = BlogComment.objects.get(id=1)
        field_label = comment._meta.get_field("blog").verbose_name
        self.assertEqual(field_label, "blog")

    def test_object_name(self):
        comment = BlogComment.objects.get(id=1)
        self.assertEqual(
            str(comment),
            f"{comment.description[:75]}..."
            if len(comment.description) > 75
            else comment.description[:75],
        )


class BlogAuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create(username="testuser", password="12345")
        test_user1.save()
        BlogAuthor.objects.create(user=test_user1, bio="This is a bio")

    def test_user_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_bio_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field("bio").verbose_name
        self.assertEqual(field_label, "bio")

    def test_max_length_label(self):
        author = BlogAuthor.objects.get(id=1)
        max_length = author._meta.get_field("bio").max_length
        self.assertEqual(max_length, 400)

    def test_help_text_label(self):
        author = BlogAuthor.objects.get(id=1)
        help_text = author._meta.get_field("bio").help_text
        self.assertEqual(help_text, "Enter your bio details here.")

    def test_object_name(self):
        author = BlogAuthor.objects.get(id=1)
        expected_object_name = author.user.username
        self.assertEqual(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = BlogAuthor.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), "/blog/blogger/1")
