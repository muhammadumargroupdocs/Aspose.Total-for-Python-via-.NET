import os
from markitdown.frontend.converter_service import ConverterService

DATA_DIR = "test"
OUTPUT_DIR = "test/output"

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def main():
    input_file = os.path.join(os.path.dirname(__file__), "WordTables.docx")
    output_file = os.path.join(os.path.dirname(__file__), "output_word.md")

def write_output(output_path, content):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


    converter = WordConverter()
    try:
        markdown = converter.convert_to_md(input_file)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Markdown successfully written to: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

def test_docx_to_markdown():
    ensure_output_dir()
    input_file = os.path.join(DATA_DIR, "WordTables.docx")
    output_file = os.path.join(OUTPUT_DIR, "WordTables.md")
    converter = ConverterService()
    markdown = converter.convert_to_markdown(input_file)
    write_output(output_file, markdown)


    assert len(markdown.strip()) > 0