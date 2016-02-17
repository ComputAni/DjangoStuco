from django.shortcuts import render
from homepage.models import blog
from .forms import BlogPosts

# Create your views here.
def home(request):
    all_objects = blog.objects.all()
    first_object = all_objects[0]
    title_first_object = first_object.title
    template = "home.html"
    form = BlogPosts(request.POST or None)

    if form.is_valid():
        variable = form.save(commit='false')
        variable.save()

    context ={
        "formvar": form,
        "variable1": all_objects,
        "variable2": first_object,
        "TITLEFIRSTOBJECT": title_first_object, 
    }
    return render(request, template,context)


