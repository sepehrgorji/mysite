from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(requset):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(requset, 'blog/blog-home.html',context)

def blog_single(requset,pid):
    posts = get_object_or_404(Post,pk=pid, status=1)
    context = {'post':posts}
    return render(requset, 'blog/blog-single.html',context)

def test(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, 'test.html',context)