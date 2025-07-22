# powerpoint_convertor

import os
import io
import aspose.slides as slides
from .interfaces import IDocumentConverter
# from interfaces import IDocumentConverter

class PptConverter(IDocumentConverter):
    def convert_to_md(self, file_path: str) -> str:
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        markdown_file_path = os.path.join(output_dir, "converted_ppt.md")

        with slides.Presentation(file_path) as pres:
            save_options = slides.export.MarkdownSaveOptions()

            # Export visual content (includes images)
            save_options.export_type = slides.export.MarkdownExportType.VISUAL

            # Save images in same directory as markdown
            save_options.images_save_folder_name = "."  # Means "same directory"
            save_options.base_path = output_dir         # Same as where markdown will go

            # Optional: GitHub-flavored Markdown
            # save_options.flavor = slides.export.MarkdownFlavor.GITHUB

            pres.save(markdown_file_path, slides.export.SaveFormat.MD, save_options)

        with open(markdown_file_path, "r", encoding="utf-8") as f:
            return f.read()

    def convert_to_json(self, file_path: str) -> str:
        raise NotImplementedError("PowerPoint to JSON conversion is not supported yet. Coming soon!")

    def convert_to_html(self, file_path: str) -> str:
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        html_file_path = os.path.join(output_dir, "converted_ppt.html")
        with slides.Presentation(file_path) as pres:
            pres.save(html_file_path, slides.export.SaveFormat.HTML)

        with open(html_file_path, "r", encoding="utf-8") as f:
            return f.read()
