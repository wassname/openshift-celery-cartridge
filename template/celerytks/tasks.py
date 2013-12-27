import celery
app = celery.Celery()
app.config_from_object('celeryconfig')

@app.task
def addtest(x, y):
    return x + y

@app.task
def run_spiders(name, **kwargs):
    """
    @param name: spider name
    """
    pass
