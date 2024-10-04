import pathlib
import shutil


def rename_files():
    path_data = pathlib.Path.cwd() / "z_ProjectFiles"
    path_output = pathlib.Path.cwd() / "z_ProjectFiles" / "Renamed Files"
    path_output.mkdir(parents=True, exist_ok=True)

    for file in path_data.iterdir():
        if file != path_output:
            print(file)
            shutil.copy(file, path_output)

    for file in path_output.iterdir():
        name_of_the_file = file.name
        name_without_the_extension = name_of_the_file.replace('.txt', '')
        new_file_name = name_without_the_extension + "_desktop" + file.suffix
        file.rename(path_output / new_file_name)


if __name__ == '__main__':
    rename_files()