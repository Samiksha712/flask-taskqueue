import time
import random

def process_task(task_name: str):
    """
    Simulates a generic, multi-step background task.
    This is a realistic placeholder for any long-running business process.
    """
    print(f"Starting task: '{task_name}'")
    
 
    time.sleep(random.uniform(1, 2))
    print(f"'{task_name}': Step 1 of 3 complete.")
    
    time.sleep(random.uniform(1, 3))
    print(f"'{task_name}': Step 2 of 3 complete.")

    time.sleep(random.uniform(1, 2))
    print(f"'{task_name}': Step 3 of 3 complete.")
    
    print(f"Finished task: '{task_name}'")
    return f"'{task_name}' was processed successfully."
