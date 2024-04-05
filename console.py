import os
import shutil


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f'Папка "{folder_name}" создана успешно')
    except FileExistsError:
        print(f'Папка "{folder_name}" уже существует')


def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f'Папка "{folder_name}" удалена успешно')
    except FileNotFoundError:
        print(f'Папка "{folder_name}" не существует')


def change_directory(folder_name):
    try:
        os.chdir(folder_name)
        print(f'Перешли в папку "{folder_name}"')
        return True
    except FileNotFoundError:
        print(f'Папка "{folder_name}" не существует')
        return False


def create_file(file_name):
    with open(file_name, 'w'):
        pass
    print(f'Файл "{file_name}" создан успешно')


def write_to_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)
    print(f'Текст записан в файл "{file_name}"')


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'Файл "{file_name}" не существует')


def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f'Файл "{file_name}" удален успешно')
    except FileNotFoundError:
        print(f'Файл "{file_name}" не существует')


def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f'Файл "{source}" скопирован в "{destination}"')
    except FileNotFoundError:
        print('Не удалось скопировать файл')


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f'Файл "{source}" перемещен в "{destination}"')
    except FileNotFoundError:
        print('Не удалось переместить файл')


def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f'Файл "{old_name}" переименован в "{new_name}"')
    except FileNotFoundError:
        print(f'Файл "{old_name}" не существует')


def show_directory(my_folder, directory):
    a = current_directory().split("\\").index(my_folder)
    b = current_directory().split("\\").index(directory)

    mass = current_directory().split("\\")[a:b + 1]

    for i in range(len(mass)):
        print(f'¬{mass[i]}')
        print("    " * (i + 1), end="")
    print(end="\n")


def show_files_in_current_directory():
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
    for i in files:
        print(f'—{i}')


def show_folders_in_current_directory():
    current_dir = os.getcwd()
    folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]
    for i in folders:
        print(f'¬{i}')


def previous_directory():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    os.chdir(parent_dir)
    return parent_dir.split("\\")[-1]


# Главная функция для управления файловым менеджером
def current_directory():
    return os.getcwd()


def info():
    print('\nДоступные действия:')
    print('sh_fi. Показать файлы в директории')
    print('sh_fo. Показать папки в директории')
    print('pr_di. Возвращение в предыдущую директорию')
    print('cr_fo. Создать папку')
    print('de_fo. Удалить папку')
    print('ch_dr. Перейти в папку')
    print('cr_fi. Создать файл')
    print('wr_to_fi. Записать текст в файл')
    print('re_fi. Просмотреть содержимое файла')
    print('de_fi. Удалить файл')
    print('co_fi. Копировать файл')
    print('mo_fi. Переместить файл')
    print('re_fi. Переименовать файл')
    print('q. Выйти')


def main():
    my_folder = current_directory().split("\\")[-1]
    print(f'Корневая папка кода - {my_folder}')
    if not os.path.exists("test"):
        print("Создаем папку для теста...")
        os.makedirs("test")
        print(f'Папка "{"test"}" создана успешно')
    else:
        print(f'Папка "{"test"}" уже существует')
    change_directory("test")
    now_dir = 'test'
    my_folder = current_directory().split("\\")[-1]
    show_directory(my_folder, now_dir)
    while True:
        print(os.getcwd())
        show_directory(my_folder, now_dir)
        print("-" * 30)
        choice = input('Выберите действие: ')
        print("-" * 30)
        if choice == "sh_fi":
            # show_directory(my_folder, now_dir)
            show_files_in_current_directory()
        elif choice == "sh_fo":
            show_folders_in_current_directory()
        elif choice == "pr_di":
            if now_dir == my_folder:
                print("Это коренная папка!")
                continue
            else:
                now_dir = previous_directory()
                print("Возвращение в предыдущую директорию")
        elif choice == "info":
            info()
        elif choice == 'cr_fo':
            folder_name = input('Введите имя папки для создания: ')
            create_folder(folder_name)
        elif choice == 'de_fo':
            folder_name = input('Введите имя папки для удаления: ')
            delete_folder(folder_name)
        elif choice == 'ch_di':
            directory_name = input('Введите имя папки для перехода: ')
            if change_directory(directory_name):
                now_dir = directory_name

        elif choice == 'cr_fi':
            file_name = input('Введите имя файла для создания: ')
            create_file(file_name)
        elif choice == 'wr_to_fi':
            file_name = input('Введите имя файла для записи текста: ')
            text = input('Введите текст для записи в файл: ')
            write_to_file(file_name, text)
        elif choice == 're_fi':
            file_name = input('Введите имя файла для просмотра: ')
            read_file(file_name)
        elif choice == 'de_fi':
            file_name = input('Введите имя файла для удаления: ')
            delete_file(file_name)
        elif choice == 'co_fi':
            source = input('Введите имя исходного файла: ')
            destination = input('Введите имя папки для копирования: ')
            copy_file(source, destination)
        elif choice == 'mo_fi':
            source = input('Введите имя исходного файла: ')
            destination = input('Введите имя папки для перемещения: ')
            move_file(source, destination)
        elif choice == 'ren_fi':
            old_name = input('Введите текущее имя файла: ')
            new_name = input('Введите новое имя файла: ')
            rename_file(old_name, new_name)
        elif choice == 'q':
            break
        else:
            print('Некорректный ввод, попробуйте снова.')
        print("-" * 30)


if __name__ == '__main__':
    main()
