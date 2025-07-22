# test_excel.py

import sys
import os

# Dynamically add the parent folder of "markitdown" to sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MARKITDOWN_PARENT = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.insert(0, MARKITDOWN_PARENT)

# Add path to "Plugins/MarkItDown" to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import your converter
from markitdown.backend.excel_converter import ExcelConverter

def main():
    converter = ExcelConverter()
    
    excel_file = os.path.join(os.path.dirname(__file__), "test.xlsx")
    try:
        markdown = converter.convert_to_md(excel_file)
        output_path = os.path.join(os.path.dirname(__file__), "excel_sample_output.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"✅ Markdown written to: {output_path}")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")

if __name__ == "__main__":
    main()
