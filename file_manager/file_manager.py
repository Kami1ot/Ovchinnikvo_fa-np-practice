import os
import shutil
from config import WORKING_DIRECTORY

class FileManager:
    def __init__(self):
        self.root = WORKING_DIRECTORY
        self.current_dir = self.root



    def change_directory(self, path):
        new_dir = os.path.realpath(os.path.join(self.current_dir, path))
        if new_dir.startswith(self.root) or new_dir.startswith("C:") and os.path.isdir(new_dir):
            self.current_dir = new_dir
        else:
            print("Переход запрещен.")

    def make_directory(self, dirname):
        os.makedirs(os.path.join(self.current_dir, dirname), exist_ok=True)

    def remove_directory(self, dirname):
        full_path = os.path.join(self.current_dir, dirname)
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            print("Папка не существует.")

    def create_file(self, filename):
        open(os.path.join(self.current_dir, filename), 'a').close()

    def write_to_file(self, filename, *content):
        with open(os.path.join(self.current_dir, filename), 'w') as file:
            file.write(" ".join(content))

    def read_file(self, filename):
        try:
            with open(os.path.join(self.current_dir, filename), 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("Файл не найден.")

    def remove_file(self, filename):
        try:
            os.remove(os.path.join(self.current_dir, filename))
        except FileNotFoundError:
            print("Файл не найден.")

    def copy_file(self, source, destination):
        src_path = os.path.join(self.current_dir, source)
        dst_path = os.path.join(self.current_dir, destination)
        shutil.copy(src_path, dst_path)

    def move_file(self, source, destination):
        src_path = os.path.join(self.current_dir, source)
        dst_path = os.path.join(self.current_dir, destination)
        shutil.move(src_path, dst_path)

    def rename_file(self, old_name, new_name):
        os.rename(os.path.join(self.current_dir, old_name), os.path.join(self.current_dir, new_name))

if __name__ == "__main__":
    fm = FileManager()
    fm.run()
