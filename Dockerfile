# Set up the base image: using python 3.14
FROM python:3.14
# move to the working directory inside the container 
WORKDIR /src

# copy the requirements.txt first
# theres noting in the requirements.txt file yet so we comment it out
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# copy the remaining project into the image
COPY . .

# this is documentation 
EXPOSE 5000

# running command 
CMD ["python", "-m","src.random_numbers"]