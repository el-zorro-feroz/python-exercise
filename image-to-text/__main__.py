import easyocr
import os


output_global_path = 'output/'


def readImage(image_path, output_file_name):
    try:
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image_path)

        with open(f'{output_global_path}{output_file_name}.txt', 'w') as f:
            for line in result:
                f.write(line[1] + '\n')
        
        print(f"Done. Output file: {output_global_path}")

    except Exception as e:
        print(f"An error occurred while reading: {e}")

            
if __name__ == "__main__":
    # Debug image asset
    # image_path = 'assets/image.png'

    image_name = input('Enter image path: (Example: C:/image.png) ')
    file_name = input('Enter result file name: (Example: result)')

    readImage(image_path=image_name, output_file_name=file_name)

