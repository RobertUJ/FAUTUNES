from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
# Forms
from djapp.apps.users.forms import formPetition
# Models
from djapp.apps.users.models import petition
import requests
 
def petitions(request):
	if request.method == "POST":
		frm = formPetition(request.POST)
		if frm.is_valid():
			frm.save()
			return HttpResponseRedirect('/dj/')
	else:
		frm = formPetition()

	if request.is_ajax():
		if request.method == "POST":
			busqueda = "%s" % request.POST['cod']
			_url = "http://tinysong.com/s/"
			_url =  _url + busqueda
			_url =  _url + "?format=json&limit=15&key=316f76c22e043542474b06e097cfb941"
			resultados = requests.get(_url)
			lista = resultados.json
			lis = ""
			if len(lista) == 0:
				return HttpResponse("<tr><td rowspan='3'>No results</td></tr>")
			else:
				for l in lista:
					lis += "<tr class='sTrack'  track='%s' artist='%s' url='%s'>" % (l['SongName'],l['ArtistName'],l['Url'])
					lis += "<td>%s</td>"%(l['SongName'])
					lis += "<td>%s</td>"%(l['ArtistName'])
					lis += "<td>%s</td>"%(l['Url'])
					lis += "</tr>"
                return HttpResponse(lis)
	else:
		mypetitions = petition.objects.filter(status=True)
		ctx = {'form':frm,'pet':mypetitions}
		return render_to_response('users/peticiones.html',ctx,context_instance=RequestContext(request))


def get_peticiones(request):
	if request.method == "POST":
		_id = int(request.POST['id'])
		entry = petition.objects.get(id=_id)
		entry.status = False
		entry.save()

	mypetitions = petition.objects.filter(status=True)
	ctx = {'pet':mypetitions}
	return render_to_response('users/dj.html',ctx,context_instance=RequestContext(request))
