import subprocess
import os

def docker_rm():
    '''Remove all old docker images before versioning'''

    # Define the Docker command to list all images
    list_images_command = ["docker", "images", "-q"]

    # Run the command to list all image IDs
    try:
        result = subprocess.run(list_images_command, capture_output=True, text=True, check=True)
        image_ids = result.stdout.strip().split('\n')

        if not image_ids:
            print("No Docker images found to delete.")
        else:
            # Define the Docker command to delete images based on their IDs
            delete_images_command = ["docker", "rmi", "-f"] + image_ids

            # Run the command to delete images
            subprocess.run(delete_images_command, capture_output=True, text=True, check=True)

            print("Deleted Docker images successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def docker_load():
    '''Load new  docker images to the local docker prepository'''

    directory_path = "/root/kassg_image"

    # Get a list of .tar files in the directory
    image_files = [file for file in os.listdir(directory_path) if file.endswith(".tar")]

    if not image_files:
        print("No Docker image files found in the directory.")
    else:
        for image_file in image_files:
            # Define the Docker command to load images from the directory
            load_image_command = ["docker", "load", "-i", os.path.join(directory_path, image_file)]

            try:
                # Run the command to load the image
                subprocess.run(load_image_command, capture_output=True, text=True, check=True)
                print(f"Loaded Docker image from {image_file} successfully.")

            except subprocess.CalledProcessError as e:
                print(f"Error loading Docker image from {image_file}: {e}")


def image_file_create():
    '''Create images file that contain image name and tag'''
    # Define the Docker command to list all images
    list_images_command = ["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"]

    # Run the command to list all image names and tags
    try:
        result = subprocess.run(list_images_command, capture_output=True, text=True, check=True)
        image_info = result.stdout.strip().split('\n')

        if not image_info:
            print("No Docker images found.")
        else:
            # Write image names and tags to a text file
            with open("docker_images.txt", "w") as file:
                file.write("\n".join(image_info))

            print("Docker images written to docker_images.txt successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
