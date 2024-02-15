from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView
from blog.models import Art

# Create your views here.
class ArticleList(LoginRequiredMixin,ListView):
	template_name = 'registration/home.html'

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Art.objects.all()
		else:
			return Art.objects.filter(author=self.request.user)

class ArticleCreate(LoginRequiredMixin,CreateView):
	model = Art
	fields = ["author","title","slug","category","description","thumbnail","publish","status"]
	template_name = 'registration/article_create_update.html'


