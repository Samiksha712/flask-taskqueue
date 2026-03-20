from flask import Flask, jsonify, render_template, request
from flask_taskqueue import FlaskTaskQueue, status_bp
from tasks import process_task


app = Flask(__name__)

task_queue = FlaskTaskQueue(app)

app.register_blueprint(status_bp)

decorated_process_task = task_queue.queue_task()(process_task)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/run-task", methods=["POST"])
def run_task():

    task_name = request.json.get('task_name', 'Unnamed Task')
    job_id = decorated_process_task(task_name)
    return jsonify({"job_id": job_id})
 
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

