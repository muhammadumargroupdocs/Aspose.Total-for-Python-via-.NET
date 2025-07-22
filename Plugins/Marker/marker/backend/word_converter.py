import os
import aspose.words as aw

from .interfaces import IDocumentConverter

class WordConverter(IDocumentConverter):
    def convert_to_md(self, file_path: str) -> str:
        doc = aw.Document(file_path)
        #with io.BytesIO() as dst_stream:
            #doc.save(stream=dst_stream, save_format=aw.SaveFormat.MARKDOWN)
        doc.save("temp.md")
        with open("temp.md", "r", encoding="utf-8") as f:
            content = f.read()
        os.remove("temp.md")
        return content        

    def convert_to_json(self, file_path: str) -> str:
        raise NotImplementedError("Word to JSON conversion is not supported yet. Coming soon!")

    def convert_to_html(self, file_path: str) -> str:
        doc = aw.Document(file_path)
        doc.save("temp.html")
        with open("temp.html", "r", encoding="utf-8") as f:
            content = f.read()
        os.remove("temp.html")
        return content        
    