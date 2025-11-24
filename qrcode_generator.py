import qrcode
from PIL import Image

def generate_qrcode(data, size=300, file_name="qrcode.png"):
    qr = qrcode.QRCode(
        # Controla o tamanho (1 a 40)
        version=1,
        # Correcao de erro
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Cria a imagem
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Muda tamanho da imagem
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    
    # Salvar a imagem
    img.save(file_name)
    print(f"QR Code generated successfully: {file_name}")
    print(f"Size: {size}x{size} pixels")
    
    return img

if __name__ == "__main__":
    generate_qrcode(
        data="https://github.com/KalilMassignaniDaRosa",
        size=1000,
        file_name="qrcode.png"
    )