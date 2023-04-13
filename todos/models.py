from django.db import models

import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.core.exceptions import ValidationError
import base64


def validate_base64_image_size(value):
    """
    Validator function to ensure the base64-encoded image is not larger than 100MB.
    """
    try:
        decoded_image = base64.b64decode(value)
        if len(decoded_image) > 104857600:  # 100MB in bytes
            raise ValidationError("Image size cannot exceed 100MB.")
    except:
        raise ValidationError("Invalid image format.")


def validate_related_task_id(value):
    """
    Validator function to ensure the related task id exists in the Task model.
    """
    try:
        task = Todos.objects.get(task_id=value)
    except Exception as e:
        raise ValidationError("Related task id does not exist.")


PRIORITY_CHOICES = (
    (0, 'Urgent'),
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low'),
    (4, 'Trivial')
)


class Todos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2,
                                   validators=[MinValueValidator(0), MaxValueValidator(4)])
    completion_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=2000)
    project = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True, )
    share = ArrayField(models.EmailField(max_length=255), blank=True, null=True)
    references = ArrayField(models.URLField(max_length=2083), blank=True, null=True)
    related = ArrayField(models.UUIDField(validators=[validate_related_task_id]), blank=True, null=True)
    estimate = models.CharField(max_length=20, blank=True, null=True,
                                validators=[RegexValidator(r'^\d+(w|d|h|m)$')])  # weeks, days, hours, minutes
    note_array = ArrayField(models.CharField(max_length=200, blank=True), blank=True, null=True)

    def __str__(self):
        return self.note

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
