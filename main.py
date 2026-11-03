import pygame
import os
import random
import math
import json

# =====================================
# 1. INICIALIZACAO
# =====================================

pygame.init()

LARGURA = 1100
ALTURA = 620

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(
    "SCOOBY'S ADVENTURE - Uma aventura nas nuvens!"
)

relogio = pygame.time.Clock()
FPS = 60

PASTA = os.path.dirname(os.path.abspath(__file__))

# =====================================
# 2. CORES
# =====================================

BRANCO = (255, 245, 235)
PRETO = (20, 15, 25)

AZUL_NOITE = (18, 35, 75)
AZUL_CEU = (65, 130, 210)
AZUL = (45, 130, 255)

ROXO = (100, 65, 150)
ROSA = (255, 170, 190)
AMARELO = (255, 220, 80)
DOURADO = (255, 195, 40)

MARROM = (155, 85, 35)
MARROM_CLARO = (210, 145, 75)
VERDE = (35, 145, 90)
VERMELHO = (180, 50, 60)

# =====================================
# 3. FONTES
# =====================================

FONTE_TITULO = pygame.font.SysFont(
    "comicsansms", 48, bold=True
)

FONTE_BOTAO = pygame.font.SysFont(
    "comicsansms", 24, bold=True
)

FONTE_PEQUENA = pygame.font.SysFont(
    "comicsansms", 18
)

FONTE_GRANDE = pygame.font.SysFont(
    "comicsansms", 58, bold=True
)

# =====================================
# 4. ARQUIVOS
# =====================================

arquivo_dados = os.path.join(
    PASTA, "dados_jogo.json"
)

arquivo_recorde_antigo = os.path.join(
    PASTA, "recorde.txt"
)

# =====================================
# 5. ARCOS-IRIS
# =====================================

ARCOS_IRIS = {
    "classico": {
        "nome": "Classico",
        "preco": 0,
        "cores": [
            (255, 45, 75),
            (255, 135, 35),
            (255, 220, 40),
            (50, 210, 110),
            (45, 150, 255),
            (150, 75, 255)
        ]
    },

    "pastel": {
        "nome": "Pastel",
        "preco": 100,
        "cores": [
            (255, 190, 205),
            (255, 220, 190),
            (255, 245, 180),
            (190, 240, 205),
            (185, 220, 255),
            (220, 190, 255)
        ]
    },

    "rosa": {
        "nome": "Rosa",
        "preco": 150,
        "cores": [
            (255, 70, 150),
            (255, 110, 190),
            (255, 155, 215),
            (230, 125, 230),
            (195, 105, 220),
            (160, 85, 190)
        ]
    },

    "azul": {
        "nome": "Azul",
        "preco": 200,
        "cores": [
            (30, 80, 200),
            (40, 125, 235),
            (50, 180, 255),
            (90, 220, 245),
            (145, 235, 255),
            (190, 245, 255)
        ]
    },

    "dourado": {
        "nome": "Dourado",
        "preco": 300,
        "cores": [
            (150, 80, 20),
            (190, 110, 25),
            (225, 155, 35),
            (255, 195, 55),
            (255, 220, 110),
            (255, 240, 175)
        ]
    }
}

# =====================================
# 6. ESTILOS DE ARCO-IRIS
# =====================================

ESTILOS_ARCO = {
    "classico": {
        "nome": "Classico",
        "preco": 0
    },

    "duplo": {
        "nome": "Duplo",
        "preco": 100
    },

    "brilhante": {
        "nome": "Brilhante",
        "preco": 150
    },

    "estrelas": {
        "nome": "Com Estrelas",
        "preco": 200
    }
}

# =====================================
# 7. COLEIRAS
# =====================================

COLEIRAS = {
    "vermelha": {
        "nome": "Coleira Vermelha",
        "preco": 50,
        "cor": (230, 45, 65)
    },

    "azul": {
        "nome": "Coleira Azul",
        "preco": 75,
        "cor": (45, 130, 255)
    },

    "rosa": {
        "nome": "Coleira Rosa",
        "preco": 100,
        "cor": (255, 100, 180)
    },

    "dourada": {
        "nome": "Coleira Dourada",
        "preco": 150,
        "cor": (255, 195, 40)
    }
}

# =====================================
# 8. PALETA DE CORES
# =====================================

PALETA_PERSONALIZACAO = [
    (255, 65, 85),
    (255, 155, 65),
    (255, 220, 80),
    (80, 220, 130),
    (75, 160, 255),
    (175, 85, 240),
    (255, 170, 200),
    (255, 210, 225),
    (245, 145, 190),
    (255, 255, 255),
    (0, 0, 0),
    (120, 70, 180),
    (100, 200, 255),
    (150, 255, 180),
    (255, 230, 150),
    (180, 120, 80),
    (255, 100, 100),
    (100, 100, 255),
    (255, 150, 50),
    (180, 255, 255),
    (200, 150, 255),
    (255, 120, 180),
    (150, 200, 100),
    (220, 220, 220)
]

# =====================================
# 9. DADOS PADRAO
# =====================================

DADOS_PADRAO = {
    "recorde": 0,
    "moedas": 0,

    "arcos_comprados": ["classico"],
    "arco_equipado": "classico",

    "estilos_arco_comprados": ["classico"],
    "estilo_arco_equipado": "classico",

    "coleiras_compradas": [],
    "coleira_equipada": None,

    "cores_personalizadas": [
        [255, 45, 75],
        [255, 135, 35],
        [255, 220, 40],
        [50, 210, 110],
        [45, 150, 255],
        [150, 75, 255]
    ]
}


def carregar_dados():
    dados = DADOS_PADRAO.copy()

    if os.path.exists(arquivo_dados):
        try:
            with open(
                arquivo_dados,
                "r",
                encoding="utf-8"
            ) as arquivo:
                dados_salvos = json.load(arquivo)

            if isinstance(dados_salvos, dict):
                dados.update(dados_salvos)

        except (json.JSONDecodeError, OSError):
            pass

    elif os.path.exists(arquivo_recorde_antigo):
        try:
            with open(
                arquivo_recorde_antigo,
                "r",
                encoding="utf-8"
            ) as arquivo:
                dados["recorde"] = int(arquivo.read())

        except (ValueError, OSError):
            pass

    # Garantir que os itens equipados existem
    if dados["arco_equipado"] not in ARCOS_IRIS:
        dados["arco_equipado"] = "classico"

    if dados["estilo_arco_equipado"] not in ESTILOS_ARCO:
        dados["estilo_arco_equipado"] = "classico"

    if dados["coleira_equipada"] not in COLEIRAS:
        dados["coleira_equipada"] = None

    return dados


