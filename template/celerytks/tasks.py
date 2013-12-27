import celery
app = celery.Celery()

@app.task
def addtest(x, y):
    return x + y
