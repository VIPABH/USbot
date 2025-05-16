from التخزين import config_vars
from typing import Any
import json
import os
def vars(key: str, file_path: str = "config.json") -> Any:
  config_vars()
  if not os.path.isfile(file_path):
      open(file_path, "w", encoding="utf-8").close()
      raise FileNotFoundError(f"[خطأ] تم إنشاء الملف '{file_path}' لأنه غير موجود، لكنه فارغ. يرجى تعبئته يدوياً.")
  try:
      with open(file_path, "r", encoding="utf-8") as f:
          data = json.load(f)
  except json.JSONDecodeError:
      raise ValueError(f"[خطأ] الملف '{file_path}' لا يحتوي على JSON صالح.")
  if key not in data:
      raise KeyError(f"[خطأ] المفتاح '{key}' غير موجود داخل '{file_path}'.")
  return data[key]
