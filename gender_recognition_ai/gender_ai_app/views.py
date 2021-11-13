from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .models import Image
from .predict import predict
from django.conf import settings


def index(request):
    return render(request, 'index.html', {'errors': []})


def upload(request):
    errors = []
    Image.objects.all().delete()
    if request.method == 'POST':
        if request.FILES.get('image', False) == False:
            errors.append('Please upload an image.')
        elif request.FILES['image'].size > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
            errors.append('File should not be larger than 2.5 MB.')
        if len(errors) == 0:
            image_object = Image.objects.create(image=request.FILES.get('image'))
            prediction = None
            try:
                prediction = predict(str(image_object.image))
            except:
                errors.append('Failed to load image: picture may contain too many faces.')
            if prediction == 'None':
                errors.append('Image should contain 1 clear and unobstructed face.')
            elif prediction is not None:
                return render(request, 'index.html', {'image': image_object, 'prediction': prediction})
    return render(request, 'index.html', {'errors': errors})