dados_jogo = carregar_dados()

recorde = dados_jogo["recorde"]
moedas = dados_jogo["moedas"]

arcos_comprados = dados_jogo["arcos_comprados"]
arco_equipado = dados_jogo["arco_equipado"]

estilos_arco_comprados = dados_jogo["estilos_arco_comprados"]
estilo_arco_equipado = dados_jogo["estilo_arco_equipado"]

coleiras_compradas = dados_jogo["coleiras_compradas"]
coleira_equipada = dados_jogo["coleira_equipada"]

cores_personalizadas = dados_jogo["cores_personalizadas"]


def salvar_dados():
    dados_jogo["recorde"] = recorde
    dados_jogo["moedas"] = moedas

    dados_jogo["arcos_comprados"] = arcos_comprados
    dados_jogo["arco_equipado"] = arco_equipado

    dados_jogo["estilos_arco_comprados"] = estilos_arco_comprados
    dados_jogo["estilo_arco_equipado"] = estilo_arco_equipado

    dados_jogo["coleiras_compradas"] = coleiras_compradas
    dados_jogo["coleira_equipada"] = coleira_equipada

    dados_jogo["cores_personalizadas"] = cores_personalizadas

    try:
        with open(
            arquivo_dados,
            "w",
            encoding="utf-8"
        ) as arquivo:
            json.dump(
                dados_jogo,
                arquivo,
                indent=4,
                ensure_ascii=False
            )
    except OSError:
        print("Nao foi possivel salvar os dados.")


# =====================================
# 10. ESTADO INICIAL
# =====================================

estado = "menu"

pontos = 0
vidas = 3
nivel = 1

scooby_x = 180
scooby_y = 280

velocidade_scooby = 420

# =====================================
# 11. BOTOES PRINCIPAIS
# =====================================

botao_jogar = pygame.Rect(74, 463, 263, 49)
botao_config = pygame.Rect(74, 510, 263, 48)
botao_sair = pygame.Rect(74, 556, 263, 50)

# Botao da loja no menu
botao_loja_menu = pygame.Rect(400, 440, 300, 55)

# =====================================
# PARTE 2 - CENARIO E ANIMACOES
# =====================================

# =====================================
# 1. ESTRELAS DO CEU
# =====================================

estrelas = []

for i in range(100):
    estrelas.append([
        random.randint(0, LARGURA),
        random.randint(0, ALTURA),
        random.randint(1, 3),
        random.randint(1, 4)
    ])


# =====================================
# 2. CARREGAR IMAGENS
# =====================================

def carregar_imagem(nome, tamanho=None):
    caminho = os.path.join(PASTA, nome)

    try:
        imagem = pygame.image.load(caminho).convert_alpha()

        if tamanho:
            imagem = pygame.transform.scale(
                imagem,
                tamanho
            )

        return imagem

    except (pygame.error, FileNotFoundError):
        return None


# =====================================
# 3. CARREGAR ANIMACOES DO SCOOBY
# =====================================

def carregar_animacao(nome_pasta):
    caminho = os.path.join(
        PASTA,
        "scooby_sprites",
        nome_pasta
    )

    frames = []

    if not os.path.isdir(caminho):
        return frames

    arquivos = sorted(os.listdir(caminho))

    for arquivo in arquivos:

        if arquivo.lower().endswith(".png"):

            caminho_imagem = os.path.join(
                caminho,
                arquivo
            )

            try:
                imagem = pygame.image.load(
                    caminho_imagem
                ).convert_alpha()

                imagem = pygame.transform.scale(
                    imagem,
                    (110, 100)
                )

                frames.append(imagem)

            except pygame.error:
                print(
                    "Nao foi possivel carregar:",
                    arquivo
                )

    return frames


# =====================================
# 4. ANIMACOES
# =====================================

animacoes = {
    "parado": carregar_animacao("parado"),
    "voando": carregar_animacao("voando"),
    "pulando": carregar_animacao("pulando"),
    "machucado": carregar_animacao("machucado"),
    "comemorando": carregar_animacao("comemorando"),
    "expressoes": carregar_animacao("expressoes")
}

# Imagem alternativa
scooby_img = carregar_imagem(
    "scooby.png",
    (110, 100)
)

menu_img = carregar_imagem(
    "menu.png",
    (LARGURA, ALTURA)
)

# Controle das animacoes
animacao_atual = "parado"
frame_atual = 0
tempo_animacao = 0

duracao_frame = 0.12


def definir_animacao(nome):
    global animacao_atual
    global frame_atual
    global tempo_animacao

    if nome not in animacoes:
        nome = "parado"

    if nome != animacao_atual:
        animacao_atual = nome
        frame_atual = 0
        tempo_animacao = 0


def atualizar_animacao(dt):
    global frame_atual
    global tempo_animacao

    frames = animacoes.get(animacao_atual, [])

    if not frames:
        return

    tempo_animacao += dt

    if tempo_animacao >= duracao_frame:
        tempo_animacao = 0
        frame_atual += 1

        if frame_atual >= len(frames):
            frame_atual = 0


# =====================================
# 5. DESENHAR ESTRELAS
# =====================================

def desenhar_estrela(x, y, tamanho, cor):

    pontos_estrela = []

    for i in range(10):

        angulo = math.pi / 2 + i * math.pi / 5

        if i % 2 == 0:
            raio = tamanho
        else:
            raio = tamanho / 2

        px = x + math.cos(angulo) * raio
        py = y - math.sin(angulo) * raio

        pontos_estrela.append((int(px), int(py)))

    pygame.draw.polygon(
        TELA,
        cor,
        pontos_estrela
    )


