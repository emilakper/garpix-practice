from typing import List, Dict
from core.utils import load_data_from_json, get_attribute_frequency
from itertools import combinations
import argparse


def find_minimal_identifiers(data: List[Dict]) -> str:
    """
    Находит минимальный набор признаков для идентификации сущностей,
    учитывая комбинации признаков и отстутствие ключей как 'null'.

    Args:
        data: Список словарей, представляющих сущности и их признаки.

    Returns:
        Строка в формате CSV, содержащая имена идентифицирующих признаков.
    """

    num_entities = len(data)

    # Получаем отсортированный список атрибутов по информативности
    sorted_attributes = [attr for attr, _ in get_attribute_frequency(data)]

    for r in range(1, len(sorted_attributes) + 1):
        # Генерируем комбинации, начиная с самых информативных атрибутов
        for subset in combinations(sorted_attributes, r):
            seen_combinations = set()
            for entity in data:
                key = tuple(entity.get(attr) for attr in subset)
                seen_combinations.add(key)
            if len(seen_combinations) == num_entities:
                return ",".join(subset)
    return ""


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
