import qrcode

# O link ou texto que você quer no QR Code
dados = "https://www.google.com"

# Configura o QR Code
qr = qrcode.QRCode(version=1, box_size=1, border=1)
qr.add_data(dados)
qr.make(fit=True)

# O segredo está aqui: print_tty() desenha o QR Code usando caracteres do terminal
qr.print_tty()