"""
- type of authentications:
    * LoginRequiredMixin
        ~ محدود کردن کل کلاس
    * @method_decorator(login_required)
        ~ محدود کردن متدهای دلخواه از کلاس

"""
# ex1
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class MyView(LoginRequiredMixin, generic.View):
    pass

# ------------
CommentCreateForm=None
CommentReplyForm=None
Post=None
# ------------
# ex2
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostDetailView(generic.View):
	form_class = CommentCreateForm
	form_class_reply = CommentReplyForm

	def setup(self, request, *args, **kwargs):
		self.post_instance = get_object_or_404(Post, pk=kwargs['post_id'], slug=kwargs['post_slug'])
		return super().setup(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		comments = self.post_instance.pcomments.filter(is_reply=False)
		can_like = False
		if request.user.is_authenticated and self.post_instance.user_can_like(request.user):
			can_like = True
		return render(request, 'home/detail.html', {'post':self.post_instance, 'comments':comments, 'form':self.form_class, 'reply_form':self.form_class_reply, 'can_like':can_like})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.user = request.user
			new_comment.post = self.post_instance
			new_comment.save()
			messages.success(request, 'your comment submitted successfully', 'success')
			return redirect('home:post_detail', self.post_instance.id, self.post_instance.slug)
