# 10 Micro SaaS com I.A. — Do Zero ao Produto Funcionando
### Protótipo de Conteúdo — Versão 2.0

---

## CAPA

**Título:** 10 Micro SaaS com I.A.
**Subtítulo:** Do Zero ao Produto Funcionando — Stack, Prompts e Plano de Monetização
**Tagline:** 10 produtos digitais validados com Claude Code, Supabase e I.A. — construídos em um fim de semana, vendidos por assinatura.

---

## COMO USAR ESTE MATERIAL

Este guia entrega 10 ideias de Micro SaaS prontas para construir — cada uma com:
- A ideia e o mercado (quem paga e quanto)
- O stack completo (front-end + back-end + IA)
- O prompt exato para o Claude Code construir o produto
- O schema do banco de dados no Supabase
- Como lançar e cobrar assinatura

Não leia tudo de uma vez. Escolha 1 ideia que mais faz sentido para você. Execute primeiro, refine depois.

---

## O STACK COMPLETO

### Front-end

**Claude Code (Recomendado)** — Ferramenta de linha de comando da Anthropic. Você dá o prompt, ele escreve todo o código Next.js/React, cria os arquivos e configura o projeto. Melhor opção para quem quer controle total.

**Google AI Studio** — Plataforma do Google para usar o Gemini API. Ideal para criar protótipos rápidos e integrar IA generativa ao seu SaaS. Funciona como playground antes de integrar ao código.

**Lovable** — Construtor no-code/low-code. Gera UI com drag-and-drop. O mais fácil de começar, mas o mais limitado em personalização. Use para validar a ideia — mas não para produção.

### Back-end

**Supabase** — Banco de dados PostgreSQL gerenciado + autenticação + storage + edge functions. É o back-end completo de qualquer Micro SaaS. Plano gratuito robusto para começar.

**PostgreSQL** — O banco de dados que roda dentro do Supabase. Você cria tabelas com SQL simples. Todos os dados do seu SaaS ficam aqui.

**Vercel** — Hospedagem gratuita para o front-end Next.js. Deploy automático com git push.

**Stripe** — Pagamento por assinatura. Você cria planos Free e Pro, e o Stripe processa os pagamentos. No Brasil, use o Stripe + Hotmart para ter o gateway local.

---

## OS 10 MICRO SAAS

---

### SaaS 01 — BioGenius
**Gerador de Bio Profissional com IA**

Toda pessoa ativa nas redes sociais precisa de uma bio que converta. Freelancers, médicos, advogados, coaches — ninguém sabe escrever a própria bio. Você resolve em 30 segundos.

- **Quem paga:** Profissionais liberals, criadores, freelancers
- **Modelo:** Grátis (5 gerações/mês) | Pro R$29/mês (ilimitado)
- **Potencial:** 200 assinantes = R$5.800/mês

**Stack:** Next.js + Supabase + Anthropic API

**Schema:**
```sql
create table bios (
  id uuid default gen_random_uuid() primary key,
  user_id uuid references auth.users,
  input jsonb,
  output text,
  created_at timestamptz default now()
);
```

**Prompt Claude Code:**
```
Construa um SaaS chamado BioGenius em Next.js 14 App Router + TypeScript + Tailwind CSS + shadcn/ui.

PRODUTO: Gerador de bio profissional com IA para redes sociais.

PÁGINAS:
- / : landing page com headline, benefícios e CTA para cadastro
- /auth : login e cadastro via Supabase Auth
- /dashboard : formulário de geração + histórico

FORMULÁRIO:
- Nome, Área de atuação, Anos de experiência (select)
- 3 conquistas principais (3 inputs de texto)
- Tom desejado (radio: Formal / Descontraído / Criativo)
- Botão "Gerar Bio"

OUTPUT:
- 4 abas: Instagram (150 chars) | LinkedIn (300 palavras) | WhatsApp (80 chars) | Pitch 30s
- Botão "Copiar" em cada aba
- Histórico das últimas 10 gerações

MODELO DE ASSINATURA:
- Free: 5 gerações/mês
- Pro R$29/mês: ilimitado (Stripe Checkout)

BACK-END:
- Supabase Auth + tabela bios (schema acima)
- Route handler /api/generate chama Anthropic API (claude-haiku-3-5)
- Middleware verifica limite de uso no plano Free

ENV:
ANTHROPIC_API_KEY, NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY, STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET

Gere todos os arquivos completos prontos para deploy na Vercel.
```

