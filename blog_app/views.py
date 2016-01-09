from django.shortcuts import render
import models
from django.http import HttpResponse

# Create your views here.
def index(request):
    all_posts = models.post.objects.all()
    return render(request, "index.html", {'posts': all_posts})


def add(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            content = request.POST['content']
            image_url = request.POST['image_url']

            new_post = models.post(title=title, content=content, image_url=image_url)
            new_post.save()
            return render(request, "success.html")
        except Exception, e:
            return HttpResponse(status=500)