from django.urls import path
from blog.views import *
from django.conf.urls import include

urlpatterns = [

    path('posts/ML/', PostListView_ML.as_view(), name = 'post_list_ML'),
    path('posts/DL/', PostListView_DL.as_view(), name = 'post_list_DL'),
    path('', HomeView.as_view(), name = 'home'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', CreatePostView.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit/', PostUpdateView_ML.as_view(), name = 'post_edit_ml'),
    path('post/<int:pk>/edit/', PostUpdateView_DL.as_view(), name = 'post_edit_dl'),
    path('post/<int:pk>/remove/', PostDeleteView_ML.as_view(), name = 'post_remove_ml'),
    path('post/<int:pk>/remove/', PostDeleteView_DL.as_view(), name = 'post_remove_dl'),
    path('drafts/', DraftListView.as_view(), name = 'post_draft_list'),
    path('post/<int:pk>/comment/', add_comments_to_post, name = 'add_comments_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name = 'comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name = 'comment_remove'),
    path('post/<int:pk>/publish/', post_publish, name = 'post_publish'),
    path('about/tanmay', TanmayView.as_view(), name = 'tanmay'),
    path('about/aniket', AniketView.as_view(), name = 'aniket'),
    path('accounts/', include('allauth.urls')),

]
