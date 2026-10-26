# Dados únicos do plano (2h/dia) — alimentam planilha, PDFs e página.
import datetime as dt
START = dt.date(2026, 11, 2)
def wk_dates(n):
    a = START + dt.timedelta(days=7*(n-1)); b = a + dt.timedelta(days=6)
    return a, b
def fmt(n):
    a, b = wk_dates(n); return f"{a:%d/%m}–{b:%d/%m/%y}"

ALUNA = "Patrícia de Miranda Oliveira"

# Tópicos do edital (unidades de estudo) — código, semana, descrição (texto do Anexo I)
ML = [
 ("ML01",1,"Normas éticas x jurídicas; processo e provas; fatos duradouros e perícias; conceitos, história e divisões da Medicina Legal; perícias médicas e documentos médico-legais"),
 ("ML02",2,"Identidade e identificação; métodos de identificação nos vivos e em cadáveres"),
 ("ML03",3,"Antropologia Forense: sexo, idade, estatura e ancestralidade"),
 ("ML04",4,"Traumatologia I: conceitos de trauma e lesão; consequências jurídicas dos traumas; agentes mecânicos (contundentes, cortantes, perfurantes e mistos)"),
 ("ML05",5,"Traumatologia II: armas de fogo (agentes perfurocontundentes)"),
 ("ML06",6,"Traumatologia III: agentes físicos, químicos e outros vulnerantes; idade da lesão e reação vital"),
 ("ML07",7,"Asfixiologia I: conceito e classificação etiológica; sufocação direta e indireta; enforcamento, estrangulamento e esganadura"),
 ("ML08",9,"Asfixiologia II: confinamento, soterramento e afogamento"),
 ("ML09",10,"Tanatologia I: diagnóstico da morte e consequências jurídicas; conceito moderno de morte e doação de órgãos; causa jurídica da morte (natural, violenta, suspeita, súbita)"),
 ("ML10",11,"Tanatologia II: cronotanatognose; fenômenos cadavéricos e estimativa do tempo de morte"),
 ("ML11",12,"Tanatologia III: declaração de óbito; necessidade da necrópsia médico-legal. Infortunística: acidentes do trabalho e doenças profissionais"),
 ("ML12",13,"Toxicologia I: cáusticos e venenos; intoxicações exógenas (acidentais, suicidas, criminosas); necrópsia na suspeita de intoxicação; coleta de material toxicológico"),
 ("ML13",14,"Toxicologia II: estudo médico-legal do abuso de álcool e de outras drogas"),
 ("ML14",16,"Sexologia I: crimes contra a liberdade sexual; conjunção carnal e atos libidinosos; manchas de sêmen; formas de violência nos atos libidinosos"),
 ("ML15",17,"Sexologia II: gravidez, parto recente e puerpério; aborto; infanticídio"),
 ("ML16",18,"Sexologia III: maus-tratos a vulneráveis; contágio venéreo; casamento; filiação por exame de DNA"),
 ("ML17",19,"Psiquiatria Forense: imputabilidade penal e capacidade civil"),
 ("ML18",20,"Diceologia e Deontologia médicas"),
]
PT = [
 ("PT01",1,"Texto: gêneros (literário e não literário), tipologia (narrativo, descritivo, argumentativo), interpretação e organização interna"),
 ("PT02",2,"Ortografia e acentuação gráfica"),
 ("PT03",3,"Morfologia I: substantivo, adjetivo, artigo, numeral e pronome"),
 ("PT04",4,"Morfologia II: verbo — flexão e emprego de tempos e modos"),
 ("PT05",5,"Advérbio, preposição e conjunção; processos de formação de palavras"),
 ("PT06",6,"Semântica: sentido e emprego dos vocábulos; campos semânticos"),
 ("PT07",7,"Sintaxe I: frase, oração e período; termos da oração"),
 ("PT08",9,"Sintaxe II: processos de coordenação e subordinação"),
 ("PT09",10,"Concordância nominal e verbal"),
 ("PT10",11,"Transitividade e regência de nomes e verbos"),
 ("PT11",12,"Emprego do sinal indicativo de crase"),
 ("PT12",13,"Padrões gerais de colocação pronominal"),
 ("PT13",14,"Pontuação"),
 ("PT14",16,"Mecanismos de coesão textual"),
 ("PT15",17,"Reescrita de frases I: substituição e deslocamento"),
 ("PT16",18,"Reescrita de frases II: paralelismo; variação linguística e norma culta"),
]
DI = [
 ("DI01",1,"Constitucional: supremacia da Constituição; direitos e deveres individuais e coletivos (art. 5º, parte 1)"),
 ("DI02",2,"Constitucional: art. 5º, parte 2 (incl. remédios constitucionais)"),
 ("DI03",3,"Constitucional: Administração Pública e servidores públicos civis (arts. 37–41)"),
 ("DI04",4,"Constitucional: Poder Executivo (forma e sistema de governo, chefias); Segurança Pública na CF e na Constituição do RJ; Ordem social"),
 ("DI05",5,"Penal: fato típico; dolo e culpa; consumação e tentativa; crime impossível"),
 ("DI06",6,"Penal: inimputabilidade penal; medidas de segurança; crimes contra a pessoa (parte 1)"),
 ("DI07",7,"Penal: crimes contra a pessoa (parte 2); crimes contra a liberdade individual"),
 ("DI08",9,"Penal: crimes contra a dignidade sexual; crimes contra a administração pública"),
 ("DI09",10,"Proc. Penal: garantias constitucionais; inquérito policial; polícia judiciária; diligências; auto de resistência; algemas (Lei 13.434/2017 e LEP)"),
 ("DI10",11,"Proc. Penal: prova pericial; corpo de delito; cadeia de custódia (Lei 13.964/2019); identificação criminal e perfil genético (Leis 12.037/2009 e 12.654/2012)"),
 ("DI11",12,"Leis especiais: Tortura (9.455/1997); Abuso de autoridade (13.869/2019); Racismo (7.716/1989)"),
 ("DI12",13,"Leis especiais: Drogas (11.343/2006); ECA (8.069/1990)"),
 ("DI13",14,"Leis especiais: Maria da Penha (11.340/2006) e Sinal Vermelho (13.505/2017, 13.894/2019, 14.188/2021); atendimento policial e pericial especializado; Estatuto do Idoso (10.741/2003); Estatuto da PcD (13.146/2015)"),
 ("DI14",16,"Administrativo: conceito de Administração Pública; organização administrativa; ato administrativo"),
 ("DI15",17,"Administrativo: poderes (hierárquico, regulamentar, disciplinar, de polícia); limites do poder de polícia; uso e abuso de poder; agentes públicos; cargo, emprego e função; responsabilidade civil do Estado"),
 ("DI16",18,"Estatuto dos Funcionários Públicos Civis do RJ (DL 220/1975) e Regulamento (Dec. 2.479/1979)"),
 ("DI17",19,"Estatuto dos Policiais Civis do RJ (DL 218/1975) e Regulamento (Dec. 3.044/1979)"),
]
TOPICS = [("Medicina Legal",)+t for t in ML] + [("Português",)+t for t in PT] + [("Direito",)+t for t in DI]

