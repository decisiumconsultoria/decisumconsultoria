# Guia simplificado (sem TAF): plano em 1 página, dia em 3 passos, cronograma curto, checklists e roteiro da mentora.
import html, plano
E = html.escape
ns = {}; exec(open("pdf_build.py").read().split("# ================= 01 GUIA")[0], ns)
CSS, doc, CB, ck = ns["CSS"], ns["doc"], ns["CB"], ns["ck"]
CSS2 = """
.hero{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px solid var(--acc);padding-bottom:10px;margin-bottom:12px}
.big{font-family:'Archivo',sans-serif;font-stretch:85%;font-size:30pt;font-weight:800;color:var(--acc);line-height:1}
.week{display:grid;grid-template-columns:repeat(7,1fr);gap:5px;margin:8px 0 12px}
.d{border:1px solid var(--line);border-radius:6px;padding:6px;font-size:8.5pt;min-height:78px}
.d b{display:block;font-family:'Archivo',sans-serif;font-stretch:85%;font-size:10pt;margin-bottom:4px}
.d.off{background:#f3f4f4;color:#8a9592;border-style:dashed}
.b{display:block;border-radius:4px;padding:2px 5px;margin-bottom:3px;font-weight:600;color:#fff}
.b.ml{background:#1d6b62}.b.pt{background:#3f4fa0}.b.dir{background:#8a3348}.b.rv{background:#6b6f2a}
.phases{display:grid;grid-template-columns:20fr 5fr 1.4fr;gap:4px;margin:6px 0 4px}
.phases div{background:var(--soft);border-radius:4px;padding:6px 8px;font-size:8.5pt}
.phases div:nth-child(2){background:#e6e9f7}.phases div:nth-child(3){background:var(--wsoft)}
.rules{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:8px 0}
.rule{border:1.5px solid var(--acc);border-radius:8px;padding:8px 10px;font-size:9.5pt}
.rule .n{font-family:'Archivo',sans-serif;font-size:18pt;font-weight:800;color:var(--acc);line-height:1}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:8px 0}
.step{border-radius:8px;padding:10px;background:#f5f8f7;border:1px solid var(--line);font-size:9.5pt}
.step h4{margin:0 0 4px;font-family:'Archivo',sans-serif;font-stretch:85%;font-size:12pt;color:var(--acc)}
.mock{font-size:8pt;margin-top:6px} .mock td,.mock th{padding:3px 5px}
.y{background:#fff4c2;text-align:center} .today td{background:#d6e9ff}
.crono table{font-size:8.3pt} .crono td{padding:4px 5px}
.script li{margin-bottom:6px}
"""
CSS += CSS2
SUB = "Patrícia de Miranda Oliveira · Perito Legista PCERJ · 2h por dia · 02/11/2026 a 02/05/2027"

def day(nm, b1, b2):
    return f"<div class='d'><b>{nm}</b><span class='b {b1[0]}'>{b1[1]}</span><span class='b {b2[0]}'>{b2[1]}</span></div>"
off = lambda nm: f"<div class='d off'><b>{nm}</b>Plantão</div>"

