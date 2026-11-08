"""Provas de conceito Manim Community: tokenização e orquestração.

Execute a partir da raiz: manim -qh --fps 30 animacoes/prototipos.py Cena03
A biblioteca e as fichas são uma analogia; IDs e exemplos são ilustrativos.
"""
from manim import *

NAVY = '#17324A'
TEAL = '#008E89'
PALE = '#E6F3F1'
PAPER = '#F7F9FA'
MUTED = '#607C8B'
GOLD = '#F0B966'


def label(text, size=27, color=NAVY, **kw):
    return Text(text, font='DejaVu Sans', font_size=size, color=color, **kw)


def card(text, width=2.2, height=.8, fill=WHITE, size=25):
    r = RoundedRectangle(width=width, height=height, corner_radius=.13,
                         color=TEAL, stroke_width=2, fill_color=fill, fill_opacity=1)
    t = label(text, size=size)
    if t.width > width-.22: t.scale_to_fit_width(width-.22)
    t.move_to(r)
    return VGroup(r, t)


def librarian():
    # Personagem vetorial original e reutilizável: óculos, paletó e livro.
    head = Circle(radius=.34, color=NAVY, fill_color='#E9B58D', fill_opacity=1).shift(UP*.62)
    hair = Arc(radius=.34, start_angle=0, angle=PI, color=NAVY, stroke_width=9).shift(UP*.72)
    glasses = VGroup(Circle(radius=.10, color=NAVY, stroke_width=2).shift(LEFT*.13+UP*.66),
                     Circle(radius=.10, color=NAVY, stroke_width=2).shift(RIGHT*.13+UP*.66),
                     Line(LEFT*.03+UP*.66, RIGHT*.03+UP*.66, color=NAVY, stroke_width=2))
    body = RoundedRectangle(width=.85, height=1, corner_radius=.1, color=NAVY,
                            fill_color=NAVY, fill_opacity=1).shift(DOWN*.06)
    book = Rectangle(width=.55, height=.42, color=WHITE, fill_color=TEAL,
                     fill_opacity=1).shift(DOWN*.08)
    legs = VGroup(Line(LEFT*.23+DOWN*.55, LEFT*.23+DOWN*.98, color=NAVY, stroke_width=8),
                  Line(RIGHT*.23+DOWN*.55, RIGHT*.23+DOWN*.98, color=NAVY, stroke_width=8))
    return VGroup(legs, body, head, hair, glasses, book)


def frame(scene, number, title, subtitle):
    scene.camera.background_color = PAPER
    head = label(f'{number:02d}/20   •   {title}', size=33, weight=BOLD).to_edge(UP, buff=.35)
    sub = label(subtitle, size=23, color=TEAL).next_to(head, DOWN, buff=.13)
    rule = Line(LEFT*6.65, RIGHT*6.65, color='#C4D9DE', stroke_width=2).next_to(sub, DOWN, buff=.2)
    who = librarian().scale(.8).move_to(LEFT*5.7+DOWN*1.35)
    cap = label('ANALOGIA DA BIBLIOTECA', 17, MUTED).to_edge(DOWN, buff=.27)
    scene.add(head, sub, rule, who, cap)
    return who


