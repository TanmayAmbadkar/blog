from django.urls import path
from blog.views import *

urlpatterns = [

    path('posts', PostListView.as_view(), name = 'post_list'),
    path('', HomeView.as_view(), name = 'home'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', CreatePostView.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/remove/', PostDeleteView.as_view(), name = 'post_remove'),
    path('drafts/', DraftListView.as_view(), name = 'post_draft_list'),
    path('post/<int:pk>/comment/', add_comments_to_post, name = 'add_comments_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name = 'comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name = 'comment_remove'),
    path('post/<int:pk>/publish/', post_publish, name = 'post_publish')

]
