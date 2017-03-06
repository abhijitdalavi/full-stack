FROM tiangolo/uwsgi-nginx-flask:flask

COPY ./app /app

# FROM ubuntu:14.04
#
# # Update OS
# RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list
# RUN apt-get update
# RUN apt-get -y upgrade
#
# # Install Python
# RUN apt-get install -y python-dev python-pip
#
# # Add requirements.txt
# COPY requirements.txt .
#
# # Install uwsgi Python web server
# RUN pip install uwsgi
# # Install app requirements
# RUN pip install -r requirements.txt
#
# # Copy in code from app directory
# COPY ./app /app
#
# # Set the default directory for our environment
# # ENV HOME /webapp
# # WORKDIR /webapp
#
# # Expose port 8000 for uwsgi
# EXPOSE 8000
#
# # ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8000", "--module", "app:app", "--processes", "1", "--threads", "8"]
