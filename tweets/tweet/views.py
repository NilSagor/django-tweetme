from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from .forms import TweetModelForm
from .mixins import FormUserNeededMixins, UserOwnerMixin 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tweet 

# Create your views here.

"""
def tweet_detail_view(request, pk):
	return render(request, 'tweet/detail_view.html', {})

def tweet_list_view(request):
	return render(request, 'tweet/list_view.html', {})
"""
class TweetListView(generic.ListView):
	model = Tweet
	template_name = 'tweet/list_view.html'	

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		#context['-another_list'] = Tweet.objects.all()
		return context

class TweetDetailView(generic.DetailView):
	model = Tweet
	template_name = 'tweet/detail_view.html'


class TweetCreateView(CreateView):
	form_class = TweetModelForm
	template_name = 'tweet/create_view.html'
	success_url = '/tweet/create/'
	login_url = '/admin/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TweetCreateView, self).form_valid(form)



class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	model = Tweet
	form_class = TweetModelForm
	template_name = 'tweet/update_view.html'
	success_url = '/tweet/'

