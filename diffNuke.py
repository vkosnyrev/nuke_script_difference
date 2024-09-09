import difflib
import re
import nuke


def decrement_version(match):
        version_number = match.group(1)  # Извлекаем текущую версию из объекта Match
        version_int = int(version_number)  # Преобразуем в число
        # Уменьшаем версию на 1 и форматируем с тем же количеством цифр
        previous_version = f"{version_int - 1:0{len(version_number)}d}"
        return f"_v{previous_version}.nk"

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except IOError:
        print(f"Не удалось открыть файл: {file_path}")
        return []

# Получаем путь к текущему скрипту
current_script_path = nuke.root().name()

# Проверяем, сохранен ли скрипт
if current_script_path == 'Root':
    print("Сценарий еще не сохранен.")
else:
    print(f"Текущий путь к скрипту: {current_script_path}")
    previous_script_path = re.sub(r'_v(\d+)\.nk$', decrement_version, current_script_path)


# Преобразуем тексты в строки
current_script_path_lines = current_script_path.splitlines(keepends=True)
previous_script_path_lines =  previous_script_path.splitlines(keepends=True)

# Сравниваем тексты
diff = difflib.unified_diff(current_script_path_lines, previous_script_path_lines, fromfile=current_script_path, tofile=previous_script_path)

# Печатаем различия
for line in diff:
    print(line)