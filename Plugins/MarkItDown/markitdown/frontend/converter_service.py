# markitdown/frontend/converter_service.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from .file_router import get_converter
from backend.markdown_postprocessor import MarkdownPostProcessor
import os

class ConverterService:
    def __init__(self):
        self.processor = MarkdownPostProcessor()

    def convert_to_markdown(self, file_path: str, mode: str = None) -> str:
        converter = get_converter(file_path)
        markdown = converter.convert_to_md(file_path)
        base_path = os.path.dirname(file_path)

        if mode == "no_images":
            markdown = self.processor.remove_images(markdown)
        elif mode == "base64":
            markdown = self.processor.encode_images_base64(markdown, base_path)
        elif mode == "ocr":
            markdown = self.processor.ocr_images(markdown, base_path)

        return markdown
