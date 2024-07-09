import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def recognize_text(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(gray_image)

    return text

def main():
   
    cap = cv2.VideoCapture(0)

    while True:
        
        ret, frame = cap.read()

        
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
    
            text = recognize_text(frame)

           
            print("Teksi i lexueshem:", text)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

