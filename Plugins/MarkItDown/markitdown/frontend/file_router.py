# markitdown/frontend/file_router.py
import sys
import os


from backend.excel_converter import ExcelConverter
from backend.word_converter import WordConverter
from backend.powerpoint_convertor import PptConverter
from backend.interfaces import IDocumentConverter

EXTENSION_MAP = {
    '.xlsx': ExcelConverter,
    '.xls': ExcelConverter,
    '.docx': WordConverter,
    '.doc': WordConverter,
    '.pptx': PptConverter,
    '.ppt': PptConverter,
    # You can add .pptx and .pdf handlers later when implemented
}

def get_converter(file_path: str) -> IDocumentConverter:
    _, ext = os.path.splitext(file_path.lower())
    if ext in EXTENSION_MAP:
        return EXTENSION_MAP[ext]()
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
