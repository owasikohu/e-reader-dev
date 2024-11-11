from PIL import Image

def convert_bmp_to_tiff(input_bmp_path, output_tiff_path, dpi):

    with Image.open(input_bmp_path) as bmp_image:

        bmp_image = bmp_image.convert("1")

        bmp_image.save(output_tiff_path, format='TIFF', dpi=dpi)

# 変換するファイルのパスを指定
input_bmp = 'main.bmp'  # ここに入力 BMP のパスを指定
output_tiff = 'print.tiff'  # ここに出力 TIFF のパスを指定
dpi_value = (600, 600)  # ここに希望の DPI を指定

# 変換実行
convert_bmp_to_tiff(input_bmp, output_tiff, dpi=dpi_value)
