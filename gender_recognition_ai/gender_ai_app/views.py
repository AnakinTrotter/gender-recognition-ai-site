from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
from .models import Image
from .predict import predict
from django.conf import settings


def index(request):
    form = ImageForm()
    return render(request, 'index.html', {'form': form, 'errors': []})


def upload(request):
    errors = []
    if request.method == 'POST' and request.FILES.get('image', False):
        form = ImageForm(request.POST, request.FILES)
        image = None
        if not form.is_valid():
            errors.append('Please try a different image.')
        if request.FILES['image'].size > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
            errors.append('File should not be larger than 2.5 MB.')
        if len(errors) == 0:
            saved_form = form.save()
            image = Image.objects.get(id=saved_form.id)
            prediction = predict(str(image.image))
            if prediction == 'None':
                errors.append('Image should contain at least 1 clear and unobstructed face.')
            else:
                return render(request, 'upload.html', {'form': form, 'image': image, 'prediction': prediction})
    return render(request, 'index.html', {'form': form, 'errors': errors})
