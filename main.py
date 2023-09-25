
from docker import docker_rm, docker_load, image_file_create, image_push
from dynamicVersioning import image_versioning

docker_rm()
docker_load()
image_file_create()
image_versioning()
image_push


