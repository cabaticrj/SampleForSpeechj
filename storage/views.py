from django.http import HttpResponse

def index(request):
	return HttpResponse("Lalagyan ng kung ano-ano.")
