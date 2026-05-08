---
name: Era da I.A. — Design System
description: Design system do eBook "Era da I.A. — Como Lucrar Agora Antes que Seja Tarde Demais". Identidade visual tech-premium com paleta navy/elétrico, tipografia editorial e componentes modulares para landing page, quiz e materiais de venda.
version: 1.0.0
author: Marketing Digital
date: 2026-05-07
---

# Era da I.A. — Design System

> Design system do eBook **"Era da I.A. — Como Lucrar Agora Antes que Seja Tarde Demais"**.
> Identidade visual **tech-premium** — paleta navy/elétrico, tipografia editorial, componentes modulares.

---

## Colors

### Primary Palette — Dark Foundation

| Token | Hex | Role | Usage |
|---|---|---|---|
| `--negro` | `#030B14` | Background darkest | Capa, contra-capa, seções de impacto |
| `--carbon` | `#0A1628` | Background dark | Sidebar, cards de carreira, divisórias |
| `--carbon2` | `#0F1E30` | Background dark alt | Variação de superfície escura |

### Primary Palette — Accent Blue

| Token | Hex | Role | Usage |
|---|---|---|---|
| `--ouro` | `#2563EB` | Primary accent | Links, regras decorativas, badges, CTAs |
| `--acento-dark` | `#38BDF8` | Accent light | Títulos em fundo escuro, destaques, bordas |
| `--pop` | `#22D3EE` | Accent pop | Estatísticas de destaque, números grandes |

### Secondary Palette

| Token | Hex | Role | Usage |
|---|---|---|---|
| `--amber` | `#FBBF24` | Warm accent | Alertas, badges de urgência (uso limitado) |

### Light Palette

| Token | Hex | Role | Usage |
|---|---|---|---|
| `--fundo` | `#EEF4FF` | Background light | Fundo principal das páginas de conteúdo |
| `--fundo-alt` | `#F0F9FF` | Background light alt | Variação sutil de fundo |

### Text Palette

| Token | Hex | Role | Usage |
|---|---|---|---|
| `--texto` | `#1E293B` | Text primary | Corpo de texto, títulos em fundo claro |
| `--texto-suave` | `#475569` | Text secondary | Legendas, labels, texto auxiliar |
| `--branco` | `#FFFFFF` | Text on dark | Texto em fundos escuros, botões |

### Semantic Aliases

| Alias | Token | Context |
|---|---|---|
| `bg-dark` | `--negro` | Seções de impacto, hero |
| `bg-surface` | `--carbon` | Cards, sidebars |
| `bg-light` | `--fundo` | Páginas de conteúdo |
| `accent-primary` | `--ouro` | CTAs, links, destaques |
| `accent-secondary` | `--acento-dark` | Títulos em dark, bordas ativas |
| `accent-data` | `--pop` | Números, estatísticas |
| `text-on-dark` | `rgba(255,255,255,.85)` | Texto em fundo escuro |
| `text-on-dark-muted` | `rgba(255,255,255,.55)` | Texto secundário em fundo escuro |

---

## Typography

### Font Stack

| Role | Font Family | Fallback | Source |
|---|---|---|---|
| **Display / Headings** | `Playfair Display` | serif | Google Fonts — weights: 700, 900 |
| **Body / Reading** | `Source Serif 4` | Georgia, serif | Google Fonts — weights: 300, 400, 600 |
| **UI / Labels / Data** | `Lato` | sans-serif | Google Fonts — weights: 300, 400, 700, 900 |
| **Accent / Italic** | `Cormorant Garamond` | serif | Google Fonts — weight: 400 italic |

### Type Scale

| Element | Font | Size | Weight | Line-Height | Letter-Spacing | Transform |
|---|---|---|---|---|---|---|
| `h1` | Playfair Display | 22pt | 900 | 1.15 | — | — |
| `h2` | Playfair Display | 15pt | 700 | 1.2 | — | — |
| `h3` | Lato | 10pt | 700 | — | 0.06em | uppercase |
| `p` (body) | Source Serif 4 | 9.5pt | 400 | 1.65 | — | — |
| `cap-num` | Lato | 7.5pt | 700 | — | 0.15em | uppercase |
| `cap-epigrafe` | Source Serif 4 | 13pt | 400 italic | 1.5 | — | — |
| `subtitulo-fino` | Cormorant Garamond | 12pt | 400 italic | — | — | — |
| `stat-n` | Playfair Display | 22pt | 900 | 1 | — | — |
| `stat-d` | Lato | 7.5pt | 400 | 1.3 | — | — |
| `label` | Lato | 7pt | 700 | — | 0.1em–0.2em | uppercase |

