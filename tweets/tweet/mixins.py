from django import forms

from django.forms.utils import Errorlist

class FormUserNeededMixins(object):
	def form_valid(self, form):
		if self.request.user.is_authenticated:
			form.instance.user = self.request.user 
			return super(FormUserNeededMixins, self).form_valid(form)
		else:
			form_errors[forms.forms.NON_FIELD_ERRORS] = Errorlist(["user must be logged in to continue"])
			return self.form_invalid(form)