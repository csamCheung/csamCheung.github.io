import os
import json

def create_image_json(directory):
    image_data = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".jpg", ".jpeg", ".png", ".gif")):
                image_path = os.path.join(root, file)
                image_name = os.path.splitext(file)[0]
                image_data.append({
                    "name": image_name,
                    "path": image_path
                })
    
    json_data = json.dumps(image_data, indent=4, ensure_ascii=False)
    print(json_data)
    with open("image_data.json", "w") as json_file:
        json_file.write(json_data)

# Provide the directory path here
directory_path = "image"

create_image_json(directory_path)
