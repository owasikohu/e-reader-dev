from PIL import Image

def convert_bmp_to_jpeg(input_bmp_path, output_jpeg_path, dpi):

    with Image.open(input_bmp_path) as bmp_image:

        bmp_image = bmp_image.convert("1")

        bmp_image.save(output_jpeg_path, format='JPEG', dpi=dpi)


input_bmp = 'main.bmp'
output_jpeg = 'print.jpg'
dpi_value = (600, 600)


convert_bmp_to_jpeg(input_bmp, output_jpeg, dpi=dpi_value)
