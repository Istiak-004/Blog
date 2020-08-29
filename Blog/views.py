from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


def HomePage(request):
    post = Post.objects.all()
    context = {
        "posts": post
    }
    return render(request,'blog/home.html',context)

class PostListViews(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # lets paginate the home page by 2 post per page
    paginate_by = 2

class UserPostListViews(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # lets paginate the home page by 2 post per page
    paginate_by = 2    

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostDetailViews(DetailView):
    model = Post   

class PostCreateViews(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateViews(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    # Now we need to validate if the current user is updating his own post or others
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    

class PostDeleteViews(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
    success_url = '/'         
         
         

def AboutPage(request):
    context = {}
    return render(request,'blog/about_page.html',context)    