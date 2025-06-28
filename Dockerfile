#Using the base image with Python 3.10
FROM python:3.10
 
#Set our working directory as app
WORKDIR /
#Copying the requirements file to the container
COPY requirements/ requirements/

#Installing Python packages through requirements.txt file
RUN pip install --upgrade pip
RUN pip install -r requirements/production.txt

# Copy the model's directory and server.py files
ADD ./app ./app

#Exposing port 5000 from the container
EXPOSE 5000
#Starting the Python application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main_app:app"]