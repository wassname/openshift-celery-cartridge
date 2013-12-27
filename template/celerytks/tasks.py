import celery
app = celery.Celery()

@app.task
def addtest(x, y):
    return x + y

@app.task
def run_spiders(name, **kwargs):
    """
    @param name: spider name
    """
    pass