class Cena03(Scene):
    def construct(self):
        frame(self, 3, 'O texto vira fichas', 'TOKENIZAÇÃO  •  TOKENS E IDs')
        note = card('Quem é você?', 4.1, .85, PALE, 32).move_to(UP*1.1+RIGHT*.4)
        self.play(FadeIn(note, shift=RIGHT*.5), run_time=2)
        self.wait(3)
        arrow = Arrow(note.get_bottom(), note.get_bottom()+DOWN*.7, buff=.05, color=TEAL)
        pieces = VGroup(*[card(x, 1.45, .78, WHITE, 25) for x in ['Quem', ' é', ' vo', 'cê', '?']]).arrange(RIGHT, buff=.15).move_to(DOWN*.5+RIGHT*.4)
        ids = VGroup(*[label('ID '+x, 19, MUTED) for x in ['14', '85', '32', '61', '7']])
        for x, p in zip(ids, pieces): x.next_to(p, DOWN, buff=.15)
        self.play(GrowArrow(arrow), run_time=1)
        self.play(LaggedStart(*(FadeIn(p, shift=DOWN*.3) for p in pieces), lag_ratio=.2), run_time=3)
        self.wait(4)
        self.play(LaggedStart(*(FadeIn(t) for t in ids), lag_ratio=.2), run_time=3)
        caveat = label('Divisão e IDs fictícios: variam conforme o tokenizador', 20, MUTED).to_edge(DOWN, buff=.7)
        self.play(FadeIn(caveat), run_time=1)
        self.wait(8)
        model = card('MODELO', 2.2, .8, PALE, 24).move_to(RIGHT*.4+DOWN*2.1)
        transfer = Arrow(ids.get_bottom()+DOWN*.1, model.get_top(), buff=.05, color=TEAL)
        self.play(GrowArrow(transfer), FadeIn(model), run_time=2)
        self.wait(10)
        self.play(Indicate(pieces[2]), Indicate(pieces[3]), run_time=2)
        self.wait(8)


class Cena17(Scene):
    def construct(self):
        frame(self, 17, 'Uma equipe coordenada', 'SUBAGENTES  •  ORQUESTRAÇÃO')
        chief = card('COORDENADOR', 2.5, .75, PALE, 23).move_to(UP*1.45+RIGHT*.8)
        hist = card('HISTÓRIA', 2.15, .75, WHITE, 23).move_to(LEFT*1.1+UP*.1)
        geo = card('GEOGRAFIA', 2.15, .75, WHITE, 23).move_to(RIGHT*2.7+UP*.1)
        review = card('VERIFICAÇÃO', 2.5, .75, WHITE, 23).move_to(RIGHT*.8+DOWN*1.4)
        result = card('INTEGRAR', 2.0, .65, PALE, 23).move_to(RIGHT*.8+DOWN*2.65)
        self.play(FadeIn(chief), run_time=2)
        self.wait(3)
        a1 = Arrow(chief.get_bottom(), hist.get_top(), buff=.12, color=TEAL)
        a2 = Arrow(chief.get_bottom(), geo.get_top(), buff=.12, color=TEAL)
        self.play(GrowArrow(a1), GrowArrow(a2), FadeIn(hist), FadeIn(geo), run_time=3)
        parallel = label('EM PARALELO', 17, MUTED).move_to(RIGHT*4.7+UP*.7)
        self.play(FadeIn(parallel), run_time=1)
        self.wait(8)
        self.play(Indicate(hist), Indicate(geo), run_time=3)
        r1 = Arrow(hist.get_bottom(), review.get_top()+LEFT*.5, buff=.12, color=TEAL)
        r2 = Arrow(geo.get_bottom(), review.get_top()+RIGHT*.5, buff=.12, color=TEAL)
        self.play(GrowArrow(r1), GrowArrow(r2), FadeIn(review), run_time=3)
        dependency = label('Revisão espera os dois resultados', 18, MUTED).next_to(review, RIGHT, buff=.2)
        self.play(FadeIn(dependency), run_time=1)
        self.wait(8)
        a3 = Arrow(review.get_bottom(), result.get_top(), buff=.1, color=TEAL)
        self.play(GrowArrow(a3), FadeIn(result), run_time=2)
        self.wait(10)
        self.play(Indicate(chief), run_time=2)
        self.wait(5)

