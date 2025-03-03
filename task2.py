from PIL import Image
import numpy as np
import os

def encrypt_decrypt_image(image_path, key, output_path):
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found!")
        return

    # Open the image and ensure it's RGB
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image, dtype=np.uint8)
    
    # Convert key to a numerical value
    key = int.from_bytes(key.encode(), 'big') % 256
    
    # Encrypt/Decrypt using XOR operation
    encrypted_array = image_array ^ key
    
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    
    # Save the encrypted/decrypted image
    encrypted_image.save(output_path)
    print(f"Processed image saved at: {output_path}")

# Example usage
image_path = "C:/Users/bhanuteja/Sandhya/task1/images/mpy.jpg"  # Use actual image path
output_path = "C:/Users/bhanuteja/Sandhya/task1/images/output.png"
key = "securekey"

encrypt_decrypt_image(image_path, key, output_path)
