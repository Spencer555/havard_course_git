FROM python:3
# copy anything in ur current directory and copy it to the specified location
COPY . /usr/src/app 
# change working directory to this
WORKDIR /usr/src/app
# install req in the working directory
RUN pip install -r requirements.txt 

# run this command when u startup the container
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]