RECOVERY = {8: "Natal", 15: "Carnaval"}
SIMULADO = {13: "Mini-simulado diagnóstico (40 q.) no domingo", 21: "Simulado 1 (100 q.) — domingo 07h–12h",
            23: "Simulado 2 (100 q.) — domingo 07h–12h", 25: "Simulado 3 (100 q.) — domingo 07h–12h"}
TAF_WEEKS = set()  # TAF retirado do plano

def short(code):
    for d,c,w,t in TOPICS:
        if c == code: return t
def by_week(lst, w):
    return [t for t in lst if t[1] == w]

PHASE2 = {
 21: ("Questões: Traumatologia e Asfixiologia (ML04–ML08)", "Questões: interpretação + concordância e regência", "Questões: Constitucional + Penal (DI01–DI08)"),
 22: ("Questões: Tanatologia, Infortunística e Toxicologia (ML09–ML13)", "Questões: sintaxe, pontuação e crase", "Questões: Processo Penal + leis especiais (DI09–DI13)"),
 23: ("Questões: Sexologia, DNA e Psiquiatria (ML14–ML17)", "Questões: coesão e reescrita", "Questões: Administrativo + estatutos RJ (DI14–DI17)"),
 24: ("Questões: Identificação, Antropologia, perícias e Deontologia (ML01–ML03, ML18) + tópicos com mais erros", "Questões mistas FGV", "Questões mistas + lei seca dos tópicos com mais erros"),
 25: ("Revisão final por resumos e flashcards (todo o conteúdo)", "Caderno de erros de Português", "Lei seca: trechos grifados"),
}

