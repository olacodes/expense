FROM python:3.7

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install requirements
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

# copy application codebase
RUN mkdir /app
WORKDIR /app
COPY expense .
