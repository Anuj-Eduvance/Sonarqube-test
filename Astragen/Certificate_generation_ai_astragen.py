#!/usr/bin/env python3
import csv
from PIL import Image, ImageDraw, ImageFont
import os

# Configuration variables – adjust these as needed
image_path = "enablar_certi_v2_tmsv_astragen_template_ai.png"            # Path to the certificate image (PNG format)
csv_path = "2025 Database - Online Courses - Paid.csv"          # CSV file containing certificate details

# Specify the start and end rows (1-indexed)
start_row = 644                                      # For example, start at row 1
end_row = 736                                        # End at row 10 (inclusive)

# CSV column indices for certificate details (0-indexed)
cert_col = 1                                       # Column index (0-indexed) for certificate number
date_col = 4                                       # Column index (0-indexed) for date
name_col = 2                                       # Column index (0-indexed) for name
couse_name_col = 3                                 # Column index (0-indexed) for course name

regfont_path = ".\calibri-font-family\calibri-regular.ttf"          # Path to the TrueType font file

date_font_size = 85                                                  # Font size for date text 90

boldfont_path = ".\calibri-font-family\calibri-bold.ttf"
namefont_size = 160
coursefont_size = 130
certifont_size = 85                              # Font size for Certificate number text

output_path = "Mahindra_Certificate.png"           # Output image file name

output_folder = "generated_certificates"           # Output folder where generated certificates will be saved
output_filename_pattern = "{}.png"                 # Naming pattern for certificate files

def add_text_to_certificate(base_image_path, certificate_number, date, name, course_name, output_path):
    # Open the certificate image
    image = Image.open(base_image_path)
    draw = ImageDraw.Draw(image)

    # Load the TrueType font with the specified size
    certificatefont = ImageFont.truetype(boldfont_path, certifont_size)
    namefont = ImageFont.truetype(boldfont_path, namefont_size)
    coursefont = ImageFont.truetype(boldfont_path, coursefont_size)
    datefont = ImageFont.truetype(regfont_path, date_font_size)
    
    # Define positions for the text – update these coordinates as per your certificate layout
    number_position = (1450, 200)                  # Position for certificate number
    date_position = (2280, 2215)                   # Position for date (1050, 2330)
    name_position = (1760, 1080)                   # Position for name
    coursename_position = (1750,1630)                    # Position for course name

    # Set text color (e.g., black)
    fill_color_black = "black"
    fill_color_white = "white"
    
    # Draw the text onto the image
    draw.text(number_position, f"{certificate_number}", font=certificatefont, fill=fill_color_white)
    draw.text(date_position, f"{date}", font=datefont, fill=fill_color_black)
    draw.text(name_position, f"{name}", font=namefont, fill=fill_color_black, anchor = "mm")
    draw.text(coursename_position, f"{course_name}", font=coursefont, fill=fill_color_black, anchor = "mm")

    # Save the updated image
    image.save(output_path)
    print(f"Certificate saved as {output_path}")

def generate_certificates():
    """
    Reads the CSV file and generates a certificate for each row from start_row to end_row.
    The row numbers provided are 1-indexed.
    """
    # Read all rows from the CSV file into a list
    with open(csv_path, newline='') as csvfile:
        reader = list(csv.reader(csvfile))
    
    # Convert the 1-indexed start and end rows to 0-indexed values
    start_index = start_row - 1
    end_index = end_row - 1
    
    # Loop over each specified row
    for i in range(start_index, end_index + 1):
        try:
            row = reader[i]
            certificate_number = row[cert_col]
            date = row[date_col]
            name = row[name_col]
            course_name = row[couse_name_col]
            
            # Generate an output filename that includes the row number
            output_filename = os.path.join(output_folder,  output_filename_pattern.format(certificate_number + "_" + name))
            
            # Generate certificate for this row
            add_text_to_certificate(image_path, certificate_number, date, name, course_name, output_filename)
        except IndexError:
            print(f"Row {i+1} not found in CSV file.")
            continue

if __name__ == '__main__':
    generate_certificates()