from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth.models import User

from blog.models import Blog, BlogAuthor


class IndexViewTest(SimpleTestCase):
    def test_view_exists_at_desired_location(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create(username="testuser1", password="12345")
        test_user1.save()
        blog_author = BlogAuthor.objects.create(
            user=test_user1,
            bio="Test Bio",
        )
        blog_author.save()

        for i in range(1, 11):
            blog = Blog.objects.create(
                name=f"Test Blog {i}",
                author=blog_author,
                description=f"Test Blog {i} Description",
            )
            blog.save()

    def test_view_exists_at_desired_location(self):
        response = self.client.get("/blog/blogs/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("blogs"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("blogs"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_list.html")

    def test_pagination_is_five(self):
        response = self.client.get(reverse("blogs"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["blog_list"]), 5)

    def test_len_of_all_blogs(self):
        response = self.client.get(reverse("blogs") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["blog_list"]), 5)

    def test_blogs_ordered_by_post_date_in_desc_order(self):
        response = self.client.get(reverse("blogs"))
        self.assertEqual(response.status_code, 200)

        last_date = 0
        for blog in response.context["blog_list"]:
            if not last_date:
                last_date = blog.post_date
            else:
                self.assertTrue(last_date >= blog.post_date)
                last_date = blog.post_date


class BloggerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(1, 8):
            test_user = User.objects.create(username=f"testuser{i}", password="12345")
            test_user.save()
            blog_author = BlogAuthor.objects.create(
                user=test_user,
                bio=f"Test User's{i} Bio",
            )
            blog_author.save()

    def test_view_exists_at_desired_location(self):
        response = self.client.get("/blog/bloggers/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("bloggers"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("bloggers"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blogauthor_list.html")

    def test_pagination_is_five(self):
        response = self.client.get(reverse("bloggers"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["blogauthor_list"]), 5)

    def test_len_of_all_bloggers(self):
        response = self.client.get(reverse("bloggers") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["blogauthor_list"]), 2)

    def test_bloggers_ordered_by_user(self):
        response = self.client.get(reverse("bloggers"))
        self.assertEqual(response.status_code, 200)

        first_blogger = "aaa"
        for bloger in response.context["blogauthor_list"]:
            blogger = bloger.user.username
            if first_blogger < blogger:
                first_blogger = blogger
            else:
                self.assertEqual(first_blogger < blogger)
                first_blogger = blogger


class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create(username="testuser", password="12345")
        test_user1.save()
        blog_author = BlogAuthor.objects.create(
            user=test_user1,
            bio="Test Bio",
        )
        blog_author.save()
        blog = Blog.objects.create(
            name="Test Blog 1",
            author=blog_author,
            description="Test Blog 1 Description",
        )
        blog.save()

    def test_view_exists_at_desired_location(self):
        response = self.client.get("/blog/blog/1")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("blog-detail", args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("blog-detail", args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_detail.html")


class BlogListByAuthorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username="testuser", password="12345")
        test_user.save()
        blog_author = BlogAuthor.objects.create(
            user=test_user,
            bio=f"Test User Bio",
        )
        blog_author.save()

        for i in range(1, 8):
            blog = Blog.objects.create(
                name=f"Test Blog {i}",
                author=blog_author,
                description=f"Test Blog {i} Description",
            )
            blog.save()

    def test_view_exists_at_desired_location(self):
        response = self.client.get("/blog/blogger/1")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("blogs-by-author", args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("blogs-by-author", args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_list_by_author.html")

    def test_get_queryset_returns_list_of_blogs_belongs_to_the_author(self):
        response = self.client.get(reverse("blogs-by-author", args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["blog_list"])
        self.assertEqual(len(response.context["blog_list"]), 5)

        for blog in response.context["blog_list"]:
            self.assertEqual(blog.author, response.context["blogger"])

    def test_view_context_include_blogger(self):
        response = self.client.get(reverse("blogs-by-author", args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["blogger"])

    def test_pagination_is_five(self):
        response = self.client.get(reverse("blogs-by-author", args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["blog_list"]), 5)

    def test_len_of_all_blogs(self):
        response = self.client.get(reverse("blogs-by-author", args=(1,)) + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["blog_list"]), 2)