# Cada quadro apresenta uma operação, não apenas uma lista de conceitos: setas
# indicam a passagem de dados e a mudança de estado entre os cartões.
STORY = {
 1: ('A grande biblioteca da IA','MODELO DE LINGUAGEM  •  LLM', [
    ('PERGUNTA','Usuário entrega um pedido'), ('CONTEXTO','Texto disponível ao modelo'),
    ('MODELO','Padrões aprendidos nos parâmetros'), ('RESPOSTA','Um token de cada vez')],
    'A estante é uma analogia; não há consulta literal obrigatória.'),
 2: ('Quem faz o quê?','ARQUITETURA DA APLICAÇÃO', [
    ('DIRETOR','Pessoa define o pedido'), ('MESA','Contexto disponível agora'),
    ('BIBLIOTECÁRIO','Modelo processa o contexto'), ('FONTES E FERRAMENTAS','Aplicação controla acesso externo')],
    'Modelo e aplicação são componentes diferentes.'),
 5: ('Como surge o contexto?','SELF-ATTENTION  •  Q, K E V', [
    ('QUERY · Q','Representação da posição atual'), ('KEYS · K','Compatibilidade Q·K gera pontuações'),
    ('PESOS','Softmax normaliza as pontuações'), ('VALUES · V','Combinação ponderada dos valores')],
    'Q, K e V são vetores projetados; cartões são analogias.'),
 6: ('Os andares do Transformer','ATENÇÃO  •  FFN  •  RESIDUAL', [
    ('ENTRADA','Representações de tokens'), ('ATENÇÃO','Cabeças processam relações em paralelo'),
    ('RESIDUAL + NORMA','Preserva caminho e estabiliza valores'), ('FFN','Rede aplicada por posição'),
    ('PRÓXIMA CAMADA','Outra passagem de processamento')],
    'A ordem exata da normalização depende da arquitetura.'),
 7: ('Ranking do próximo token','LOGITS  •  SOFTMAX', [
    ('CONTEXTO','A capital do Brasil é…'), ('LOGITS','Pontuações para os candidatos'),
    ('SOFTMAX','Converte pontuações em probabilidades'), ('DISTRIBUIÇÃO','A escolha ainda não aconteceu')],
    'Probabilidades dependem do contexto e do modelo.'),
 8: ('Escolher, escrever e repetir','TEMPERATURA  •  TOP-K  •  TOP-P  •  EOS', [
    ('DISTRIBUIÇÃO','Probabilidades dos candidatos'), ('TEMPERATURA','Ajusta concentração da distribuição'),
    ('TOP-K / TOP-P','Filtram candidatos conforme configuração'), ('AMOSTRAGEM','Escolhe e acrescenta um token'),
    ('REPETIR / EOS','Repete até fim de sequência ou outro limite')],
    'EOS é um sinal de término; probabilidades não precisam chegar a zero.'),
 9: ('Como o bibliotecário aprende?','TREINAMENTO  •  LOSS  •  BACKPROP', [
    ('EXERCÍCIO','Prever o próximo token'), ('PREVISÃO','Modelo atribui probabilidades'),
    ('LOSS','Compara previsão e referência'), ('BACKPROP','Calcula gradientes para ajuste'),
    ('REPETIR','Otimizador atualiza parâmetros')],
    'Treinamento é diferente de inferência; fine-tuning é ajuste adicional.'),
 10: ('Quanto cabe na mesa?','JANELA DE CONTEXTO  •  KV CACHE', [
    ('MESA','Entrada e saída ocupam a janela'), ('LIMITE','A aplicação controla o que cabe'),
    ('KV CACHE','Reutiliza chaves e valores calculados'), ('GERAÇÃO','Evita recalcular etapas anteriores')],
    'KV Cache não é memória persistente.'),
 11: ('Como pedir bem?','PROMPT ENGINEERING', [
    ('PEDIDO VAGO','“Faça uma exposição”'), ('OBJETIVO','Tema, público e resultado'),
    ('CONTEXTO','Fontes e informações relevantes'), ('REQUISITOS','Formato, limites e critérios'),
    ('PEDIDO CLARO','Melhora a orientação do trabalho')],
    'Um bom pedido ajuda, mas não garante acerto.'),
 12: ('Trazer livros à mesa','RAG  •  RECUPERAÇÃO EXTERNA', [
    ('PERGUNTA','Aplicação formula busca'), ('CATÁLOGO','Recupera documentos relevantes'),
    ('TRECHOS','Conteúdo selecionado entra no contexto'), ('RESPOSTA','Modelo usa contexto e aponta fontes')],
    'RAG adiciona contexto; não altera os pesos do modelo.'),
 13: ('Pedir ajuda externa','TOOL CALLING', [
    ('MODELO','Solicita operação e argumentos'), ('APLICAÇÃO','Valida e executa ferramenta externa'),
    ('FERRAMENTA','Calcula e devolve resultado'), ('MODELO','Recebe resultado e continua')],
    'A chamada e o resultado são mensagens distintas.'),
 14: ('Uma conexão padronizada','MODEL CONTEXT PROTOCOL  •  MCP', [
    ('CLIENTE','Aplicação conecta aos servidores'), ('MCP','Padrão de comunicação e descoberta'),
    ('SERVIDORES','Publicam ferramentas, recursos e prompts'), ('CHAMADA','Ferramenta ainda é executada separadamente')],
    'MCP é externo ao Transformer; acesso deve ser controlado.'),
 15: ('O manual do bibliotecário','SKILLS  •  PROCEDIMENTOS', [
    ('MANUAL','Instruções reutilizáveis confiáveis'), ('1 · BUSCAR','Consultar as fontes autorizadas'),
    ('2 · ANALISAR','Aplicar o procedimento'), ('3 · CONFERIR','Validar e registrar evidências'),
    ('4 · ENTREGAR','Usar os critérios definidos')],
    'Skill orienta o procedimento; RAG fornece conteúdo.'),
 16: ('Do objetivo ao resultado','AGENTE  •  CICLO DE AÇÃO', [
    ('OBJETIVO','Preparar uma exposição'), ('PLANEJAR','Definir etapas e critérios'),
    ('AGIR','Usar recursos autorizados'), ('OBSERVAR','Examinar resultado e falhas'),
    ('AVALIAR','Repetir, concluir ou pedir aprovação')],
    'Limites de tempo, custo e permissão governam o ciclo.'),
 18: ('Cadernos além da mesa','MEMÓRIA PERSISTENTE  •  RECUPERAÇÃO', [
    ('MESA ATUAL','Contexto da tarefa presente'), ('ARQUIVO','Informação útil é armazenada'),
    ('BUSCA','Ferramenta recupera registro relevante'), ('MESA FUTURA','Trecho recuperado volta ao contexto')],
    'Memória externa difere de parâmetros e do KV Cache.'),
 19: ('Conferir antes de publicar','EVALS  •  QA  •  OBSERVABILIDADE', [
    ('FICHA','Conferir data e fonte'), ('EVAL','Caso de teste e critério explícito'),
    ('ERRO','Divergência devolvida para correção'), ('REVISÃO','Conferir novamente antes de publicar'),
    ('MÉTRICAS','Registrar erros, tempo e custo')],
    'Evidência e revisão humana são essenciais em casos críticos.'),
 20: ('Quem pode abrir os arquivos?','PROMPT INJECTION  •  GOVERNANÇA', [
    ('LIVRO','“Ignore o diretor” é dado não confiável'), ('FRONTEIRA','Documento não concede autoridade'),
    ('MENOR PRIVILÉGIO','Acesso limitado ao necessário'), ('APROVAÇÃO','Pessoa autoriza ação sensível'),
    ('AUDITORIA','Registrar, avaliar e monitorar')],
    'Validar ferramentas e saídas; aplicar políticas de governança.'),
}

