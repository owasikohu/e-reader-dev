from PIL import Image

def convert_bmp_to_tiff(input_bmp_path, output_tiff_path, dpi):

    with Image.open(input_bmp_path) as bmp_image:

        bmp_image = bmp_image.convert("1")

        bmp_image.save(output_tiff_path, format='TIFF', dpi=dpi)


input_bmp = 'main.bmp'
output_tiff = 'print.tiff'
dpi_value = (600, 600)


convert_bmp_to_tiff(input_bmp, output_tiff, dpi=dpi_value)
