import json
import os
def get_json_value(key: str, file_path: str = "config.json"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"لم يتم العثور على الملف: {file_path}")
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            value = data.get(key)
            if value is None:
                raise KeyError(f"المفتاح '{key}' غير موجود في الملف.")
            return value
    except json.JSONDecodeError:
        raise ValueError(f"الملف {file_path} لا يحتوي على تنسيق JSON صالح.")