# =====================================
# 6. DESENHAR CENARIO
# =====================================

def desenhar_cenario():

    TELA.fill(AZUL_NOITE)

    # Estrelas
    for estrela in estrelas:

        x, y, tamanho, brilho = estrela

        pygame.draw.circle(
            TELA,
            BRANCO,
            (x, y),
            tamanho
        )

    # Lua
    pygame.draw.circle(
        TELA,
        AMARELO,
        (950, 90),
        42
    )

    pygame.draw.circle(
        TELA,
        AZUL_NOITE,
        (970, 75),
        38
    )

    # Nuvens
    nuvens = [
        (150, 130),
        (500, 90),
        (750, 190),
        (350, 480),
        (900, 450)
    ]

    for x, y in nuvens:

        pygame.draw.circle(
            TELA,
            BRANCO,
            (x, y),
            25
        )

        pygame.draw.circle(
            TELA,
            BRANCO,
            (x + 25, y - 10),
            30
        )

        pygame.draw.circle(
            TELA,
            BRANCO,
            (x + 55, y),
            25
        )

        pygame.draw.rect(
            TELA,
            BRANCO,
            (x, y, 55, 25)
        )


# =====================================
# 7. DESENHAR TEXTO
# =====================================

def desenhar_texto(
    texto,
    fonte,
    cor,
    x,
    y,
    centralizar=False
):

    imagem = fonte.render(
        str(texto),
        True,
        cor
    )

    retangulo = imagem.get_rect()

    if centralizar:
        retangulo.center = (x, y)

    else:
        retangulo.topleft = (x, y)

    TELA.blit(
        imagem,
        retangulo
    )


# =====================================
# 8. DESENHAR BOTOES
# =====================================

def desenhar_botao(
    texto,
    retangulo,
    cor,
    cor_texto=BRANCO
):

    pygame.draw.rect(
        TELA,
        cor,
        retangulo,
        border_radius=15
    )

    pygame.draw.rect(
        TELA,
        BRANCO,
        retangulo,
        2,
        border_radius=15
    )

    desenhar_texto(
        texto,
        FONTE_BOTAO,
        cor_texto,
        retangulo.centerx,
        retangulo.centery,
        True
    )

# =====================================
# PARTE 3 - SCOOBY E ACESSORIOS
# =====================================

# =====================================
# 1. DESENHAR ARCO-IRIS
# =====================================

def desenhar_arco_iris(x, y):

    configuracao = ARCOS_IRIS.get(
        arco_equipado,
        ARCOS_IRIS["classico"]
    )

    cores = configuracao["cores"]

    estilo = estilo_arco_equipado

    # Se o jogador estiver usando cores personalizadas
    if arco_equipado == "classico":
        cores = [
            tuple(cor)
            for cor in cores_personalizadas[:6]
        ]

    retangulo = pygame.Rect(
        x - 30,
        y - 65,
        170,
        145
    )

    # Estilo classico
    if estilo == "classico":

        for i, cor in enumerate(cores):

            area = retangulo.inflate(
                -i * 13,
                -i * 13
            )

            pygame.draw.arc(
                TELA,
                cor,
                area,
                0,
                math.pi,
                9
            )

    # Estilo duplo
    elif estilo == "duplo":

        for deslocamento in [0, 18]:

            area = retangulo.move(
                deslocamento,
                0
            )

            for i, cor in enumerate(cores):

                arco = area.inflate(
                    -i * 11,
                    -i * 11
                )

                pygame.draw.arc(
                    TELA,
                    cor,
                    arco,
                    0,
                    math.pi,
                    7
                )

    # Estilo brilhante
    elif estilo == "brilhante":

        for i, cor in enumerate(cores):

            area = retangulo.inflate(
                -i * 13,
                -i * 13
            )

            pygame.draw.arc(
                TELA,
                cor,
                area,
                0,
                math.pi,
                12
            )

            pygame.draw.arc(
                TELA,
                BRANCO,
                area.inflate(-5, -5),
                0,
                math.pi,
                2
            )

        desenhar_estrela(
            x + 20,
            y - 50,
            10,
            BRANCO
        )

        desenhar_estrela(
            x + 130,
            y - 40,
            8,
            AMARELO
        )

    # Estilo com estrelas
    elif estilo == "estrelas":

        for i, cor in enumerate(cores):

            area = retangulo.inflate(
                -i * 13,
                -i * 13
            )

            pygame.draw.arc(
                TELA,
                cor,
                area,
                0,
                math.pi,
                8
            )

        desenhar_estrela(
            x + 5,
            y - 45,
            10,
            AMARELO
        )

        desenhar_estrela(
            x + 145,
            y - 55,
            12,
            BRANCO
        )

        desenhar_estrela(
            x + 75,
            y - 100,
            9,
            AMARELO
        )


# =====================================
# 2. DESENHAR COLEIRA
# =====================================

def desenhar_coleira(x, y):

    if coleira_equipada is None:
        return

    configuracao = COLEIRAS.get(
        coleira_equipada
    )

    if configuracao is None:
        return

    cor = configuracao["cor"]

    # Coleira no pescoco
    pygame.draw.arc(
        TELA,
        cor,
        pygame.Rect(
            x + 48,
            y + 35,
            43,
            35
        ),
        math.pi,
        math.pi * 2,
        7
    )

    # Pingente
    pygame.draw.circle(
        TELA,
        DOURADO,
        (int(x + 70), int(y + 68)),
        7
    )

    pygame.draw.circle(
        TELA,
        AMARELO,
        (int(x + 70), int(y + 68)),
        3
    )


# =====================================
# 3. DESENHAR SCOOBY
# =====================================

