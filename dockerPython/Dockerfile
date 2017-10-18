# FROM alpine:latest
# # Standard docker hub python 3 image setup
# RUN apk add --no-cache python3 && \
#     python3 -m ensurepip && \
#     rm -r /usr/lib/python*/ensurepip && \
#     pip3 install --upgrade pip setuptools && \
#     rm -r /root/.cache
#
# # These are the requirements needed for the image to run, specified in requirements.txt
# COPY requirements.txt /tmp/
# RUN pip3 install -qr /tmp/requirements.txt
#
# # copy over our app folder to the /app folder in docker
# COPY ./app /app
# # Now tell docker where our working directory is
# # WORKDIR /app
# # EXPOSE 80
# # CMD ["main.py"]

FROM tiangolo/uwsgi-nginx-flask:flask

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY ./app /app

# set an environmental variable, MESSAGE,
# which the app will use and display
ENV MESSAGE "hello from Docker"
