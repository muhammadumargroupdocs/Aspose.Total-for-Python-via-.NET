# interfaces.py

from abc import ABC, abstractmethod

class IDocumentConverter(ABC):
    @abstractmethod
    def convert_to_md(self, file_path: str) -> str:
        pass

    @abstractmethod
    def convert_to_json(self, file_path: str) -> str:
        pass

    @abstractmethod
    def convert_to_html(self, file_path: str) -> str:
        pass


class IMarkdownPostProcessor(ABC):
    @abstractmethod
    def remove_images(self, markdown: str) -> str:
        pass

    @abstractmethod
    def encode_images_base64(self, markdown: str, base_path: str) -> str:
        pass

    @abstractmethod
    def ocr_images(self, markdown: str, base_path: str) -> str:
        pass

    @abstractmethod
    def convert_plain_math_to_latex(self, markdown: str) -> str:
        """Converts simple math expressions to LaTeX inside markdown"""
        pass
