from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from djapp.apps.users.models import petition


def home(request):
	mypetitions = petition.objects.filter(status=True)
	ctx = {'pet':mypetitions}
	return render_to_response('home/home.html',ctx,context_instance=RequestContext(request))


