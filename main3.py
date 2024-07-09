import cv2
import pytesseract
from tkinter import filedialog
from tkinter import Tk  

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   
    binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return binary_image

def perform_ocr(image):
    
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config, lang='eng')

    return text

def select_image():
    
    root = Tk()
    root.withdraw()  # 

    
    file_path = filedialog.askopenfilename(title="Selektine imazhin tuaj", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    
    root.destroy()

    return file_path

def main():
    
    image_path = select_image()

    if image_path:
     
        binary_image = preprocess_image(image_path)

        
        extracted_text = perform_ocr(binary_image)

        print("\n:Teksi i lexueshem")
        print(extracted_text)

      
        output_file_path = 'extracted_text.txt'
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(extracted_text)

        print(f"\nTeksti eshte ruajtur ne : {output_file_path}")
    else:
        print("\nJu nuk keni selektuar asnje imazh ")

if __name__ == "__main__":
    main()
