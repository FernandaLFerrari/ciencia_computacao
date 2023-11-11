from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import styles
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

# Create a PDF canvas
c = canvas.Canvas("justified_text.pdf", pagesize=letter)

# Define the coordinates and dimensions of the rectangle
x = 100  # X-coordinate
y = 500  # Y-coordinate
width = 400  # Width of the rectangle
height = 200  # Height of the rectangle

# Define the text to be justified
text = "This is an example of justified text. " * 10  # Create a long text for demonstration

# Define a style for the text
style = getSampleStyleSheet()["Normal"]
style.leading = 14  # Line spacing

# Create a text object
text_object = c.beginText(x, y)
text_object.setFont("Helvetica", 12)
text_object.setTextOrigin(x, y + height)
text_object.textLines(text)

# Calculate the width of the text
text_width = c.stringWidth(text, "Helvetica", 12)

# Calculate the space between words
space_width = (width - text_width) / (len(text.split()) - 1)

# Justify the text by adding spaces between words
for line in text.split("\n"):
    words = line.split()
    line_width = sum(c.stringWidth(word, "Helvetica", 12) for word in words)
    space_count = len(words) - 1
    if space_count > 0:
        space_size = space_width / space_count
    else:
        space_size = 0
    text_object.moveCursor(0, style.leading)
    for word in words:
        text_object.textLine(word)
        if space_count > 0:
            text_object.moveCursor(space_size, 0)
            space_count -= 1

# Draw the text on the canvas
c.drawText(text_object)

# Save the PDF file
c.save()