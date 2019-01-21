from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.db.models import Q

from .forms import TweetModelForm
from .mixins import FormUserNeededMixins, UserOwnerMixin 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Tweet 

# Create your views here.

"""
def tweet_detail_view(request, pk):
	return render(request, 'tweet/detail_view.html', {})

def tweet_list_view(request):
	return render(request, 'tweet/list_view.html', {})
"""
"""
class HomePageView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_tweet'] = Tweet.objects.all()
		return context
"""

class TweetListView(generic.ListView):
	#model = Tweet
	#template_name = 'tweet/list_view.html'	
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		#print(qs)
		query=self.request.GET.get('q', None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query)|
				Q(user__username__icontains=query)
			)
		return qs 
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['create_form']=TweetModelForm
		context['create_url']=reverse_lazy('tweet:tweet-create')
		#context['-another_list'] = Tweet.objects.all()
		return context

class TweetDetailView(generic.DetailView):
	model = Tweet
	template_name = 'tweet/tweet_detail.html'
	succec_url = reverse_lazy("tweet:tweet-detail")



class TweetCreateView(CreateView):
	form_class = TweetModelForm
	template_name = 'tweet/create_view.html'
	#success_url = '/tweet/create/'
	login_url = '/admin/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)



class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	model = Tweet
	form_class = TweetModelForm
	template_name = 'tweet/update_view.html'
	#success_url = '/tweet/'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet 
	template_name = 'tweet/delete_confirm.html'
	success_url = reverse_lazy('tweet:tweet-list') 