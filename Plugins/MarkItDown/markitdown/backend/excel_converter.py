# excel_converter.py

import aspose.cells as ac
from interfaces import IDocumentConverter

class ExcelConverter(IDocumentConverter):
    def convert_to_md(self, file_path: str) -> str:
        workbook = ac.Workbook(file_path)
        opts = ac.MarkdownSaveOptions()
        stream = ac.system.io.MemoryStream()
        workbook.save(stream, opts)
        stream.seek(0)
        return stream.to_array().tobytes().decode("utf-8")

    def convert_to_json(self, file_path: str) -> str:
        workbook = ac.Workbook(file_path)
        stream = ac.system.io.MemoryStream()
        workbook.save(stream, ac.SaveFormat.JSON)
        stream.seek(0)
        return stream.to_array().tobytes().decode("utf-8")

    def convert_to_html(self, file_path: str) -> str:
        workbook = ac.Workbook(file_path)
        stream = ac.system.io.MemoryStream()
        workbook.save(stream, ac.SaveFormat.HTML)
        stream.seek(0)
        return stream.to_array().tobytes().decode("utf-8")
