# markitdown/main.py

import argparse
from frontend.converter_service import ConverterService

def main():
    parser = argparse.ArgumentParser(description="Convert Office files to Markdown")
    parser.add_argument("input", help="Path to input file (.docx, .xlsx, etc.)")
    parser.add_argument("-o", "--output", help="Path to save output markdown", default=None)

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--no-images", action="store_true", help="Remove image references")
    group.add_argument("--base64-images", action="store_true", help="Embed images as base64")
    group.add_argument("--ocr-images", action="store_true", help="Extract text from images using OCR")

    args = parser.parse_args()

    mode = None
    if args.no_images:
        mode = "no_images"
    elif args.base64_images:
        mode = "base64"
    elif args.ocr_images:
        mode = "ocr"

    service = ConverterService()
    markdown = service.convert_to_markdown(args.input, mode)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"✅ Markdown saved to: {args.output}")
    else:
        print(markdown)

if __name__ == "__main__":
    main()
