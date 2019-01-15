from django.shortcuts import render


from django.views.generic.base import TemplateView

from tweet.models import Tweet

# def home(request):
# 	return render(request, 'home.html', {})

class HomePageView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_tweet'] = Tweet.objects.all()
		return context