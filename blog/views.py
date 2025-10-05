from django.shortcuts import render
from blog.models import Post
# Create your views here.
def blog_view(requset):
    return render(requset, 'blog/blog-home.html')

def blog_single(requset):
    return render(requset, 'blog/blog-single.html')

def test(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, 'test.html',context)