def week(n):
    """Retorna dict com o plano da semana n."""
    a,b = wk_dates(n)
    d = dict(n=n, datas=fmt(n), ini=a, fim=b)
    if n <= 20: d["fase"] = "1 · Base"
    elif n <= 25: d["fase"] = "2 · Questões e simulados"
    else: d["fase"] = "3 · Reta final"
    if n in RECOVERY:
        d.update(ml="—", pt="—", di="—", rec=True,
                 resumo=f"Semana de recuperação ({RECOVERY[n]}): carga reduzida (≈5h). Sem conteúdo novo: pôr atrasos em dia, revisão de 30 dias de {'S1–S7' if n==8 else 'S9–S14'}, flashcards e caderno de erros.")
    elif n == 26:
        d.update(ml="Revisões leves", pt="Revisões leves", di="Revisões leves", rec=False,
                 resumo="Semana pré-prova: nada de conteúdo novo; mini-simulado de 30 q. até quarta; logística da prova; descanso na véspera.")
    elif n in PHASE2:
        d.update(ml=PHASE2[n][0], pt=PHASE2[n][1], di=PHASE2[n][2], rec=False, resumo="")
    else:
        def f(lst, extra):
            x = by_week(lst, n)
            return (x[0][0] + " · " + x[0][2]) if x else extra
        d.update(ml=f(ML, ""), pt=f(PT, {19:"Bateria de interpretação de textos FGV", 20:"Revisão de gramática pelo caderno de erros"}.get(n,"")),
                 di=f(DI, {20:"Questões mistas de Direito (todas as áreas)"}.get(n,"")), rec=False, resumo="")
    # metas
    if n in RECOVERY: q = 30
    elif n == 26: q = 40
    elif n <= 7: q = 50
    elif n <= 20: q = 70
    else: q = 120
    d["questoes"] = q
    d["q_split"] = {50:"ML 25 · Port 15 · Dir 10", 70:"ML 35 · Port 20 · Dir 15", 120:"ML 60 · Port 35 · Dir 25", 30:"livre (revisão)", 40:"mini-simulado 30 + revisão"}[q]
    # horas planejadas
    d["horas"] = 5 if n in RECOVERY else (6 if n == 26 else (13 if n in (21,23,25) else 10))
    # revisão 30 dias
    rev30 = {5:"S1",6:"S2",7:"S3",9:"S5",10:"S6",11:"S7",12:"S9",13:"S10",14:"S11",16:"S12",17:"S13",18:"S14",19:"S16",20:"S17",21:"S18",22:"S19",23:"S20"}
    d["rev30"] = rev30.get(n, "—")
    d["simulado"] = SIMULADO.get(n, "")
    d["taf"] = n in TAF_WEEKS
    exp = {1:"Conhece os documentos médico-legais e o método de estudo está rodando",3:"Fecha a parte de identificação e antropologia",
           4:"Fecha Constitucional na 1ª leitura",6:"Fecha Traumatologia",7:"Fecha Penal parte geral",9:"Fecha Asfixiologia",
           11:"Proc. Penal completo; linha do tempo cadavérica sem consulta",13:"Primeira medida real de desempenho (diagnóstico)",
           14:"Fecha Toxicologia e as leis especiais",18:"Fecha Sexologia e reescrita",19:"Fecha os estatutos do RJ",
           20:"1ª leitura de TODO o edital concluída",21:"Acima de 60% em cada módulo no Simulado 1",23:"Acima de 65% no geral",
           24:"Lista final de pontos fracos atacada",25:"Acima de 70% no geral e de 60% em cada módulo",26:"Chega à prova descansada"}
    d["esperado"] = exp.get(n, "Tópicos da semana com teoria, questões e resumo feitos")
    return d

WEEKS = [week(n) for n in range(1,27)]

GRADE = [  # dia, bloco, horário, disciplina, atividade
 ("Segunda","1","07:00–08:00","Medicina Legal","Teoria do tópico da semana"),
 ("Segunda","2","08:00–09:00","Medicina Legal","Questões do tópico + resumo"),
 ("Terça","—","—","Plantão","Sem estudo"),
 ("Quarta","1","07:00–08:00","Português","Teoria + questões"),
 ("Quarta","2","08:00–09:00","Direito","Teoria resumida + lei seca"),
 ("Quinta","1","07:00–08:00","Medicina Legal","Teoria (continuação)"),
 ("Quinta","2","08:00–09:00","Português","Questões FGV"),
 ("Sexta","1","07:00–08:00","Medicina Legal","Questões + flashcards"),
 ("Sexta","2","08:00–09:00","Direito","Questões"),
 ("Sábado","—","—","Plantão","Sem estudo"),
 ("Domingo","1","07:00–08:00","Português","Interpretação de textos FGV"),
 ("Domingo","2","08:00–09:00","Revisão","Revisão de 7 e 30 dias, caderno de erros, painel"),
]

