"""
Gera logo Era da I.A. em PNG para redes sociais.
Saída: logo-180.png (perfil), logo-512.png (alta resolução)
"""
from PIL import Image, ImageDraw, ImageFont
import math, os

def draw_logo(size=512):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    s = size

    # — Fundo arredondado dark —
    radius = s * 0.22
    bg_color = (15, 23, 42)       # #0f172a
    rect = [0, 0, s, s]

    # Desenhar retângulo arredondado como fundo
    d.rounded_rectangle(rect, radius=radius, fill=bg_color)

    cx, cy = s / 2, s / 2

    # — Nós e linhas neurais —
    node_dist = s * 0.38          # distância do centro aos nós
    cardinal = [0, 90, 180, 270]
    diagonal = [45, 135, 225, 315]

    blue  = (96, 165, 250)        # #60a5fa
    indigo= (129, 140, 248)       # #818cf8
    line_blue  = (59, 130, 246, 140)  # semi-transparente
    line_indigo= (129, 140, 248, 100)

    def polar(angle_deg, dist):
        rad = math.radians(angle_deg - 90)
        return cx + dist * math.cos(rad), cy + dist * math.sin(rad)

    # Linhas cardinais
    lw_card = max(2, int(s * 0.025))
    for a in cardinal:
        x, y = polar(a, node_dist)
        d.line([(cx, cy), (x, y)], fill=line_blue, width=lw_card)

    # Linhas diagonais
    lw_diag = max(1, int(s * 0.018))
    for a in diagonal:
        x, y = polar(a, node_dist * 0.88)
        d.line([(cx, cy), (x, y)], fill=line_indigo, width=lw_diag)

    # Nós cardinais
    nr = max(4, int(s * 0.055))
    for a in cardinal:
        x, y = polar(a, node_dist)
        d.ellipse([x-nr, y-nr, x+nr, y+nr], fill=blue)

    # Nós diagonais (menores)
    nrd = max(3, int(s * 0.04))
    for a in diagonal:
        x, y = polar(a, node_dist * 0.88)
        d.ellipse([x-nrd, y-nrd, x+nrd, y+nrd], fill=(*indigo, 190))

    # — Círculo central com gradiente simulado —
    cr = int(s * 0.21)
    # Camadas para simular gradiente radial
    steps = 30
    for i in range(steps, 0, -1):
        t = i / steps
        r = int(59  + (96  - 59)  * (1 - t))
        g = int(130 + (165 - 130) * (1 - t))
        b = int(246 + (250 - 246) * (1 - t))
        ri = int(cr * t)
        d.ellipse([cx-ri, cy-ri, cx+ri, cy+ri], fill=(r, g, b))

    # — Texto "IA" —
    font_size = int(s * 0.30)
    try:
        font = ImageFont.truetype("arialbd.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", font_size)
        except:
            font = ImageFont.load_default()

    text = "IA"
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = cx - tw / 2 - bbox[0]
    ty = cy - th / 2 - bbox[1]
    d.text((tx, ty), text, fill=(15, 23, 42), font=font)

    return img


out_dir = os.path.join(os.path.dirname(__file__), "..", "criativos")
os.makedirs(out_dir, exist_ok=True)

for sz, name in [(512, "logo-512.png"), (180, "logo-180.png")]:
    img = draw_logo(sz)
    path = os.path.join(out_dir, name)
    img.save(path, "PNG")
    print(f"OK: {name} gerado em criativos/")

print("\nUse logo-180.png para foto de perfil do Facebook.")
print("Use logo-512.png para qualidade máxima (outros usos).")