class FluxoBiblioteca(Scene):
    numero = 1
    def construct(self):
        title, subtitle, steps, caveat = STORY[self.numero]
        frame(self, self.numero, title, subtitle)
        count = len(steps)
        # Trilho vertical preserva espaço para a narração e usa letras grandes.
        cards = VGroup()
        arrows = VGroup()
        y_top = 1.55
        gap = 3.75 / max(1, count-1)
        for i, (name, explanation) in enumerate(steps):
            y = y_top-i*gap
            box = card(name, 2.85, .62, PALE if i in (0,count-1) else WHITE, 20)
            box.move_to(LEFT*2.3 + UP*y)
            detail = label(explanation, 20, NAVY)
            if detail.width > 6.0: detail.scale_to_fit_width(6.0)
            detail.next_to(box, RIGHT, buff=.38)
            cards.add(VGroup(box, detail))
            if i:
                arrows.add(Arrow(cards[i-1][0].get_bottom(), box.get_top(), buff=.04,
                                 color=TEAL, stroke_width=3, max_tip_length_to_length_ratio=.18))
        for i, group in enumerate(cards):
            animations = [FadeIn(group, shift=RIGHT*.18)]
            if i: animations.append(GrowArrow(arrows[i-1]))
            self.play(*animations, run_time=1.4)
            self.wait(6.5)
        foot = label(caveat, 17, MUTED)
        if foot.width > 12: foot.scale_to_fit_width(12)
        foot.to_edge(DOWN, buff=.7)
        self.play(FadeIn(foot), run_time=1)
        self.wait(max(2, 47-7.9*count))

