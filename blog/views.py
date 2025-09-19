from django.shortcuts import render

# Create your views here.
def blog_view(requset):
    return render(requset, 'blog/blog-home.html')

def blog_single(requset):
    return render(requset, 'blog/blog-single.html')
