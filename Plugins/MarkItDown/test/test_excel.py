import os
from markitdown.frontend.converter_service import ConverterService

DATA_DIR = "test"
OUTPUT_DIR = "test/output"

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def write_output(output_path, content):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
def test_xlsx_to_markdown():
    ensure_output_dir()
    input_file = os.path.join(DATA_DIR, "test-01.xlsx")
    output_file = os.path.join(OUTPUT_DIR, "test-01_xlsx.md")

    converter = ConverterService()
    markdown = converter.convert_to_markdown(input_file)
    write_output(output_file, markdown)

    assert "| " in markdown or len(markdown.strip()) > 0