# Guia único: junta guia + cronograma + checklists num PDF só (os outros materiais ficam na planilha).
import re, plano
ns = {}; exec(open("pdf_build.py").read(), ns)
g, c, k, doc, cover, ck, SUB = ns["g"], ns["c"], ns["k"], ns["doc"], ns["cover"], ns["ck"], ns["SUB"]

def parts(s): 
    p = re.split(r"(?=<h2)", s); return p[0], p[1:]
def body(h2part): return re.sub(r"^<h2[^>]*>.*?</h2>", "", h2part, count=1, flags=re.S)
def title(h2part): return re.sub(r"^\d+\.\s*", "", re.search(r"<h2[^>]*>(.*?)</h2>", h2part, re.S).group(1))

g0, gs = parts(g); c0, cs = parts(c); k0, ks = parts(k)
facts = g0[g0.index("<div class=\"facts\">"):]
diag = c0[c0.index("<div class=\"two\">"):]
G = {title(x): body(x) for x in gs}; C = {title(x): body(x) for x in cs}; K = {title(x): body(x) for x in ks}

mats = """<table><tr><th>Material</th><th>Para quê</th><th>Quando usar</th></tr>
<tr><td><b>Este guia</b> (PDF)</td><td>Tudo o que você precisa SABER: o plano, como estudar, o cronograma das 26 semanas e os checklists</td><td>Ler inteiro antes da semana 1. Todo domingo, consultar o cronograma (parte 3) e o checklist do domingo (parte 4)</td></tr>
<tr><td><b>Planilha de estudos</b> (Excel)</td><td>Tudo o que você precisa PREENCHER: registro diário, checklist semanal, checklist do edital com revisões automáticas, caderno de erros, simulados, TAF e painel com alertas</td><td>Todos os dias, 3 minutos ao fim do estudo. No domingo, ler o painel e mandar um print para a mentora</td></tr></table>
<p class="muted">Só células amarelas são preenchidas. O resto a planilha calcula sozinha.</p>"""
estudo = G["Seus materiais e quando usar cada um"].split("<h3>Materiais de estudo", 1)[1]
estudo = "<h3>Materiais de estudo" + estudo

def fix(s):
    return (s.replace("uma linha na aba <i>Registro diário</i>.", "uma linha na aba <i>Registro diário</i> e ✓ no bloco na aba <i>Checklist semanal</i>.")
             .replace('Use a folha "Checklist do domingo" nos primeiros meses, até virar hábito.', "Use o checklist do domingo (parte 4) nos primeiros meses, até virar hábito.")
             .replace('Use a folha "Checklist: edital publicado".', 'Use o checklist "Edital publicado" (parte 4).'))

H = cover("Mentoria · Guia da aluna", "Guia do seu plano de estudos", SUB) + facts
H += """<div class="box"><b>Como este guia está organizado</b><ol style="margin:4px 0 0">
<li>Seus materiais</li><li>Seu plano: diagnóstico e grade semanal</li><li>Como estudar: blocos, domingo, revisões, questões, simulados e imprevistos</li><li>Cronograma das 26 semanas</li><li>Checklists</li><li>TAF, edital novo e acompanhamento da mentora</li></ol></div>"""
H += "<h2>1. Seus materiais</h2>" + mats + estudo
H += "<h2 class='pb'>2. Seu plano</h2>" + diag + "<h3>Grade semanal</h3>" + C["Grade semanal"]
H += "<h2 class='pb'>3. Como estudar</h2>"
for i, t in enumerate(["Como fazer cada bloco de 1 hora", "O ritual de domingo (bloco 2, das 08h às 09h)", "Sistema de revisão", "Questões e caderno de erros", "Simulados", "Quando algo der errado"], 1):
    H += f"<h3 style='font-size:13pt;margin-top:16px'>3.{i} {t}</h3>" + fix(G[t])
cr = re.sub(r"<table>(<tr><th.*?</tr>)", r"<table><thead>\1</thead>", C["Plano semana a semana"], count=1, flags=re.S)
H += "<h2 class='pb'>4. Cronograma das 26 semanas</h2><div class='crono'>" + cr + "</div>"
H += "<h2 class='pb'>5. Checklists</h2><p>O checklist do dia a dia (blocos, flashcards, ritual de domingo) e o checklist dos 51 tópicos do edital ficam na planilha, nas abas <i>Checklist semanal</i> e <i>Edital</i>. Os checklists abaixo são para momentos específicos.</p>"
for t in ["Checklist do domingo (bloco 2, das 08h às 09h)", "Checklist mensal (semanas 4, 8, 12, 16, 20 e 24)", "Checklist do simulado", "Checklist: edital publicado", "Checklist da semana da prova", "Checklist do dia da prova"]:
    H += f"<h3 style='font-size:13pt;margin-top:14px'>{t}</h3>" + K[t].replace("Mandei o print do painel para a mentora", "Marquei o ritual de domingo na aba Checklist semanal e mandei o print do painel para a mentora")
H += "<h2 class='pb'>6. TAF, edital novo e acompanhamento</h2>"
H += "<h3 style='font-size:13pt'>Teste físico (TAF)</h3>" + G["Teste físico (TAF)"]
H += "<h3 style='font-size:13pt'>Quando sair o novo edital</h3>" + fix(G["Quando sair o novo edital"])
H += "<h3 style='font-size:13pt'>Para a mentora: acompanhamento semanal (10 min)</h3>" + G["Para a mentora: acompanhamento semanal (10 min)"]
H = H.replace("</style>", "")  # no-op safety
html_doc = doc("Guia da Aluna", H).replace("</style>", ".crono table{font-size:7.8pt}.crono td{padding:4px 5px}</style>", 1)
open("Guia_da_Aluna.html", "w").write(html_doc)
print("ok", len(H))
