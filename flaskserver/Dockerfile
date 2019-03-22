FROM python:3.7.2-slim

# Update aptitude with new repo
RUN apt-get update
RUN pip3 install flask python-logstash requests

# Create a work directory
RUN mkdir -p /usr/ikigailabs

# Copy all files
COPY management_manager /usr/ikigailabs

# Run service server in staging location
WORKDIR /usr/ikigailabs/

# Define entrypoint
CMD ["bash", "launch_server.sh"]


