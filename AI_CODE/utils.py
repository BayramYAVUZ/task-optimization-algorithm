import random
from task import Task

# --------------------------------------------------------------------
def generate_random_tasks(n=10, min_duration=1, max_duration=10, max_deadline=50):
    tasks = []
    for i in range(1, n + 1):
        processing = random.randint(min_duration, max_duration)
        due_time = random.randint(processing + 2, max_deadline)
        release_time = random.randint(0, 5) 

        t = Task(
            id=i,
            name=f"Task_{i}",
            processing_time=processing,
            due_time=due_time,
            release_time=release_time
        )

        tasks.append(t)

    return tasks
