#Create a ubuntu base image with python 3 installed.
FROM python:3

#Set the working directory
WORKDIR /assignment4MD

#copy all the files from current dir into image's working directory
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

#Expose the required port
EXPOSE 5000

#Run the command
CMD ["python3", "./main.py"]

CMD ["python3", "./app.py"]

CMD ["flask", "run", "-h", "172.17.0.2", "-p", "5000"]