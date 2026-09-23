from django.shortcuts import render
from blog.forms import AuthorForm
from blog.models import Authors

def index_view(request):
    return render(request, 'index.html')

def blog_list_view(request):
    return render(request, 'blog_list.html')

def add_author_form(request):
    message = ''
    if request.method == "POST":
        author_form = AuthorForm(request.POST)

        if author_form.is_valid():
            author_form.save()
            message = 'Author added successfully'

    else:
        author_form = AuthorForm()

    author = Authors.objects.all()

    context = {
        'forms' : author_form,
        'msg' : message,
        'author' : author
    }
    return render(request, 'add_author.html', context)