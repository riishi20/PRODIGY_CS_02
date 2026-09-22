from PIL import Image
import numpy as np


def image_cryptor(image_path, key, mode):
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)

    key = np.resize(key, img_array.shape)

    if mode == "encrypt":
        result_array = np.bitwise_xor(img_array, key)
        result_img = Image.fromarray(result_array)
        result_img.save("encrypted_image.png")

        print("Image encrypted successfully.")

    elif mode == "decrypt":
        result_array = np.bitwise_xor(img_array, key)
        result_img = Image.fromarray(result_array)
        result_img.save("decrypted_image.png")

        print("Image decrypted successfully.")

    else:
        print("Invalid mode.")


def main():
    print("===== Image Encryption Tool =====")

    image_path = input("Enter path of image file: ")

    # Generate random key
    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)

    print("Encryption started...")

    image_cryptor(image_path, key, "encrypt")

    print("Decryption started...")

    image_cryptor("encrypted_image.png", key, "decrypt")


if __name__ == "__main__":
    main()