---

### SaaS 02 — PropostaAI
**Gerador de Propostas Comerciais**

Freelancers e agências mandam orçamento no WhatsApp. Quem envia uma proposta profissional em PDF já ganhou a conta. Você entrega isso em 3 minutos.

- **Quem paga:** Freelancers, agências, consultores
- **Modelo:** Grátis (2 propostas/mês) | Pro R$47/mês (ilimitado + templates premium)
- **Potencial:** 150 assinantes = R$7.050/mês

**Stack:** Next.js + Supabase + Claude API + react-pdf

**Prompt Claude Code:**
```
Construa um SaaS chamado PropostaAI em Next.js 14 + TypeScript + Tailwind CSS.

PRODUTO: Gerador de propostas comerciais profissionais em PDF.

FORMULÁRIO:
- Dados do prestador: nome, empresa, serviço, cases/resultados
- Dados do cliente: nome empresa, segmento, problema relatado, objetivo
- Proposta: serviço proposto, prazo, valor, forma de pagamento, garantia

OUTPUT:
- Proposta em PDF com 6 seções: Sumário Executivo, Diagnóstico, Solução, Investimento, Próximos Passos, Sobre Nós
- Gerada pelo Claude API com base no formulário
- Preview na tela + botão Download PDF (usando @react-pdf/renderer)
- Histórico de propostas salvas

MODELO: Free 2/mês | Pro R$47/mês

BACK-END: Supabase Auth + tabela proposals + Route handler /api/generate-proposal

Gere todos os arquivos completos.
```

---

### SaaS 03 — ContentPilot
**Planejador de Conteúdo Mensal com IA**

Social media managers gastam horas criando calendários editoriais. Com o ContentPilot, preenchem o briefing e recebem 30 posts prontos com tema, formato e legenda.

- **Quem paga:** Social media managers, agências, empreendedores
- **Modelo:** Grátis (1 calendário/mês) | Pro R$37/mês (ilimitado + múltiplos clientes)
- **Potencial:** 300 assinantes = R$11.100/mês

**Prompt Claude Code:**
```
Construa um SaaS chamado ContentPilot em Next.js 14 + TypeScript + Tailwind CSS.

PRODUTO: Gerador de calendário de conteúdo mensal com IA.

FORMULÁRIO:
- Nome da marca, segmento, público-alvo
- Objetivo do mês (lançamento/branding/vendas/engajamento)
- Produto/serviço em foco
- Datas especiais do mês

OUTPUT:
- Tabela com 30 posts: Data | Tipo (carrossel/reel/estático) | Tema | Ângulo | Legenda completa | CTA | 10 hashtags
- Exportar como CSV (para importar em ferramentas de agendamento)
- Histórico por cliente (workspace multi-cliente)

MODELO: Free 1 calendário/mês | Pro R$37/mês

Back-end: Supabase + Claude API. Gere todos os arquivos.
```

---

### SaaS 04 — ColdPitch
**Gerador de E-mails de Prospecção Fria**

SDRs e empreendedores perdem horas escrevendo e-mails frios genéricos. O ColdPitch gera e-mail principal + 3 follow-ups personalizados em 60 segundos.

- **Quem paga:** Vendedores, SDRs, agências B2B, consultores
- **Modelo:** Grátis (10 e-mails/mês) | Pro R$49/mês (ilimitado)
- **Potencial:** 200 assinantes = R$9.800/mês