# Classes explícitas tornam as 18 cenas acessíveis à CLI do Manim.
class Cena01(FluxoBiblioteca): numero = 1
class Cena02(FluxoBiblioteca): numero = 2
class Cena05(FluxoBiblioteca): numero = 5
class Cena06(FluxoBiblioteca): numero = 6
class Cena07(FluxoBiblioteca): numero = 7
class Cena08(FluxoBiblioteca): numero = 8
class Cena09(FluxoBiblioteca): numero = 9
class Cena10(FluxoBiblioteca): numero = 10
class Cena11(FluxoBiblioteca): numero = 11
class Cena12(FluxoBiblioteca): numero = 12
class Cena13(FluxoBiblioteca): numero = 13
class Cena14(FluxoBiblioteca): numero = 14
class Cena15(FluxoBiblioteca): numero = 15
class Cena16(FluxoBiblioteca): numero = 16
class Cena18(FluxoBiblioteca): numero = 18
class Cena19(FluxoBiblioteca): numero = 19
class Cena20(FluxoBiblioteca): numero = 20

class Cena04(Scene):
    def construct(self):
        frame(self, 4, 'Fichas viram vetores', 'EMBEDDINGS  •  SIMILARIDADE DE COSSENO')
        ficha = card('ID 32', 1.7, .8, PALE, 27).move_to(LEFT*2.8+UP*1.4)
        vetor = card('[0,8; 0,4; …]', 2.8, .8, WHITE, 25).move_to(RIGHT*.7+UP*1.4)
        self.play(FadeIn(ficha), run_time=2)
        self.wait(4)
        self.play(GrowArrow(Arrow(ficha.get_right(), vetor.get_left(), buff=.1, color=TEAL)), FadeIn(vetor), run_time=2)
        self.wait(5)
        origin=LEFT*.6+DOWN*1.5
        arrows=VGroup(Arrow(origin,origin+RIGHT*2.3+UP*1.0,buff=0,color=TEAL),
                      Arrow(origin,origin+RIGHT*2.1+UP*.6,buff=0,color=BLUE),
                      Arrow(origin,origin+LEFT*1.7+DOWN*.7,buff=0,color=ORANGE))
        self.play(LaggedStart(*(GrowArrow(a) for a in arrows),lag_ratio=.4),run_time=4)
        self.wait(5)
        words=VGroup(label('direções semelhantes',20,TEAL),label('direção oposta',20,ORANGE)).arrange(DOWN,buff=.15).move_to(RIGHT*3.6+DOWN*1.3)
        self.play(FadeIn(words),run_time=2)
        self.wait(10)
        info=label('Cosseno compara direção: 1 igual  •  0 ortogonal  •  −1 oposta',19,MUTED).to_edge(DOWN,buff=.8)
        self.play(FadeIn(info),run_time=2)
        self.wait(10)