def desenhar_scooby():

    x = int(scooby_x)
    y = int(scooby_y)

    # Arco-iris atras do Scooby
    desenhar_arco_iris(x, y)

    frames = animacoes.get(
        animacao_atual,
        []
    )

    # Usar animacoes
    if frames:

        imagem = frames[
            frame_atual % len(frames)
        ]

        TELA.blit(
            imagem,
            (x, y)
        )

    # Usar imagem alternativa
    elif scooby_img:

        TELA.blit(
            scooby_img,
            (x, y)
        )

    # Desenho provisório se nao houver imagem
    else:

        pygame.draw.ellipse(
            TELA,
            MARROM,
            (x + 15, y + 15, 80, 65)
        )

        pygame.draw.circle(
            TELA,
            MARROM_CLARO,
            (x + 85, y + 35),
            25
        )

        pygame.draw.circle(
            TELA,
            PRETO,
            (x + 95, y + 30),
            4
        )

        pygame.draw.ellipse(
            TELA,
            PRETO,
            (x + 100, y + 45, 12, 8)
        )

        # Orelhas
        pygame.draw.ellipse(
            TELA,
            MARROM,
            (x + 72, y + 5, 16, 35)
        )

    # Coleira por cima do personagem
    desenhar_coleira(x, y)


# =====================================
# 4. CONTROLAR ANIMACAO
# =====================================

def controlar_animacao_scooby(dt):

    teclas = pygame.key.get_pressed()

    andando = (
        teclas[pygame.K_LEFT]
        or teclas[pygame.K_RIGHT]
        or teclas[pygame.K_UP]
        or teclas[pygame.K_DOWN]
        or teclas[pygame.K_a]
        or teclas[pygame.K_d]
        or teclas[pygame.K_w]
        or teclas[pygame.K_s]
    )

    if andando:
        definir_animacao("voando")

    else:
        definir_animacao("parado")

    atualizar_animacao(dt)

# =====================================
# PARTE 4 - MECANICA DO JOGO
# =====================================

# =====================================
# 1. LISTAS DE OBJETOS
# =====================================

ossos = []
obstaculos = []
biscoitos = []
moedas_objetos = []

tempo_ossos = 0
tempo_obstaculos = 0
tempo_biscoitos = 0
tempo_moedas = 0

mensagem_jogo = ""
tempo_mensagem = 0


# =====================================
# 2. INICIAR JOGO
# =====================================

def iniciar_jogo():

    global estado
    global pontos, vidas, nivel
    global scooby_x, scooby_y
    global tempo_ossos, tempo_obstaculos
    global tempo_biscoitos, tempo_moedas
    global ossos, obstaculos
    global biscoitos, moedas_objetos
    global mensagem_jogo, tempo_mensagem

    estado = "jogando"

    pontos = 0
    vidas = 3
    nivel = 1

    scooby_x = 180
    scooby_y = 280

    ossos = []
    obstaculos = []
    biscoitos = []
    moedas_objetos = []

    tempo_ossos = 0
    tempo_obstaculos = 0
    tempo_biscoitos = 0
    tempo_moedas = 0

    mensagem_jogo = ""
    tempo_mensagem = 0

    definir_animacao("parado")


# =====================================
# 3. CRIAR OBJETOS
# =====================================

def criar_osso():

    ossos.append({
        "x": LARGURA + 30,
        "y": random.randint(100, ALTURA - 100),
        "velocidade": random.randint(230, 330)
    })


def criar_obstaculo():

    obstaculos.append({
        "x": LARGURA + 30,
        "y": random.randint(100, ALTURA - 100),
        "velocidade": random.randint(280, 380),
        "tamanho": random.randint(25, 40)
    })


def criar_biscoito():

    biscoitos.append({
        "x": LARGURA + 30,
        "y": random.randint(100, ALTURA - 100),
        "velocidade": random.randint(220, 300)
    })


def criar_moeda():

    moedas_objetos.append({
        "x": LARGURA + 30,
        "y": random.randint(100, ALTURA - 100),
        "velocidade": random.randint(240, 320)
    })


# =====================================
# 4. DESENHAR OBJETOS
# =====================================

def desenhar_osso(x, y):

    pygame.draw.line(
        TELA,
        BRANCO,
        (int(x), int(y)),
        (int(x + 25), int(y)),
        7
    )

    pygame.draw.circle(
        TELA,
        BRANCO,
        (int(x), int(y - 5)),
        6
    )

    pygame.draw.circle(
        TELA,
        BRANCO,
        (int(x), int(y + 5)),
        6
    )

    pygame.draw.circle(
        TELA,
        BRANCO,
        (int(x + 25), int(y - 5)),
        6
    )

    pygame.draw.circle(
        TELA,
        BRANCO,
        (int(x + 25), int(y + 5)),
        6
    )


