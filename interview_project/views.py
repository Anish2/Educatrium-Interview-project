from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json

from .models import Element

# Create your views here.
def index(request): # main page
	num_elements = 10
	# fetch randomly ordered elements
	divs = Element.objects.all().order_by('?')[:num_elements]
	context = {'divs': divs}
	return render(request, 'interview_project/index.html', context)

def get_element(request, element_id):
	e = get_object_or_404(Element, element_id=element_id)
	data = {'random_popup_title': e.random_popup_title, 'random_popup_text': e.random_popup_text}
	return HttpResponse(json.dumps(data))

def generate(request):
	for i in xrange(1, 11):
		e = Element(element_id=i, random_header="Div Element #"+str(i), random_text="Random text for element "+str(i), random_popup_title="Unrelated element "+str(i), random_popup_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ex eros, laoreet vitae enim eu, hendrerit rutrum mi. Curabitur eu justo aliquam, ornare orci vitae, lobortis eros. Etiam pulvinar posuere leo, sed sollicitudin purus viverra eget. Cras id metus est. Maecenas eget ipsum lorem. Vivamus dignissim interdum consectetur. Curabitur non mauris at est ultrices consectetur eu quis quam. Proin et urna a urna ultricies tincidunt. Duis efficitur nisi sed velit rhoncus, sit amet mollis leo tristique. Vestibulum sollicitudin placerat maximus. Maecenas faucibus enim sed lectus rutrum efficitur. Phasellus in enim mi.")
		e.save()
	return HttpResponse("done generating.")