h = f"""<div class='hero'><div><div class='eyebrow'>Mentoria · Guia da aluna</div><h1>Seu plano de estudos</h1><p class='muted' style='margin:2px 0 0'>{SUB}</p></div></div>
<h2 style='border:0;margin-top:0'>Seu plano em uma página</h2>
<div class="facts">
 <div class="fact"><div class="v mono">2h</div><div class="l">por dia, das 07h às 09h</div></div>
 <div class="fact"><div class="v mono">5 dias</div><div class="l">por semana. Terça e sábado são de plantão</div></div>
 <div class="fact"><div class="v mono">26</div><div class="l">semanas, de 02/11/2026 a 02/05/2027</div></div>
 <div class="fact"><div class="v mono">50%</div><div class="l">é o mínimo em CADA matéria da prova</div></div>
</div>
<h3>Sua semana</h3>
<div class='week'>
{day("Segunda",("ml","Med. Legal"),("ml","Med. Legal"))}{off("Terça")}
{day("Quarta",("pt","Português"),("dir","Direito"))}
{day("Quinta",("ml","Med. Legal"),("pt","Português"))}
{day("Sexta",("ml","Med. Legal"),("dir","Direito"))}{off("Sábado")}
{day("Domingo",("pt","Português"),("rv","Revisão"))}
</div>
<p class='muted' style='font-size:9pt'>Bloco de cima: 07h–08h. Bloco de baixo: 08h–09h. Por semana: Medicina Legal 4h (metade da prova) · Português 3h · Direito 2h · Revisão 1h.</p>
<h3>Os 6 meses</h3>
<div class='phases'><div><b>Semanas 1 a 20 · Aprender</b><br>Teoria de todo o edital, com questões depois de cada tópico</div><div><b>21 a 25 · Treinar</b><br>Questões e 3 simulados</div><div><b>26</b><br>Descanso</div></div>
<p class='muted' style='font-size:9pt'>As semanas 8 (Natal) e 15 (Carnaval) são leves: servem só para revisar e pôr atrasos em dia.</p>
<h3>As 3 regras de ouro</h3>
<div class='rules'>
<div class='rule'><div class='n'>1</div><b>Faça os blocos, não maratonas.</b> Duas horas todo dia valem mais que 8 horas num domingo.</div>
<div class='rule'><div class='n'>2</div><b>Sempre questões depois da teoria.</b> É fazendo questões que se aprende o que a prova cobra.</div>
<div class='rule'><div class='n'>3</div><b>Registre em 2 minutos.</b> Sem registro, não dá para saber se o plano está funcionando.</div>
</div>

<h2 class='pb'>Seus 2 materiais</h2>
<table><tr><th style='width:22%'>Material</th><th>Para quê</th></tr>
<tr><td><b>Este guia</b></td><td>Para <b>ler</b>: como estudar, o conteúdo de cada semana e os checklists. Leia inteiro uma vez e volte quando tiver dúvida.</td></tr>
<tr><td><b>A planilha</b></td><td>Para <b>preencher</b>, 2 minutos por dia. Você só mexe nas células amarelas. O resto ela faz sozinha.</td></tr></table>
<p><b>Antes de começar</b>, combine com a mentora: (1) o material de teoria de cada matéria; (2) o site de questões (com filtro por banca FGV); (3) onde fazer flashcards (o Anki é gratuito). A lei seca vem dos sites oficiais (planalto.gov.br e alerj.rj.gov.br).</p>

<h2>Seu dia em 3 passos</h2>
<div class='steps'>
<div class='step'><h4>1 · Abra o Diário</h4>Na aba <b>Diário</b>, a linha de hoje fica <b>azul</b>. Ela já diz o que estudar em cada bloco.</div>
<div class='step'><h4>2 · Estude os 2 blocos</h4>Cada bloco tem 1 hora. Veja abaixo como fazer um bloco de teoria e um de questões.</div>
<div class='step'><h4>3 · Marque e anote</h4>Marque <b>✓</b> em cada bloco feito e escreva quantas questões fez e quantas acertou.</div>
</div>
<p style='margin-bottom:2px'><b>Como fica a linha do Diário depois de preenchida</b> (em amarelo, o que você escreve):</p>
<table class='mock'><tr><th>Data</th><th>Dia</th><th>Bloco 1 · 07h–08h</th><th>Feito?</th><th>Questões</th><th>Acertos</th><th>Bloco 2 · 08h–09h</th><th>Feito?</th><th>Questões</th><th>Acertos</th></tr>
<tr class='today'><td>02/11/26</td><td>Segunda</td><td>Medicina Legal · Teoria: Introdução, perícias e documentos</td><td class='y'>✓</td><td class='y'>6</td><td class='y'>4</td><td>Medicina Legal · Questões: Introdução, perícias e documentos</td><td class='y'>✓</td><td class='y'>15</td><td class='y'>10</td></tr></table>

<h2>Como fazer cada bloco de 1 hora</h2>
<div class='two'><div class='box'><h3 style='margin-top:0'>Bloco de TEORIA</h3><ol>
<li><b>10 min:</b> sem olhar nada, escreva 5 coisas que lembra da última aula dessa matéria. Depois confira.</li>
<li><b>35 min:</b> estude o tópico do dia e faça um resumo curto, com as suas palavras.</li>
<li><b>12 min:</b> faça de 5 a 8 questões do tópico.</li>
<li><b>3 min:</b> marque na planilha.</li></ol>
<p class='muted' style='margin:0'>Terminou a teoria do tópico? Escreva a data na aba <b>Edital</b>.</p></div>
<div class='box'><h3 style='margin-top:0'>Bloco de QUESTÕES</h3><ol>
<li><b>10 min:</b> o mesmo exercício de memória.</li>
<li><b>40 min:</b> questões do tópico (comece pela banca FGV). Corrija uma por uma.</li>
<li><b>7 min:</b> leia a explicação de cada erro. Os erros importantes vão para a aba <b>Erros</b>.</li>
<li><b>3 min:</b> marque na planilha.</li></ol>
<p class='muted' style='margin:0'>Acertou no chute? Conte como erro.</p></div></div>
<p><b>Flashcards:</b> mais 10 minutos por dia, quando der (fila, pausa, à tarde). Servem para decorar números de Medicina Legal e prazos das leis.</p>

<h2 class='pb'>Domingo: 4 passos (no bloco de revisão)</h2>
<ol>
<li><b>Revise a semana (25 min):</b> releia os resumos da semana e refaça as questões que errou.</li>
<li><b>Faça o que está amarelo (20 min):</b> nas abas <b>Edital</b> e <b>Erros</b>, faça as revisões marcadas com 🟡 e depois marque ✓.</li>
<li><b>Olhe o Painel (5 min):</b> veja a cor da semana e mande um print para a mentora.</li>
<li><b>Veja a próxima semana (5 min):</b> confira os tópicos e separe o material.</li>
</ol>
<table><tr><th>Cor no Painel</th><th>O que significa</th><th>O que fazer</th></tr>
<tr><td>🟢 No ritmo</td><td>Fez pelo menos 80% dos blocos e acertou 60% ou mais em todas as matérias</td><td>Continue</td></tr>
<tr><td>🟡 Atenção</td><td>Fez poucos blocos ou alguma matéria ficou abaixo de 60%</td><td>A matéria fraca ganha 1 bloco extra por 2 semanas (combine com a mentora)</td></tr>
<tr><td>🔴 Alerta</td><td>Fez menos da metade dos blocos ou não registrou a semana</td><td>Fale com a mentora para ajustar o plano</td></tr></table>

<h2>Revisões: a planilha avisa</h2>
<table><tr><th>Quando</th><th>Como</th></tr>
<tr><td>No dia seguinte</td><td>Nos 10 minutos de memória do início de cada bloco</td></tr>
<tr><td>7 dias depois</td><td>A aba <b>Edital</b> mostra 🟡 <i>Fazer revisão de 7 dias</i>. Releia o resumo e faça 5 questões</td></tr>
<tr><td>30 dias depois</td><td>A aba <b>Edital</b> mostra 🟡 <i>Fazer revisão de 30 dias</i>. Mesma coisa</td></tr>
<tr><td>Erros</td><td>A aba <b>Erros</b> mostra 🟡 <i>Revisar</i> 7 dias depois. Releia a regra certa</td></tr></table>

<h2>Se algo der errado</h2>
<table><tr><th style='width:35%'>Aconteceu</th><th>Faça</th></tr>
<tr><td>Perdi um dia</td><td>No próximo dia, continue de onde parou. Não pule o conteúdo perdido</td></tr>
<tr><td>Perdi 1 bloco na semana</td><td>Use metade do bloco de revisão de domingo para repor</td></tr>
<tr><td>Perdi vários blocos</td><td>Anote o que ficou e reponha na semana leve (8 ou 15)</td></tr>
<tr><td>Plantão pesado, estou exausta</td><td>Faça só o bloco 1. Melhor 1 hora do que nada</td></tr>
<tr><td>Atrasei mais de 2 semanas</td><td>Fale com a mentora para replanejar. Não estude de madrugada para compensar</td></tr></table>

<h2>Metas de questões</h2>
<table><tr><th>Semanas</th><th>Questões por semana</th><th>Meta de acerto</th></tr>
<tr><td>1 a 7</td><td>50</td><td>Acima de 50% (no começo é normal errar)</td></tr>
<tr><td>9 a 20</td><td>70</td><td>Acima de 60%</td></tr>
<tr><td>21 a 25</td><td>120 + simulados</td><td>Acima de 70% no geral e de 60% em cada matéria</td></tr></table>
<p><b>Simulados:</b> mini-simulado na semana 13 e simulados completos nos domingos das semanas 21, 23 e 25, das 07h às 12h. Como na prova: sem celular, consulta ou relógio. Lance na aba <b>Simulados</b>.</p>
"""
# cronograma
h += "<h2 class='pb'>O que estudar em cada semana</h2><p class='muted'>É o mesmo conteúdo da aba <b>O que estudar</b> da planilha. O Diário já mostra o que fazer em cada dia.</p><div class='crono'><table><thead><tr><th style='width:8%'>Semana</th><th style='width:27%'>Medicina Legal</th><th style='width:22%'>Português</th><th style='width:27%'>Direito</th><th style='width:16%'>Destaque</th></tr></thead>"
for w in plano.WEEKS:
    ml, pt, di = plano.week_short(w["n"])
    dest = w["simulado"] or ("Semana leve: " + plano.RECOVERY[w["n"]] if w["rec"] else ("Semana da prova" if w["n"] == 26 else ""))
    first = f"<td><b>S{w['n']}</b><br><span class='muted mono' style='font-size:7pt'>{w['datas']}</span></td>"
    if w["rec"] or w["n"] == 26:
        h += f"<tr class='rec'>{first}<td colspan='3'>{E(w['resumo'])}</td><td>{E(dest)}</td></tr>"
    else:
        h += f"<tr>{first}<td>{E(ml)}</td><td>{E(pt)}</td><td>{E(di)}</td><td>{E(dest)}</td></tr>"
