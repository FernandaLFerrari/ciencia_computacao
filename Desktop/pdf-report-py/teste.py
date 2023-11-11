from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Create a canvas and add a rectangle to it
c = canvas.Canvas("link_test.pdf")
c.translate(inch, 9 * inch)
c.rect(inch,inch,1*inch,1*inch, fill=1)

# example.xlsx is in the same directory as the pdf
c.linkURL(r'example.xlsx', (inch, inch, 2*inch, 2*inch), relative=1)
c.save()