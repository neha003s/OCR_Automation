from PIL import Image
import pytesseract
# Load the image
image_path = "image/directory/path"
img = Image.open(image_path)
# Extract text
extracted_text = pytesseract.image_to_string(img, config='--psm 6')
# Save to .txt file
with open("output_text.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)
print("work.txt")
