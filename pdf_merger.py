import PyPDF2
import os 

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page_index in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page_index])

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def split_pdfs(input_path, output_path, split_at):
    pdf_reader = PyPDF2.PdfReader(input_path)
    
    pdf_writer = PyPDF2.PdfWriter()
    spliter_index = 0
    spliter = split_at[spliter_index]
    for page_index in range(len(pdf_reader.pages)): 
        if page_index == spliter:
            output_file_path = output_path + f'-part{spliter_index+1}.pdf'
            with open(output_file_path, 'wb') as out:
                 pdf_writer.write(out)
            
            spliter_index += 1
            if spliter_index < len(split_at):
                spliter = split_at[spliter_index]
            
            pdf_writer = PyPDF2.PdfWriter()

        pdf_writer.add_page(pdf_reader.pages[page_index])    
    
    output_file_path = output_path + f'-part{spliter_index+1}.pdf'
    with open(output_file_path, 'wb') as out:
        pdf_writer.write(out)


def merge_pdfs_from_directory(input_directory, output_directory):
    pdf_writer = PyPDF2.PdfWriter()
    file_paths = []
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    for path in file_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page_index in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page_index])

    # Write out the merged PDF
    with open(output_directory, 'wb') as out:
        pdf_writer.write(out)


# input_path = 'source/CanadianImmigrationRecords.pdf'
# output_path = 'output/CanadianImmigrationRecords.pdf'
# split_at = [1]

# split_pdfs(input_path, output_path, split_at)

#pdf_files = ['source/AccountDescription.pdf', 'source/January 18, 2024.pdf', 'source/December 18, 2023.pdf', 'source/November 17, 2023.pdf', 'source/October 18, 2023.pdf', 'source/September 18, 2023.pdf', 'source/August 18, 2023.pdf']
#pdf_files = ['source/AccountDescription.pdf', 'source/January 9, 2024.pdf', 'source/December 8, 2023.pdf', 'source/November 9, 2023.pdf']
pdf_files = ['source/RentalAgreement.pdf', 'source/rental addendum-2024-2025.pdf']

output_path = 'output/RentalAgreement2024-2025.pdf'

merge_pdfs(pdf_files, output_path)


# input_directory = 'source/paystubs'
# output_directory = 'output/paystubs.pdf'

# merge_pdfs_from_directory(input_directory, output_directory)