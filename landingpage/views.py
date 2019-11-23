from django.shortcuts import render

from django.views.generic.edit import CreateView, ModelFormMixin
from django.http import HttpResponse
# Create your views here.
from .models import Join
from django.urls import reverse
# from django.core.urlresolvers import reverse

class JoinForm(CreateView, ModelFormMixin):
	model = Join
	template_name = 'landingpage/home.html'
	fields = ['email', 'file']

	# def save(self, form):z
	# 	new_message = form.save(commit=False)
	# 	new_message = new_message + 'Да ладно тебе'
	# 	new_message.save()
	# 	self.object = new_message

	# 	return super(ModelFormMixin, self).save()




def index(request):
    context = {'form': JoinForm}
    template_name = 'landingpage/index.html'
    return render(request, template_name)
		






	# def form_valid(self, form):
	# 	email = form.cleaned_data.get('email')

	# 	return super(HomeView, self).form_valid(form)