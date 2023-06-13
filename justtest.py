import qrcode

def generate_and_display_qrcode():  # 生成并显示二维码

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data('www.baidu.com')  # 二维码内容
    qr.make(fit=True)
    img = qr.make_image()
    img.show()