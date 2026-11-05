import cv2

def detect_faces(image_path):
    # Load OpenCV's pre-trained Haar Cascade face classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load the input image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from '{image_path}'. Please check that 'group_photo.jpeg' is in your folder!")
        return

    # Convert the image to grayscale for accurate and fast cascade detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30)
    )

    print(f"Success! Found {len(faces)} face(s) in the image.")

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        # Draw a bright green rectangle (BGR: 0, 255, 0) with thickness of 2
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Add a text label above the box
        cv2.putText(img, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Save the processed output image
    output_path = 'detected_faces_output.jpg'
    cv2.imwrite(output_path, img)
    print(f"Processed image saved successfully as '{output_path}'")

    # Display the output image in a popup window
    cv2.imshow('Face Detector - Press any key to close', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_file = 'group_photo.jpeg'
    detect_faces(image_file)