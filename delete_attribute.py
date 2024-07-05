import json
import sys

def remove_attribute_from_json(file_path: str, attribute_name: str):
  """Удаляет указанный атрибут из каждого объекта в JSON-файле.

  Args:
    file_path: Путь к JSON-файлу.
    attribute_name: Название атрибута для удаления.
  """

  try:
    with open(file_path, 'r', encoding='utf-8') as f:
      data = json.load(f)

    for item in data:
      if attribute_name in item:
        del item[attribute_name]

    with open(file_path, 'w', encoding='utf-8') as f:
      json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Атрибут '{attribute_name}' успешно удален из файла {file_path}")

  except FileNotFoundError:
    print(f"Ошибка: Файл не найден: {file_path}")
  except json.JSONDecodeError:
    print(f"Ошибка: Некорректный JSON-формат в файле {file_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Ошибка: Необходимо указать имя файла и название атрибута.")
        print("Пример: python delete_attribute.py data.json about")
    else:
        file_path = sys.argv[1]
        attribute_name = sys.argv[2]
        remove_attribute_from_json(file_path, attribute_name)