**Prompt Claude Code:**
```
Construa um SaaS chamado ColdPitch em Next.js 14 + TypeScript + Tailwind CSS.

PRODUTO: Gerador de e-mails de prospecção fria com sequência de follow-up.

FORMULÁRIO:
- Empresa alvo: nome, segmento, porte, cargo do contato
- Meu serviço: o que ofereço, resultado principal, diferencial
- Tom: direto/consultivo/curioso

OUTPUT:
- E-mail principal (assunto + corpo, max 150 palavras)
- Follow-up 1 (após 3 dias, ângulo diferente)
- Follow-up 2 (após 7 dias, prova social)
- Follow-up 3 (após 14 dias, breakup email)
- Botão copiar individual para cada e-mail

Histórico de sequências salvas. MODELO: Free 10/mês | Pro R$49/mês.
Back-end: Supabase + Claude API. Gere todos os arquivos.
```

---

### SaaS 05 — AdForge
**Criador de Anúncios para Meta e Google**

Gestores de tráfego criam dezenas de variações de anúncio por semana. O AdForge gera copy, headline e descrição em segundos — com variações para teste A/B.

- **Quem paga:** Gestores de tráfego, empreendedores, agências
- **Modelo:** Grátis (20 criações/mês) | Pro R$39/mês
- **Potencial:** 400 assinantes = R$15.600/mês

**Prompt Claude Code:**
```
Construa um SaaS chamado AdForge em Next.js 14 + TypeScript + Tailwind CSS.

PRODUTO: Gerador de anúncios para Meta Ads e Google Ads.

FORMULÁRIO:
- Produto/serviço, preço, público-alvo
- Plataforma (Meta Ads / Google Ads / Ambos)
- Objetivo (tráfego/conversão/geração de leads/app)
- Tom (urgência/benefício/curiosidade/história)

OUTPUT para Meta:
- 3 variações de headline (max 40 chars)
- 3 variações de texto primário (max 125 chars)
- 2 variações de descrição

OUTPUT para Google:
- 3 headlines responsivos (max 30 chars)
- 2 descrições (max 90 chars)
- 10 palavras-chave sugeridas

Histórico de campanhas. MODELO: Free 20/mês | Pro R$39/mês.
Back-end: Supabase + Claude API. Gere todos os arquivos.
```

---

### SaaS 06 — ContratoFácil
**Gerador de Contratos para Freelancers**

A maioria dos freelancers trabalha sem contrato e perde dinheiro em disputas. O ContratoFácil gera contratos profissionais em PDF adaptados ao tipo de serviço — em 2 minutos, sem advogado.

- **Quem paga:** Freelancers, prestadores de serviço, autônomos
- **Modelo:** Grátis (1 contrato/mês) | Pro R$27/mês (ilimitado)
- **Potencial:** 500 assinantes = R$13.500/mês

**Prompt Claude Code:**
```
Construa o SaaS ContratoFácil em Next.js 14 + TypeScript + Tailwind + shadcn/ui + @react-pdf/renderer.

PRODUTO: Gerador de contratos simples para freelancers com download em PDF.
FORMULÁRIO:
  Tipo de serviço (select: Design / Desenvolvimento / Marketing / Consultoria / Conteúdo / Outro)
  Partes: Prestador (nome, CPF/CNPJ, endereço) + Contratante (nome, CPF/CNPJ)
  Detalhes: descrição do serviço, valor total, forma de pagamento (à vista / 50-50 / parcelado), prazo de entrega, número de revisões inclusas, o que NÃO está incluso, multa por cancelamento (%), confidencialidade (sim/não)
OUTPUT: Contrato em português jurídico simples — preview na tela + Download PDF
  Seções: Objeto do Contrato, Valor e Pagamento, Prazo, Revisões, Propriedade Intelectual, Confidencialidade, Rescisão, Foro.
Histórico de contratos com status (rascunho/enviado/assinado).
PLANOS: Free 1 contrato/mês | Pro R$27/mês ilimitado
BACK-END: Supabase + tabela contracts (id, user_id, input jsonb, content text, status, created_at)
Route /api/generate-contract → claude-3-5-sonnet-20241022
Gere todos os arquivos prontos para Vercel.
```

---

### SaaS 07 — CVScanner
**Analisador de Currículo para Vagas Específicas**

80% dos currículos são eliminados por sistemas automáticos antes de um humano ler. O CVScanner analisa o currículo do candidato contra a descrição da vaga e retorna um score de 0 a 100 com as mudanças exatas para aumentar as chances.

