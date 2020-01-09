
import os
import pdf2image
import glob


def convert_to_jpeg(filepath, filename, output_path, max_pages=1):
    if (filepath is None) or (filename is None) or (output_path is None):
        print('filepath, filename and output_path are mandatory parameters')
        return None
    pdf2image.convert_from_path(os.path.join(filepath, filename),
                                output_folder=output_path,
                                first_page=1,
                                last_page=max_pages,
                                fmt='jpg')


def convert_all_pdfs(filepath, output_path, max_pages=1):
    if (filepath is None) or (output_path is None):
        print('filepath and output_path are mandatory parameters')
        return None
    start_loc = os.getcwd()
    os.chdir(filepath)
    filenames = glob.glob('*.pdf')
    os.chdir(start_loc)
    for filename in filenames:
        convert_to_jpeg(filepath, filename, output_path, max_pages)


test = True
if test:
    filepath = r'C:\python_projects\pdf_data_extraction\pdf_data_extraction\sample_pdfs'
    filename = '08_chapter 1.pdf'
    max_pages = 10
    output_path = r'C:\python_projects\pdf_data_extraction\pdf_data_extraction\pdf_images'
    convert_all_pdfs(filepath, output_path, max_pages)
