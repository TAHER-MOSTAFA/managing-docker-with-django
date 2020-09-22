from celery import shared_task
from .models import Docker
import docker



client = docker.from_env()


@shared_task
def MakingContainer(instance_id):
    instance = Docker.objects.get(id=instance_id)
    cn = client.containers.run(image=instance.image,command=instance.command,detach=True)
    instance.cotainer_id = cn.id
    instance.status = 'Done'
    instance.save()
