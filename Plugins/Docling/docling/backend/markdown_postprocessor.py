# markdown_postprocessor.py

import base64
import os
import re
from interfaces import IMarkdownPostProcessor
from PIL import Image
import pytesseract

class MarkdownPostProcessor(IMarkdownPostProcessor):
    def remove_images(self, markdown: str) -> str:
        return re.sub(r'!\[.*?\]\(.*?\)', '', markdown)

    def encode_images_base64(self, markdown: str, base_path: str) -> str:
        def embed(match):
            alt_text, img_path = match.groups()
            full_path = os.path.join(base_path, img_path)

            if not os.path.isfile(full_path):
                return match.group(0)

            with open(full_path, 'rb') as f:
                encoded = base64.b64encode(f.read()).decode('utf-8')
                ext = os.path.splitext(full_path)[1][1:]  # "png", "jpg"
                return f'![{alt_text}](data:image/{ext};base64,{encoded})'

        return re.sub(r'!\[(.*?)\]\((.*?)\)', embed, markdown)

    def ocr_images(self, markdown: str, base_path: str) -> str:
        def extract_text(match):
            alt_text, img_path = match.groups()
            full_path = os.path.join(base_path, img_path)

            if not os.path.isfile(full_path):
                return match.group(0)

            try:
                text = pytesseract.image_to_string(Image.open(full_path)).strip()
                return f'**Extracted Text:** {text}'
            except Exception:
                return match.group(0)

        return re.sub(r'!\[(.*?)\]\((.*?)\)', extract_text, markdown)

    def convert_plain_math_to_latex(self, markdown: str) -> str:
        def looks_like_plain_math(line: str) -> bool:
            return any(sym in line for sym in ['×', '10^-', 'θ=', 'rad', '=sin', '=cos'])

        def convert_line(line: str) -> str:
            line = re.sub(r'10\^(-?\d+)', r'10^{\1}', line)
            line = line.replace('×', r'\times')
            line = re.sub(r'sin-1', r'\sin^{-1}', line)
            line = re.sub(r'cos-1', r'\cos^{-1}', line)
            line = re.sub(r'\bsin\b', r'\\sin', line)
            line = re.sub(r'\bcos\b', r'\\cos', line)
            line = line.replace('θ', r'\theta')
            line = line.replace('∘', r'^{\circ}')
            return f"$$\n{line.strip()}\n$$"

        lines = markdown.splitlines()
        processed_lines = [
            convert_line(line) if looks_like_plain_math(line) else line
            for line in lines
        ]
        return "\n".join(processed_lines)