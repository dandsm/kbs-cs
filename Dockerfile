# Use a base Python image (adjust version as needed)
FROM python:3.12

# Install SWI-Prolog (Debian/Ubuntu style)
RUN apt-get update && \
    apt-get install -y swi-prolog && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install PySWIP (so Python can interface with Prolog)
RUN pip install pyswip

# Create and set a working directory (inside the container)
WORKDIR /app

COPY ./. ./.

# The default command if you just run the container
CMD [ "sh" ]