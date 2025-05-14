# import json
# import os
# from typing import Any
# def vars(key: str, file_path: str = "config.json") -> Any:
#     if not os.path.isfile(file_path):
#         raise FileNotFoundError(f"[خطأ] لم يتم العثور على الملف المطلوب: '{file_path}'")
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:
#             data = json.load(f)
#     except json.JSONDecodeError:
#         raise ValueError(f"[خطأ] الملف '{file_path}' لا يحتوي على JSON صالح.")
#     if key not in data:
#         raise KeyError(f"[خطأ] المفتاح '{key}' غير موجود داخل '{file_path}'.")
#     return data[key]
