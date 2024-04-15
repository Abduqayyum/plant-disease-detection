from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import tensorflow as tf
import matplotlib.pylab as plt
from tensorflow import keras
from keras.models import load_model
from django.http import JsonResponse
from .models import Image
from .serializers import ImageSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
import keras.utils as keras_utils
import tensorflow_hub as hub


class_names = ['Apple_Apple_scab', 'Apple_Black_rot', 'Apple_healthy',
       'Cherry_Powdery_mildew', 'Cherry_healthy', 'Corn_Common_rust',
       'Corn_Gray_leaf_spot', 'Corn_healthy', 'Grape_Black_rot',
       'Grape_Esca_(Black_Measles)',
       'Grape_Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape_healthy',
       'Peach_Bacterial_spot', 'Peach_healthy',
       'Pepper_bell_Bacterial_spot', 'Pepper_bell_healthy',
       'Potato_Early_blight', 'Potato_Late_blight', 'Potato_healthy',
       'Strawberry_Leaf_scorch', 'Strawberry_healthy',
       'Tomato_Bacterial_spot', 'Tomato_Early_blight',
       'Tomato_Late_blight', 'Tomato_Leaf_Mold',
       'Tomato_Septoria_leaf_spot', 'Tomato_Tomato_mosaic_virus',
       'Tomato_healthy']




def load_and_preprocess_image(filename, filesize=224):
  # read in the image
  img = tf.io.read_file(filename)
  # decode the read file into tensor
  img = tf.image.decode_image(img)
  # resize the image
  img = tf.image.resize(img, [filesize, filesize])
  # rescale the pixel values of the image
  img = img / 255

  return img
  
def predict_image(filename, model, class_names=class_names):
  img = load_and_preprocess_image(filename.path)

  pred = model.predict(tf.expand_dims(img, axis=0))
  print(pred)

  class_name = class_names[tf.argmax(pred[0])]

  return class_name


def index(request):
    return JsonResponse({"working": "Yes it is working"})

# @api_view(['POST'])
# def image_view(request):

#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



class ImageModelVS(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def destroy(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"response": "Image has been deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

       


# class ImageView(APIView):
#     def post(self, request, format=None):
#         print(request.data)

#         # return Response({"ok":"ok"})
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictionView(APIView):
    def post(self, request, pk):
        with keras_utils.custom_object_scope({'KerasLayer': hub.KerasLayer}):
              model = keras.models.load_model("efficiennet_model_aug.h5")
        image = Image.objects.get(id=pk)
        uploaded_img = image.image 
        pred = predict_image(uploaded_img, model, class_names=class_names)
        image.prediction = pred
        image.save()

        return Response({"predicted class": pred})




        
