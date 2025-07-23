import os
import sys

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from markitdown.backend.word_converter import WordConverter

def main():
    input_file = os.path.join(os.path.dirname(__file__), "WordTables.docx")
    output_file = os.path.join(os.path.dirname(__file__), "output_word.md")

    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}")
        return

    converter = WordConverter()
    try:
        markdown = converter.convert_to_md(input_file)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Markdown successfully written to: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    main()
