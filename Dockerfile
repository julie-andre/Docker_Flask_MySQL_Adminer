FROM python:3
# Set the working directory for COPY and CMD instructions
WORKDIR /app
# Necessary otherwise recv failure
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copy the file containing the names of the librairies we need and install them
COPY requirements.txt requirements.txt

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port 5000 of the future container (on which it will listen for connections)
# Flask apps use port 5000 by default 
EXPOSE 5000

# We copy all the files (even if we don't need the dockerfile and ymal files because it
# is simpler to copy this way)
COPY . .
CMD ["flask", "run"]