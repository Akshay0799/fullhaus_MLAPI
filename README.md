# Overview
This repo contains the code for a Machine Learning model based API of a deep learning classifier trained to classify images. The code is wrapped into an API and containerised.

## Technologies
### VGG16
 VGG16 was used for the image classification task. After unfreezing the last layer of the neural netowork, transfer learning was performed on the current dataset and the trained model is saved in the 'models' directory which is located in 'api/imagepredictor'. The code for training the VGG16 model is in fulhaus_VGG16.ipynb
### Django
  The Wrapper API for the ML model was developed using Django. The server can be run on a port using Django with which the ML model can be accessed by hitting the end point of the Django server. Images can be fed to the server in the multi-part format.
### Docker
  Docker was utilized to containerize the API, build an image and automate the process of reproducing the code.
### CI/CD with Github Actions
  CI/CD workflows were implemented on Github actions to ensure that the code is runnning. Workflows to build the environment and test if the Django server is running without any bugs were written.
## Instructions to start the Django server in Docker

After cloning the repository and navigating to the project's root directory, ensure that docker is installed in your system and run the following command to build the docker image.

```
docker build . -t django-api
```
Once all the required packages are isntalled and the docker is built, run the following command to run the server from the docker.
```
docker run -it -p 8000:8000 django-api
```

This will run the Django server on the port 8000 of your system.

## Instructions to test the API using POSTMAN

Once the Django server is running, you can use Postman to test the API end-point. Open Postman and send a ```POST``` request to ```127.0.0.1:8000/api/v1```. Under ```Body```, choose the form-data category and set the key  of the content to ```image```. After setting the Key type to file, you can upload an image of your choice. On clicking the 'POST' button the post request will be sent to the backend, the ML model will be called to make a prediction and the output will be returned as the response in Postman. The output is in the Json format with the keys - 'Status' of the request and 'Prediction' from the model.

