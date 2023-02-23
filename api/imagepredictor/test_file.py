import pytest
from django.urls import reverse
from imagepredictor.views import call_model
from requests.packages.urllib3.filepost import encode_multipart_formdata
from django.test import RequestFactory



@pytest.mark.django_db 
def test_view():
    path = reverse("call_model")
    
    fields = {
        "image":("chair_test.jpg", open("chair_test.jpg").read(), "image/jpg"),
    }
    body, header = encode_multipart_formdata(fields)
    request = RequestFactory().get(path, headers={'Content-Type': header}, data=body)   # get the path for the list of contacts
    response = call_model(request)
    assert response.status_code == 200