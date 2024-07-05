import csv
import io
from typing import List, Dict
from utils import load_data_from_json
from itertools import combinations
import argparse


def find_minimal_identifiers(data: List[Dict]) -> str:
    """
    Находит минимальный набор признаков для идентификации сущностей,
    учитывая комбинации признаков.

    Args:
        data: Список словарей, представляющих сущности и их признаки.

    Returns:
        Строка в формате CSV, содержащая имена идентифицирующих признаков.
    """

    all_attributes = list(data[0].keys())  # Получаем список всех признаков
    num_entities = len(data)

    # Проверяем комбинации признаков, начиная с одиночных
    for r in range(1, len(all_attributes) + 1):
        for subset in combinations(all_attributes, r):
            temp_dict = {}
            for entity in data:
                try:  # <-- Добавляем блок try...except
                    key = tuple(entity[attr] for attr in subset)
                except KeyError:
                    continue  # Пропускаем сущность, если ключа нет

                if key not in temp_dict:
                    temp_dict[key] = 1
                else:
                    temp_dict[key] += 1

            # Если все ключи уникальны
            if len(temp_dict) == num_entities:  
                output = io.StringIO()
                writer = csv.writer(output)
                writer.writerow(subset)
                return output.getvalue() 

    return ""  # Возвращаем пустую строку, если комбинаций не найдено

def main(file_path: str = None) -> str:
    """
    Основная функция для обработки JSON и запуска алгоритма.

    Args:
        file_path: Путь к JSON-файлу с данными о сущностях.

    Returns:
        Строка в формате CSV с идентифицирующими признаками.
    """
    if file_path:
        data = load_data_from_json(file_path)
    else:
        raise ValueError("JSON-file path must be provided.")

    result = find_minimal_identifiers(data)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Путь к JSON-файлу")
    args = parser.parse_args()

    result = main(file_path=args.file_path)
    print(result)