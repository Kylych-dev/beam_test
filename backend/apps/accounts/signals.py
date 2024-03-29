from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_user_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'user_notifications',
            {
                'type': 'send_notification',
                'message': 'New user has been created!'
            }
        )