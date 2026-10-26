import plano, html
E = html.escape
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,500..800&family=Public+Sans:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');
:root{--ink:#17201e;--muted:#5a6863;--line:#cfd8d5;--acc:#1d6b62;--soft:#e4f0ed;--warn:#a65d12;--wsoft:#fbf0e3;--ml:#1d6b62;--pt:#3f4fa0;--dir:#8a3348}
*{box-sizing:border-box}
body{font-family:'Public Sans',Arial,sans-serif;color:var(--ink);font-size:10.5pt;line-height:1.5;margin:0}
h1,h2,h3{font-family:'Archivo','Arial Narrow',sans-serif;font-stretch:85%;line-height:1.15;margin:0}
h1{font-size:26pt;font-weight:800;color:var(--acc)}
h2{font-size:16pt;font-weight:750;margin:18px 0 8px;padding-top:6px;border-top:2px solid var(--acc)}
h3{font-size:12pt;font-weight:700;margin:12px 0 4px}
p{margin:0 0 7px} ul,ol{margin:0 0 8px;padding-left:20px} li{margin-bottom:3px}
.eyebrow{font-family:'IBM Plex Mono',monospace;font-size:8pt;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.mono{font-family:'IBM Plex Mono',monospace}
.muted{color:var(--muted)}
table{border-collapse:collapse;width:100%;font-size:9pt;margin:4px 0 10px;page-break-inside:auto}
tr{page-break-inside:avoid}
th{font-family:'IBM Plex Mono',monospace;font-size:7.5pt;text-transform:uppercase;letter-spacing:.05em;color:#fff;background:var(--acc);text-align:left;padding:5px 6px;font-weight:500}
td{border-bottom:1px solid var(--line);padding:5px 6px;vertical-align:top}
tr.rec td{background:var(--wsoft)} tr.ph td{background:var(--soft);font-weight:700;font-family:'Archivo',sans-serif;font-stretch:85%;font-size:10.5pt}
.note{background:var(--wsoft);border-left:3px solid var(--warn);padding:8px 12px;margin:8px 0 12px}
.note b{color:var(--warn)}
.box{border:1px solid var(--line);border-radius:6px;padding:10px 12px;margin:6px 0 10px;break-inside:avoid}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:10px 0}
.fact{border:1px solid var(--line);border-radius:6px;padding:8px 10px}
.fact .v{font-family:'Archivo',sans-serif;font-stretch:85%;font-size:17pt;font-weight:750;color:var(--acc)}
.fact .l{font-size:8.5pt;color:var(--muted)}
.cb{display:inline-block;width:11px;height:11px;border:1.3px solid var(--ink);border-radius:2px;vertical-align:-1px;margin-right:6px}
ul.ck{list-style:none;padding-left:0} ul.ck li{padding-left:0}
td.c{text-align:center}
.pb{page-break-before:always}
.cover{border-bottom:1px solid var(--line);padding-bottom:12px;margin-bottom:6px}
.tag{font-size:8pt;font-weight:700;padding:0 6px;border-radius:9px;border:1px solid currentColor}
.ml{color:var(--ml)}.pt{color:var(--pt)}.dir{color:var(--dir)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.line{border-bottom:1px solid var(--ink);display:inline-block;min-width:120px}
"""
def doc(title, body, landscape=False):
    return f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>{E(title)}</title><style>{CSS}@page{{size:A4 {'landscape' if landscape else 'portrait'};margin:14mm 13mm}}</style></head><body>{body}</body></html>"
def cover(eyebrow, title, subtitle):
    return f"<div class='cover'><div class='eyebrow'>{E(eyebrow)}</div><h1>{title}</h1><p class='muted'>{subtitle}</p></div>"
CB = "<span class='cb'></span>"
def ck(items): return "<ul class='ck'>" + "".join(f"<li>{CB}{i}</li>" for i in items) + "</ul>"
SUB = f"{plano.ALUNA} · Perito Legista PCERJ · 2h por dia · 02/11/2026 → 02/05/2027"

# ================= 01 GUIA =================
g = cover("Mentoria · Guia de uso", "Como seguir o seu plano", SUB)
g += """
<div class="facts">
 <div class="fact"><div class="v mono">2h</div><div class="l">por dia, das 07h às 09h, em 2 blocos de 1h</div></div>
 <div class="fact"><div class="v mono">5 dias</div><div class="l">seg, qua, qui, sex e dom. Terça e sábado são plantão</div></div>
 <div class="fact"><div class="v mono">10h</div><div class="l">por semana: ML 4h · Port. 3h · Dir. 2h · Revisão 1h</div></div>
 <div class="fact"><div class="v mono">26 sem.</div><div class="l">1ª leitura do edital até S20, depois questões e simulados</div></div>
</div>
<h2>1. Seus materiais e quando usar cada um</h2>
<table><tr><th>Material</th><th>Para quê</th><th>Quando usar</th></tr>
<tr><td><b>Este guia</b></td><td>Explica como estudar e como usar os outros materiais</td><td>Ler inteiro antes da semana 1 e voltar sempre que tiver dúvida</td></tr>
<tr><td><b>Cronograma de 26 semanas</b> (PDF)</td><td>O que estudar em cada semana: tópicos, metas, revisões e simulados</td><td>Todo domingo, para ver a semana seguinte. Vale imprimir e deixar à vista</td></tr>
<tr><td><b>Planilha de estudos</b> (Excel)</td><td>Registro diário, checklist do edital, revisões, caderno de erros, simulados, TAF e painel automático</td><td>Todos os dias, 2 minutos ao fim do estudo. No domingo, ler o painel</td></tr>
<tr><td><b>Checklists</b> (PDF)</td><td>Folhas para marcar: semana, domingo, mês, edital, simulado, edital publicado, prova</td><td>Imprimir a folha semanal (uma por semana) e as outras quando chegar o momento</td></tr>
<tr><td><b>Página online do plano</b></td><td>Versão do plano para consultar no celular</td><td>Quando estiver longe do computador</td></tr>
</table>
<h3>Materiais de estudo (definir com a mentora antes de começar)</h3>
<ul>
<li><b>Teoria:</b> um material completo por disciplina (PDF de curso preparatório para perito legista ou livro). Em Medicina Legal, um livro de referência para consulta, por exemplo <i>Medicina Legal</i> (Genival Veloso de França) ou <i>Medicina Legal: Texto e Atlas</i> (Hygino de C. Hércules).</li>
<li><b>Lei seca:</b> textos oficiais atualizados (planalto.gov.br para leis federais e a CF; site da ALERJ para a Constituição do RJ e os estatutos estaduais).</li>
<li><b>Questões:</b> uma plataforma com filtro por banca (FGV) e por assunto, mais a prova FGV/PCERJ Perito Legista do concurso anterior.</li>
<li><b>Flashcards:</b> Anki (gratuito) ou cartões de papel.</li>
<li><b>Caderno de resumos:</b> um por disciplina, em papel ou digital. O resumo é seu, escrito com as suas palavras.</li>
</ul>

<h2>2. Como fazer cada bloco de 1 hora</h2>
<div class="two"><div class="box"><h3>Bloco de TEORIA</h3>
<ol><li><b>0–10 min · revisão de 24h:</b> sem abrir nada, escreva de memória 5 pontos do conteúdo anterior dessa matéria. Depois confira no resumo.</li>
<li><b>10–45 min · teoria:</b> leia ou assista ao tópico do dia e anote no caderno de resumos só o que é essencial: conceitos, classificações, números, prazos.</li>
<li><b>45–57 min · questões rápidas:</b> 5 a 8 questões do mesmo tópico.</li>
<li><b>57–60 min · registro:</b> uma linha na aba <i>Registro diário</i>.</li></ol></div>
<div class="box"><h3>Bloco de QUESTÕES</h3>
<ol><li><b>0–10 min · revisão de 24h</b> (igual ao bloco de teoria).</li>
<li><b>10–50 min · questões:</b> do tópico da semana, filtradas por FGV. Corrija cada uma logo depois de responder.</li>
<li><b>50–57 min · erros:</b> leia o comentário de cada erro e de cada chute. Registre os importantes no <i>Caderno de erros</i> e crie flashcards.</li>
<li><b>57–60 min · registro</b> na planilha (questões e acertos).</li></ol></div></div>
<p><b>Flashcards:</b> mais 10 a 15 minutos por dia, fora do horário dos blocos (pausas, fila, tarde). São essenciais para os números de Medicina Legal (tempos dos fenômenos cadavéricos, critérios de lesão) e para prazos e penas das leis.</p>

<h2>3. O ritual de domingo (bloco 2, das 08h às 09h)</h2>
<ol>
<li><b>Revisão de 7 dias (30 min):</b> releia os resumos da semana e refaça as questões que errou.</li>
<li><b>Revisão de 30 dias (15 min):</b> revise o conteúdo indicado na coluna "Revisão 30 dias" do cronograma.</li>
<li><b>Painel (10 min):</b> abra a aba <i>Painel semanal</i>, leia a coluna ALERTA e veja as revisões PENDENTES na aba <i>Edital</i>.</li>
<li><b>Planejar (5 min):</b> veja no cronograma os tópicos da próxima semana e marque o status desta semana.</li>
</ol>
<p class="muted">Use a folha "Checklist do domingo" nos primeiros meses, até virar hábito.</p>

<h2>4. Sistema de revisão</h2>
<table><tr><th>Revisão</th><th>Quando</th><th>Como</th></tr>
<tr><td>24 horas</td><td>Início do próximo bloco da mesma matéria</td><td>Escrever de memória e depois conferir (recuperação ativa)</td></tr>
<tr><td>7 dias</td><td>Domingo</td><td>Resumos da semana e questões erradas</td></tr>
<tr><td>30 dias</td><td>Domingo (conteúdo de 4 semanas antes) e semanas de recuperação</td><td>Resumo, flashcards e 5 a 10 questões do tópico</td></tr>
<tr><td>Diária</td><td>Todos os dias, 10–15 min</td><td>Flashcards</td></tr></table>
<p>Na aba <i>Edital</i> da planilha, quando você coloca a data do 1º estudo, as datas das revisões aparecem sozinhas. Quando passar a data sem a revisão marcada como feita, a linha mostra <b>PENDENTE</b>.</p>

<h2>5. Questões e caderno de erros</h2>
<ul>
<li>Faça questões sempre do tópico que acabou de estudar. Comece pela FGV. Se faltarem questões FGV de algum tópico de Medicina Legal, use questões de perícia de outras bancas.</li>
<li>Acertou no chute? Conte como erro no caderno.</li>
<li>No <b>Caderno de erros</b>, escreva a <b>regra correta em 1 linha</b>. É essa linha que você revisa 7 dias depois.</li>
<li>Escolha sempre um motivo para o erro: não sabia, confundi conceitos, interpretação, falta de atenção ou tempo. Se a maioria for "interpretação", o reforço é em Português. Se for "confundi", faça quadros comparativos.</li>
</ul>
<h3>Metas</h3>
<table><tr><th>Período</th><th>Questões/semana</th><th>Meta de acerto</th></tr>
<tr><td>S1–S7</td><td>50 (ML 25 · Port 15 · Dir 10)</td><td>Acima de 50%. No início, errar faz parte</td></tr>
<tr><td>S9–S20</td><td>70 (ML 35 · Port 20 · Dir 15)</td><td>Acima de 55–60%</td></tr>
<tr><td>S21–S25</td><td>120 (ML 60 · Port 35 · Dir 25) + simulados</td><td>Acima de 65–70% no geral e de 60% em cada módulo</td></tr></table>
<p>Na prova, o mínimo é <b>50% em cada módulo</b> (25/50, 15/30, 10/20). Ir mal em um único módulo elimina, mesmo com nota alta nos outros.</p>

<h2>6. Simulados</h2>
<ul>
<li><b>S13:</b> mini-simulado diagnóstico de 40 questões no domingo (ML 20 · Port 12 · Dir 8).</li>
<li><b>S21, S23 e S25:</b> simulado completo de 100 questões no domingo, das 07h às 12h. São as mesmas 5 horas da prova.</li>
<li>Faça em condições de prova: sem celular, sem consulta, folha de respostas preenchida com caneta preta ou azul. No edital de 2021 era proibido levar relógio de qualquer tipo, então treine controlar o tempo por blocos de questões.</li>
<li>Corrija na segunda (bloco 1). Lance as notas na aba <i>Simulados</i> e os erros no caderno.</li>
</ul>

<h2>7. Quando algo der errado</h2>
<ol>
<li><b>Perdeu um dia ou um bloco:</b> no próximo dia, faça o <b>próximo bloco da sequência</b>, não o bloco "do dia".</li>
<li><b>Perdeu 1 bloco na semana:</b> use metade do bloco de revisão de domingo para repor.</li>
<li><b>Perdeu 2 ou mais blocos:</b> não empilhe tudo. Anote o tópico e reponha na semana de recuperação (S8 ou S15).</li>
<li><b>Plantão extra ou exaustão:</b> faça só o bloco 1 (de preferência Medicina Legal) e registre. A meta da semana manda mais que a do dia.</li>
<li><b>Atraso de mais de 2 semanas no cronograma:</b> converse com a mentora para replanejar. Não tente compensar estudando de madrugada.</li>
</ol>

<h2>8. Teste físico (TAF)</h2>
<p>Índices femininos do edital de 2021, com <b>uma única tentativa</b> em cada teste: 15 flexões de braço em 1 min · 20 abdominais em 1 min · 100 m em até 22 s · 1.600 m em até 12 min.</p>
<ul><li>Treine 3 vezes por semana, de 45 a 60 minutos, à tarde, de preferência com educador físico.</li>
<li>Faça os 4 testes nas semanas 4, 8, 12, 16, 20 e 24 e registre na aba <i>TAF</i>.</li></ul>

<h2>9. Quando sair o novo edital</h2>
<p>Avise a mentora no mesmo dia. Ela vai comparar o conteúdo com este plano e recalcular as semanas. Use a folha "Checklist: edital publicado".</p>

<h2>10. Para a mentora: acompanhamento semanal (10 min)</h2>
""" + ck(["Recebi o print do <i>Painel semanal</i> e li a coluna ALERTA",
          "Horas executadas ≥ 80% das planejadas (se não, por 2 semanas seguidas, reduzir a carga)",
          "Acerto por disciplina ≥ 60% (se não, +1 bloco por 2 semanas, tirado da disciplina com melhor acerto)",
          "Revisões pendentes em zero ou só da semana atual",
          "Edital concluído (aba Edital) ≥ edital previsto (coluna do painel)",
          "Perguntei sobre sono, cansaço e plantões. Ajustei se necessário"])
open("01_Guia_da_Aluna.html","w").write(doc("Guia da Aluna", g))

# ================= 02 CRONOGRAMA =================
c = cover("Mentoria · Cronograma", "Cronograma de 26 semanas", SUB)
c += """
<div class="two"><div>
<h3>Diagnóstico</h3>
<ul><li>Disponibilidade: 2h por dia × 5 dias = <b>10h por semana</b> (cerca de 255h em 26 semanas).</li>
<li>Nível atual: zero em Medicina Legal pericial e em Direito. Português com nota 1–2. Ética médica com nota 2.</li>
<li>Primeiro concurso. Plantões às terças e aos sábados.</li>
<li>Prova (edital de 2021): 100 questões FGV. ML 50 · Port 30 · Dir 20. Mínimo de 50% em cada módulo. Os 300 primeiros vão ao TAF, para 25 vagas.</li></ul>
</div><div>
<h3>Distribuição semanal</h3>
<table><tr><th>Disciplina</th><th>Peso</th><th>Horas</th><th>Por quê</th></tr>
<tr><td><span class='tag ml'>Medicina Legal</span></td><td>50%</td><td>4h</td><td>Metade da prova e 1º critério de desempate</td></tr>
<tr><td><span class='tag pt'>Português</span></td><td>30%</td><td>3h</td><td>2º maior peso e gramática fraca</td></tr>
<tr><td><span class='tag dir'>Direito</span></td><td>20%</td><td>2h</td><td>Estudo enxuto: lei seca e questões, garantindo o mínimo de 10/20</td></tr>
<tr><td>Revisão</td><td>–</td><td>1h</td><td>7 e 30 dias, erros e painel</td></tr></table>
</div></div>
<div class="note"><b>Com 2h por dia, o plano é possível, mas apertado.</b> A 1ª leitura do edital termina só na semana 20, e sobram 5 semanas de questões e simulados. Direito vai ser estudado em nível de "noções" (lei seca e questões), sem aprofundar. Para ter mais margem, as alternativas são: (a) estender o horizonte para 9–12 meses, mantendo as 2h; ou (b) subir para 3h em 2 dias da semana (por exemplo, domingo e segunda), o que antecipa o fim da 1ª leitura para cerca da semana 15. Como ainda não há edital publicado, a opção (a) costuma ser a mais realista.</div>
<h2 class='pb'>Grade semanal</h2>
<table><tr><th>Dia</th><th>07:00–08:00</th><th>08:00–09:00</th></tr>
<tr><td>Segunda</td><td><span class='tag ml'>ML</span> Teoria</td><td><span class='tag ml'>ML</span> Questões + resumo</td></tr>
<tr><td class='muted'>Terça</td><td colspan='2' class='muted'>Plantão</td></tr>
<tr><td>Quarta</td><td><span class='tag pt'>Port.</span> Teoria + questões</td><td><span class='tag dir'>Dir.</span> Teoria resumida + lei seca</td></tr>
<tr><td>Quinta</td><td><span class='tag ml'>ML</span> Teoria (continuação)</td><td><span class='tag pt'>Port.</span> Questões FGV</td></tr>
<tr><td>Sexta</td><td><span class='tag ml'>ML</span> Questões + flashcards</td><td><span class='tag dir'>Dir.</span> Questões</td></tr>
<tr><td class='muted'>Sábado</td><td colspan='2' class='muted'>Plantão</td></tr>
<tr><td>Domingo</td><td><span class='tag pt'>Port.</span> Interpretação FGV</td><td>Revisão 7/30 dias + painel</td></tr></table>
<p class='muted'>Fase 2 (S21–S25): os blocos de teoria viram questões dirigidas aos erros. Em S21, S23 e S25, o domingo é um simulado de 100 questões, das 07h às 12h.</p>
<h2>Plano semana a semana</h2>
<table><tr><th style='width:7%'>Semana</th><th style='width:25%'>Medicina Legal (4h)</th><th style='width:19%'>Português (3h)</th><th style='width:24%'>Direito (2h)</th><th style='width:13%'>Questões · revisão · extras</th><th style='width:12%'>Resultado esperado</th></tr>
"""
ph_titles = {1:"Fase 1 · Base: 1ª leitura de todo o edital com questões (S1–S20)", 21:"Fase 2 · Questões e simulados (S21–S25)", 26:"Fase 3 · Reta final"}
for w in plano.WEEKS:
    if w["n"] in ph_titles: c += f"<tr class='ph'><td colspan='6'>{ph_titles[w['n']]}</td></tr>"
    extras = [f"{w['questoes']} q. ({w['q_split']})"]
    if w["rev30"] != "—": extras.append(f"Rev. 30d: {w['rev30']}")
    if w["simulado"]: extras.append(f"<b>{E(w['simulado'])}</b>")
    if w["taf"]: extras.append("Teste físico")
    first = f"<td><b>S{w['n']}</b><br><span class='muted mono' style='font-size:7.5pt'>{w['datas']}</span></td>"
    if w["rec"] or w["n"] == 26:
        c += f"<tr class='{'rec' if w['rec'] else ''}'>{first}<td colspan='3'>{E(w['resumo'])}</td><td>{'<br>'.join(extras)}</td><td>{E(w['esperado'])}</td></tr>"
    else:
        c += f"<tr>{first}<td>{E(w['ml'])}</td><td>{E(w['pt'])}</td><td>{E(w['di'])}</td><td>{'<br>'.join(extras)}</td><td>{E(w['esperado'])}</td></tr>"
c += "</table><p class='muted'>Tópicos: Anexo I do Edital nº 05/2021 (SEPOL/RJ, retificado em 10/05/2022). Os códigos (ML01, PT01, DI01…) são os mesmos da planilha.</p>"
open("02_Cronograma_26_Semanas.html","w").write(doc("Cronograma 26 Semanas", c, landscape=True))

# ================= 03 CHECKLISTS =================
k = cover("Mentoria · Checklists para imprimir", "Checklists", SUB)
k += "<p>Imprima a <b>folha semanal</b> uma vez por semana (26 cópias). Use as outras quando chegar o momento indicado.</p>"
# semanal
days = ["Seg","Qua","Qui","Sex","Dom"]
rows = ["Revisão de 24h no início de cada bloco","Bloco 1 feito","Bloco 2 feito","Flashcards (10–15 min)","Registro na planilha","Treino físico (se for dia de treino)"]
k += "<h2>Folha semanal</h2><p>Semana nº <span class='line' style='min-width:50px'></span> &nbsp; de <span class='line' style='min-width:80px'></span> a <span class='line' style='min-width:80px'></span></p>"
k += "<table><tr><th>Item</th>" + "".join(f"<th style='text-align:center'>{d}</th>" for d in days) + "</tr>"
for r in rows: k += f"<tr><td>{r}</td>" + "".join(f"<td class='c'>{CB}</td>" for _ in days) + "</tr>"
k += "<tr><td>Questões feitas / acertos</td>" + "".join("<td class='c'>___/___</td>" for _ in days) + "</tr></table>"
k += "<div class='two'><div><h3>Tópicos da semana (ver cronograma)</h3><p>ML: <span class='line' style='min-width:85%'></span></p><p>Port.: <span class='line' style='min-width:82%'></span></p><p>Dir.: <span class='line' style='min-width:84%'></span></p></div>"
k += "<div><h3>Fechamento</h3><p>Horas executadas: <span class='line' style='min-width:60px'></span> de 10h</p><p>Questões: <span class='line' style='min-width:60px'></span> (meta: ____)</p><p>Maior dificuldade da semana: <span class='line' style='min-width:45%'></span></p></div></div>"
# domingo
k += "<h2 class='pb'>Checklist do domingo (bloco 2, das 08h às 09h)</h2>" + ck([
 "Reli os resumos da semana (revisão de 7 dias)",
 "Refiz as questões que errei na semana",
 "Revisei os itens do caderno de erros com data de revisão até hoje e marquei Revisado = Sim",
 "Fiz a revisão de 30 dias indicada no cronograma",
 "Fiz as revisões PENDENTES da aba Edital",
 "Marquei 'Teoria concluída' e a data nos tópicos da semana (aba Edital)",
 "Li a coluna ALERTA do Painel semanal",
 "Marquei o status da semana na aba Cronograma",
 "Mandei o print do painel para a mentora",
 "Vi os tópicos da próxima semana e separei o material"])
k += "<h2>Checklist mensal (semanas 4, 8, 12, 16, 20 e 24)</h2>" + ck([
 "Fiz os 4 testes físicos e registrei na aba TAF",
 "Comparei 'Edital concluído' com 'Edital previsto' no painel",
 "Identifiquei os 3 tópicos com menor % de acerto (aba Edital) e combinei com a mentora como reforçar",
 "Vi o resumo de motivos do caderno de erros e qual motivo mais aparece",
 "Avaliei sono, cansaço e escala de plantões. Avisei a mentora se algo mudou",
 "Conferi se saiu notícia ou edital do concurso"])
k += "<h2>Checklist do simulado</h2><div class='two'><div><h3>Antes</h3>" + ck([
 "Domingo das 07h às 12h reservado, sem compromissos",
 "Prova impressa ou plataforma pronta, folha de respostas e caneta",
 "Celular fora do ambiente e sem relógio no pulso",
 "Café da manhã igual ao que vou tomar no dia da prova"]) + "</div><div><h3>Durante e depois</h3>" + ck([
 "Fiz tudo em até 5h, passando as respostas para a folha",
 "Corrigi na segunda (bloco 1)",
 "Lancei as notas na aba Simulados e conferi o mínimo de 50% em cada módulo",
 "Lancei os erros no caderno e anotei os 3 tópicos mais fracos",
 "Revi a estratégia de tempo: em qual módulo perdi mais tempo?"]) + "</div></div>"
k += "<h2 class='pb'>Checklist: edital publicado</h2>" + ck([
 "Avisei a mentora no mesmo dia",
 "Anotei a data da prova, as datas de inscrição e de pagamento da taxa e fiz a inscrição",
 "Conferi a banca, o número de questões por módulo e a nota mínima",
 "A mentora comparou o conteúdo programático novo com o plano (tópicos incluídos ou retirados)",
 "Recebi o cronograma recalculado até a data da prova",
 "Conferi os índices do TAF no novo edital",
 "Separei os documentos exigidos (inscrição, cotas, isenção, títulos)"])
k += "<h2>Checklist da semana da prova</h2>" + ck([
 "Nada de conteúdo novo, só resumos, flashcards e caderno de erros",
 "Mini-simulado de 30 questões até quarta, depois só revisão leve",
 "Conferi o local de prova e o horário de fechamento dos portões. Planejei chegar 1h antes",
 "Fiz o trajeto até o local (ou simulei o tempo de deslocamento)",
 "Separei o documento de identificação original com foto",
 "Separei caneta esferográfica de corpo transparente, tinta azul ou preta (regra do edital de 2021)",
 "Organizei a escala para não ter plantão na véspera da prova",
 "Véspera: descanso, refeição leve e sono cedo"])
k += "<h2>Checklist do dia da prova</h2>" + ck([
 "Documento original com foto e caneta transparente na bolsa",
 "Saí de casa com folga para chegar 1h antes do fechamento dos portões",
 "Água e lanche permitidos",
 "Celular desligado e guardado no envelope fornecido. Sem relógio",
 "Estratégia: começar pelo módulo de maior segurança e garantir 50% em cada módulo",
 "Transcrever as respostas para o cartão com pelo menos 30 min de folga"])
# checklist edital
k += "<h2 class='pb'>Checklist do edital (51 tópicos)</h2><p class='muted'>Marque cada etapa ao concluir. A mesma lista está na aba <i>Edital</i> da planilha, com as datas calculadas.</p>"
k += "<table><tr><th style='width:7%'>Código</th><th style='width:6%'>Sem.</th><th>Tópico</th><th class='c'>Teoria</th><th class='c'>Questões</th><th class='c'>Rev 24h</th><th class='c'>Rev 7d</th><th class='c'>Rev 30d</th></tr>"
last = None
for disc, code, wk, t in plano.TOPICS:
    if disc != last:
        k += f"<tr class='ph'><td colspan='8'>{disc}</td></tr>"; last = disc
    k += f"<tr><td class='mono'>{code}</td><td class='c'>S{wk}</td><td style='font-size:8.5pt'>{E(t)}</td>" + "".join(f"<td class='c'>{CB}</td>" for _ in range(5)) + "</tr>"
k += "</table>"
open("03_Checklists.html","w").write(doc("Checklists", k))
print("ok")
