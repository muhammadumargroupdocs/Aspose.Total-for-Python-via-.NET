# test-powerpoint

import sys
import os

# Ensure markitdown module is in the Python path
# sys.path.append(os.path.join(os.path.dirname(__file__), 'markitdown'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from markitdown.backend.powerpoint_convertor import PptConverter

def main():
    pptx_file = "powerpoint_sample.pptx"  # Replace with your test file path
    converter = PptConverter()
    markdown = converter.convert_to_md(pptx_file)
    
    print("Generated Markdown:\n")
    print(markdown)

if __name__ == "__main__":
    main()
