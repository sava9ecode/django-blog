from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Blog, BlogAuthor


def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(request, "index.html")


class BlogListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """

    model = Blog
    paginate_by = 5


class BlogListByAuthorView(generic.ListView):
    """
    Generic class-based view for a list of blogs posted by a particular BlogAuthor.
    """

    model = Blog
    paginate_by = 5
    template_name = "blog/blog_list_by_author.html"

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        id = self.kwargs["pk"]
        target_author = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogListByAuthorView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context["blogger"] = get_object_or_404(BlogAuthor, pk=self.kwargs["pk"])
        return context


class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """

    model = Blog


class BloggerListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """

    model = BlogAuthor
    paginate_by = 5
