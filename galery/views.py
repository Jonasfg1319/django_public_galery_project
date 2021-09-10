from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.list import ListView
from .models import Images
from django.urls import reverse
# Create your views here.


class IndexView(generic.ListView):
	template_name = "galery/index.html"
	context_object_name = "images_list"

	def get_queryset(self):
		return Images.objects.all()
 


class UploadView(generic.ListView):
   template_name = "galery/upload.html"
   context_object_name = ""
   

   def get_queryset(self):
	  	pass

class ImageView(generic.DetailView):
	model = Images
	template_name = "galery/image.html"


def uploadig_view(request):
	img = Images()
	message = "files can´t uploaded:"
	try: 
		if(img.verify_field(request.POST['description'], request.POST['name']) != "empty"):
			if (img.verify_format(request.FILES['image'].content_type) == True):
			     img.image_name = request.FILES['image'].name
			     img.description = request.POST['description']
			     img.name_user = request.POST['name']
			     img.file = request.FILES['image']
			     img.save()
			     return HttpResponseRedirect(reverse("galery:index"))
			else:
				message += " invald format"
		else:
			message += "invalid field"
	except:
		return HttpResponseRedirect(reverse("galery:index"))
	return render(request,
		          "galery/upload.html", 
		          {"message": message}
		          )
