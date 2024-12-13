import logging
from queue import PriorityQueue

logging.basicConfig(level=logging.INFO)

class TaskScheduler:
    def __init__(self):
        self.task_queue = PriorityQueue()

    def add_task(self, task_id, priority):
        """
        Add a task to the scheduling queue.
        Args:
            task_id (str): Unique identifier for the task.
            priority (int): Priority of the task (lower is higher priority).
        """
        self.task_queue.put((priority, task_id))
        logging.info(f"Task {task_id} added with priority {priority}.")

    def allocate_tasks(self):
        """
        Allocate tasks to available GPUs based on priority.
        Returns:
            str: The task being allocated (for simulation purposes).
        """
        if self.task_queue.empty():
            logging.info("No tasks to allocate.")
            return None
        priority, task_id = self.task_queue.get()
        logging.info(f"Allocating Task {task_id} with priority {priority}.")
        return task_id

if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.add_task("task_1", 1)
    scheduler.add_task("task_2", 2)
    scheduler.add_task("task_3", 0)
    scheduler.allocate_tasks()
    scheduler.allocate_tasks()
    scheduler.allocate_tasks()
