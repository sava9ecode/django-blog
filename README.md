# Django DIY Blog
## Basic blog site written in Django
This web application creates an very basic blog site using
Django. The site allows blog authors to create text-only blogs using
the Admin site, and any logged in user to add comments via a form. Any
user can list all bloggers, all blogs, and detail for bloggers and blogs
(including comments for each blog).

The models for this site are as shown below:

![Local_library_model_uml.](https://raw.githubusercontent.com/mdn/django-diy-blog/main/blog/static/images/diy_django_mini_blog_models.png)

## Quick start
To get this project up and running locally on your computer:
1. Set up the Python development environment. I recommend using a Python virtual environment.
2. Assuming you have Python setup, run the following commands (if you're on Windows you may use ```py``` or ```py -3``` instead of ```python``` to start Python):
   ```
   mkdir diyblog
   cd diyblog
   git clone https://github.com/sava9ecode/django_diy_blog.git .
   cp .env.template .env # And fill it out.
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser.
   python3 manage.py runserver
   ```
4. Open a browser to ```http://127.0.0.1:8000/<your_very_secret_url>/admin/``` to open the admin site.
5. Create a few test objects of each type.
6. Open tab to ```http://127.0.0.1:8000``` to see the main site, with your new objects.
