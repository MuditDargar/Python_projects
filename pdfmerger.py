from PyPDF2 import PdfMerger

def merge_pdf(input_files, output_file):
    merger = PdfMerger()
    
    for file in input_files:
        merger.append(file)
    
    merger.write(output_file)
    merger.close()

# Example usage
input_files = ['E:\Desktop\Python Project\projects\oops 1.pdf', 'E:\Desktop\Python Project\projects\oops 2.pdf']  # Replace with your input PDF files
output_file = 'merged.pdf'  # Replace with the desired output file name

merge_pdf(input_files, output_file)