### Font Import

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;1,8..60,400&family=Lato:wght@300;400;700;900&family=Cormorant+Garamond:ital,wght@0,400;1,400&display=swap" rel="stylesheet">
```

---

## Spacing

### Base Unit

`1mm` ≈ 3.78px (A4 print context). Web context uses `mm` or `rem` equivalent.

| Token | mm | px (approx) | Usage |
|---|---|---|---|
| `space-xs` | 1.5mm | 6px | Padding mínima, gaps internos |
| `space-sm` | 2mm | 8px | Gaps entre elementos compactos |
| `space-md` | 3mm | 11px | Margem entre parágrafos |
| `space-base` | 4mm | 15px | Margem padrão de componentes |
| `space-lg` | 5mm | 19px | Padding de blocos |
| `space-xl` | 8mm | 30px | Seções, gaps grandes |

### Page Margins (A4 Print)

| Edge | Margin |
|---|---|
| Top | 22mm |
| Right | 20mm |
| Bottom | 20mm |
| Left | 24mm |
| Header/Footer | 9mm from edge |

---

## Border Radius

| Token | Value | Usage |
|---|---|---|
| `radius-none` | 0 | Cards, badges (estilo editorial quadrado) |
| `radius-sm` | 1mm | Chart bars, micro elements |
| `radius-md` | 2mm | Feature images, featured cards |

> O design system prioriza **cantos retos** (estética tech/editorial). Radius é exceção, não regra.

---

## Decorative Rules

| Element | Height | Color | Opacity | Usage |
|---|---|---|---|---|
| `.rule` | 0.5mm | `--ouro` | 0.7 | Separador horizontal entre blocos |
| `.capa-rule` | 0.5mm | `--acento-dark` | 1.0 | Separador na capa |
| `.sidebar-rule` | 0.4mm | `--acento-dark` | 0.5 | Separador em sidebar escura |
| `.div-rule` | 0.5mm | `--acento-dark` | 1.0 | Separador em divisória |
| `.close-rule` | 0.5mm | `--acento-dark` | 1.0 | Separador em fechamento |
| Header/Footer rule | 0.3mm | `--ouro` | 0.25 | Linha sutil de header/footer |

---

## Components

### 1. Callout Block (`.bloco-callout`)

Fundamental para destacar informações importantes.

| Property | Value |
|---|---|
| Background | `#DBEAFE` |
| Border-left | 1.5mm solid `--ouro` |
| Padding | 4mm 5mm |
| Label | 7pt, uppercase, `--ouro`, weight 700 |
| Body | 9pt, `--texto` |

### 2. Stat Row (`.stat-row`)

Linha de estatísticas lado a lado.

| Property | Value |
|---|---|
| Layout | flex, gap 4mm |
| Item bg | `#DBEAFE` |
| Item padding | 4mm 3mm |
| Number | Playfair Display, 22pt, 900, `--ouro` |
| Description | 7.5pt, `--texto-suave` |

### 3. Dark Stat Grid (`.dark-stat-grid`)

Estatísticas em fundo escuro — alto impacto.

| Property | Value |
|---|---|
| Layout | flex, gap 3mm |
| Card bg | `--negro` |
| Card border-top | 1.5px solid `--pop` |
| Number | Lato, 24pt, 900, `--pop` |
| Description | 7.5pt, white at 70% |

### 4. Tool Card (`.ferramenta-card`)

Card para apresentar ferramentas de I.A.

| Property | Value |
|---|---|
| Background | `--branco` |
| Border | 0.3mm solid `#CBD5E1` |
| Padding | 4mm 5mm |
| Name | Lato, 10pt, 700, `--negro` |
| Tag | 6.5pt, uppercase, white on `--ouro`, padding 0.5mm 2mm |
| Body | 8.5pt, `--texto-suave` |

### 5. Career Card (`.carreira-card`)

Card para carreiras/nichos de renda.

| Property | Value |
|---|---|
| Background | `--carbon` |
| Padding | 4mm 5mm |
| Title | Lato, 10.5pt, 700, white |
| Value | Playfair Display, 16pt, 900, `--acento-dark` |
| Period | 7.5pt, white at 50% |
| Body | 8.5pt, white at 75% |

### 6. Exercise Block (`.bloco-exercicio`)

Bloco de exercícios práticos — fundo escuro.

| Property | Value |
|---|---|
| Background | `--carbon` |
| Padding | 5mm |
| Label | 7pt, uppercase, `--acento-dark` |
| Title | Lato, 10pt, 700, white |
| Body | 9pt, white at 80% |
| Prompt box | bg white at 7%, border-left 1mm `--acento-dark`, monospace 8pt |

### 7. Summary Block (`.bloco-resumo`)

Resumo de capítulo — fundo negro.

| Property | Value |
|---|---|
| Background | `--negro` |
| Padding | 5mm 6mm |
| Label | 7pt, uppercase, `--acento-dark` |
| List | sem bullets, 9pt, white at 85% |
| Separator | border-bottom 0.2mm white at 8% |
| Dash indicator | `—` positioned left, `--acento-dark` |

### 8. Pull Quote (`.pull-quote`)

Citação centralizada.

| Property | Value |
|---|---|
| Padding | 5mm 8mm |
| Text | Cormorant Garamond, 15pt, italic, `--negro` |
| Cite | 8pt, uppercase, `--ouro`, letter-spacing 0.08em |

### 9. Chapter Divider (`.div-wrap`)

