import qrcode
from PIL import Image
import io

# Función para generar y mostrar el código QR
def mostrar_qr(url):
    """
    Muestra un código QR generado a partir de la URL proporcionada.

    Args:
        url (str): La URL para la cual se generará el código QR.

    Returns:
        None
    """
    # Crear objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear imagen QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Mostrar imagen QR usando PIL (Python Imaging Library)
    img.show()

# URL que deseas incluir en el QR
url = "https://ceeeeeeees.github.io/Proyecto-Gestion/"

# Llamar a la función para mostrar el QR
mostrar_qr(url)