def desenhar_obstaculo(x, y, tamanho):

    pygame.draw.circle(
        TELA,
        ROXO,
        (int(x), int(y)),
        tamanho
    )

    pygame.draw.circle(
        TELA,
        ROSA,
        (int(x - tamanho // 3), int(y - tamanho // 3)),
        tamanho // 4
    )

    pygame.draw.circle(
        TELA,
        BRANCO,
        (int(x + tamanho // 3), int(y - tamanho // 3)),
        tamanho // 5
    )


def desenhar_biscoito(x, y):

    pygame.draw.circle(
        TELA,
        MARROM_CLARO,
        (int(x), int(y)),
        14
    )

    pygame.draw.circle(
        TELA,
        MARROM,
        (int(x - 5), int(y - 4)),
        3
    )

    pygame.draw.circle(
        TELA,
        MARROM,
        (int(x + 5), int(y - 4)),
        3
    )

    pygame.draw.circle(
        TELA,
        MARROM,
        (int(x), int(y + 5)),
        3
    )


def desenhar_moeda(x, y):

    pygame.draw.circle(
        TELA,
        DOURADO,
        (int(x), int(y)),
        13
    )

    pygame.draw.circle(
        TELA,
        AMARELO,
        (int(x), int(y)),
        9
    )

    desenhar_texto(
        "$",
        FONTE_PEQUENA,
        MARROM,
        x,
        y,
        True
    )


# =====================================
# 5. MOVIMENTAR SCOOBY
# =====================================

def movimentar_scooby(dt):

    global scooby_x, scooby_y

    teclas = pygame.key.get_pressed()

    velocidade = velocidade_scooby * dt

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        scooby_x -= velocidade

    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        scooby_x += velocidade

    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        scooby_y -= velocidade

    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        scooby_y += velocidade

    # Limites da tela
    scooby_x = max(0, min(scooby_x, LARGURA - 110))

    scooby_y = max(65, min(scooby_y, ALTURA - 105))


# =====================================
# 6. ATUALIZAR OBJETOS
# =====================================

def atualizar_objetos(dt):

    global tempo_ossos
    global tempo_obstaculos
    global tempo_biscoitos
    global tempo_moedas

    # Criar ossos
    tempo_ossos += dt

    if tempo_ossos >= 1.8:
        criar_osso()
        tempo_ossos = 0

    # Criar obstaculos
    tempo_obstaculos += dt

    if tempo_obstaculos >= 2.5:
        criar_obstaculo()
        tempo_obstaculos = 0

    # Criar biscoitos
    tempo_biscoitos += dt

    if tempo_biscoitos >= 4:
        criar_biscoito()
        tempo_biscoitos = 0

    # Criar moedas
    tempo_moedas += dt

    if tempo_moedas >= 5:
        criar_moeda()
        tempo_moedas = 0

    # Movimentar ossos
    for osso in ossos:
        osso["x"] -= osso["velocidade"] * dt

    # Movimentar obstaculos
    for obstaculo in obstaculos:
        obstaculo["x"] -= obstaculo["velocidade"] * dt

    # Movimentar biscoitos
    for biscoito in biscoitos:
        biscoito["x"] -= biscoito["velocidade"] * dt

    # Movimentar moedas
    for moeda_obj in moedas_objetos:
        moeda_obj["x"] -= moeda_obj["velocidade"] * dt

    # Remover objetos que sairam da tela
    ossos[:] = [
        item for item in ossos
        if item["x"] > -50
    ]

    obstaculos[:] = [
        item for item in obstaculos
        if item["x"] > -60
    ]

    biscoitos[:] = [
        item for item in biscoitos
        if item["x"] > -50
    ]

    moedas_objetos[:] = [
        item for item in moedas_objetos
        if item["x"] > -50
    ]


# =====================================
# 7. COLISOES
# =====================================

def verificar_colisoes():

    global pontos, vidas
    global moedas, recorde
    global nivel, estado
    global mensagem_jogo, tempo_mensagem

    scooby_rect = pygame.Rect(
        int(scooby_x + 15),
        int(scooby_y + 15),
        80,
        70
    )

    # Ossos
    for osso in ossos[:]:

        objeto_rect = pygame.Rect(
            int(osso["x"]),
            int(osso["y"] - 8),
            30,
            18
        )

        if scooby_rect.colliderect(objeto_rect):

            ossos.remove(osso)

            pontos += 10

            mensagem_jogo = "+10 pontos!"
            tempo_mensagem = 1

    # Biscoitos
    for biscoito in biscoitos[:]:

        objeto_rect = pygame.Rect(
            int(biscoito["x"] - 14),
            int(biscoito["y"] - 14),
            28,
            28
        )

        if scooby_rect.colliderect(objeto_rect):

            biscoitos.remove(biscoito)

            pontos += 20

            mensagem_jogo = "Scooby ama biscoitos!"
            tempo_mensagem = 1.5

    # Moedas
    for moeda_obj in moedas_objetos[:]:

        objeto_rect = pygame.Rect(
            int(moeda_obj["x"] - 13),
            int(moeda_obj["y"] - 13),
            26,
            26
        )

        if scooby_rect.colliderect(objeto_rect):

            moedas_objetos.remove(moeda_obj)

            moedas += 5

            mensagem_jogo = "+5 moedas!"
            tempo_mensagem = 1.5

            salvar_dados()

    # Obstaculos
    for obstaculo in obstaculos[:]:

        tamanho = obstaculo["tamanho"]

        objeto_rect = pygame.Rect(
            int(obstaculo["x"] - tamanho),
            int(obstaculo["y"] - tamanho),
            tamanho * 2,
            tamanho * 2
        )

        if scooby_rect.colliderect(objeto_rect):

            obstaculos.remove(obstaculo)

            vidas -= 1

            mensagem_jogo = "Cuidado, Scooby!"
            tempo_mensagem = 1.5

            if vidas <= 0:

                if pontos > recorde:
                    recorde = pontos

                salvar_dados()

                estado = "game_over"

                return

    # Atualizar nivel
    nivel = pontos // 100 + 1

    if pontos > recorde:
        recorde = pontos


# =====================================
# 8. DESENHAR INFORMACOES
# =====================================

def desenhar_hud():

    pygame.draw.rect(
        TELA,
        AZUL_NOITE,
        (0, 0, LARGURA, 55)
    )

    desenhar_texto(
        f"Pontos: {pontos}",
        FONTE_BOTAO,
        BRANCO,
        20,
        15
    )

    desenhar_texto(
        f"Vidas: {vidas}",
        FONTE_BOTAO,
        ROSA,
        220,
        15
    )

    desenhar_texto(
        f"Nivel: {nivel}",
        FONTE_BOTAO,
        AMARELO,
        390,
        15
    )

    desenhar_texto(
        f"Moedas: {moedas}",
        FONTE_BOTAO,
        DOURADO,
        550,
        15
    )

    desenhar_texto(
        f"Recorde: {recorde}",
        FONTE_BOTAO,
        BRANCO,
        800,
        15
    )

    if tempo_mensagem > 0:

        desenhar_texto(
            mensagem_jogo,
            FONTE_BOTAO,
            AMARELO,
            LARGURA // 2,
            85,
            True
        )


# =====================================
# 9. ATUALIZAR JOGO
# =====================================

def atualizar_jogo(dt):

    global tempo_mensagem

    movimentar_scooby(dt)

    controlar_animacao_scooby(dt)

    atualizar_objetos(dt)

    verificar_colisoes()

    if tempo_mensagem > 0:
        tempo_mensagem -= dt


# =====================================
# 10. DESENHAR JOGO
# =====================================

def desenhar_jogo():

    desenhar_cenario()

    # Objetos
    for osso in ossos:
        desenhar_osso(
            osso["x"],
            osso["y"]
        )

    for obstaculo in obstaculos:
        desenhar_obstaculo(
            obstaculo["x"],
            obstaculo["y"],
            obstaculo["tamanho"]
        )

    for biscoito in biscoitos:
        desenhar_biscoito(
            biscoito["x"],
            biscoito["y"]
        )

    for moeda_obj in moedas_objetos:
        desenhar_moeda(
            moeda_obj["x"],
            moeda_obj["y"]
        )

    desenhar_scooby()

    desenhar_hud()

# =====================================
# PARTE 5 - MENU, LOJA E PERSONALIZACAO
# =====================================

# =====================================
# 1. CONFIGURACOES DA LOJA
# =====================================

categoria_loja = "arcos"

mensagem_loja = ""
tempo_mensagem_loja = 0

cor_selecionada = 0

# Botoes das categorias
aba_arcos = pygame.Rect(70, 105, 190, 45)
aba_estilos = pygame.Rect(280, 105, 190, 45)
aba_coleiras = pygame.Rect(490, 105, 190, 45)
aba_personalizar = pygame.Rect(700, 105, 300, 45)

botao_voltar_loja = pygame.Rect(
    30, 540, 150, 50
)


# =====================================
# 2. MOSTRAR MENSAGEM DA LOJA
# =====================================

def mostrar_mensagem_loja(mensagem):

    global mensagem_loja
    global tempo_mensagem_loja

    mensagem_loja = mensagem
    tempo_mensagem_loja = 2


# =====================================
# 3. DESENHAR MENU
# =====================================

def desenhar_menu():

    desenhar_cenario()

    # Titulo
    desenhar_texto(
        "SCOOBY'S ADVENTURE",
        FONTE_TITULO,
        AMARELO,
        LARGURA // 2,
        85,
        True
    )

    desenhar_texto(
        "Uma aventura nas nuvens!",
        FONTE_BOTAO,
        BRANCO,
        LARGURA // 2,
        130,
        True
    )

    # Scooby no menu
    desenhar_scooby()

    # Botoes
    desenhar_botao(
        "JOGAR",
        botao_jogar,
        VERDE
    )

    desenhar_botao(
        "CONFIGURACOES",
        botao_config,
        AZUL
    )

    desenhar_botao(
        "SAIR",
        botao_sair,
        VERMELHO
    )

    desenhar_botao(
        "LOJA",
        botao_loja_menu,
        ROXO
    )

    desenhar_texto(
        f"Recorde: {recorde}",
        FONTE_BOTAO,
        BRANCO,
        LARGURA // 2,
        510,
        True
    )

    desenhar_texto(
        f"Moedas: {moedas}",
        FONTE_BOTAO,
        DOURADO,
        LARGURA // 2,
        550,
        True
    )


# =====================================
# 4. DESENHAR PRODUTO DA LOJA
# =====================================

def desenhar_produto(
    retangulo,
    nome,
    preco,
    comprado,
    equipado,
    cor
):

    pygame.draw.rect(
        TELA,
        (35, 45, 95),
        retangulo,
        border_radius=15
    )

    pygame.draw.rect(
        TELA,
        cor,
        retangulo,
        3,
        border_radius=15
    )

    desenhar_texto(
        nome,
        FONTE_BOTAO,
        BRANCO,
        retangulo.centerx,
        retangulo.y + 27,
        True
    )

    if equipado:

        texto = "EQUIPADO"

    elif comprado:

        texto = "EQUIPAR"

    else:

        texto = f"COMPRAR: {preco}"

    desenhar_texto(
        texto,
        FONTE_PEQUENA,
        AMARELO,
        retangulo.centerx,
        retangulo.y + 85,
        True
    )


# =====================================
# 5. DESENHAR LOJA
# =====================================

def desenhar_loja():

    desenhar_cenario()

    desenhar_texto(
        "LOJA DO SCOOBY",
        FONTE_TITULO,
        AMARELO,
        LARGURA // 2,
        55,
        True
    )

    desenhar_texto(
        f"Suas moedas: {moedas}",
        FONTE_BOTAO,
        DOURADO,
        LARGURA - 180,
        20,
        True
    )

    # Abas
    desenhar_botao(
        "ARCOS",
        aba_arcos,
        ROXO if categoria_loja == "arcos" else AZUL
    )

    desenhar_botao(
        "ESTILOS",
        aba_estilos,
        ROXO if categoria_loja == "estilos" else AZUL
    )

    desenhar_botao(
        "COLEIRAS",
        aba_coleiras,
        ROXO if categoria_loja == "coleiras" else AZUL
    )

    desenhar_botao(
        "PERSONALIZAR",
        aba_personalizar,
        ROXO if categoria_loja == "personalizar" else AZUL
    )

    # Produtos
    if categoria_loja == "arcos":

        produtos = list(ARCOS_IRIS.keys()) + [
            "personalizado"
        ]

        for i, identificador in enumerate(produtos):

            coluna = i % 3
            linha = i // 3

            x = 100 + coluna * 310
            y = 185 + linha * 145

            retangulo = pygame.Rect(
                x,
                y,
                260,
                115
            )

            if identificador == "personalizado":

                nome = "Personalizado"
                preco = 0
                comprado = (
                    "personalizado" in arcos_comprados
                )

                equipado = (
                    arco_equipado == "personalizado"
                )

                cor = ROSA

            else:

                item = ARCOS_IRIS[identificador]

                nome = item["nome"]
                preco = item["preco"]

                comprado = (
                    identificador in arcos_comprados
                )

                equipado = (
                    arco_equipado == identificador
                )

                cor = item["cores"][0]

            desenhar_produto(
                retangulo,
                nome,
                preco,
                comprado,
                equipado,
                cor
            )

    elif categoria_loja == "estilos":

        for i, identificador in enumerate(
            ESTILOS_ARCO.keys()
        ):

            coluna = i % 3
            linha = i // 3

            x = 100 + coluna * 310
            y = 185 + linha * 145

            retangulo = pygame.Rect(
                x,
                y,
                260,
                115
            )

            item = ESTILOS_ARCO[identificador]

            desenhar_produto(
                retangulo,
                item["nome"],
                item["preco"],
                identificador in estilos_arco_comprados,
                identificador == estilo_arco_equipado,
                AMARELO
            )

    elif categoria_loja == "coleiras":

        for i, identificador in enumerate(
            COLEIRAS.keys()
        ):

            coluna = i % 3
            linha = i // 3

            x = 100 + coluna * 310
            y = 185 + linha * 145

            retangulo = pygame.Rect(
                x,
                y,
                260,
                115
            )

            item = COLEIRAS[identificador]

            desenhar_produto(
                retangulo,
                item["nome"],
                item["preco"],
                identificador in coleiras_compradas,
                identificador == coleira_equipada,
                item["cor"]
            )

    elif categoria_loja == "personalizar":

        desenhar_texto(
            "Escolha uma faixa do arco-iris:",
            FONTE_BOTAO,
            BRANCO,
            LARGURA // 2,
            185,
            True
        )

        # Seis faixas selecionaveis
        for i in range(6):

            retangulo = pygame.Rect(
                240 + i * 105,
                220,
                65,
                45
            )

            pygame.draw.rect(
                TELA,
                cores_personalizadas[i],
                retangulo,
                border_radius=8
            )

            pygame.draw.rect(
                TELA,
                AMARELO if cor_selecionada == i else BRANCO,
                retangulo,
                3,
                border_radius=8
            )

            desenhar_texto(
                str(i + 1),
                FONTE_PEQUENA,
                PRETO,
                retangulo.centerx,
                retangulo.centery,
                True
            )

        desenhar_texto(
            "Agora escolha uma cor:",
            FONTE_BOTAO,
            BRANCO,
            LARGURA // 2,
            305,
            True
        )

        # Paleta de cores
        for i, cor in enumerate(PALETA_PERSONALIZACAO):

            coluna = i % 8
            linha = i // 8

            x = 250 + coluna * 85
            y = 345 + linha * 55

            pygame.draw.circle(
                TELA,
                cor,
                (x, y),
                19
            )

            pygame.draw.circle(
                TELA,
                BRANCO,
                (x, y),
                19,
                2
            )

    # Mensagem
    if tempo_mensagem_loja > 0:

        desenhar_texto(
            mensagem_loja,
            FONTE_BOTAO,
            AMARELO,
            LARGURA // 2,
            500,
            True
        )

    desenhar_botao(
        "VOLTAR",
        botao_voltar_loja,
        VERMELHO
    )


# =====================================
# 6. COMPRAR OU EQUIPAR PRODUTOS
# =====================================

def comprar_ou_equipar(identificador):

    global moedas
    global arco_equipado
    global estilo_arco_equipado
    global coleira_equipada

    if categoria_loja == "arcos":

        if identificador == "personalizado":

            if identificador not in arcos_comprados:
                arcos_comprados.append(identificador)

            arco_equipado = identificador

            mostrar_mensagem_loja(
                "Arco personalizado equipado!"
            )

        else:

            item = ARCOS_IRIS[identificador]

            if identificador in arcos_comprados:

                arco_equipado = identificador

                mostrar_mensagem_loja(
                    "Arco-iris equipado!"
                )

            elif moedas >= item["preco"]:

                moedas -= item["preco"]

                arcos_comprados.append(
                    identificador
                )

                arco_equipado = identificador

                mostrar_mensagem_loja(
                    "Compra realizada!"
                )

            else:

                mostrar_mensagem_loja(
                    "Moedas insuficientes!"
                )

    elif categoria_loja == "estilos":

        item = ESTILOS_ARCO[identificador]

        if identificador in estilos_arco_comprados:

            estilo_arco_equipado = identificador

            mostrar_mensagem_loja(
                "Estilo equipado!"
            )

        elif moedas >= item["preco"]:

            moedas -= item["preco"]

            estilos_arco_comprados.append(
                identificador
            )

            estilo_arco_equipado = identificador

            mostrar_mensagem_loja(
                "Novo estilo comprado!"
            )

        else:

            mostrar_mensagem_loja(
                "Moedas insuficientes!"
            )

    elif categoria_loja == "coleiras":

        item = COLEIRAS[identificador]

        if identificador in coleiras_compradas:

            coleira_equipada = identificador

            mostrar_mensagem_loja(
                "Coleira equipada!"
            )

        elif moedas >= item["preco"]:

            moedas -= item["preco"]

            coleiras_compradas.append(
                identificador
            )

            coleira_equipada = identificador

            mostrar_mensagem_loja(
                "Coleira comprada!"
            )

        else:

            mostrar_mensagem_loja(
                "Moedas insuficientes!"
            )

    salvar_dados()


# =====================================
# 7. CLIQUES NA LOJA
# =====================================

def tratar_clique_loja(posicao):

    global estado
    global categoria_loja
    global cor_selecionada

    if botao_voltar_loja.collidepoint(posicao):

        estado = "menu"
        return

    if aba_arcos.collidepoint(posicao):

        categoria_loja = "arcos"
        return

    if aba_estilos.collidepoint(posicao):

        categoria_loja = "estilos"
        return

    if aba_coleiras.collidepoint(posicao):

        categoria_loja = "coleiras"
        return

    if aba_personalizar.collidepoint(posicao):

        categoria_loja = "personalizar"
        return

    x, y = posicao

    # Selecionar faixa e cor personalizada
    if categoria_loja == "personalizar":

        for i in range(6):

            retangulo = pygame.Rect(
                240 + i * 105,
                220,
                65,
                45
            )

            if retangulo.collidepoint(posicao):

                cor_selecionada = i

                mostrar_mensagem_loja(
                    f"Faixa {i + 1} selecionada!"
                )

                return

        for i, cor in enumerate(PALETA_PERSONALIZACAO):

            coluna = i % 8
            linha = i // 8

            cx = 250 + coluna * 85
            cy = 345 + linha * 55

            if math.dist((x, y), (cx, cy)) <= 20:

                cores_personalizadas[
                    cor_selecionada
                ] = list(cor)

                if "personalizado" not in arcos_comprados:
                    arcos_comprados.append(
                        "personalizado"
                    )

                arco_equipado = "personalizado"

                salvar_dados()

                mostrar_mensagem_loja(
                    "Cor personalizada aplicada!"
                )

                return

    # Clicar nos produtos
    if categoria_loja in [
        "arcos",
        "estilos",
        "coleiras"
    ]:

        if categoria_loja == "arcos":

            produtos = list(ARCOS_IRIS.keys()) + [
                "personalizado"
            ]

        elif categoria_loja == "estilos":

            produtos = list(ESTILOS_ARCO.keys())

        else:

            produtos = list(COLEIRAS.keys())

        for i, identificador in enumerate(produtos):

            coluna = i % 3
            linha = i // 3

            retangulo = pygame.Rect(
                100 + coluna * 310,
                185 + linha * 145,
                260,
                115
            )

            if retangulo.collidepoint(posicao):

                comprar_ou_equipar(
                    identificador
                )

                return


# =====================================
# 8. CONFIGURACOES
# =====================================

botao_config_voltar = pygame.Rect(
    420, 430, 260, 55
)


def desenhar_configuracoes():

    desenhar_cenario()

    desenhar_texto(
        "CONFIGURACOES",
        FONTE_TITULO,
        AMARELO,
        LARGURA // 2,
        120,
        True
    )

    desenhar_texto(
        "MOVIMENTACAO",
        FONTE_BOTAO,
        BRANCO,
        LARGURA // 2,
        220,
        True
    )

    desenhar_texto(
        "Use as setas ou W, A, S, D",
        FONTE_BOTAO,
        BRANCO,
        LARGURA // 2,
        270,
        True
    )

    desenhar_texto(
        "ESC: voltar ao menu",
        FONTE_PEQUENA,
        BRANCO,
        LARGURA // 2,
        330,
        True
    )

    desenhar_botao(
        "VOLTAR",
        botao_config_voltar,
        AZUL
    )


# =====================================
# 9. GAME OVER
# =====================================

botao_jogar_novamente = pygame.Rect(
    350, 390, 190, 60
)

botao_menu_game_over = pygame.Rect(
    570, 390, 190, 60
)


def desenhar_game_over():

    desenhar_cenario()

    desenhar_texto(
        "FIM DE JOGO!",
        FONTE_GRANDE,
        VERMELHO,
        LARGURA // 2,
        140,
        True
    )

    desenhar_texto(
        "O Scooby precisa descansar!",
        FONTE_BOTAO,
        BRANCO,
        LARGURA // 2,
        220,
        True
    )

    desenhar_texto(
        f"Pontuacao: {pontos}",
        FONTE_BOTAO,
        AMARELO,
        LARGURA // 2,
        280,
        True
    )

    desenhar_texto(
        f"Recorde: {recorde}",
        FONTE_BOTAO,
        DOURADO,
        LARGURA // 2,
        325,
        True
    )

    desenhar_botao(
        "JOGAR NOVAMENTE",
        botao_jogar_novamente,
        VERDE
    )

    desenhar_botao(
        "MENU",
        botao_menu_game_over,
        AZUL
    )


# =====================================
# 10. ATUALIZAR MENSAGEM DA LOJA
# =====================================

def atualizar_mensagem_loja(dt):

    global tempo_mensagem_loja

    if tempo_mensagem_loja > 0:

        tempo_mensagem_loja -= dt

# =====================================
# PARTE 6 - CONTROLES E LOOP PRINCIPAL
# =====================================

# =====================================
# 1. CLIQUES NO MENU
# =====================================

def tratar_clique_menu(posicao):

    global estado

    if botao_jogar.collidepoint(posicao):

        iniciar_jogo()

    elif botao_config.collidepoint(posicao):

        estado = "config"

    elif botao_loja_menu.collidepoint(posicao):

        estado = "loja"
        categoria_loja = "arcos"

    elif botao_sair.collidepoint(posicao):

        salvar_dados()
        return False

    return True


# =====================================
# 2. CLIQUES NAS CONFIGURACOES
# =====================================

def tratar_clique_config(posicao):

    global estado

    if botao_config_voltar.collidepoint(posicao):

        estado = "menu"


# =====================================
# 3. CLIQUES NO GAME OVER
# =====================================

def tratar_clique_game_over(posicao):

    global estado

    if botao_jogar_novamente.collidepoint(posicao):

        iniciar_jogo()

    elif botao_menu_game_over.collidepoint(posicao):

        estado = "menu"


# =====================================
# 4. CONTROLES DO TECLADO
# =====================================

def tratar_teclado(tecla):

    global estado

    if tecla == pygame.K_ESCAPE:

        if estado == "jogando":

            estado = "menu"

        elif estado in [
            "loja",
            "config",
            "game_over"
        ]:

            estado = "menu"

        elif estado == "menu":

            salvar_dados()
            return False

    if tecla == pygame.K_RETURN:

        if estado == "game_over":

            iniciar_jogo()

    return True


# =====================================
# 5. LOOP PRINCIPAL
# =====================================

executando = True

while executando:

    # Tempo entre os frames
    dt = relogio.tick(FPS) / 1000

    # Evita grandes saltos de movimento
    dt = min(dt, 0.05)

    # =================================
    # EVENTOS
    # =================================

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            salvar_dados()
            executando = False

        elif evento.type == pygame.KEYDOWN:

            if not tratar_teclado(evento.key):

                executando = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.button == 1:

                posicao = evento.pos

                if estado == "menu":

                    if not tratar_clique_menu(posicao):
                        executando = False

                elif estado == "loja":

                    tratar_clique_loja(posicao)

                elif estado == "config":

                    tratar_clique_config(posicao)

                elif estado == "game_over":

                    tratar_clique_game_over(posicao)

    # =================================
    # ATUALIZAR
    # =================================

    if estado == "jogando":

        atualizar_jogo(dt)

    elif estado == "loja":

        atualizar_mensagem_loja(dt)

    # =================================
    # DESENHAR
    # =================================

    if estado == "menu":

        desenhar_menu()

    elif estado == "jogando":

        desenhar_jogo()

    elif estado == "loja":

        desenhar_loja()

    elif estado == "config":

        desenhar_configuracoes()

    elif estado == "game_over":

        desenhar_game_over()

    # Atualizar tela
    pygame.display.flip()


# =====================================
# 6. ENCERRAR JOGO
# =====================================

salvar_dados()

pygame.quit()