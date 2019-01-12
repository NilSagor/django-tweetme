from django import forms

from django.forms.utils import ErrorList

class FormUserNeededMixins(object):
	def form_valid(self, form):
		if self.request.user.is_authenticated:
			form.instance.user = self.request.user 
			return super(FormUserNeededMixins, self).form_valid(form)
		else:
			form_errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["user must be logged in to continue"])
			return self.form_invalid(form)


class UserOwnerMixin(object):
	def form_valid(self, form):
		if form.instance.user == self.request.user:
			return super(FormUserNeededMixins, self).form_valid(form)
		else:
			form._errors[forms.NON_FIELD_ERRORS]=ErrorList(["this user is not allowed to change this data"])
		return self.form_invlaid(form)