# As cenas abaixo substituem fluxos lineares por diagramas específicos.
class Cena07(Scene):
    def construct(self):
        frame(self, 7, 'Ranking do próximo token', 'LOGITS  •  SOFTMAX')
        phrase = card('A capital do Brasil é…', 5, .8, PALE, 28).move_to(UP*1.55+RIGHT*.5)
        self.play(FadeIn(phrase), run_time=2)
        self.wait(5)
        candidates = ['Brasília', 'Rio', 'Salvador']
        vals = [2.0, 1.0, .4]
        probs = [.637, .234, .129]
        bars = VGroup()
        names = VGroup()
        for i, (word, val) in enumerate(zip(candidates, vals)):
            x = -1.8+i*2.25
            rect = Rectangle(width=1.05, height=val, color=TEAL, fill_color=TEAL, fill_opacity=.75).move_to([x,-1.75+val/2,0])
            bars.add(rect)
            names.add(label(word, 19, NAVY).next_to(rect, DOWN, buff=.15))
        state = label('LOGITS · pontuações ilustrativas', 22, MUTED).move_to(UP*.85+RIGHT*.5)
        self.play(FadeIn(state), LaggedStart(*(GrowFromEdge(b, DOWN) for b in bars), lag_ratio=.2), FadeIn(names), run_time=4)
        self.wait(7)
        self.play(Transform(state, label('SOFTMAX · probabilidades ilustrativas', 22, TEAL).move_to(state)), run_time=2)
        newbars=VGroup()
        percent=VGroup()
        for i,p in enumerate(probs):
            x=-1.8+i*2.25
            h=p*3
            b=Rectangle(width=1.05,height=h,color=TEAL,fill_color=TEAL,fill_opacity=.75).move_to([x,-1.75+h/2,0])
            newbars.add(b)
            percent.add(label(f'{p*100:.1f}%'.replace('.',','),18,NAVY).next_to(b,UP,buff=.08))
        self.play(Transform(bars,newbars), FadeIn(percent),run_time=3)
        self.wait(11)
        foot=label('Distribuição calculada; nenhum token foi escolhido ainda.',20,MUTED).to_edge(DOWN,buff=.8)
        self.play(FadeIn(foot),run_time=1)
        self.wait(12)

class Cena20(Scene):
    def construct(self):
        frame(self, 20, 'Quem pode abrir os arquivos?', 'PROMPT INJECTION  •  GOVERNANÇA')
        book=card('LIVRO EXTERNO',3.0,.8,PALE,23).move_to(LEFT*2.5+UP*1.4)
        attack=label('“Ignore o diretor”',22,NAVY).next_to(book,DOWN,buff=.2)
        boundary=Line(UP*2.0,DOWN*2.5,color=ORANGE,stroke_width=5).shift(RIGHT*.3)
        gate=label('FRONTEIRA\nDE CONFIANÇA',18,ORANGE).next_to(boundary,UP,buff=.12)
        self.play(FadeIn(book),FadeIn(attack),run_time=3)
        self.wait(5)
        self.play(Create(boundary),FadeIn(gate),run_time=2)
        self.wait(5)
        denied=card('DADO ≠ ORDEM',2.6,.7,WHITE,21).move_to(RIGHT*2.6+UP*1.3)
        self.play(FadeIn(denied),run_time=2)
        self.wait(6)
        privilege=card('ACESSO LIMITADO',3.1,.7,PALE,21).move_to(RIGHT*2.6+UP*.25)
        approval=card('APROVAÇÃO HUMANA',3.1,.7,WHITE,20).move_to(RIGHT*2.6+DOWN*.75)
        audit=card('LOGS E AUDITORIA',3.1,.7,WHITE,20).move_to(RIGHT*2.6+DOWN*1.75)
        self.play(FadeIn(privilege),run_time=2)
        self.wait(4)
        self.play(FadeIn(approval),run_time=2)
        self.wait(4)
        self.play(FadeIn(audit),run_time=2)
        self.wait(4)
        footer=label('Validação • testes • políticas • monitoramento',20,MUTED).to_edge(DOWN,buff=.8)
        self.play(FadeIn(footer),run_time=1)
        self.wait(8)

