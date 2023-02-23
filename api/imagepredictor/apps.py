from django.apps import AppConfig
from tensorflow.keras.models import load_model
import os
from django.conf import settings
import warnings


class ImagepredictorConfig(AppConfig):
    warnings.filterwarnings('ignore')
    default_auto_field = "django.db.models.BigAutoField"
    name = "imagepredictor"
    MODEL_FILE = os.path.join(settings.MODELS, "vgg_model.h5")
    model = load_model(MODEL_FILE)
