# Flask-TaskQueue Plugin

A simple reusable Flask extension that allows you to enqueue background tasks using Redis Queue (RQ).

## Features
- Turn any function into a background task using a decorator
- Check task status via a built-in blueprint
- Works as a global plugin service shared among apps

## Setup
1. Start Redis:
   \\\ash
   docker run --name redis -d -p 6379:6379 redis:6.0
   \\\

   Confirm it’s running:
   \\\ash
   docker ps
   \\\


2. Start an RQ Worker:
   \\\ash
   cd flask-taskqueue-demo
   rq worker -w rq.worker.SimpleWorker --path .\example_app
   \\\

3. Run the Flask app:
   \\\ash
   cd flask-taskqueue-demo
   python app.py
   \\\






## To set up this project for first time : 

python --version

python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

pip install -e .


## open docker(terminal 1):

1. docker run --name redis -d -p 6379:6379 redis:6.0

## Confirm it’s running:

2. docker ps

## Start the RQ worker (Terminal 2):

3. cd flask-taskqueue-demo

4. .\.venv\Scripts\Activate.ps1

5. rq worker -w rq.worker.SimpleWorker --path .\example_app

## Run (Terminal 3): 

6. cd example_app

7. .\.venv\Scripts\Activate.ps1

8. python app.py
