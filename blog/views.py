from abc import ABC

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.views import generic

from .models import BlogPost
from .forms import NewOrUpdateBlogPostForm


# blog list class-based view
class PostListView(generic.ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        return BlogPost.objects.filter(status='pub').order_by('-datetime_edited')


# blog detail class-based view
class BlogDetailView(generic.DetailView):
    template_name = 'blog/blog_detail.html'
    model = BlogPost
    context_object_name = 'blog'


# add blog functional view
@staff_member_required()
def add_blog_response(request):
    print('method:', request.method)
    if request.method == 'POST':
        blogpost_form = NewOrUpdateBlogPostForm(request.POST)
        if blogpost_form.is_valid():
            new_blogpost_form = blogpost_form.save(commit=False)
            new_blogpost_form.author = request.user
            new_blogpost_form.save()
            return redirect('blog_list_url')
        else:
            blogpost_form = NewOrUpdateBlogPostForm()
    else:
        blogpost_form = NewOrUpdateBlogPostForm()
    return render(request, 'blog/add_blog.html', context={'form': blogpost_form, 'page_title': 'AddNewBlog'})


# update blog functional view
def update_blog_response(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    print('blog post:', blog_post)
    blogpost_form = NewOrUpdateBlogPostForm(request.POST or None, instance=blog_post)
    if blogpost_form.is_valid():
        blogpost_form.save()
        return redirect('blog_detail_url', blog_post.pk, blog_post.title)
    else:
        blogpost_form = NewOrUpdateBlogPostForm(request.POST or None, instance=blog_post)
    return render(request, 'blog/add_blog.html', context={'form': blogpost_form, 'page_title': 'UpdateBlog'})


# update blog class-based view
class UpdateBlogView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView, ABC):
    form_class = NewOrUpdateBlogPostForm
    template_name = 'blog/add_blog.html'
    model = BlogPost

    def test_func(self):
        return self.request.user.is_staff


# delete blog functional view
@staff_member_required()
def delete_blog_response(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('blog_list_url')
    return render(request, 'blog/blog_delete.html', context={'blog_post': blog_post})


# delete blog class-based view
class DeleteBlogView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/blog_delete.html'
    # success_url = '/blog/'

    def get_success_url(self):
        return reverse('blog_list_url')