h += "</table></div>"
# checklists
h += "<h2 class='pb'>Checklists</h2><p class='muted'>O checklist do dia a dia é a própria planilha. Estes são para momentos especiais.</p><div class='two'><div>"
h += "<h3>Dia de simulado</h3>" + ck(["Domingo das 07h às 12h livre","Prova pronta, folha de respostas e caneta","Celular longe, sem relógio","Fiz em até 5 horas","Na segunda: corrigi e lancei na aba Simulados","Coloquei os erros importantes na aba Erros"])
h += "<h3>Saiu o edital novo</h3>" + ck(["Avisei a mentora no mesmo dia","Anotei a data da prova e os prazos de inscrição e de pagamento","Fiz a inscrição","Recebi da mentora o plano ajustado ao novo edital"])
h += "</div><div>"
h += "<h3>Semana da prova</h3>" + ck(["Nada de conteúdo novo: só resumos, flashcards e erros","Conferi o local e o horário de fechamento dos portões","Fiz ou planejei o trajeto (chegar 1h antes)","Separei o documento original com foto","Separei caneta de corpo transparente, tinta azul ou preta","Sem plantão na véspera","Véspera: descanso e dormir cedo"])
h += "<h3>Dia da prova</h3>" + ck(["Documento e caneta na bolsa","Água e lanche","Celular desligado, sem relógio","Garantir 50% em cada matéria","Passar as respostas para o cartão com 30 min de folga"])
h += "</div></div>"
# mentora
h += """<h2 class='pb'>Para a mentora: como apresentar o material (15 min)</h2>
<ol class='script'>
<li><b>Plano em uma página (3 min).</b> Mostre a página 1 do guia: 2h por dia, a semana colorida, os 3 períodos (aprender, treinar, descansar) e as 3 regras de ouro. A mensagem: <i>"é pouco por dia, mas é todo dia"</i>.</li>
<li><b>A planilha: só o amarelo (2 min).</b> Abra a aba <b>Comece aqui</b> e mostre a regra única: ela só preenche as células amarelas.</li>
<li><b>Preencher o primeiro dia juntas (5 min).</b> Na aba <b>Diário</b>, use a linha de 02/11 como teste: marque ✓, escreva 15 questões e 10 acertos, e depois apague. Mostre que o <b>Painel</b> mudou sozinho.</li>
<li><b>Edital e Erros (3 min).</b> Escreva uma data de teste na aba <b>Edital</b> e mostre que as datas de revisão aparecem sozinhas e que o 🟡 avisa quando revisar.</li>
<li><b>O combinado (2 min).</b> Todo domingo ela manda um print do Painel. Se aparecer 🔴, vocês conversam.</li>
</ol>
<h3>Seu acompanhamento semanal (5 min, com o print do Painel)</h3>""" + ck([
 "Cor da semana: 🟢 segue; 🟡 matéria fraca ganha 1 bloco por 2 semanas; 🔴 conversar e ajustar",
 "Blocos feitos: abaixo de 80% por 2 semanas seguidas significa que o plano está pesado demais para a rotina dela",
 "Revisões para fazer: devem estar perto de zero",
 "Edital estudado: comparar com a semana atual (ver a aba O que estudar)",
 "Perguntar sobre sono, cansaço e plantões"]) + """
<div class='note'><b>Lembrete:</b> com 2h por dia, o plano é possível, mas apertado (a teoria só termina na semana 20). Se o edital demorar, estenda o prazo em vez de aumentar a carga diária. Quando o edital sair, compare o conteúdo programático com a aba <b>Edital</b> e ajuste.</div>
<p class='muted' style='font-size:8.5pt'>Conteúdo baseado no Anexo I do Edital nº 05/2021 da SEPOL/RJ (retificado em 10/05/2022), banca FGV.</p>"""
open("Guia_da_Aluna.html","w").write(doc("Guia da Aluna", h).replace("</style>", CSS2 + "</style>", 1))
print("ok")
