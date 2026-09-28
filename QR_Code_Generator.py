import qrcode
onLoop = True

while onLoop:
    url = input("Enter the URL: ").strip()
    fileName = input("Enter QR code file name: ")
    filePath = fileName + ".png"

    qr = qrcode.QRCode()
    qr.add_data(url)

    img = qr.make_image()
    img.save(filePath)

    print("Qr code generated succesfully")

    onLoop = input('Would you care to generate another QR code? (Y|N) ')
    while True:
        match onLoop:
            case 'Y' | 'y':
                break
            case 'N' | 'n':
                onLoop = False
                break
            case _:
                onLoop = input('Invalid input. Please choose between between (Y|N) ')
print("Thank you for using my project!")