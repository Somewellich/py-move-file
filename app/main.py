import os


def move_file(command: str) -> None:
    action, source, destination = command.split(" ")
    path_parts = destination.split("/")
    target_file_name = path_parts.pop(-1)

    if target_file_name == "":
        target_file_name = source

    current_dir_path = ""
    for folder in path_parts:
        current_dir_path += folder + "/"
        if not os.path.exists(current_dir_path):
            os.mkdir(current_dir_path)

    with open(source, "r") as file:
        content = file.read()

    with open(os.path.join(current_dir_path, target_file_name), "w") as file:
        file.write(content)

    os.remove(source)
