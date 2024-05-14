from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap 


def Report():
    # Define the table data
    table_data = [

        ["WSTG-INFO-01", "Conduct Search Engine Discovery Reconnaissance for Information Leakage"," ", "Pass"],
        ["WSTG -INFO-02", "Fingerprint Web Server", " -", "N/A"],
        ["WSTG -INFO-03", "Review Webserver Metafiles for Information Leakage","- ", "N/A"],
        ["WSTG-INFO-04", "Enumerate Applications on Webserver", "- ", "N/A"],
        ["WSTG-INFO-05", "Review Web Page Content for Information Leakage", " -", "Fail"],
        ["WSTG-INFO-06", "Identify Application Entry Points", "- ", "N/A"],
        ["WSTG-INFO-07", "Map Execution Paths Through Application", "-", "N/A"],
        ["WSTG-INFO-08", "Fingerprint Web Application Framework", "- ", "N/A"],
        ["WSTG-INFO-09", "Fingerprint Web Application (Merged into WSTG-INFO-08)", " -", "N/A"],
        ["WSTG-INFO-10", "Map Application Architecture", "- ", "N/A"],
        ["WSTG", "Information Gathering", "Description", "Result"]
    ]

    # Function to wrap text
    def wrap_text(text, width):
        return "\n".join(textwrap.wrap(text, width))

    # Update table_data to use wrap_text for long descriptions
    for row in table_data:
        if len(row) > 2:  # Assuming the third column contains the description
            row[2] = wrap_text(row[2], 140)  # Adjust the width as needed

    # Define the table width and height
    table_width = 540
    table_height = 720

    # Define the table border width and color
    table_border_width = 1
    table_border_color = (0, 0, 0)

    # Define the table cell padding
    table_cell_padding = 5
    header_row_padding = 10

    # Define the table cell widths
    table_cell_widths = [50, 140, 280, 50]

    # Define the table cell height
    table_cell_height = 20

    # Define the PDF page size
    page_width = letter[0]
    page_height = letter[1]

    # Define the color dictionary with corrected RGB values
    color_dict = {
        "Green": (0, 255, 0),  # Corrected to 0-255 range
        "Red": (255, 0, 0),    # Corrected to 0-255 range
        "Blue": (0, 0, 255)    # Corrected to 0-255 range
    }

    # Define the header row background color
    header_row_background_color = (230, 230, 230)

    # Create a new PDF file
    pdf_file = "table.pdf"
    c = canvas.Canvas(pdf_file, pagesize=(page_width, page_height))

    # Calculate the table position on the page
    table_x = (page_width - table_width) / 2
    table_y = (page_height - table_height) / 2

    # Draw the table border
    for i in range(5):
        c.line(table_x, table_y + i, table_x + table_width, table_y + i)
        c.line(table_x + i, table_y, table_x + i, table_y + table_height)

    # Draw the table cells
    for row_index, row_data in enumerate(table_data):
        is_header_row = row_index == 0
        if is_header_row:
            row_background_color = header_row_background_color
        else:
            row_background_color = (255, 255, 255)

        for col_index, cell_data in enumerate(row_data):
            cell_x = table_x + table_cell_padding + sum(table_cell_widths[:col_index])
            if is_header_row:
                cell_y = table_y + header_row_padding + row_index * table_cell_height
            else:
                cell_y = table_y + table_cell_padding + row_index * table_cell_height
            cell_width = table_cell_widths[col_index]
            cell_height = table_cell_height

            # Determine the background color based on the row type
            #background_color = row_background_color

                    # Determine the background color based on the cell content
            if cell_data == "Pass":
                background_color = color_dict["Green"]  # Use the green color from color_dict
            elif cell_data == "Fail":
                background_color = color_dict["Red"]  # Use the red color from color_dict
            else:
                background_color = row_background_color  # Default to row background color

            # Draw the cell background
            #c.rect(cell_x, cell_y, cell_width, cell_height, fill=background_color)

            # Draw the cell text with black color
            c.setFillColor((0, 0, 0))  # Set text color to black
            c.drawString(cell_x + table_cell_padding, cell_y + table_cell_padding, cell_data)

            # Optionally, draw a border around the cell
            c.setStrokeColor(table_border_color)
            c.line(cell_x, cell_y, cell_x + cell_width, cell_y)
            c.line(cell_x, cell_y, cell_x, cell_y + cell_height)
            c.line(cell_x + cell_width, cell_y, cell_x + cell_width, cell_y + cell_height)
            c.line(cell_x, cell_y + cell_height, cell_x + cell_width, cell_y + cell_height)

    # Save the PDF file
    c.save()