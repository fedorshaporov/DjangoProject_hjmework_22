from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'preview_image', 'is_published']

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views_count += 1
        post.save()
        return post

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})  # Перенаправление на детальную страницу отредактированного поста

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')