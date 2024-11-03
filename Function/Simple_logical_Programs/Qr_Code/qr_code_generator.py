import qrcode

def qr_code_generator(fill_color= 'black', back_color='white'):
    data = input("Enter the text or url: ").strip()
    filename = input("Enter the filename: ").strip()
    qr = qrcode.QRCode(box_size=15, border=5)
    qr.add_data(data)
    img = qr.make_image(fill_color= fill_color, back_color=back_color)
    img.save(filename+'.jpg')
    print(f"QR code save as {filename}")

choice = input("Do you want to Customize your QR code Style? (Y / N): ").upper()
if choice == 'Y':
    fill_color = input("Enter a color name for fill color: ")
    back_color = input("Enter a color name for back color: ")
    qr_code_generator(fill_color, back_color)

else:
    qr_code_generator()