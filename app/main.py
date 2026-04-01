import os


def move_file(command: str) -> None:
    cmnd, file_name, new_path = command.split(" ")
    if "/" in new_path:
        new_path_dir = new_path[:new_path.rfind("/")]
        if not os.path.exists(new_path_dir):
            os.makedirs(new_path_dir)
    os.rename(file_name, new_path)
