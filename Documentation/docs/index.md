# Setup

## Purpose and Scope
The purpose of this site is document a Payment Service. It is a service made for the discipline of Service Engineering, Computer Engineering and Telematics course at the University of Aveiro.

This service contemples just a generation and management of an account and the payments made by this account.

In the API TAB has a description of the methods of API. 
In the Thoughts and Decisions TAB has some publications to justify why was made a specific choice for a specific point in API

## Project Structure


    mkdocs.yml              # The configuration file.
    docs/
        index.md            # The documentation homepage.
        account.md          # The description about the account methods
        payment.md          # The description about the payment methods
        apiOperations.md    # Some considerations about the API
        about.md            # Some points about the author of the Service
        gunicorn.md         # The file descriving why using gunicorn
        img/                # A folder with the images used in the documentation

## How to initiate?

### Conventional

#### Create a virtual environment
```bash
    sudo pip install virtualenv
    virtualenv venv --python=python3
    source venv/bin/activate
```
#### Install the requirements
```bash    
    pip install -r requirements.pip
```
#### Initiate the Gunicorn

In the file PaymentService.py, you can change the exposed port for the database
```bash
    gunicorn PaymentService:app -b 0.0.0.0:6000
```
### Docker

You must install **docker** and **docker-compose**

Into the folder "Project" run the command :
```bash  
    docker-compose up
```

If you want run the containers in the background, change the command to:
```bash  
    docker-compose up -d
```
To stop the containers, inside the Project folder, run the command:
```bash  
    docker-compose stop
```