class Cena05(Scene):
    def construct(self):
        frame(self, 5, 'Como surge o contexto?', 'SELF-ATTENTION  •  Q, K E V')
        query=card('QUERY · Q',2.2,.7,PALE,22).move_to(LEFT*3.4+UP*1.0)
        self.play(FadeIn(query),run_time=2)
        self.wait(4)
        keys=VGroup(*[card('KEY '+str(i),1.7,.62,WHITE,20) for i in (1,2,3)]).arrange(DOWN,buff=.35).move_to(LEFT*.4+UP*.15)
        values=VGroup(*[card('VALUE '+str(i),1.9,.62,WHITE,20) for i in (1,2,3)]).arrange(DOWN,buff=.35).move_to(RIGHT*3.2+UP*.15)
        self.play(LaggedStart(*(FadeIn(k) for k in keys),lag_ratio=.3),run_time=3)
        links=VGroup(*[Arrow(query.get_right(),k.get_left(),buff=.08,color=TEAL,stroke_width=2) for k in keys])
        self.play(LaggedStart(*(GrowArrow(a) for a in links),lag_ratio=.2),run_time=3)
        caption=label('Q · K → pontuações → softmax',20,MUTED).move_to(UP*1.85+RIGHT*.2)
        self.play(FadeIn(caption),run_time=1)
        self.wait(5)
        weights=['0,60','0,30','0,10']
        w=VGroup(*[label(x,19,TEAL).next_to(k,RIGHT,buff=.28) for x,k in zip(weights,keys)])
        self.play(FadeIn(w),run_time=2)
        self.wait(4)
        self.play(LaggedStart(*(FadeIn(v) for v in values),lag_ratio=.25),run_time=3)
        self.wait(3)
        result=card('SOMA PONDERADA DE V',4.3,.7,PALE,21).move_to(RIGHT*3.2+DOWN*2.25)
        merge=Arrow(values.get_bottom(), result.get_top(), buff=.08, color=TEAL)
        self.play(GrowArrow(merge),FadeIn(result),run_time=3)
        self.wait(8)
        caveat=label('Q, K e V são vetores projetados; fichas são analogia.',18,MUTED).to_edge(DOWN,buff=.7)
        self.play(FadeIn(caveat),run_time=1)
        self.wait(8)

class Cena08(Scene):
    def construct(self):
        frame(self, 8, 'Escolher, escrever e repetir', 'TEMPERATURA  •  TOP-K  •  TOP-P  •  EOS')
        terms=['A','B','C','D']; probs=['50%','25%','15%','10%']
        fichas=VGroup(*[card(f'{t}\n{p}',1.3,1.0,PALE,24) for t,p in zip(terms,probs)]).arrange(RIGHT,buff=.22).move_to(UP*.9+RIGHT*.3)
        title=label('Distribuição ilustrativa de candidatos',21,MUTED).next_to(fichas,UP,buff=.3)
        self.play(FadeIn(title),LaggedStart(*(FadeIn(c) for c in fichas),lag_ratio=.2),run_time=3)
        self.wait(6)
        temp=label('Temperatura ajusta a concentração',21,TEAL).move_to(DOWN*.2+RIGHT*.3)
        self.play(FadeIn(temp),run_time=1)
        self.wait(5)
        filt=label('Exemplo: Top-K = 3',21,NAVY).move_to(DOWN*.85+RIGHT*.3)
        self.play(FadeIn(filt),fichas[3].animate.set_opacity(.2),run_time=2)
        self.wait(5)
        # Top-p neste exemplo é aplicado à distribuição original, não depois do top-k.
        self.play(Transform(filt,label('Alternativa: Top-P = 0,75',21,NAVY).move_to(filt)),fichas[2].animate.set_opacity(.2),run_time=2)
        self.wait(5)
        self.play(Transform(temp,label('Após o filtro, probabilidades são renormalizadas',19,TEAL).move_to(temp)),run_time=1)
        select=card('ESCOLHA: B',2.1,.7,WHITE,22).move_to(DOWN*1.75+LEFT*1.3)
        self.play(Indicate(fichas[1]),FadeIn(select),run_time=2)
        out=card('ACRESCENTAR → REPETIR',3.7,.7,PALE,20).next_to(select,RIGHT,buff=.35)
        self.play(FadeIn(out),run_time=2)
        self.wait(5)
        eos=label('EOS ou outro limite encerra a geração',19,MUTED).to_edge(DOWN,buff=.7)
        self.play(FadeIn(eos),run_time=1)
        self.wait(7)
