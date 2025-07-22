# word_converter.py

import aspose.words as aw
from .interfaces import IDocumentConverter

class WordConverter(IDocumentConverter):
    def convert_to_md(self, file_path: str) -> str:
        doc = aw.Document(file_path)
        stream = aw.io.MemoryStream()
        doc.save(stream, aw.SaveFormat.MARKDOWN)
        stream.seek(0)
        return stream.read().decode("utf-8")

    def convert_to_json(self, file_path: str) -> str:
        raise NotImplementedError("Word to JSON conversion is not supported yet. Coming soon!")

    def convert_to_html(self, file_path: str) -> str:
        doc = aw.Document(file_path)
        stream = aw.io.MemoryStream()
        doc.save(stream, aw.SaveFormat.HTML)
        stream.seek(0)
        return stream.read().decode("utf-8")
