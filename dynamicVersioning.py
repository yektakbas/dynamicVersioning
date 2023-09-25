import subprocess
import os


def image_versioning():
    # Define the filenames and variables
    docker_file_name = "docker_images.txt"  # Replace with the actual file name
    version = "version.txt"
    versioned_image_file = "versioned_image_file.txt"

    try:
        # Open the file for reading
        with open(docker_file_name, "r") as file:
            # Initialize a list to store the extracted parts
            full_parts = []
            extracted_parts = []
            # Iterate through each line in the file
            for line in file:
                # Strip leading/trailing whitespace from the line
                line = line.strip()
                full_parts.append(line)

                # Split the line by '/' and get the last part (iiot-map-service:0.9.14)
                parts = line.split('/')
                last_part = parts[-1]

                # Split the last part by ':' and get the first part (iiot-map-service)
                service_name = last_part.split(':')[0]

                # Append the extracted service name to the list
                extracted_parts.append(service_name)

        with open(version, "r") as vr:
            # Read the content of the version.txt file
            version_content = vr.read().strip()

            # Check if version_content is a valid float or empty
            if version_content:
                # Convert version_content to float and increment by 0.1
                tag = float(version_content) + 0.1
                formatted_tag = "{:.2f}".format(tag)
            else:
                # Set a default value if version.txt is empty or not a valid float
                tag = 1.0
                formatted_tag = "{:.2f}".format(tag)

        with open(version, "w") as vr:
            vr.write(str(formatted_tag))

        # Open the versioned_image_file.txt for writing
        with open(versioned_image_file, "w") as vf:
            # Write versioned_image values to the file line by line
            print("Writing Versioned Images to versioned_image_file.txt:")
            for part in extracted_parts:
                image_name = part
                image_tag = formatted_tag
                versioned_image = f'harbor1.akillisebeke.lab/scada-botas/{image_name}:{image_tag}'
                tag_image_command = ["docker", "tag", line, versioned_image]
                vf.write(versioned_image + "\n")
                print(versioned_image)  # Print for verification

        print("Updated Tag Value:")
        print(formatted_tag)

    except FileNotFoundError:
        print(f"The file '{docker_file_name}' or '{version}' was not found.")
    except IOError as e:
        print(f"An error occurred while reading or writing the file: {e}")
