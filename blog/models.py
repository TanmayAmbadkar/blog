from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)

    profile_img = models.ImageField(upload_to = 'profile_pics', blank = True)
    cover_image = models.ImageField(upload_to = 'cover_profile_img', blank = True)

    description = models.TextField(blank = True)
    writeup = models.TextField(blank = True)

    instagram = models.URLField(blank = True)
    facebook = models.URLField(blank = True)
    github = models.URLField(blank = True)
    linkedin = models.URLField(blank = True)
    email = models.EmailField(blank = True)
    def __str__(self):

        return self.user.username


class Post(models.Model):

    types = (
        ('D', 'Deep Learning'),
        ('M', 'Machine Learning'),
    )
    author = models.ForeignKey('UserProfileInfo', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    cover_img = models.ImageField(upload_to = 'cover_image', blank = True)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    type = models.CharField(max_length = 1, choices = types, blank = True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dis_likes.users.count()

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey('blog.Post', related_name = 'comments', on_delete = models.CASCADE)
    author = models.CharField(max_length = 100)
    profile_img = models.ImageField(upload_to = 'profile_pics', blank = True)
    text= models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        if(self.post.type == 'M'):
            return reverse('post_list_ML')
        else:
            return reverse('post_list_DL')

    def __str__(self):
        return self.text

class Like(models.Model):

    post = models.OneToOneField(Post, related_name = 'likes', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_post_likes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.title)



class DisLike(models.Model):

    post = models.OneToOneField(Post, related_name = 'dis_likes', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_post_dis_likes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.title)
