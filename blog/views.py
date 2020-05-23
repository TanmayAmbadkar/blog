from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from blog.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.decorators import login_required
from blog.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
# Create your views here.


class TanmayView(TemplateView):

    template_name = 'tanmay.html'


    def get_context_data(self, **kwargs):

         context = super(TanmayView, self).get_context_data(**kwargs)
         context['users'] = User.objects.filter(username__startswith = 'tanmay')
         context['posts'] = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:3]
         return context

class AniketView(TemplateView):

    template_name = 'tanmay.html'


    def get_context_data(self, **kwargs):

         context = super(AniketView, self).get_context_data(**kwargs)
         context['users'] = User.objects.filter(username__startswith = 'aniket')
         context['posts'] = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:3]
         return context

class HomeView(TemplateView):


    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super(HomeView, self).get_context_data(**kwargs)
        context['users'] = UserProfileInfo.objects.all()
        context['posts'] = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:3]
        return context


class PostListView_ML(TemplateView, TemplateResponseMixin):

    template_name = 'post_list_ML.html'

    def get_context_data(self, **kwargs):

         context = super(PostListView_ML, self).get_context_data(**kwargs)
         context['posts'] = Post.objects.filter(type__startswith = 'M').order_by('-published_date')
         context['topthree'] = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:3]
         return context

class PostListView_DL(ListView, TemplateResponseMixin):

    model = Post
    template_name = 'post_list_DL.html'

    def get_context_data(self, **kwargs):

         context = super(PostListView_DL, self).get_context_data(**kwargs)
         context['posts'] = Post.objects.filter(type__startswith = 'D').order_by('-published_date')
         context['topthree'] = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:3]
         return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):

         context = super(PostDetailView, self).get_context_data(**kwargs)
         context['post'] = Post.objects.get(pk = self.kwargs['pk'])
         context['topthree'] = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:3]
         return context



class CreatePostView(LoginRequiredMixin, CreateView):

    template_name = 'post_form.html'
    success_url = reverse_lazy('post_draft_list')
    login_url = '/login/'
    form_class = PostForm
    model = Post

class PostUpdateView_ML(LoginRequiredMixin, UpdateView):

    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list_ML')
    login_url = '/login/'
    form_class = PostForm
    model = Post

class PostUpdateView_DL(LoginRequiredMixin, UpdateView):

    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list_DL')
    login_url = '/login/'
    form_class = PostForm
    model = Post

class PostDeleteView_ML(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = reverse_lazy('post_list_ML')

class PostDeleteView_DL(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = reverse_lazy('post_list_DL')


class DraftListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post
    template_name = 'post_draft_list.html'

    def get_queryset(self):

        return Post.objects.filter(published_date__isnull = True).order_by('created_date')


def add_comments_to_post(request, pk):

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':

        form_class = CommentForm(request.POST)

        if form_class.is_valid():
            comment = form_class.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk = post.pk)

    else:
        form_class = CommentForm()

    return render(request, 'blog/comment_form.html', {'form': form_class})

@login_required()
def comment_approve(request, pk):

    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()

    return redirect('post_detail', pk = comment.post.pk)

@login_required
def comment_remove(request, pk):

    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk = post_pk)

@login_required
def post_publish(request, pk):

    post = get_object_or_404(Post, pk = pk)
    post.publish()
    return redirect('post_detail', pk = post.pk)

def signup_view(request):
    form_class = UserForm
    if request.method == 'POST':

        form_class = UserForm(request.POST)

        if form_class.is_valid():
            form_class.save()
            return redirect('home')

    else:
        form_class = UserForm()

    return render(request, 'registration/signup.html', {'form': form_class})


class UpdatePostVote(LoginRequiredMixin, View):
    login_url = '/accounts/google/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):

        post_id = self.kwargs.get('post_id', None)
        opinion = self.kwargs.get('opinion', None) # like or dislike button clicked

        post = get_object_or_404(Post, id=post_id)

        try:
            # If child DisLike model doesnot exit then create
            post.dis_likes
        except Post.dis_likes.RelatedObjectDoesNotExist as identifier:
            DisLike.objects.create(post = post)

        try:
            # If child Like model doesnot exit then create
            post.likes
        except Post.likes.RelatedObjectDoesNotExist as identifier:
            Like.objects.create(post = post)

        if opinion.lower() == 'like':

            if request.user in post.likes.users.all():
                post.likes.users.remove(request.user)
            else:
                post.likes.users.add(request.user)
                post.dis_likes.users.remove(request.user)

        elif opinion.lower() == 'dis_like':

            if request.user in post.dis_likes.users.all():
                post.dis_likes.users.remove(request.user)
            else:
                post.dis_likes.users.add(request.user)
                post.likes.users.remove(request.user)
        else:
            return redirect('post_detail', pk = post.pk)
        return redirect('post_detail', pk = post.pk)
