import pandas as pd
import pytesseract
# Explicitly set the path to the Tesseract binary
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

import cv2


def processImage(imagePath):
    img = cv2.imread(imagePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh

def extract_text(image):
    return pytesseract.image_to_string(image)


if __name__ == "__main__":
    image_path = "orders_data/WhatsApp Image 2025-05-17 at 10.17.20.jpeg"
    processed_image = processImage(image_path)
    extracted_text = extract_text(processed_image)
    
    print("Extracted Text:\n", extracted_text)

    