SHORT = {
 "ML01":"Introdução, perícias e documentos","ML02":"Identificação","ML03":"Antropologia Forense",
 "ML04":"Traumatologia I (agentes mecânicos)","ML05":"Traumatologia II (armas de fogo)","ML06":"Traumatologia III (físicos, químicos, idade da lesão)",
 "ML07":"Asfixias I (sufocação e constrição do pescoço)","ML08":"Asfixias II (afogamento, soterramento, confinamento)",
 "ML09":"Tanatologia I (diagnóstico e causa da morte)","ML10":"Tanatologia II (tempo de morte)","ML11":"Tanatologia III + Infortunística",
 "ML12":"Toxicologia I (intoxicações)","ML13":"Toxicologia II (álcool e drogas)","ML14":"Sexologia I (crimes sexuais)",
 "ML15":"Sexologia II (gravidez, aborto, infanticídio)","ML16":"Sexologia III (maus-tratos, DNA)","ML17":"Psiquiatria Forense","ML18":"Ética médica",
 "PT01":"Texto e interpretação","PT02":"Ortografia e acentuação","PT03":"Classes de palavras","PT04":"Verbos",
 "PT05":"Advérbio, preposição, conjunção e formação de palavras","PT06":"Semântica","PT07":"Termos da oração","PT08":"Coordenação e subordinação",
 "PT09":"Concordância","PT10":"Regência","PT11":"Crase","PT12":"Colocação pronominal","PT13":"Pontuação","PT14":"Coesão textual",
 "PT15":"Reescrita de frases I","PT16":"Reescrita de frases II e variação linguística",
 "DI01":"Constitucional: direitos fundamentais I","DI02":"Constitucional: direitos fundamentais II","DI03":"Constitucional: Adm. Pública e servidores",
 "DI04":"Constitucional: Executivo, Segurança Pública e Ordem social","DI05":"Penal: teoria do crime","DI06":"Penal: inimputabilidade e crimes contra a pessoa I",
 "DI07":"Penal: crimes contra a pessoa II e contra a liberdade","DI08":"Penal: crimes sexuais e contra a Adm. Pública",
 "DI09":"Proc. Penal: inquérito e polícia judiciária","DI10":"Proc. Penal: prova pericial e cadeia de custódia",
 "DI11":"Leis: tortura, abuso de autoridade e racismo","DI12":"Leis: drogas e ECA","DI13":"Leis: Maria da Penha, Idoso e PcD",
 "DI14":"Administrativo: organização e ato administrativo","DI15":"Administrativo: poderes, agentes e responsabilidade",
 "DI16":"Estatuto dos servidores do RJ","DI17":"Estatuto dos policiais civis do RJ",
}
PHASE2_SHORT = {
 21:("Questões: Traumatologia e Asfixias","Questões: interpretação, concordância e regência","Questões: Constitucional e Penal"),
 22:("Questões: Tanatologia e Toxicologia","Questões: sintaxe, pontuação e crase","Questões: Proc. Penal e leis especiais"),
 23:("Questões: Sexologia e Psiquiatria","Questões: coesão e reescrita","Questões: Administrativo e estatutos"),
 24:("Questões: Identificação, Antropologia, Ética + seus erros","Questões mistas","Questões mistas + lei seca"),
 25:("Revisão final (resumos e flashcards)","Revisão do caderno de erros","Lei seca: trechos grifados"),
}
def week_short(n):
    """(ML, PT, DI) em linguagem curta para a semana n."""
    if n in RECOVERY: return ("Semana leve: revisão e atrasos",)*3
    if n == 26: return ("Revisões leves (sem conteúdo novo)",)*3
    if n in PHASE2_SHORT: return PHASE2_SHORT[n]
    out = []
    for lst, extra in ((ML, {}), (PT, {19:"Interpretação de textos FGV", 20:"Revisão de gramática (caderno de erros)"}), (DI, {20:"Questões mistas de Direito"})):
        x = by_week(lst, n); out.append(SHORT[x[0][0]] if x else extra.get(n, ""))
    return tuple(out)
