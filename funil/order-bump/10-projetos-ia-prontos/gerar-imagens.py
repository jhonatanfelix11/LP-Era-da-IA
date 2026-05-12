"""
Gera imagens via Google Imagen 4 para o order-bump "10 Projetos de I.A. Prontos".
Salva em assets/ e retorna caminhos relativos.
"""

import os, base64
from pathlib import Path
from google import genai
from google.genai import types

API_KEY = "AIzaSyDh7y5eBvUFZkq3BLU8SE13l1ATCaTQk2A"
MODEL   = "imagen-4.0-generate-001"
ASSETS  = Path(__file__).parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

client = genai.Client(api_key=API_KEY)

IMAGES = [
    {
        "file": "capa.png",
        "aspect": "9:16",
        "prompt": (
            "A highly conceptual, photorealistic editorial photography masterpiece. "
            "Pitch black charcoal studio background #0C0C0C with subtle textured floor. "
            "A single masculine hand emerges from the bottom of the frame, sharply lit "
            "from above with dramatic cinematic light, holding a luminous beam of vibrant "
            "amber-gold #F59E0B liquid light. The beam ascends and explodes mid-air into "
            "ten distinct floating holographic artifacts in an arc: minimalist logo mark, "
            "chart bar, video frame icon, copy text fragment, reel mockup, thumbnail mock, "
            "envelope, document, product tag, storyboard. Each artifact glows with internal "
            "amber light, connected to the beam with thin gold filaments. Ample dark negative "
            "space at top for editorial typography. Masterpiece, 8k, volumetric cinematic "
            "lighting, ultra-detailed hyper-realistic. NO text, NO typography, NO book mockup, "
            "NO robot."
        ),
        "negative": (
            "book, book mockup, 3d book, text, words, letters, typography, title, "
            "author name, robot face, android, generic cybernetics, low quality, "
            "cartoon, frame, border."
        ),
    },
    {
        "file": "divisoria.png",
        "aspect": "3:4",
        "prompt": (
            "A highly conceptual, photorealistic editorial photograph. Minimalist dark "
            "wood desk shot from hero low angle 24mm in a dim studio with vibrant amber "
            "#F59E0B rim lighting. On the desk: a single luxury leather notebook open, "
            "vintage fountain pen, and exactly ten levitating semi-transparent floating "
            "cards rising in a graceful spiral above the notebook, each card glowing with "
            "internal warm amber light and containing abstract micro-icons. Hyper-realistic "
            "glass texture with delicate gold-foil edges. Charcoal #0C0C0C background with "
            "subtle smoke particles. Cinematic chiaroscuro, masterpiece, 8K, editorial "
            "gallery quality. NO text, NO letters, NO book mockup, NO frame."
        ),
        "negative": (
            "book, book mockup, 3d book, text, words, letters, typography, title, "
            "author name, robot face, android, generic cybernetics, low quality, "
            "cartoon, frame, border."
        ),
    },
]


def generate_image(img_def):
    filepath = ASSETS / img_def["file"]
    if filepath.exists():
        print(f"  [skip] {img_def['file']} ja existe")
        return True

    print(f"  Gerando {img_def['file']} ({img_def['aspect']})...")
    try:
        full_prompt = img_def["prompt"]
        if img_def.get("negative"):
            full_prompt += f"\n\nDo NOT include: {img_def['negative']}"

        response = client.models.generate_images(
            model=MODEL,
            prompt=full_prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio=img_def["aspect"],
                output_mime_type="image/png",
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


print("=== Gerando imagens order-bump 10 Projetos de I.A. ===\n")
success = 0
for img_def in IMAGES:
    if generate_image(img_def):
        success += 1

print(f"\n{success}/{len(IMAGES)} imagens geradas em {ASSETS}")
if success < len(IMAGES):
    print("\nFALLBACK: Use Unsplash como alternativa:")
    print("  capa.png -> photo-1677442135703-1787eea5ce01")
    print("  divisoria.png -> photo-1485827404703-89b55fcc595e")
