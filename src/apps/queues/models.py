from django.db import models
from django.db.models.signals import post_save
import uuid
from .scheduler import JobController


class Job(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    error = models.TextField(blank=True)

    def __str__(self):
        return f"Job-ID: {self.id}"


def post_save_run_job(sender, instance, created, *args, **kwargs):
    if created:
        task = JobController()
        task.job_weather_create()
post_save.connect(post_save_run_job, sender=Job)