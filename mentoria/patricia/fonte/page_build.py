import plano, html, re, sys
E = html.escape
P = sys.argv[1]
old = open(P).read()
head = old[:old.index("<div class=\"wrap\">")]
TAG = {"ML":"t-ml","Port.":"t-pt","Dir.":"t-dir","Revisão":"t-rev"}
def slot(h, tag, txt): return f'<div class="slot"><span class="h">{h}</span><span><span class="tag {TAG[tag]}">{tag}</span> {txt}</span></div>'
def day(name, a, b): return f'<div class="day"><h4>{name}</h4>{slot("07:00–08:00",*a)}{slot("08:00–09:00",*b)}</div>'
off = lambda n: f'<div class="day off"><h4>{n}</h4><div class="slot"><span>Plantão · sem estudo</span></div></div>'
rows = []
ph = {1:"Fase 1 · Base: 1ª leitura de todo o edital com questões (S1–S20)", 21:"Fase 2 · Questões e simulados (S21–S25)", 26:"Fase 3 · Reta final"}
for w in plano.WEEKS:
    if w["n"] in ph: rows.append(f'<tr class="phase-head"><td colspan="6">{ph[w["n"]]}</td></tr>')
    ex = [f"{w['questoes']} q. ({w['q_split']})"]
    if w["rev30"] != "—": ex.append(f"Rev. 30d: {w['rev30']}")
    if w["simulado"]: ex.append(f'<span class="tag t-sim">{E(w["simulado"])}</span>')
    if w["taf"]: ex.append("Teste físico")
    first = f'<td>S{w["n"]}<br><span class="muted">{w["datas"]}</span></td>'
    if w["rec"] or w["n"] == 26:
        rows.append(f'<tr class="{"recovery" if w["rec"] else "phase-row"}">{first}<td colspan="3">{E(w["resumo"])}</td><td>{"<br>".join(ex)}</td><td>{E(w["esperado"])}</td></tr>')
    else:
        rows.append(f'<tr class="phase-row">{first}<td>{E(w["ml"])}</td><td>{E(w["pt"])}</td><td>{E(w["di"])}</td><td>{"<br>".join(ex)}</td><td>{E(w["esperado"])}</td></tr>')

