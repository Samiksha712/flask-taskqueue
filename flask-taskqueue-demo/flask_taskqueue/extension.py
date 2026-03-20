import redis
from rq import Queue
from rq.job import Job
from flask import current_app
from functools import wraps
import os  # <-- Make sure to import 'os'

class FlaskTaskQueue:
    # Get Redis URL from an environment variable, with a fallback for local development
    def __init__(self, app=None, redis_url=os.environ.get("REDIS_URL", "redis://localhost:6379/0")):
        self.redis_url = redis_url
        self.redis_conn = None
        self.queue = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        # The rest of the file remains unchanged
        self.redis_conn = redis.from_url(self.redis_url)
        self.queue = Queue(connection=self.redis_conn)
        app.extensions['task_queue'] = self

    def queue_task(self):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                job = self.queue.enqueue(func, *args, **kwargs)
                return job.get_id()
            return wrapper
        return decorator

    def get_status(self, job_id):
        job = Job.fetch(job_id, connection=self.redis_conn)
        return {
            "id": job.get_id(),
            "status": job.get_status(),
            "result": job.result
        }
