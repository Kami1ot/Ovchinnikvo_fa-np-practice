import os
from file_manager import FileManager

def print_help():
    print("""
Доступные команды:
mkdir [имя_папки] - Создать папку
rmdir [имя_папки] - Удалить папку
cd [путь] - Перейти в папку
mkfile [имя_файла] - Создать файл
write [имя_файла] [текст] - Записать в файл
read [имя_файла] - Читать файл
rmfile [имя_файла] - Удалить файл
cpfile [источник] [назначение] - Копировать файл
mvfile [источник] [назначение] - Переместить файл
rename [старое_имя] [новое_имя] - Переименовать файл
exit - Выход
help - Показать справку
""")
    

def main():
    print("Простой файловый менеджер. Введите 'help' для списка команд.")
    fm = FileManager()

    while True:
        command = input(f"{fm.current_dir}> ").strip().split()
        action = command[0] if command else ''
        arguments = command[1:] if len(command) > 1 else []

        try:
            if action == "cd":
                fm.change_directory(*arguments)
            elif action == "mkdir":
                fm.make_directory(*arguments)
            elif action == "rmdir":
                fm.remove_directory(*arguments)
            elif action == "mkfile":
                fm.create_file(*arguments)
            elif action == "write":
                fm.write_to_file(*arguments)
            elif action == "read":
                fm.read_file(*arguments)
            elif action == "rmfile":
                fm.remove_file(*arguments)
            elif action == "cpfile":
                fm.copy_file(*arguments)
            elif action == "mvfile":
                fm.move_file(*arguments)
            elif action == "rename":
                fm.rename_file(*arguments)
            elif action == "exit":
                print("Выход из программы.")
                break
            elif action == "help":
                print_help()
            else:
                print("Неизвестная команда, введите 'help' для помощи.")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
