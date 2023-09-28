# your_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Record
from .consumer import model_post_save_handler

post_save.connect(model_post_save_handler, sender=Record)
