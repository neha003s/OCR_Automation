# OCR_Automation
This project demonstrates how to extract readable and editable text from an image using Python.
It applies a technique called Optical Character Recognition (OCR) — a method that allows computers to "read" text inside image files. The goal is to take a scanned document or image (like a photo of a textbook or screenshot) and automatically convert it into a plain text file with perfect accuracy in terms of formatting, capitalization, punctuation, and line breaks.

# Expectation
 extract all the text without manually typing it out. This project automates that task.
- Opens an image from your computer
- Reads and understands the text using OCR
- Writes that text into a text file exactly as it appears in the image

# Tools & Technologies
- Python
- Tesseract-OCR, An open-source OCR engine developed by Google that performs the actual text recognition.
- pytesseract, A Python wrapper for Tesseract that lets us access its power from Python scripts.
- Pillow (PIL), A Python imaging library used to open and manipulate images before sending them to Tesseract.
