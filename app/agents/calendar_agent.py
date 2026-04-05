def schedule_tasks(tasks):
    times = ["9:00 AM", "1:00 PM", "6:00 PM"]
    schedule = []

    for i, task in enumerate(tasks):
        schedule.append({
            "task": task,
            "time": times[i % len(times)]
        })

    return schedule
