import os
from pdf2image import convert_from_path


def extract_images_from_pdf():
    for file in os.listdir('reports'):
        pages = convert_from_path('reports/' + file, 500)
        pages[2].save('images/' + file.replace('.pdf', '.jpg'), 'JPEG')
        print("Extracted " + file + " ...")
