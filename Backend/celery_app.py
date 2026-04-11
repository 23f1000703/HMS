from celery import Celery

celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
)

celery.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False,
)

from app import app
import time
#from mail import send_email
#from controllers.models import User

@celery.task()
def example_task():
    # with app.app_context():
        time.sleep(20)

        print("Task completed!")
        # return "Task completed!"
