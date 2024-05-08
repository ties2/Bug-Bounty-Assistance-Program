# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter

# def print_sum(numbers):
#     sum_of_numbers = sum(numbers)
#     return f"The sum of the numbers is: {sum_of_numbers}"

# def generate_pdf(data, output_path):
#     c = canvas.Canvas(output_path, pagesize=letter)
#     c.drawString(50, 750, data)
#     c.save()

# # Example usage:
# numbers = [1, 2, 3, 4, 5]
# result = print_sum(numbers)
# generate_pdf(result, "output.pdf")

########################################
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Define the table data
table_data = [
    ["WSTG", "Information Gathering", "Description", "Result"],
    ["WSTG-INFO-01", "Conduct Search Engine Discovery Reconnaissance for Information Leakage", "Pass", "Green"],
    ["WSTG -INFO-02", "Fingerprint Web Server", "Pass", "Green"],
    ["WSTG -INFO-03", "Review Webserver Metafiles for Information Leakage", "Pass", "Green"],
    ["WSTG-INFO-04", "Enumerate Applications on Webserver", "Pass", "Green"],
    ["WSTG-INFO-05", "Review Web Page Content for Information Leakage", "Pass", "Green"],
    ["WSTG-INFO-06", "Identify Application Entry Points", "Fail", "Red"],
    ["WSTG-INFO-07", "Map Execution Paths Through Application", "Pass", "Green"],
    ["WSTG-INFO-08", "Fingerprint Web Application Framework", "Pass", "Green"],
    ["WSTG-INFO-09", "Fingerprint Web Application (Merged into WSTG-INFO-08)", "Pass", "Green"],
    ["WSTG-INFO-10", "Map Application Architecture", "Pass", "Green"]
]

# Define the table width and height
table_width = 540
table_height = 720

# Define the table border width and color
table_border_width = 1
table_border_color = (0, 0, 0)

# Define the table cell padding
table_cell_padding = 5

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
    "Red": (255, 0, 0)     # Corrected to 0-255 range
}

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
# for row_index, row_data in enumerate(table_data):
#     for col_index, cell_data in enumerate(row_data):
#         cell_x = table_x + table_cell_padding + sum(table_cell_widths[:col_index])
#         cell_y = table_y + table_cell_padding + row_index * table_cell_height
#         cell_width = table_cell_widths[col_index]
#         cell_height = table_cell_height

#         # Draw the cell border
#         c.line(cell_x, cell_y, cell_x + cell_width, cell_y)
#         c.line(cell_x, cell_y, cell_x, cell_y + cell_height)
#         c.line(cell_x + cell_width, cell_y, cell_x + cell_width, cell_y + cell_height)
#         c.line(cell_x, cell_y + cell_height, cell_x + cell_width, cell_y + cell_height)

#         # Draw the cell text with correct color
#         text_color = color_dict.get(cell_data, (0, 0, 0))  # Default to black if no color match found
#         c.setFillColor(text_color)
#         c.drawString(cell_x + table_cell_padding, cell_y + table_cell_padding, cell_data)
#         c.setFillColor((0, 0, 0))  # Reset fill color to black after drawing


# Draw the table cells
for row_index, row_data in enumerate(table_data):
    for col_index, cell_data in enumerate(row_data):
        cell_x = table_x + table_cell_padding + sum(table_cell_widths[:col_index])
        cell_y = table_y + table_cell_padding + row_index * table_cell_height
        cell_width = table_cell_widths[col_index]
        cell_height = table_cell_height

        # Determine the background color based on the Result
        if cell_data in color_dict:
            background_color = color_dict[cell_data]
        else:
            background_color = (255, 255, 255)  # Default to white if no color match found

        # Draw the cell background
        c.rect(cell_x, cell_y, cell_width, cell_height, fill=background_color)

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
