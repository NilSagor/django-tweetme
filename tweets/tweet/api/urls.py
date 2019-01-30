"""tweets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from . import views



app_name = 'tweet-api'
urlpatterns = [
	path('', views.TweetListAPIView.as_view(), name = 'tweet-list'),
	# path('', RedirectView.as_view(url="/")),
	# path('search/', views.TweetListView.as_view(), name = 'search'),
	# path('<int:pk>/', views.TweetDetailView.as_view(), name = 'tweet-detail'),
	# path('create/', views.TweetCreateView.as_view(), name = 'tweet-create'),
	# path('<int:pk>/update/', views.TweetUpdateView.as_view(), name = 'tweet-update'),
	# path('<int:pk>/delete/', views.TweetDeleteView.as_view(), name = 'tweet-delete'),

]

