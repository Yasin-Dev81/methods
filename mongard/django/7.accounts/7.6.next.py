"""
- بعد از اینکه لاگین شد ریدایرکت بشه به صفحه اولش
"""

from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UserLoginView(View):
	form_class = UserLoginForm
	template_name = 'account/login.html'

	def setup(self, request, *args, **kwargs):
		self.next = request.GET.get('next') # <-------------------------
		return super().setup(request, *args, **kwargs)

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home:home')
		return super().dispatch(request, *args, **kwargs)

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user is not None:
				login(request, user)
				messages.success(request, 'you logged in successfully', 'success')
				if self.next: # <----------------------------------------
					return redirect(self.next) # <-----------------------
				return redirect('home:home')
			messages.error(request, 'username or password is wrong', 'warning')
		return render(request, self.template_name, {'form':form})
