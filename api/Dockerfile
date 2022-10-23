
# Working from Python version 3.9
FROM python:3.9-alpine

# setting the working directory inside the container to /code
WORKDIR /code

# setting up some environment variables for the flask command
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# installing some dependencies inside the container
RUN apk add --no-cache gcc musl-dev linux-headers

# copying the requirements.txt file from the host system to
# inside the container
COPY requirements.txt requirements.txt

# install requirements inside the container using pip
RUN pip install -r requirements.txt

# expose port 5000 from the container
EXPOSE 5000

# copy the contents of the current directory to the
# container's working directory
# TODO - Merge this with the COPY above or create a src dir that doesn't include requirements? 
COPY . .

# tell the container to run the flask application
CMD ["flask", "run"]