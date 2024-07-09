import json
from typing import List, Dict, Tuple


def load_data_from_json(file_path: str) -> List[Dict]:
    """Функция загрузки данных из json-файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading data from {file_path}: {e}")


def get_attribute_frequency(data: List[Dict]) -> List[Tuple[str, int]]:
    """
    Анализирует данные и возвращает список атрибутов,
    отсортированных по убыванию частоты уникальных значений.

    Args:
        data: Список словарей, представляющих сущности и их признаки.

    Returns:
        Список кортежей (название_атрибута, количество_уникальных_значений),
        отсортированный по убыванию количества уникальных значений.
    """

    attribute_counts = {}
    for entity in data:
        for attribute, value in entity.items():
            if attribute not in attribute_counts:
                attribute_counts[attribute] = set()
            attribute_counts[attribute].add(value)

    sorted_attributes = sorted(attribute_counts.items(),
                               key=lambda item: len(item[1]),
                               reverse=True)
    return sorted_attributes