- **Quem paga:** Candidatos a emprego, profissionais em transição
- **Modelo:** Grátis (2 análises/mês) | Pro R$19/mês
- **Potencial:** 800 assinantes = R$15.200/mês

**Prompt Claude Code:**
```
Construa o SaaS CVScanner em Next.js 14 + TypeScript + Tailwind + shadcn/ui.

PRODUTO: Analisador de currículo contra descrição de vaga com score e melhorias.
PÁGINAS: / | /auth | /dashboard (análise) | /historico
INPUTS:
  - Textarea para colar o texto do currículo (ou upload PDF via Supabase Storage)
  - Textarea para colar a descrição completa da vaga
  - Campo: empresa e cargo (para personalização)
OUTPUT:
  - Score geral de 0 a 100 (barra de progresso colorida)
  - Score por categoria: Palavras-chave, Experiência, Formação, Formato/ATS
  - Lista de palavras-chave da vaga ausentes no currículo
  - Lista de melhorias específicas (numeradas, priorizadas)
  - Versão reescrita do resumo profissional
PLANOS: Free 2 análises/mês | Pro R$19/mês ilimitado
BACK-END: Supabase + tabela analyses (id, user_id, cv_text text, job_text text, score int, result jsonb, created_at)
Route /api/analyze-cv → Gemini 2.0 Flash
ENV: GOOGLE_AI_API_KEY, NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY, STRIPE_SECRET_KEY
Gere todos os arquivos prontos para Vercel.
```

---

### SaaS 08 — FAQForge
**Criador de FAQ para E-commerce**

Lojas online com FAQ bem estruturada convertem 23% mais. A maioria não tem FAQ. O FAQForge gera 20 perguntas e respostas otimizadas para SEO em 60 segundos.

- **Quem paga:** Lojistas, e-commerces, empreendedores digitais
- **Modelo:** Grátis (3 FAQs/mês) | Pro R$29/mês
- **Potencial:** 300 assinantes = R$8.700/mês

**Prompt Claude Code:**
```
Construa FAQForge em Next.js 14 + TypeScript + Tailwind. PRODUTO: Gerador de FAQ para e-commerce. 
FORMULÁRIO: Nome da loja, categoria (moda/eletrônicos/cosméticos/alimentos/outro), produto principal, política de frete, política de troca, formas de pagamento, prazo de entrega. 
OUTPUT: 20 pares P+R em 4 categorias (Produto 6, Envio 5, Pagamento 5, Trocas 4) + versão HTML para copiar no site + versão JSON Schema (rich snippet Google). 
PLANOS: Free 3 FAQs/mês | Pro R$29/mês. 
BACK-END: Supabase + Claude API. Gere todos os arquivos.
```

---

### SaaS 09 — ListingPro
**Descrições de Produto Otimizadas para E-commerce**

Descrição genérica = produto invisível. O ListingPro gera título SEO, descrição persuasiva, bullets de benefícios e palavras-chave para Shopee, ML e lojas próprias.

- **Quem paga:** Lojistas Shopee/ML/Shopify
- **Modelo:** Grátis (5 produtos/mês) | Pro R$37/mês (ilimitado)
- **Potencial:** 400 assinantes = R$14.800/mês

**Prompt Claude Code:**
```
Construa ListingPro em Next.js 14 + TypeScript + Tailwind. PRODUTO: Gerador de descrições de produto para e-commerce. 
FORMULÁRIO: Nome do produto, especificações técnicas (textarea), público comprador, problema que resolve, diferencial vs concorrentes, plataforma (Shopee/ML/Shopify/WooCommerce/Outro). 
OUTPUT: Título SEO (max 80 chars), Subtítulo, Descrição (3-4 parágrafos), 8 bullets de vantagens, Tabela de specs, 5 P+R frequentes, 15 palavras-chave SEO, Versão para anúncio (headline 40 chars + texto 125 chars). 
Processamento em lote (até 10 produtos de uma vez no Pro). 
PLANOS: Free 5 produtos/mês | Pro R$37/mês ilimitado. 
BACK-END: Supabase + Gemini 2.0 Flash. Gere todos os arquivos.
```

