"""
Capa Facebook — Era da I.A.
Design: premium, clean, minimalista
1640x624px (2x para nitidez)
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os

W, H = 1640, 624
OUT = os.path.join(os.path.dirname(__file__), "..", "criativos", "capa-facebook.png")

def font(name, size):
    for path in [
        f"C:/Windows/Fonts/{name}.ttf",
        f"C:/Windows/Fonts/{name}bd.ttf",
        f"C:/Windows/Fonts/{name}i.ttf",
        f"C:/Windows/Fonts/arial.ttf",
    ]:
        try: return ImageFont.truetype(path, size)
        except: pass
    return ImageFont.load_default()

# ── Canvas ──────────────────────────────────────────────────────
base = Image.new("RGB", (W, H), (6, 9, 20))
d    = ImageDraw.Draw(base, "RGBA")

# ── 1. Fundo — gradiente vertical muito sutil ────────────────────
for y in range(H):
    t = y / H
    r = int(6  + (14 - 6)  * t)
    g = int(9  + (18 - 9)  * t)
    b = int(20 + (38 - 20) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

# ── 2. Bloom de luz — único, elegante, lado direito ──────────────
bloom = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bd    = ImageDraw.Draw(bloom, "RGBA")

cx, cy = 1180, 220
# Camadas do bloom (de fora pra dentro)
layers = [
    (580, (67, 56, 202,  6)),   # violeta externo
    (440, (59, 130, 246, 10)),  # azul médio
    (300, (96, 165, 250, 18)),  # azul claro
    (180, (147, 197, 253, 30)), # azul brilhante
    (90,  (219, 234, 254, 50)), # quase branco
    (40,  (255, 255, 255, 70)), # núcleo
]
for radius, color in layers:
    bd.ellipse([cx-radius, cy-radius, cx+radius, cy+radius], fill=color)

bloom = bloom.filter(ImageFilter.GaussianBlur(radius=60))
base  = base.convert("RGBA")
base  = Image.alpha_composite(base, bloom)
base  = base.convert("RGB")
d     = ImageDraw.Draw(base, "RGBA")

# ── 3. Bloom secundário — baixo-direita (reflexo) ────────────────
bloom2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bd2    = ImageDraw.Draw(bloom2, "RGBA")
bd2.ellipse([980, 380, 1640, 800], fill=(67, 56, 202, 8))
bloom2 = bloom2.filter(ImageFilter.GaussianBlur(radius=80))
base   = base.convert("RGBA")
base   = Image.alpha_composite(base, bloom2)
base   = base.convert("RGB")
d      = ImageDraw.Draw(base, "RGBA")

# ── 4. Linha diagonal de luz (sutil) ────────────────────────────
line_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ld = ImageDraw.Draw(line_layer, "RGBA")
for w in range(12, 0, -1):
    alpha = int(18 * (w / 12) ** 2)
    ld.line([(680, 0), (W, H * 0.55)], fill=(96, 165, 250, alpha), width=w*4)
line_layer = line_layer.filter(ImageFilter.GaussianBlur(radius=8))
base = base.convert("RGBA")
base = Image.alpha_composite(base, line_layer)
base = base.convert("RGB")
d    = ImageDraw.Draw(base, "RGBA")

# ── 5. Linha horizontal fina — accent ───────────────────────────
acc_y = H - 100
# Linha que vai do pad até ~60% da largura, sumindo suavemente
for x in range(W):
    t = x / W
    if t < 0.05:
        alpha = int(160 * (t / 0.05))
    elif t > 0.55:
        alpha = int(160 * (1 - (t - 0.55) / 0.45))
    else:
        alpha = 160
    d.point((x, acc_y), fill=(96, 165, 250, alpha))

# ── 6. Barra superior ───────────────────────────────────────────
for x in range(W):
    t = x / W
    if t < 0.6:
        r = int(59  + (99  - 59)  * (t / 0.6))
        g = int(130 + (102 - 130) * (t / 0.6))
        b = 246
        alpha = int(255 * (1 - t / 0.6 * 0.3))
    else:
        alpha = 0
        r, g, b = 59, 130, 246
    d.line([(x, 0), (x, 3)], fill=(r, g, b, alpha))

# ── 7. TIPOGRAFIA ────────────────────────────────────────────────
PAD = 100

f_ebook   = font("arial",   28)
f_era     = font("arialbd", 108)
f_ia      = font("arialbd", 148)
f_tagline = font("arial",    34)

# "EBOOK" — label elegante com espaçamento
ebook_text = "E  B  O  O  K"
d.text((PAD, 82), ebook_text, font=f_ebook, fill=(96, 165, 250, 200))

# Tracinho decorativo ao lado
bb = d.textbbox((0,0), ebook_text, font=f_ebook)
line_x = PAD + bb[2] + 24
d.rectangle([line_x, 98, line_x + 60, 101], fill=(96, 165, 250, 120))

# "Era da" — branco, peso normal
d.text((PAD, 138), "Era da", font=f_era, fill=(245, 248, 255, 245))

# "I.A." — azul brilhante, levemente maior, com micro-sombra
ia_x, ia_y = PAD - 4, 246
# Sombra suave
d.text((ia_x + 3, ia_y + 4), "I.A.", font=f_ia, fill=(15, 30, 80, 120))
# Texto principal
d.text((ia_x, ia_y), "I.A.", font=f_ia, fill=(147, 197, 253, 255))

# Tagline — cinza suave, elegante
tagline = "O mapa completo das ferramentas de I.A. que estão pagando hoje."
d.text((PAD, acc_y + 16), tagline, font=f_tagline, fill=(148, 163, 184, 190))

# ── 8. Borda direita sutil ───────────────────────────────────────
for y in range(H):
    t = y / H
    alpha = int(40 * math.sin(math.pi * t))
    d.point((W-1, y), fill=(96, 165, 250, alpha))

# ── 9. Vinheta nas bordas (torna mais premium) ───────────────────
vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vd = ImageDraw.Draw(vignette, "RGBA")
steps = 80
for i in range(steps):
    t     = i / steps
    alpha = int(120 * (1 - t) ** 2)
    pad   = i * 5
    vd.rectangle([pad, pad, W - pad, H - pad],
                 outline=(0, 0, 0, alpha), width=1)
vignette = vignette.filter(ImageFilter.GaussianBlur(radius=2))
base = base.convert("RGBA")
base = Image.alpha_composite(base, vignette)
base = base.convert("RGB")

# ── Salvar ───────────────────────────────────────────────────────
os.makedirs(os.path.dirname(OUT), exist_ok=True)
base.save(OUT, "PNG", optimize=True)
print(f"OK: capa-facebook.png  ({W}x{H}px)")
print(f"Arquivo: {OUT}")
