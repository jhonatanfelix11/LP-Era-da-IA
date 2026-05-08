"""
Gerador de Imagens para Quiz — Era da I.A.
==========================================
Gera as 2 imagens das telas intercaladas do quiz.
Modelo : imagen-4.0-generate-001 (Google DeepMind)
Custo  : ~US$ 0.03 por imagem | 2 imagens = ~US$ 0.06

Como usar:
  cd Produtos/mercado-ia-2025/pages
  python gerar-imagens-quiz.py

A chave API e lida automaticamente do arquivo .env na raiz do projeto.
As imagens sao salvas em assets/ e referenciadas pelo quiz HTML.
"""

import os
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

# ================================================================
#  CARREGADOR DE .env
# ================================================================
def _load_env_file():
    current = Path(__file__).resolve().parent
    for _ in range(6):
        candidate = current / ".env"
        if candidate.exists():
            with open(candidate, encoding="utf-8") as f:
                for raw in f:
                    line = raw.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, val = line.partition("=")
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key and key not in os.environ:
                        os.environ[key] = val
            break
        current = current.parent

_load_env_file()

GOOGLE_AI_API_KEY = os.environ.get("GOOGLE_AI_API_KEY", "")
MODELO   = "imagen-4.0-generate-001"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELO}:predict"
ASPECT   = "16:9"

# Prompts especificos para o quiz "Era da I.A."
SLOTS = [
    {
        "id":      "quiz-img-1",
        "uso":     "Tela intercalada 1 — Consequencia da inacao (Pain Angle)",
        "arquivo": "assets/quiz-img-1.png",
        "prompt":  "Cinematic editorial photography, young Brazilian professional sitting alone at a cluttered desk late at night, head resting on hands with a defeated exhausted expression, multiple browser tabs open on a dim laptop screen casting harsh blue light on their face, dark moody room, papers scattered, sense of anxiety and falling behind, shallow depth of field, dramatic chiaroscuro lighting, photorealistic, 8k, absolutely no text no logos no watermarks no UI overlays no code no captions",
    },
    {
        "id":      "quiz-img-2",
        "uso":     "Tela intercalada 2 — Ativacao de desejo (Desire Angle)",
        "arquivo": "assets/quiz-img-2.png",
        "prompt":  "Cinematic editorial photography, young Brazilian professional working calmly at a clean minimal desk during a sunny afternoon, soft warm natural light through large window, single open laptop with bright clean screen, relaxed confident posture leaning back with a subtle satisfied smile, organized workspace, sense of freedom and control, shallow depth of field, warm color grade, photorealistic, 8k, absolutely no text no logos no watermarks no UI overlays no code no captions",
    },
]


def linha(char="=", n=58):
    print(char * n)


def validar_chave():
    if not GOOGLE_AI_API_KEY or GOOGLE_AI_API_KEY.strip() in ("", "INSIRA_SUA_CHAVE_AQUI"):
        print("\n" + "=" * 58)
        print("  CHAVE API NAO CONFIGURADA")
        print("=" * 58)
        print("\n  Edite o arquivo .env na raiz do projeto:")
        print("  GOOGLE_AI_API_KEY=sua_chave_aqui")
        print("\n  Obter chave: https://aistudio.google.com/app/apikey\n")
        raise SystemExit(1)


def gerar_imagem(prompt, aspect_ratio, caminho_saida):
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "sampleCount":      1,
            "aspectRatio":      aspect_ratio,
            "safetySetting":    "block_low_and_above",
            "personGeneration": "allow_adult",
        },
    }

    url  = f"{ENDPOINT}?key={GOOGLE_AI_API_KEY}"
    data = json.dumps(payload).encode("utf-8")
    req  = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            resultado = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Erro HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Erro de conexao: {e.reason}")

    predicoes = resultado.get("predictions", [])
    if not predicoes:
        raise RuntimeError("API nao retornou imagem. Verifique o prompt.")

    img_b64 = predicoes[0].get("bytesBase64Encoded", "")
    if not img_b64:
        raise RuntimeError("Resposta da API sem dados de imagem.")

    destino = Path(caminho_saida)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(base64.b64decode(img_b64))
    return str(destino)


def main():
    validar_chave()

    print()
    linha()
    print("  GERADOR DE IMAGENS — QUIZ ERA DA I.A.")
    print(f"  Modelo : Google {MODELO}")
    print(f"  Custo  : ~US$ 0.03 por imagem")
    linha()

    print(f"\n  Serao geradas {len(SLOTS)} imagens em 'assets/':\n")
    for i, s in enumerate(SLOTS, 1):
        print(f"  {i}. {s['uso']}")
    linha("-")

    confirmar = input("\n  Confirmar geracao? (s/n): ").strip().lower()
    if confirmar != "s":
        print("\n  Cancelado.\n")
        return

    print()
    geradas = []

    for i, slot in enumerate(SLOTS, 1):
        print(f"  [{i}/{len(SLOTS)}] {slot['uso']}")
        print(f"  Prompt: {slot['prompt'][:90]}...")

        alterar = input("  Usar este prompt? (s = sim / n = editar): ").strip().lower()
        if alterar == "n":
            slot["prompt"] = input("  Seu prompt: ").strip()

        print("  Gerando... aguarde (~15-30 segundos)...")
        try:
            caminho = gerar_imagem(slot["prompt"], ASPECT, slot["arquivo"])
            geradas.append(caminho)
            print(f"  Salva: {caminho}\n")
        except Exception as e:
            print(f"  ERRO: {e}\n")

    linha()
    print(f"  Concluido: {len(geradas)}/{len(SLOTS)} imagens geradas")
    if geradas:
        print("  As imagens ja estao referenciadas no quiz HTML.")
        print("  Abra o quiz no browser para visualizar.")
    linha()
    print()


if __name__ == "__main__":
    main()
