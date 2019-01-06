from django.shortcuts import render
from django.views import generic

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