---

### SaaS 10 — ReportAI
**Gerador de Relatórios de Performance para Agências**

Agências digitais gastam 3 a 5 horas por semana criando relatórios de resultado para clientes. O ReportAI transforma dados brutos em relatório executivo em 5 minutos.

- **Quem paga:** Agências digitais, gestores de tráfego, consultores de marketing
- **Modelo:** Grátis (2 relatórios/mês) | Pro R$57/mês (ilimitado + white-label)
- **Potencial:** 150 assinantes = R$8.550/mês

**Prompt Claude Code:**
```
Construa o SaaS ReportAI em Next.js 14 + TypeScript + Tailwind + shadcn/ui + @react-pdf/renderer.

PRODUTO: Gerador de relatórios de performance para agências digitais com exportação PDF.
FORMULÁRIO (estruturado):
  Cliente: nome, segmento, objetivo da campanha, período (de/até)
  Dados Meta Ads: investimento, alcance, impressões, cliques, conversões, custo por resultado
  Dados Google Analytics: sessões, usuários novos, taxa de rejeição, duração média, conversões
  Dados de redes sociais: seguidores, alcance orgânico, engajamento, posts publicados
  Observações: conquistas do período, o que não funcionou, plano próximo mês
OUTPUT (relatório executivo):
  Capa com logo do cliente e período | Sumário executivo (análise da IA) | Resultados em destaque (3 métricas principais) | Análise por canal com gráficos CSS | Pontos positivos e de atenção | Recomendações
  Exportar como PDF (branding configurável no plano Pro/White-label)
PLANOS: Free 2 relatórios/mês | Pro R$57/mês ilimitado + white-label
BACK-END: Supabase + tabela reports + tabela clients
Route /api/generate-report → claude-3-5-sonnet-20241022
Gere todos os arquivos prontos para deploy na Vercel.
```

---

## MONETIZAÇÃO

### Stripe + Supabase (stack de pagamento)

1. Criar conta no Stripe (stripe.com)
2. Criar produto + plano mensal no Stripe Dashboard
3. Instalar `stripe` no Next.js
4. Criar Route handler /api/create-checkout com Stripe Checkout
5. Webhook /api/webhook atualiza campo `plan` no Supabase quando pagamento confirmar
6. Middleware verifica `plan === 'pro'` para liberar funcionalidades

```sql
-- Adicionar ao perfil do usuário
alter table profiles add column plan text default 'free';
alter table profiles add column stripe_customer_id text;
alter table profiles add column current_period_end timestamptz;
```

---

## POTENCIAL DE FATURAMENTO

| SaaS | Assinantes 100 | Assinantes 300 | Assinantes 500 |
|---|---|---|---|
| BioGenius R$29 | R$2.900 | R$8.700 | R$14.500 |
| PropostaAI R$47 | R$4.700 | R$14.100 | R$23.500 |
| ContentPilot R$37 | R$3.700 | R$11.100 | R$18.500 |
| ColdPitch R$49 | R$4.900 | R$14.700 | R$24.500 |
| AdForge R$39 | R$3.900 | R$11.700 | R$19.500 |

**O objetivo de 300 assinantes em um SaaS B2B de R$37-49 é atingível em 3-6 meses com tráfego orgânico.**

---

## PRÓXIMOS PASSOS

1. Escolha 1 SaaS desta lista que resolve um problema que você mesmo tem
2. Instale o Claude Code: `npm install -g @anthropic-ai/claude-code`
3. Cole o prompt do SaaS escolhido no Claude Code
4. Crie a conta no Supabase (supabase.com) — gratuito
5. Deploy na Vercel (vercel.com) — gratuito
6. Configure o Stripe para cobrar assinatura
7. Lance com preço baixo (R$19-29/mês) para os primeiros 20 clientes
8. Valide a retenção antes de escalar o preço

---

*Fim do Protótipo — 10 Micro SaaS com I.A.*
*Versão 2.0 — Para execução imediata*
