from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Event
from .generate_vector import generate_embedding
from .save_vector_db import save_event_vector, delete_event_vector


@receiver(post_save, sender=Event)
def create_vector(sender, instance, created, **kwargs):
    if created:
        event_text = f"Event title: {instance.title} \n Event description: {instance.description}"
        vector = generate_embedding(event_text)
        save_event_vector(instance.id, instance.description,  vector)

@receiver(post_delete, sender=Event)
def delete_vector(sender, instance, **kwargs):
    delete_event_vector(instance.id)