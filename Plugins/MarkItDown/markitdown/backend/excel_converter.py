# excel_converter.py
import clr
import os
import System

#import asposecells as ac
from .interfaces import IDocumentConverter

# Load the Aspose.Cells .NET DLL
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../lib/Aspose.Cells.dll"))
clr.AddReference(dll_path)

# Now import .NET types (VS Code will not recognize them)
from System.IO import MemoryStream, SeekOrigin
from Aspose.Cells import Workbook, SaveFormat, MarkdownSaveOptions,JsonSaveOptions,HtmlSaveOptions

class ExcelConverter(IDocumentConverter):
    def convert_to_md(self, file_path: str) -> str:
        workbook = Workbook(file_path)
        opts = MarkdownSaveOptions()
        stream = MemoryStream()
        workbook.Save(stream, opts)
        stream.Seek(0, SeekOrigin.Begin)
        # Read stream to string (as UTF-8)
        reader = System.IO.StreamReader(stream)
        markdown_text = reader.ReadToEnd()
        # return stream.to_array().tobytes().decode("utf-8")
        return markdown_text

    def convert_to_json(self, file_path: str) -> str:
        workbook = Workbook(file_path)
        opts = JsonSaveOptions()
        stream = MemoryStream()
        workbook.Save(stream, opts)
        stream.Seek(0, SeekOrigin.Begin)
        reader = System.IO.StreamReader(stream)
        json_text = reader.ReadToEnd()
        return json_text

    def convert_to_html(self, file_path: str) -> str:
        workbook = Workbook(file_path)
        opts = HtmlSaveOptions()
        stream = MemoryStream()
        workbook.Save(stream, opts)
        stream.Seek(0, SeekOrigin.Begin)
        reader = System.IO.StreamReader(stream)
        html_text = reader.ReadToEnd()
        return html_text