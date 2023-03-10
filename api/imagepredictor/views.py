from django.shortcuts import render 
from .apps import ImagepredictorConfig 
from django.http import JsonResponse
from rest_framework.views import APIView
from skimage.transform import rescale, resize
from PIL import Image
import numpy as np
import pandas as pd
from rest_framework.parsers import MultiPartParser, JSONParser


class call_model(APIView):
    parser_classes = [MultiPartParser]
    def get(self,request):

        if request.method == 'GET':            
            # val = request.GET.get('text')
            response = {"Status": 'No image received but server is running successfully...'}

        return JsonResponse(response)
    
    def post(self, request):

        if request.method == 'POST':            
        # val = request.GET.get('text')
            image_file = request.FILES.get('image')

                
            class_dict = {0: 'Bed',
                        1: 'Chair',
                        2: 'Sofa',
                        }
            
            vgg_model = ImagepredictorConfig.model

            if image_file is not None:
                image = Image.open(image_file)
                
                img_arr = np.array(image)
                img = resize(img_arr,(128,128))
                img = np.expand_dims(img, axis = 0)
                output = vgg_model.predict(img).argmax(axis=-1) 
                # print('img shape', img_arr.shape)

                val = class_dict[output[0]]
                # print("Printing text in server:",val)
                response = {'Status': 'Success',
                    'Prediction': val}       
            else: 
                response = {"Status": 'No image received but server is running successfully...'}

            return JsonResponse(response)

           

