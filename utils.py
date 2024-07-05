import json
from typing import List, Dict


def load_data_from_json(file_path: str) -> List[Dict]:
    """Функция загрузки данных из json-файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading data from {file_path}: {e}")