Página de divisória entre capítulos — layout split.

| Property | Value |
|---|---|
| Left | Image 75mm, gradient overlay to `--carbon` |
| Right | Background `--carbon` |
| Label | 7.5pt, uppercase, `--acento-dark` |
| Title | Playfair Display, 18pt, 900, white |
| Description | Cormorant Garamond, 11pt, italic, white at 65% |
| Tags | 7pt, uppercase, border 0.3mm `--acento-dark` at 40% |

### 10. Sidebar Split (`.split-content`)

Layout com sidebar escura + conteúdo claro.

| Property | Value |
|---|---|
| Sidebar width | 52mm |
| Sidebar bg | `--negro` |
| Content bg | `--fundo` |
| Sidebar title | Playfair Display, 15pt, 900, white |
| Index item | 8.5pt, white at 45% |
| Active item | white, 700 |

### 11. FAQ Item (`.faq-item`)

Pergunta e resposta.

| Property | Value |
|---|---|
| Border-left | 2.5px solid `--ouro` |
| Background | `--ouro` at 4% |
| Border-radius | 0 1mm 1mm 0 |
| Question | Lato, 9pt, 700, `--texto` |
| Answer | Source Serif 4, 8.5pt, `--texto-suave`, line-height 1.55 |

### 12. Chart Bar (`.chart-wrap`)

Barras de dados/estatísticas.

| Property | Value |
|---|---|
| Bar bg | `--ouro` at 12% |
| Bar height | 5.5mm |
| Bar radius | 1mm |
| Fill | solid `--ouro` |
| Value label | Lato, 7pt, 900, white |

### 13. Feature Row (`.feat-row`)

Imagem + texto lado a lado.

| Property | Value |
|---|---|
| Image width | 52mm |
| Image radius | 2mm |
| Image shadow | 0 2mm 6mm rgba(0,0,0,.15) |
| Image height | 48mm |
| Tag | Lato, 6.5pt, 700, uppercase, `--ouro` |

---

## Page Templates

### Cover (Capa)

- Full-bleed image with gradient vignette: `linear-gradient(110deg, rgba(5,14,26,.95) 0%, rgba(5,14,26,.75) 55%, rgba(5,14,26,.3) 100%)`
- Content positioned bottom-left (14mm from edges)
- Title: Playfair Display 28pt, 900, white — `span` colored `--acento-dark`
- Subtitle: Cormorant Garamond 12pt, italic, white at 80%

### Back Cover (Contra-capa)

- Full `--negro` background
- Centered content
- Title: Playfair Display 18pt, 900, white
- Subtitle: Cormorant Garamond 11pt, italic, white at 60%
- Rule: 0.5mm, 15mm wide, `--acento-dark`

### Chapter Intro (Split)

- Left: image column 75mm
- Right: text on `--fundo`
- Tag: 7.5pt, uppercase, `--ouro`

### Closing Page

- Full-bleed image with overlay: `rgba(5,14,26,.88)`
- Centered content
- CTA button: `--ouro` bg, Lato 9pt, 700, uppercase, padding 3.5mm 10mm

---

## Animation (Screen Only)

| Class | Effect |
|---|---|
| `.av` | opacity: 0, base state |
| `.av.up` | translateY(6mm) |
| `.av.scale` | scale(.97) |
| `.av.left` | translateX(-6mm) |
| `.av.visible` | opacity: 1, transform: none |
| `.d1`–`.d5` | Staggered delays: .1s, .25s, .4s, .55s, .65s |

> All animations disabled in print/PDF via `@media print`.

---

## Print / PDF

- Format: A4 portrait (210mm x 297mm)
- `page-break-after: always` on each `.page`
- `-webkit-print-color-adjust: exact` forced on all elements
- UI-only elements (`.ui-only`) hidden in print
- Animations disabled in print context

---

## Accessibility

- Body text contrast on `--fundo`: `--texto` (#1E293B) — ratio **11.5:1** (AAA)
- Body text contrast on `--negro`: white at 85% — ratio **14.2:1** (AAA)
- Accent on dark: `--acento-dark` (#38BDF8) on `--negro` — ratio **8.7:1** (AAA)
- Minimum text size: 6.5pt (tag labels) — acceptable for print
- Interactive elements have visible focus states via underline on hover

---

## Usage Guidelines

### For Landing Page

- Use `--fundo` as base background
- Hero section: `--negro` with `--acento-dark` accents
- CTAs: `--ouro` background, white text
- Stat blocks: use Dark Stat Grid for impact
- Tool cards: use standard Tool Card component

### For Quiz

- Use light theme (`--fundo` base)
- Progress bar: `--ouro` fill
- Option cards: white bg, `--ouro` border on selected
- Result screen: Dark theme with career card style
- CTA button: same as closing page CTA

### For Sales Page

- Combine cover aesthetic (dark hero) with light content sections
- Use pull quotes for testimonials
- FAQ section uses FAQ Item component
- Pricing: Career Card style for price display
- Guarantee badge: `--amber` accent for urgency
