from flask import Blueprint, jsonify, current_app

status_bp = Blueprint("task_status", __name__)

@status_bp.route("/task_status/<job_id>", methods=["GET"])
def task_status(job_id):

    task_queue = current_app.extensions.get("task_queue")
    if not task_queue:
        return jsonify({"error": "TaskQueue not initialized"}), 500

    try:
        status = task_queue.get_status(job_id)
        return jsonify(status)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
