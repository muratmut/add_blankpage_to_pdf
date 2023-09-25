import PyPDF2


def main():
    input_pdf = 'C:\\Users\\mutmu\\OneDrive\\Desktop\\output\\input_book.pdf'
    output_pdf = 'C:\\Users\\mutmu\\OneDrive\\Desktop\\output\\output_book.pdf'

    first_page_number = 23
    # It will start adding blank pages after page 24, i.e., 24, blank, 25, blank etc.
    # Note that if you want to start from page 24, first_page_number should be 23
    add_blank_pages(first_page_number, input_pdf, output_pdf)


def add_blank_pages(first_page_number, input_pdf, output_pdf):
    with open(input_pdf, 'rb') as original_file:
        original_pdf = PyPDF2.PdfReader(original_file)
        num_pages = len(original_pdf.pages)

        # Create a new PDF
        new_pdf = PyPDF2.PdfWriter()

        for page_num in range(0, num_pages):
            # Add the original page to the new PDF
            page = original_pdf.pages[page_num]
            new_pdf.add_page(page)
            if page_num >= first_page_number:
                new_pdf.add_blank_page()

        # Save the new PDF to a file
        with open(output_pdf, 'wb') as output_file:
            new_pdf.write(output_file)

    print('done')


if __name__ == '__main__':
    main()
