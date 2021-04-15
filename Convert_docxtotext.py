import docxpy

def docx_to_text(file_path):
    document = docxpy.process(file_path)

    return document