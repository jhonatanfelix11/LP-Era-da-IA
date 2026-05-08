"""
Gera imagens via Google Imagen 4 para o eBook Era da I.A.
Salva em assets/images/ e atualiza os src no HTML.
"""

import os, base64, re
from pathlib import Path
from google import genai
from google.genai import types

API_KEY = "AIzaSyDh7y5eBvUFZkq3BLU8SE13l1ATCaTQk2A"
MODEL   = "imagen-4.0-generate-001"
ASSETS  = Path(r"c:\Users\JHONATAN\Downloads\Marketing Digital\Produtos\mercado-ia-2025\assets\images")
HTML    = Path(r"c:\Users\JHONATAN\Downloads\Marketing Digital\Produtos\mercado-ia-2025\mercado-ia-2025-ebook.html")

ASSETS.mkdir(parents=True, exist_ok=True)
client = genai.Client(api_key=API_KEY)

# ── Mapa: arquivo local → prompt de geração ─────────────────────────────────

IMAGES = [
    {
        "file": "capa-ai.jpg",
        "aspect": "9:16",
        "prompt": (
            "Abstract artificial intelligence neural network visualization. "
            "Deep dark navy black background #050E1A. Glowing electric blue "
            "interconnected nodes and data streams flowing in 3D space. "
            "Cinematic volumetric light, photorealistic, 8K quality, "
            "premium editorial photography style. No text, no UI elements."
        ),
        "unsplash_ids": [
            "photo-1677442135703-1787eea5ce01",  # usado 4x
        ],
    },
    {
        "file": "robot-tech.jpg",
        "aspect": "3:4",
        "prompt": (
            "Humanoid robot hand with metallic fingers reaching toward a "
            "holographic blue interface panel. Dark studio background. "
            "Electric blue neon glow, dramatic cinematic lighting, "
            "ultra-detailed metal texture, 8K, commercial product photography. "
            "No text, no watermark."
        ),
        "unsplash_ids": [
            "photo-1485827404703-89b55fcc595e",  # usado 2x
        ],
    },
    {
        "file": "circuit-board.jpg",
        "aspect": "3:4",
        "prompt": (
            "Extreme macro photography of a modern circuit board. "
            "Electric blue glowing traces and capacitors. "
            "Dark navy background, shallow depth of field, "
            "dramatic studio lighting, ultra-sharp detail, 8K quality. "
            "No text, no watermark."
        ),
        "unsplash_ids": [
            "photo-1518770660439-4636190af475",  # usado 2x
        ],
    },
    {
        "file": "keyboard-dark.jpg",
        "aspect": "16:9",
        "prompt": (
            "Dark mechanical keyboard with electric blue RGB backlighting on a "
            "sleek black desk. Blurred monitor showing code in background. "
            "Cinematic low-key lighting, professional product photography, "
            "moody atmosphere, 8K ultra-sharp. No text visible."
        ),
        "unsplash_ids": [
            "photo-1558494949-ef010cbdcc31",  # usado 2x
        ],
    },
    {
        "file": "data-analysis.jpg",
        "aspect": "3:4",
        "prompt": (
            "Data scientist analyzing AI dashboard on dual monitors in a "
            "dark modern office. Multiple glowing screens showing charts, "
            "graphs and data visualizations in blue tones. "
            "Dramatic ambient blue light, cinematic wide shot, 8K. "
            "No text, no watermark."
        ),
        "unsplash_ids": [
            "photo-1460925895917-afdab827c52f",
        ],
    },
    {
        "file": "laptop-premium.jpg",
        "aspect": "3:4",
        "prompt": (
            "Premium open laptop on a minimalist dark desk showing an AI "
            "interface with glowing blue elements. Clean workspace, "
            "soft blue ambient light from the screen, editorial photography, "
            "8K, luxury tech aesthetic. No text on screen, no watermark."
        ),
        "unsplash_ids": [
            "photo-1551434678-e076c223a692",
        ],
    },
    {
        "file": "desk-overhead.jpg",
        "aspect": "3:4",
        "prompt": (
            "Overhead flat lay of a modern creative tech workspace. "
            "Dark desk surface with laptop, smartphone, wireless headphones "
            "and subtle blue ambient light accents. "
            "Editorial overhead photography, ultra-clean minimal composition, "
            "8K quality. No text, no watermark."
        ),
        "unsplash_ids": [
            "photo-1531297484001-80022131f5a1",
        ],
    },
]

# ── Geração e salvamento ─────────────────────────────────────────────────────

def generate_image(img_def):
    filepath = ASSETS / img_def["file"]
    if filepath.exists():
        print(f"  [skip] {img_def['file']} ja existe")
        return True

    print(f"  Gerando {img_def['file']} ({img_def['aspect']})...")
    try:
        response = client.models.generate_images(
            model=MODEL,
            prompt=img_def["prompt"],
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio=img_def["aspect"],
                output_mime_type="image/jpeg",
            ),
        )
        img_bytes = response.generated_images[0].image.image_bytes
        filepath.write_bytes(img_bytes)
        kb = len(img_bytes) // 1024
        print(f"  OK {img_def['file']} ({kb}kb)")
        return True
    except Exception as e:
        print(f"  ERRO {img_def['file']}: {e}")
        return False

# ── Atualização do HTML ──────────────────────────────────────────────────────

def update_html():
    html = HTML.read_text(encoding="utf-8")

    # Monta mapa: unsplash_id → caminho relativo local
    replace_map = {}
    for img_def in IMAGES:
        local_path = f"assets/images/{img_def['file']}"
        for uid in img_def["unsplash_ids"]:
            replace_map[uid] = local_path

    changes = 0
    for uid, local in replace_map.items():
        # Substitui qualquer URL Unsplash que contenha o ID, com qualquer querystring
        pattern = rf"https://images\.unsplash\.com/{re.escape(uid)}[^\"]*"
        new_html, n = re.subn(pattern, local, html)
        if n:
            html = new_html
            changes += n
            print(f"  {uid[:30]}... -> {local} ({n}x)")

    if changes:
        HTML.write_text(html, encoding="utf-8")
        print(f"\nHTML atualizado: {changes} substituicoes em {HTML.name}")
    else:
        print("Nenhuma substituicao feita (verifique os IDs).")

# ── Main ─────────────────────────────────────────────────────────────────────

print("=== Gerando imagens via Google Imagen 4 ===\n")
success = 0
for img_def in IMAGES:
    if generate_image(img_def):
        success += 1

print(f"\n{success}/{len(IMAGES)} imagens geradas.\n")
print("=== Atualizando HTML ===\n")
update_html()
print("\nPronto.")