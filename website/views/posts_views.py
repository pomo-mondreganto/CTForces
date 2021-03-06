from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from website.decorators import custom_login_required as login_required
from website.forms import PostCreationForm, CommentCreationForm
from website.models import Post, User
from .view_classes import PagedTemplateView, GetPostTemplateViewWithAjax


@require_POST
@login_required
def leave_comment(request):
    parent_id = request.POST.get('parent_id')
    form = CommentCreationForm(request.POST, user=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'comment added successfully')
    else:
        for field in form.errors:
            for error in form.errors[field]:
                extra_tags = [field]
                if parent_id:
                    extra_tags.append(str(parent_id))
                else:
                    extra_tags.append('top')
                messages.error(request, error, extra_tags=extra_tags)
        print(form.errors)

    if not request.POST.get('post_id'):
        return redirect('main_view')
    return redirect('post_view', post_id=request.POST['post_id'])


class UserBlogView(PagedTemplateView):
    template_name = 'profile_templates/user_blog.html'

    def get_context_data(self, **kwargs):
        context = super(UserBlogView, self).get_context_data(**kwargs)
        username = kwargs.get('username')
        page = context['page']

        user = User.objects.filter(
            username=username
        ).annotate(
            post_count=Count(
                'posts'
            )
        ).first()

        if not user:
            raise Http404()

        posts = user.posts.order_by(
            '-created'
        ).select_related(
            'author'
        ).all()[(page - 1) * 10: page * 10]

        page_count = (user.post_count + settings.POSTS_ON_PAGE - 1) // settings.POSTS_ON_PAGE
        context['user'] = user
        context['posts'] = posts
        context['page_count'] = page_count
        return context


class PostCreationView(LoginRequiredMixin, GetPostTemplateViewWithAjax):
    template_name = 'post_templates/create_post.html'

    def handle_ajax(self, request, *args, **kwargs):
        form = PostCreationForm(request.POST, user=request.user)
        result = dict()
        if form.is_valid():
            form.save()
            result['success'] = True
            result['next'] = reverse('user_blog_view', kwargs=dict(username=request.user.username))
        else:
            print(form.errors)

            result['success'] = False
            result['errors'] = form.errors

        return JsonResponse(result)


class PostView(TemplateView):
    template_name = 'post_templates/post_view.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        post_id = kwargs.get('post_id')
        post = Post.objects.filter(
            id=post_id
        ).prefetch_related(
            'comments',
        ).select_related(
            'author'
        ).first()

        if not post:
            raise Http404()

        context['post'] = post
        context['user'] = post.author
        return context
