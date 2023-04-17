
import { jsPDF } from "jspdf";

var fs = require('fs');

var imageAsBase64 = fs.readFileSync('C:/Users/Usuario/Downloads/CApa_MAP.png', 'base64');



var canvas = new Canvas();

const doc = new jsPDF({
    orientation: "landscape",
    unit: "in",
    format: [4, 2]
  });

  doc.addImage(imageAsBase64, 'PNG', 15, 40, 180, 160);
  doc.addPage();
  doc.text("Hello world!", 1, 1);
  doc.save("two-by-four.pdf");