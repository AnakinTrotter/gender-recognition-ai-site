from django.shortcuts import redirect, render
from .models import Image
from .predict import predict as predict_gender
from django.conf import settings
from django.core.files.storage import default_storage
import os


def index(request):
    return render(request, 'index.html')


def predict(request):
    errors = []
    Image.objects.all().delete()
    if request.method == 'POST':
        if request.FILES.get('image', False) == False:
            errors.append('Please upload an image.')
        elif request.FILES['image'].size > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
            errors.append('File may not be larger than 10 MB.')
        if len(errors) == 0:
            image_object = Image.objects.create(
                image=request.FILES.get('image'))
            prediction = None
            try:
                prediction = predict_gender(str(image_object.image))
            except:
                errors.append(
                    'Failed to load image: picture may contain too many faces.')
            if prediction == 'None':
                errors.append(
                    'Image should contain 1 clear and unobstructed face.')
            elif prediction == 'Male' or prediction == 'Female':
                return render(request, 'predict.html', {'image': image_object, 'prediction': prediction})
    return render(request, 'error.html', {'errors': errors})
