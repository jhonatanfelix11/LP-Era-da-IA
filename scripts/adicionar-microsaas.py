"""
Adiciona Capítulo 8 — Micro SaaS com I.A. ao ebook principal.
Páginas inseridas antes de P43 (CONCLUSÃO).
"""
import re
from pathlib import Path

EBOOK = Path(r"C:\Users\JHONATAN\Downloads\Marketing Digital\Produtos\mercado-ia-2025\ebook\mercado-ia-2025-ebook.html")
html = EBOOK.read_text(encoding="utf-8")

INSERT_BEFORE = '<!-- ═══════════════════════════════════ P43 — CONCLUSÃO'

PAGES = r"""
<!-- ═══════════════════════════════════ P_MICROSAAS_DIV — DIVISÓRIA CAP 8 ═══════════════════════════════════ -->
<div class="page no-hf" id="p_microsaas_div" style="background:var(--negro);position:relative;overflow:hidden">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 20% 60%,rgba(34,211,238,.18) 0%,transparent 60%),radial-gradient(ellipse at 80% 30%,rgba(37,99,235,.15) 0%,transparent 55%)"></div>
  <div class="div-bg-num" style="color:rgba(255,255,255,.04);font-size:160pt;right:-10mm;bottom:-15mm">08</div>
  <div style="position:absolute;top:0;left:0;right:0;bottom:0;display:flex;flex-direction:column;justify-content:center;padding:0 20mm 0 24mm">
    <div class="div-label">Capítulo 08</div>
    <h1 class="div-titulo" style="font-size:26pt;max-width:140mm">Micro SaaS com I.A.:<br>Do Zero ao Produto em<br>um Final de Semana</h1>
    <div class="div-desc" style="max-width:120mm;margin-top:4mm">Você não precisa de equipe de tecnologia nem de investimento. Com Claude Code, Supabase e Vercel, qualquer profissional pode lançar um produto digital recorrente — e começar a faturar enquanto dorme.</div>
    <div style="display:flex;gap:3mm;margin-top:8mm;flex-wrap:wrap">
      <span class="div-tag">Claude Code</span>
      <span class="div-tag">Supabase</span>
      <span class="div-tag">Vercel</span>
      <span class="div-tag">Stitch</span>
      <span class="div-tag">Google AI Studio</span>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════ P_MICROSAAS_1 — O QUE É + MERCADO ═══════════════════════════════════ -->
<div class="page" id="p_microsaas_1">
  <div class="ph"><span>ERA DA I.A.</span><span>CAP. 08 — MICRO SAAS COM I.A.</span></div>
  <div class="page-inner">
    <div class="cap-num av in">Capítulo 08</div>
    <h1 class="av up d1" style="font-size:17pt;margin-bottom:2mm">O Que é Micro SaaS — e Por Que Agora É o Melhor Momento</h1>
    <span class="rule av scale d2" style="width:22mm"></span>

    <div style="display:flex;gap:5mm;margin-top:3mm">
      <div style="flex:1">
        <p class="av up d2" style="font-size:8.5pt;line-height:1.65;margin-bottom:3mm">
          <strong>Micro SaaS</strong> é um software como serviço (SaaS) focado em resolver <strong>um problema específico</strong> para um nicho pequeno — criado e operado por 1 a 3 pessoas, sem venture capital, sem equipe de 50 engenheiros.
        </p>
        <p class="av up d2" style="font-size:8.5pt;line-height:1.65;margin-bottom:3mm">
          Com I.A. gerando o código, o que levava 6 meses de desenvolvimento agora leva <strong>1 fim de semana</strong>. Você foca na ideia e na venda — a I.A. escreve o código.
        </p>
        <div class="bloco-callout av scale d3" style="margin-top:0">
          <div class="label">Por que Micro SaaS bate freela</div>
          <p style="font-size:8pt;line-height:1.7">Freela: você vende tempo. Micro SaaS: você vende acesso. O cliente paga todo mês. Você dorme — a receita não para.</p>
        </div>
      </div>

      <div style="flex:1">
        <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ouro);margin-bottom:3mm">Mercado Global de SaaS — Crescimento (US$ bilhões)</div>
        <div class="chart-wrap av up d3" style="gap:2mm">
          <div class="chart-row">
            <span class="chart-label">2020</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:28%;background:var(--ouro)"><span class="chart-val">157B</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label">2021</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:38%;background:var(--ouro)"><span class="chart-val">209B</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label">2022</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:48%;background:var(--ouro)"><span class="chart-val">261B</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label">2023</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:60%;background:var(--pop)"><span class="chart-val">317B</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label">2024</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:72%;background:var(--pop)"><span class="chart-val">390B</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label">2025</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:85%;background:var(--pop)"><span class="chart-val">462B</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label" style="color:var(--ouro);font-weight:700">2026 ↗</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:100%;background:linear-gradient(90deg,var(--pop),var(--ouro))"><span class="chart-val">550B+</span></div></div>
          </div>
        </div>
        <p style="font-size:7pt;color:var(--texto-suave);margin-top:2mm;font-style:italic">Fonte: Gartner / Statista 2026. CAGR ~18% ao ano.</p>

        <div style="display:flex;gap:3mm;margin-top:4mm">
          <div style="flex:1;text-align:center;padding:3mm;background:var(--fundo-alt);border-radius:2mm;border-bottom:2.5px solid var(--ouro)">
            <span style="font-family:'Lato',sans-serif;font-size:14pt;font-weight:900;color:var(--ouro);display:block;line-height:1">18%</span>
            <span style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave);display:block;margin-top:1mm">crescimento anual</span>
          </div>
          <div style="flex:1;text-align:center;padding:3mm;background:var(--fundo-alt);border-radius:2mm;border-bottom:2.5px solid var(--pop)">
            <span style="font-family:'Lato',sans-serif;font-size:14pt;font-weight:900;color:var(--pop);display:block;line-height:1">R$0</span>
            <span style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave);display:block;margin-top:1mm">custo inicial (plano free)</span>
          </div>
          <div style="flex:1;text-align:center;padding:3mm;background:var(--fundo-alt);border-radius:2mm;border-bottom:2.5px solid var(--amber)">
            <span style="font-family:'Lato',sans-serif;font-size:14pt;font-weight:900;color:var(--amber);display:block;line-height:1">48h</span>
            <span style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave);display:block;margin-top:1mm">do zero ao ar com I.A.</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="pf"><span>Equipe Era da I.A.</span><span class="pnum">99</span></div>
</div>

<!-- ═══════════════════════════════════ P_MICROSAAS_2 — STACK FERRAMENTAS ═══════════════════════════════════ -->
<div class="page" id="p_microsaas_2">
  <div class="ph"><span>ERA DA I.A.</span><span>CAP. 08 — MICRO SAAS COM I.A.</span></div>
  <div class="page-inner" style="padding-top:18mm">
    <h2 class="av up d1" style="font-size:15pt;margin-bottom:1.5mm">A Stack Completa — 5 Ferramentas, Custo Quase Zero</h2>
    <span class="rule av scale d1" style="width:22mm;margin-bottom:3mm"></span>
    <p class="av up d2" style="font-size:8.5pt;margin-bottom:4mm;line-height:1.6">Todas têm plano gratuito para começar. Você só paga quando começa a faturar.</p>

    <div style="display:flex;flex-direction:column;gap:3mm">

      <!-- Claude Code -->
      <div class="av up d2" style="display:flex;align-items:center;gap:4mm;padding:3.5mm 4mm;background:#fff;border-radius:2mm;border-left:3px solid var(--ouro);box-shadow:0 1px 4px rgba(0,0,0,.06)">
        <div style="flex:0 0 28mm;text-align:center">
          <div style="font-family:'Lato',sans-serif;font-size:10pt;font-weight:900;color:var(--ouro);line-height:1">Claude Code</div>
          <div style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave);margin-top:.5mm">claude.ai/code</div>
        </div>
        <div style="flex:1;border-left:1px solid rgba(0,0,0,.07);padding-left:4mm">
          <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ouro);margin-bottom:1mm">Código · Lógica · Back-end · Integração</div>
          <p style="font-size:8pt;color:var(--texto);line-height:1.5;margin:0">Agente de terminal que escreve, testa e corrige código completo. Diga o que o produto deve fazer — ele gera o projeto inteiro, configura banco de dados e faz deploy.</p>
        </div>
        <div style="flex:0 0 20mm;text-align:center">
          <span style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:900;color:var(--ouro);display:block">~R$110</span>
          <span style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave)">Pro/mês</span>
        </div>
      </div>

      <!-- Codex / OpenAI -->
      <div class="av up d2" style="display:flex;align-items:center;gap:4mm;padding:3.5mm 4mm;background:#fff;border-radius:2mm;border-left:3px solid var(--pop);box-shadow:0 1px 4px rgba(0,0,0,.06)">
        <div style="flex:0 0 28mm;text-align:center">
          <div style="font-family:'Lato',sans-serif;font-size:10pt;font-weight:900;color:var(--pop);line-height:1">Codex</div>
          <div style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave);margin-top:.5mm">openai.com/codex</div>
        </div>
        <div style="flex:1;border-left:1px solid rgba(0,0,0,.07);padding-left:4mm">
          <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--pop);margin-bottom:1mm">Front-end · React · Componentes · UI</div>
          <p style="font-size:8pt;color:var(--texto);line-height:1.5;margin:0">Especialista em geração de código front-end. Ideal para criar componentes React, páginas responsivas e interfaces completas a partir de uma descrição em texto.</p>
        </div>
        <div style="flex:0 0 20mm;text-align:center">
          <span style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:900;color:var(--pop);display:block">Gratuito</span>
          <span style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave)">plano free</span>
        </div>
      </div>

      <!-- Google AI Studio -->
      <div class="av up d3" style="display:flex;align-items:center;gap:4mm;padding:3.5mm 4mm;background:#fff;border-radius:2mm;border-left:3px solid var(--amber);box-shadow:0 1px 4px rgba(0,0,0,.06)">
        <div style="flex:0 0 28mm;text-align:center">
          <div style="font-family:'Lato',sans-serif;font-size:10pt;font-weight:900;color:var(--amber);line-height:1">AI Studio</div>
          <div style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave);margin-top:.5mm">aistudio.google.com</div>
        </div>
        <div style="flex:1;border-left:1px solid rgba(0,0,0,.07);padding-left:4mm">
          <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--amber);margin-bottom:1mm">Design · Prototipagem · Gemini API</div>
          <p style="font-size:8pt;color:var(--texto);line-height:1.5;margin:0">Gemini para criação de interfaces, geração de assets visuais e prototipagem rápida. Integra diretamente com código via API — ideal para features de I.A. dentro do seu SaaS.</p>
        </div>
        <div style="flex:0 0 20mm;text-align:center">
          <span style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:900;color:var(--amber);display:block">Gratuito</span>
          <span style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave)">plano free</span>
        </div>
      </div>

      <!-- Supabase -->
      <div class="av up d3" style="display:flex;align-items:center;gap:4mm;padding:3.5mm 4mm;background:#fff;border-radius:2mm;border-left:3px solid #3ECF8E;box-shadow:0 1px 4px rgba(0,0,0,.06)">
        <div style="flex:0 0 28mm;text-align:center">
          <div style="font-family:'Lato',sans-serif;font-size:10pt;font-weight:900;color:#3ECF8E;line-height:1">Supabase</div>
          <div style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave);margin-top:.5mm">supabase.com</div>
        </div>
        <div style="flex:1;border-left:1px solid rgba(0,0,0,.07);padding-left:4mm">
          <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#3ECF8E;margin-bottom:1mm">Banco de Dados · Auth · API · Storage</div>
          <p style="font-size:8pt;color:var(--texto);line-height:1.5;margin:0">Backend completo em minutos. PostgreSQL gerenciado + autenticação de usuários + API automática. Substitui uma equipe de back-end inteira. "Build in a weekend, scale to millions."</p>
        </div>
        <div style="flex:0 0 20mm;text-align:center">
          <span style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:900;color:#3ECF8E;display:block">Gratuito</span>
          <span style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave)">até 500MB</span>
        </div>
      </div>

      <!-- Vercel -->
      <div class="av up d4" style="display:flex;align-items:center;gap:4mm;padding:3.5mm 4mm;background:#fff;border-radius:2mm;border-left:3px solid var(--negro);box-shadow:0 1px 4px rgba(0,0,0,.06)">
        <div style="flex:0 0 28mm;text-align:center">
          <div style="font-family:'Lato',sans-serif;font-size:10pt;font-weight:900;color:var(--negro);line-height:1">Vercel</div>
          <div style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave);margin-top:.5mm">vercel.com</div>
        </div>
        <div style="flex:1;border-left:1px solid rgba(0,0,0,.07);padding-left:4mm">
          <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--negro);margin-bottom:1mm">Hospedagem · Deploy · CDN Global</div>
          <p style="font-size:8pt;color:var(--texto);line-height:1.5;margin:0">Deploy com um comando. Seu SaaS fica no ar em segundos, com SSL automático, CDN global e preview de cada atualização. Integra diretamente com GitHub.</p>
        </div>
        <div style="flex:0 0 20mm;text-align:center">
          <span style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:900;color:var(--negro);display:block">Gratuito</span>
          <span style="font-family:'Lato',sans-serif;font-size:6pt;color:var(--texto-suave)">hobby plan</span>
        </div>
      </div>

    </div>
  </div>
  <div class="pf"><span>Equipe Era da I.A.</span><span class="pnum">99</span></div>
</div>

<!-- ═══════════════════════════════════ P_MICROSAAS_3 — SCREENSHOTS SUPABASE + STITCH ════════════════════════ -->
<div class="page" id="p_microsaas_3">
  <div class="ph"><span>ERA DA I.A.</span><span>CAP. 08 — MICRO SAAS COM I.A.</span></div>
  <div class="page-inner" style="padding-top:18mm;display:flex;flex-direction:column;gap:0">

    <h2 class="av up d1" style="font-size:14pt;margin-bottom:3mm">As Plataformas em Ação</h2>

    <!-- Supabase screenshot -->
    <div class="av up d2" style="flex:1;display:flex;gap:4mm;align-items:stretch;margin-bottom:4mm;min-height:0">
      <div style="flex:0 0 52%;border-radius:2.5mm;overflow:hidden;box-shadow:0 3px 12px rgba(0,0,0,.15);position:relative">
        <img src="assets/images/supabase-screenshot.png" alt="Supabase — Build in a weekend, Scale to millions"
             style="width:100%;height:100%;object-fit:cover;object-position:top;display:block">
        <div style="position:absolute;bottom:0;left:0;right:0;padding:3mm 4mm;background:linear-gradient(transparent,rgba(3,11,20,.92))">
          <div style="font-family:'Lato',sans-serif;font-size:6pt;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#3ECF8E;margin-bottom:.5mm">Backend</div>
          <div style="font-family:'Playfair Display',serif;font-size:11pt;font-weight:700;color:#fff;line-height:1.2">Supabase</div>
          <div style="font-family:'Lato',sans-serif;font-size:7pt;color:rgba(255,255,255,.65)">supabase.com</div>
        </div>
      </div>
      <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:2.5mm">
        <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#3ECF8E;margin-bottom:1mm">Por que usar o Supabase</div>
        <div style="display:flex;align-items:flex-start;gap:2mm">
          <span style="color:#3ECF8E;font-weight:700;font-size:9pt;flex-shrink:0">—</span>
          <p style="font-size:8pt;line-height:1.55;color:var(--texto);margin:0">PostgreSQL gerenciado com painel visual — sem escrever SQL complexo</p>
        </div>
        <div style="display:flex;align-items:flex-start;gap:2mm">
          <span style="color:#3ECF8E;font-weight:700;font-size:9pt;flex-shrink:0">—</span>
          <p style="font-size:8pt;line-height:1.55;color:var(--texto);margin:0">Login de usuários pronto (email, Google, GitHub) em minutos</p>
        </div>
        <div style="display:flex;align-items:flex-start;gap:2mm">
          <span style="color:#3ECF8E;font-weight:700;font-size:9pt;flex-shrink:0">—</span>
          <p style="font-size:8pt;line-height:1.55;color:var(--texto);margin:0">API REST e realtime gerada automaticamente — zero backend manual</p>
        </div>
        <div style="display:flex;align-items:flex-start;gap:2mm">
          <span style="color:#3ECF8E;font-weight:700;font-size:9pt;flex-shrink:0">—</span>
          <p style="font-size:8pt;line-height:1.55;color:var(--texto);margin:0">Plano gratuito suporta projetos em produção com até 50.000 usuários ativos</p>
        </div>
        <div style="padding:2.5mm 3mm;background:rgba(62,207,142,.08);border-left:2px solid #3ECF8E;border-radius:.5mm;margin-top:1mm">
          <p style="font-size:7.5pt;color:var(--texto);line-height:1.5;margin:0"><strong>"Build in a weekend, scale to millions"</strong> — o slogan é a realidade para micro SaaS.</p>
        </div>
      </div>
    </div>

    <!-- Stitch screenshot -->
    <div class="av up d3" style="flex:1;display:flex;gap:4mm;align-items:stretch;min-height:0">
      <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:2.5mm">
        <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--pop);margin-bottom:1mm">Por que usar o Stitch</div>
        <div style="display:flex;align-items:flex-start;gap:2mm">
          <span style="color:var(--pop);font-weight:700;font-size:9pt;flex-shrink:0">—</span>
          <p style="font-size:8pt;line-height:1.55;color:var(--texto);margin:0">Gera UI de apps mobile e web a partir de uma descrição em português</p>
        </div>
        <div style="display:flex;align-items:flex-start;gap:2mm">
          <span style="color:var(--pop);font-weight:700;font-size:9pt;flex-shrink:0">—</span>
          <p style="font-size:8pt;line-height:1.55;color:var(--texto);margin:0">Entrega o design pronto para exportar como código React ou Flutter</p>
        </div>
        <div style="display:flex;align-items:flex-start;gap:2mm">
          <span style="color:var(--pop);font-weight:700;font-size:9pt;flex-shrink:0">—</span>
          <p style="font-size:8pt;line-height:1.55;color:var(--texto);margin:0">Alternativa: Google AI Studio e Claude Code também geram interfaces completas</p>
        </div>
        <div style="display:flex;align-items:flex-start;gap:2mm">
          <span style="color:var(--pop);font-weight:700;font-size:9pt;flex-shrink:0">—</span>
          <p style="font-size:8pt;line-height:1.55;color:var(--texto);margin:0">Ideal para quem não tem experiência em design — I.A. cuida do visual</p>
        </div>
        <div style="padding:2.5mm 3mm;background:rgba(34,211,238,.08);border-left:2px solid var(--pop);border-radius:.5mm;margin-top:1mm">
          <p style="font-size:7.5pt;color:var(--texto);line-height:1.5;margin:0"><strong>"Design at the speed of AI"</strong> — da ideia à interface funcional em minutos.</p>
        </div>
      </div>
      <div style="flex:0 0 52%;border-radius:2.5mm;overflow:hidden;box-shadow:0 3px 12px rgba(0,0,0,.15);position:relative">
        <img src="assets/images/stitch-screenshot.png" alt="Stitch — Design at the speed of AI"
             style="width:100%;height:100%;object-fit:cover;object-position:top;display:block">
        <div style="position:absolute;bottom:0;left:0;right:0;padding:3mm 4mm;background:linear-gradient(transparent,rgba(3,11,20,.92))">
          <div style="font-family:'Lato',sans-serif;font-size:6pt;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--pop);margin-bottom:.5mm">Design de UI</div>
          <div style="font-family:'Playfair Display',serif;font-size:11pt;font-weight:700;color:#fff;line-height:1.2">Stitch</div>
          <div style="font-family:'Lato',sans-serif;font-size:7pt;color:rgba(255,255,255,.65)">stitch.withgoogle.com</div>
        </div>
      </div>
    </div>

  </div>
  <div class="pf"><span>Equipe Era da I.A.</span><span class="pnum">99</span></div>
</div>

<!-- ═══════════════════════════════════ P_MICROSAAS_4 — COMO CONSTRUIR (TIMELINE) ══════════════════════════ -->
<div class="page" id="p_microsaas_4">
  <div class="ph"><span>ERA DA I.A.</span><span>CAP. 08 — MICRO SAAS COM I.A.</span></div>
  <div class="page-inner" style="padding-top:18mm">
    <h2 class="av up d1" style="font-size:14pt;margin-bottom:1mm">Do Zero ao SaaS em 48 Horas — O Processo</h2>
    <span class="rule av scale d1" style="width:22mm;margin-bottom:3mm"></span>

    <div style="display:flex;gap:5mm">
      <div style="flex:1">

        <!-- Timeline -->
        <div style="position:relative;padding-left:7mm">
          <div style="position:absolute;left:2.5mm;top:0;bottom:0;width:.3mm;background:linear-gradient(180deg,var(--ouro),var(--pop),var(--amber))"></div>

          <div class="av up d2" style="margin-bottom:4mm;position:relative">
            <div style="position:absolute;left:-7mm;top:1mm;width:4mm;height:4mm;border-radius:50%;background:var(--ouro);border:1.5px solid white;box-shadow:0 0 0 2px var(--ouro)"></div>
            <div style="font-family:'Lato',sans-serif;font-size:6.5pt;font-weight:700;color:var(--ouro);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.5mm">Sexta-feira — Noite (2h)</div>
            <div style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:700;color:var(--texto);margin-bottom:1mm">Definir a ideia com precisão cirúrgica</div>
            <p style="font-size:8pt;line-height:1.55;color:var(--texto-suave);margin:0">Escolha 1 problema específico de 1 nicho específico. Use o Claude para validar: "Esse problema tem pessoas dispostas a pagar R$37/mês para resolvê-lo?"</p>
          </div>

          <div class="av up d2" style="margin-bottom:4mm;position:relative">
            <div style="position:absolute;left:-7mm;top:1mm;width:4mm;height:4mm;border-radius:50%;background:var(--ouro);border:1.5px solid white;box-shadow:0 0 0 2px var(--ouro)"></div>
            <div style="font-family:'Lato',sans-serif;font-size:6.5pt;font-weight:700;color:var(--ouro);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.5mm">Sábado — Manhã (4h)</div>
            <div style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:700;color:var(--texto);margin-bottom:1mm">Design da interface com Stitch ou Claude Code</div>
            <p style="font-size:8pt;line-height:1.55;color:var(--texto-suave);margin:0">Descreva as telas em português: "Preciso de uma tela de login, dashboard com métricas e página de configurações." Stitch ou Claude Code geram o HTML/React.</p>
          </div>

          <div class="av up d3" style="margin-bottom:4mm;position:relative">
            <div style="position:absolute;left:-7mm;top:1mm;width:4mm;height:4mm;border-radius:50%;background:var(--pop);border:1.5px solid white;box-shadow:0 0 0 2px var(--pop)"></div>
            <div style="font-family:'Lato',sans-serif;font-size:6.5pt;font-weight:700;color:var(--pop);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.5mm">Sábado — Tarde (4h)</div>
            <div style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:700;color:var(--texto);margin-bottom:1mm">Back-end com Supabase + Claude Code</div>
            <p style="font-size:8pt;line-height:1.55;color:var(--texto-suave);margin:0">Crie o projeto no Supabase (gratuito). Peça ao Claude Code: "Configure o banco de dados, autenticação e API para este SaaS." Ele escreve toda a lógica.</p>
          </div>

          <div class="av up d3" style="margin-bottom:4mm;position:relative">
            <div style="position:absolute;left:-7mm;top:1mm;width:4mm;height:4mm;border-radius:50%;background:var(--pop);border:1.5px solid white;box-shadow:0 0 0 2px var(--pop)"></div>
            <div style="font-family:'Lato',sans-serif;font-size:6.5pt;font-weight:700;color:var(--pop);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.5mm">Sábado — Noite (2h)</div>
            <div style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:700;color:var(--texto);margin-bottom:1mm">Deploy no Vercel em 1 comando</div>
            <p style="font-size:8pt;line-height:1.55;color:var(--texto-suave);margin:0"><code style="background:var(--fundo-alt);padding:.5mm 1.5mm;border-radius:.5mm;font-size:7.5pt">vercel --prod</code> — SSL automático, CDN global, URL pública. Seu SaaS está no ar.</p>
          </div>

          <div class="av up d4" style="position:relative">
            <div style="position:absolute;left:-7mm;top:1mm;width:4mm;height:4mm;border-radius:50%;background:var(--amber);border:1.5px solid white;box-shadow:0 0 0 2px var(--amber)"></div>
            <div style="font-family:'Lato',sans-serif;font-size:6.5pt;font-weight:700;color:var(--amber);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.5mm">Domingo (4h)</div>
            <div style="font-family:'Lato',sans-serif;font-size:9pt;font-weight:700;color:var(--texto);margin-bottom:1mm">Pagamento + primeiros clientes</div>
            <p style="font-size:8pt;line-height:1.55;color:var(--texto-suave);margin:0">Integre Stripe ou Hotmart (30 min). Poste no LinkedIn/Instagram mostrando o produto. Ofereça 5 vagas com desconto de lançamento. Receita recorrente começa aqui.</p>
          </div>
        </div>
      </div>

      <div style="flex:0 0 52mm;display:flex;flex-direction:column;gap:3mm">
        <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ouro);margin-bottom:1mm">Receita Potencial — Micro SaaS</div>

        <div class="chart-wrap" style="gap:2.5mm">
          <div class="chart-row">
            <span class="chart-label" style="font-size:6.5pt">10 clientes</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:18%;background:var(--ouro)"><span class="chart-val" style="font-size:6pt">R$370</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label" style="font-size:6.5pt">50 clientes</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:40%;background:var(--ouro)"><span class="chart-val" style="font-size:6pt">R$1.850</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label" style="font-size:6.5pt">100 clientes</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:58%;background:var(--pop)"><span class="chart-val" style="font-size:6pt">R$3.700</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label" style="font-size:6.5pt">300 clientes</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:80%;background:var(--pop)"><span class="chart-val" style="font-size:6pt">R$11.100</span></div></div>
          </div>
          <div class="chart-row">
            <span class="chart-label" style="font-size:6.5pt">500 clientes</span>
            <div class="chart-bar-bg"><div class="chart-fill" style="width:100%;background:linear-gradient(90deg,var(--pop),var(--amber))"><span class="chart-val" style="font-size:6pt">R$18.500</span></div></div>
          </div>
        </div>
        <p style="font-size:6.5pt;color:var(--texto-suave);font-style:italic">Base: R$37/mês por cliente. Custo da stack: ~R$0 até 500 clientes.</p>

        <div style="background:var(--fundo-alt);border-radius:2mm;padding:3mm;border-left:2px solid var(--amber);margin-top:1mm">
          <div style="font-family:'Lato',sans-serif;font-size:6.5pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--amber);margin-bottom:1.5mm">Ideias validadas de Micro SaaS</div>
          <ul style="list-style:none;margin:0;padding:0">
            <li style="font-size:7.5pt;color:var(--texto);padding:1mm 0;border-bottom:.2mm solid rgba(0,0,0,.06)">Gerador de legendas com IA para Instagram</li>
            <li style="font-size:7.5pt;color:var(--texto);padding:1mm 0;border-bottom:.2mm solid rgba(0,0,0,.06)">Proposta comercial automática para freelas</li>
            <li style="font-size:7.5pt;color:var(--texto);padding:1mm 0;border-bottom:.2mm solid rgba(0,0,0,.06)">Dashboard de métricas para criadores</li>
            <li style="font-size:7.5pt;color:var(--texto);padding:1mm 0;border-bottom:.2mm solid rgba(0,0,0,.06)">Agendador de conteúdo com IA</li>
            <li style="font-size:7.5pt;color:var(--texto);padding:1mm 0">Analisador de concorrentes para e-commerce</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="pf"><span>Equipe Era da I.A.</span><span class="pnum">99</span></div>
</div>

<!-- ═══════════════════════════════════ P_MICROSAAS_5 — COMPARATIVO + RESUMO DARK ══════════════════════════ -->
<div class="page" id="p_microsaas_5" style="background:var(--negro)">
  <div class="ph" style="color:rgba(255,255,255,.3)"><span>ERA DA I.A.</span><span>CAP. 08 — MICRO SAAS COM I.A.</span></div>
  <div class="page-inner">
    <div class="cap-num av in" style="color:var(--pop)">Capítulo 08 — Resumo</div>
    <h2 class="av up d1" style="font-family:'Playfair Display',serif;font-size:16pt;color:#fff;margin-bottom:3mm">SaaS Tradicional vs. Micro SaaS com I.A.</h2>

    <!-- Comparativo -->
    <div class="av up d2" style="display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin-bottom:5mm">

      <div style="background:rgba(255,255,255,.04);border-radius:2mm;padding:4mm;border-top:2px solid rgba(255,255,255,.15)">
        <div style="font-family:'Lato',sans-serif;font-size:8pt;font-weight:700;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.1em;margin-bottom:3mm">SaaS Tradicional</div>
        <ul style="list-style:none;padding:0;margin:0">
          <li style="font-size:8pt;color:rgba(255,255,255,.6);padding:1.5mm 0;border-bottom:.2mm solid rgba(255,255,255,.06)">Equipe de 5–20 devs</li>
          <li style="font-size:8pt;color:rgba(255,255,255,.6);padding:1.5mm 0;border-bottom:.2mm solid rgba(255,255,255,.06)">6–18 meses para lançar</li>
          <li style="font-size:8pt;color:rgba(255,255,255,.6);padding:1.5mm 0;border-bottom:.2mm solid rgba(255,255,255,.06)">Investimento: R$500K+</li>
          <li style="font-size:8pt;color:rgba(255,255,255,.6);padding:1.5mm 0;border-bottom:.2mm solid rgba(255,255,255,.06)">Mercado amplo, muita concorrência</li>
          <li style="font-size:8pt;color:rgba(255,255,255,.6);padding:1.5mm 0">Venture Capital necessário</li>
        </ul>
      </div>

      <div style="background:rgba(34,211,238,.07);border-radius:2mm;padding:4mm;border-top:2px solid var(--pop)">
        <div style="font-family:'Lato',sans-serif;font-size:8pt;font-weight:700;color:var(--pop);text-transform:uppercase;letter-spacing:.1em;margin-bottom:3mm">Micro SaaS com I.A. ✓</div>
        <ul style="list-style:none;padding:0;margin:0">
          <li style="font-size:8pt;color:rgba(255,255,255,.85);padding:1.5mm 0;border-bottom:.2mm solid rgba(255,255,255,.06)">1 pessoa + I.A. = equipe completa</li>
          <li style="font-size:8pt;color:rgba(255,255,255,.85);padding:1.5mm 0;border-bottom:.2mm solid rgba(255,255,255,.06)">48 horas do zero ao ar</li>
          <li style="font-size:8pt;color:rgba(255,255,255,.85);padding:1.5mm 0;border-bottom:.2mm solid rgba(255,255,255,.06)">Investimento: R$0 (planos free)</li>
          <li style="font-size:8pt;color:rgba(255,255,255,.85);padding:1.5mm 0;border-bottom:.2mm solid rgba(255,255,255,.06)">Nicho específico, baixa concorrência</li>
          <li style="font-size:8pt;color:rgba(255,255,255,.85);padding:1.5mm 0">Bootstrapped — você fica com 100%</li>
        </ul>
      </div>
    </div>

    <!-- Key takeaways -->
    <div class="av up d3">
      <div style="font-family:'Lato',sans-serif;font-size:7pt;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--pop);margin-bottom:3mm">O que levar deste capítulo</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.5mm">
        <div style="display:flex;gap:2.5mm;align-items:flex-start">
          <span style="color:var(--pop);font-size:10pt;line-height:1.2;flex-shrink:0">—</span>
          <p style="font-size:8pt;color:rgba(255,255,255,.8);line-height:1.55;margin:0">Claude Code escreve o código. Você define a ideia e vende o produto.</p>
        </div>
        <div style="display:flex;gap:2.5mm;align-items:flex-start">
          <span style="color:var(--pop);font-size:10pt;line-height:1.2;flex-shrink:0">—</span>
          <p style="font-size:8pt;color:rgba(255,255,255,.8);line-height:1.55;margin:0">Supabase substitui uma equipe de back-end inteira — banco, auth e API em minutos.</p>
        </div>
        <div style="display:flex;gap:2.5mm;align-items:flex-start">
          <span style="color:var(--ouro);font-size:10pt;line-height:1.2;flex-shrink:0">—</span>
          <p style="font-size:8pt;color:rgba(255,255,255,.8);line-height:1.55;margin:0">Stitch e Google AI Studio eliminam a necessidade de designer para criar interfaces.</p>
        </div>
        <div style="display:flex;gap:2.5mm;align-items:flex-start">
          <span style="color:var(--ouro);font-size:10pt;line-height:1.2;flex-shrink:0">—</span>
          <p style="font-size:8pt;color:rgba(255,255,255,.8);line-height:1.55;margin:0">Vercel coloca seu produto no ar com SSL e CDN global em 1 comando.</p>
        </div>
        <div style="display:flex;gap:2.5mm;align-items:flex-start">
          <span style="color:var(--amber);font-size:10pt;line-height:1.2;flex-shrink:0">—</span>
          <p style="font-size:8pt;color:rgba(255,255,255,.8);line-height:1.55;margin:0">100 clientes a R$37/mês = R$3.700/mês recorrente, sem trocar hora por dinheiro.</p>
        </div>
        <div style="display:flex;gap:2.5mm;align-items:flex-start">
          <span style="color:var(--amber);font-size:10pt;line-height:1.2;flex-shrink:0">—</span>
          <p style="font-size:8pt;color:rgba(255,255,255,.8);line-height:1.55;margin:0">O mercado SaaS cresce 18% ao ano. Quem entrar agora tem vantagem de pioneiro.</p>
        </div>
      </div>
    </div>

    <div class="av scale d4" style="margin-top:4mm;padding:3mm 4mm;background:rgba(255,255,255,.04);border-radius:2mm;border-left:3px solid var(--amber)">
      <p style="font-size:8.5pt;color:rgba(255,255,255,.85);line-height:1.6;margin:0"><strong style="color:var(--amber);font-family:'Lato',sans-serif">Ação imediata:</strong> Escolha um problema que você mesmo tem — ou que vê nos seus clientes. Descreva em 1 frase. Pergunte ao Claude: "Como eu construiria um Micro SaaS para resolver isso com Supabase e Vercel?" O plano estará na sua tela em 30 segundos.</p>
    </div>
  </div>
  <div class="pf" style="color:rgba(255,255,255,.3)"><span>Equipe Era da I.A.</span><span class="pnum">99</span></div>
</div>

"""

# Insert before conclusion
if INSERT_BEFORE in html:
    html = html.replace(INSERT_BEFORE, PAGES + INSERT_BEFORE)
    print("OK: 5 páginas de Micro SaaS inseridas")
else:
    print("ERRO: marcador de conclusão não encontrado")
    exit()

# Renumber pages
num = 1
def renumber(m):
    global num
    result = re.sub(r'<span class="pnum">\d+</span>', f'<span class="pnum">{num}</span>', m.group(0))
    num += 1
    return result

html = re.sub(r'<div class="pf"[^>]*>.*?<span class="pnum">\d+</span>', renumber, html, flags=re.DOTALL)

pages_total = len(re.findall(r'<div class="page[^"]*" id="p', html))
EBOOK.write_text(html, encoding="utf-8")
print(f"OK: ebook salvo — {pages_total} páginas totais")