body = f'''<div class="wrap">
<header class="top">
  <span class="eyebrow">Mentoria · Plano de estudos individual · versão 2h/dia</span>
  <h1>Patrícia de Miranda Oliveira<br><span style="color:var(--accent)">Perito Legista · PCERJ</span></h1>
  <div class="meta">
    <span>Base: <b>Edital nº 05/2021 (retif. 10/05/2022), banca FGV</b></span>
    <span>Horizonte: <b>26 semanas · 02/11/2026 → 02/05/2027</b></span>
    <span>Carga: <b>2h por dia · 10h por semana</b></span>
  </div>
</header>
<nav class="index" aria-label="Seções">
  <a href="#diagnostico">1 Diagnóstico</a><a href="#semana">2 Semana</a><a href="#ciclo">3 Imprevistos</a><a href="#conteudo">4 Plano por semana</a><a href="#revisao">5 Revisão e questões</a><a href="#materiais">6 Materiais</a><a href="#taf">TAF</a><a href="#pendencias">Pendências</a>
</nav>

<section id="diagnostico"><span class="sec-num">1</span><h2>Diagnóstico inicial</h2>
<div class="facts">
 <div class="fact"><div class="v mono">10h</div><div class="l">por semana: 5 dias × 2h (07h–09h, 2 blocos de 1h)</div></div>
 <div class="fact"><div class="v mono">26 sem.</div><div class="l">cerca de 255 h no total, com 2 semanas de recuperação</div></div>
 <div class="fact"><div class="v mono">100 q.</div><div class="l">ML 50 · Port 30 · Dir 20. Mínimo de 50% em cada módulo</div></div>
 <div class="fact"><div class="v mono">Top 300</div><div class="l">vão ao TAF (195 vagas na ampla concorrência) para 25 vagas</div></div>
</div>
<p>Estuda na segunda, quarta, quinta, sexta e domingo, das 07h às 09h. Terça e sábado são dias de plantão. Nível atual: zero em Medicina Legal pericial e em Direito, Português com nota 1–2 e Ética médica com nota 2. É o primeiro concurso.</p>
<div class="tbl mid"><table>
<thead><tr><th>Disciplina</th><th class="num">Peso</th><th class="num">Horas/sem.</th><th>Participação</th><th>Por quê</th></tr></thead><tbody>
<tr><td><span class="tag t-ml">Medicina Legal</span></td><td class="num">50%</td><td class="num">4h</td><td><div class="bar"><i style="width:40%"></i></div></td><td><b>Prioridade 1.</b> Metade da prova e 1º critério de desempate. A formação médica acelera o aprendizado.</td></tr>
<tr><td><span class="tag t-pt">Português</span></td><td class="num">30%</td><td class="num">3h</td><td><div class="bar"><i style="width:30%"></i></div></td><td><b>Prioridade 2.</b> Segundo maior peso e gramática fraca. Interpretação toda semana.</td></tr>
<tr><td><span class="tag t-dir">Direito</span></td><td class="num">20%</td><td class="num">2h</td><td><div class="bar"><i style="width:20%"></i></div></td><td><b>Mínimo protegido.</b> Estudo enxuto (lei seca e questões) para garantir pelo menos 10 de 20.</td></tr>
<tr><td><span class="tag t-rev">Revisão</span></td><td class="num">–</td><td class="num">1h</td><td><div class="bar"><i style="width:10%"></i></div></td><td>Revisão de 7 e 30 dias, caderno de erros e painel, no domingo.</td></tr>
</tbody></table></div>
<div class="note"><p><strong>Com 2h por dia, o plano é possível, mas apertado.</strong> A 1ª leitura do edital termina só na semana 20, e sobram 5 semanas de questões e simulados. Direito fica em nível de "noções".</p>
<p>Para ter mais margem: (a) estender o horizonte para 9–12 meses mantendo as 2h, o mais realista enquanto não há edital; ou (b) subir para 3h em 2 dias da semana, o que antecipa a 1ª leitura para cerca da semana 15.</p>
<p>Outros riscos: ainda não há edital publicado (conteúdo e data podem mudar), não há nenhum dia totalmente livre e o TAF ainda não foi avaliado.</p></div>
</section>

<section id="semana"><span class="sec-num">2</span><h2>Distribuição semanal</h2>
<p>Dois blocos de 1h. Cada bloco começa com 10 minutos de revisão de 24h da mesma matéria e termina com 3 minutos de registro na planilha.</p>
<div class="grid-days">
{day("Segunda",("ML","Teoria"),("ML","Questões + resumo"))}{off("Terça")}
{day("Quarta",("Port.","Teoria + questões"),("Dir.","Teoria resumida + lei seca"))}
{day("Quinta",("ML","Teoria (continuação)"),("Port.","Questões FGV"))}
{day("Sexta",("ML","Questões + flashcards"),("Dir.","Questões"))}{off("Sábado")}
{day("Domingo",("Port.","Interpretação FGV"),("Revisão","7/30 dias + painel"))}
</div>
<p class="muted">Fase 2 (S21–S25): os blocos de teoria viram questões dirigidas aos erros. Em S21, S23 e S25, o domingo é um simulado de 100 questões das 07h às 12h, a mesma duração da prova. Semanas 8 (Natal) e 15 (Carnaval): carga reduzida, só revisão e atrasos.</p>
</section>

<section id="ciclo"><span class="sec-num">3</span><h2>Quando algo der errado</h2>
<p>A semana é uma sequência de 10 blocos. Depois de um imprevisto, faça o <b>próximo bloco da sequência</b>, não o bloco "do dia".</p>
<div class="cycle"><span class="t-ml">ML teoria</span><span class="t-ml">ML questões</span><span class="t-pt">Port. teoria</span><span class="t-dir">Dir. teoria</span><span class="t-ml">ML teoria</span><span class="t-pt">Port. questões</span><span class="t-ml">ML questões</span><span class="t-dir">Dir. questões</span><span class="t-pt">Port. interpretação</span><span class="t-rev">Revisão</span></div>
<ol><li><b>1 bloco perdido:</b> metade do bloco de revisão de domingo repõe.</li>
<li><b>2 ou mais blocos perdidos:</b> anote o tópico e reponha na semana de recuperação (S8 ou S15).</li>
<li><b>Disciplina abaixo de 60% de acerto:</b> ganha 1 bloco por 2 semanas, tirado da disciplina com melhor acerto. Medicina Legal nunca perde bloco.</li>
<li><b>Plantão extra ou exaustão:</b> faça só o bloco 1. A meta da semana manda mais que a do dia.</li>
<li><b>Atraso de mais de 2 semanas:</b> replanejar com a mentora.</li></ol>
</section>

<section id="conteudo"><span class="sec-num">4</span><h2>Plano do conteúdo por semana</h2>
<p>Tópicos do Anexo I do edital de 2021. Os códigos (ML01, PT01, DI01…) são os mesmos da planilha e do checklist do edital.</p>
<div class="tbl wide"><table><thead><tr><th>Semana</th><th>Medicina Legal (4h)</th><th>Português (3h)</th><th>Direito (2h)</th><th>Questões · revisão · extras</th><th>Resultado esperado</th></tr></thead><tbody>
{"".join(rows)}
</tbody></table></div>
</section>

<section id="revisao"><span class="sec-num">5</span><h2>Sistema de revisão e questões</h2>
<div class="two"><div>
<h3>Revisões</h3><ul>
<li><b>24h:</b> início do próximo bloco da matéria. Escreve de memória 5 pontos e depois confere.</li>
<li><b>7 dias:</b> domingo. Resumos da semana e questões erradas.</li>
<li><b>30 dias:</b> domingo, com o conteúdo indicado na tabela. Nas semanas 8 e 15, em bloco.</li>
<li><b>Flashcards:</b> 10–15 min por dia, fora dos blocos.</li></ul></div><div>
<h3>Questões e erros</h3><ul>
<li>Sempre do tópico recém-estudado, começando pela FGV.</li>
<li>Chute certo conta como erro no caderno.</li>
<li>Caderno de erros: motivo do erro e a regra correta em 1 linha. Revisão 7 dias depois.</li></ul></div></div>
<div class="tbl mid"><table><thead><tr><th>Período</th><th class="num">Questões/sem.</th><th>Meta de acerto</th></tr></thead><tbody>
<tr><td>S1–S7</td><td class="num">50</td><td>Acima de 50%</td></tr>
<tr><td>S9–S20</td><td class="num">70</td><td>Acima de 55–60%</td></tr>
<tr><td>S21–S25</td><td class="num">120 + simulados</td><td>Acima de 65–70% no geral e de 60% em cada módulo</td></tr></tbody></table></div>
</section>

<section id="materiais"><span class="sec-num">6</span><h2>Materiais da mentoria</h2>
<div class="tbl mid"><table><thead><tr><th>Material</th><th>Uso</th></tr></thead><tbody>
<tr><td><b>Guia da Aluna</b> (PDF)</td><td>Como estudar cada bloco, o ritual de domingo, revisões, simulados, regras de atraso e TAF. Ler antes da semana 1.</td></tr>
<tr><td><b>Cronograma de 26 semanas</b> (PDF)</td><td>O que estudar em cada semana. Consultar todo domingo.</td></tr>
<tr><td><b>Planilha de estudos</b> (Excel)</td><td>Registro diário, checklist do edital com datas de revisão automáticas, caderno de erros, simulados, TAF e painel com alertas.</td></tr>
<tr><td><b>Checklists</b> (PDF)</td><td>Folha semanal (imprimir 26 vezes), domingo, mês, simulado, edital publicado, semana e dia da prova, e checklist dos 51 tópicos.</td></tr>
</tbody></table></div>
</section>

<section id="taf"><span class="sec-num">Extra</span><h2>Teste de Aptidão Física</h2>
<p>Índices femininos do edital de 2021, com uma única tentativa em cada teste: 15 flexões de braço em 1 min · 20 abdominais em 1 min · 100 m em até 22 s · 1.600 m em até 12 min. Treino 3 vezes por semana à tarde. Testes nas semanas 4, 8, 12, 16, 20 e 24.</p>
</section>

<section id="pendencias"><span class="sec-num">Pendências</span><h2>A confirmar com a Patrícia</h2>
<ol><li>Os plantões de terça e sábado são diurnos, noturnos ou de 24h?</li>
<li>Qual material teórico e qual plataforma de questões ela vai usar?</li>
<li>Como está o condicionamento físico e quais tardes estão livres para treinar?</li>
<li>Prefere manter 2h com horizonte maior ou aumentar a carga em alguns dias?</li></ol>
</section>
<footer>Plano elaborado a partir do Edital nº 05/2021 da SEPOL/RJ (retificado em 10/05/2022). Revisar quando o novo edital for publicado.</footer>
</div>
'''
open(P, "w").write(head + body)
print("ok")
