import pytest
from django.urls import reverse, resolve
from imagepredictor.views import call_model
from requests.packages.urllib3.filepost import encode_multipart_formdata
from django.test import RequestFactory


# Sends a sample empty get request to check if the server is running
@pytest.mark.django_db 
def test_view():
    path = reverse("call_model_prediction")
    status = ""

    request = RequestFactory().get(path)
    response = call_model().get(request)
    status = response.status_code
    assert status == 200

# Checks if the url to which requests are sent is right
def test_url():            
    path = reverse('call_model_prediction')
    print(path)     
    assert resolve(path).view_name == "call_model_prediction"