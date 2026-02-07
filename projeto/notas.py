def validar_nota(nota):
    if nota in range(0, 11):
        return True
    return False

def calcular_media(notas):
    medias = 0
    quantidade = 0
    if len(notas) == 0:
        raise ValueError("Lista de notas vazia")
    for nota in notas:
        medias += nota
        quantidade += 1
    
    media_final = medias/quantidade
    return media_final

def obter_situacao(media):
    if not isinstance(media, (int, float)) or media < 0 or media > 10:
        raise ValueError("Média inválida")
    
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"


def calcular_estatisticas(notas):
    if len(notas) == 0:
        raise ValueError("Lista de notas vazia")
    
    media = calcular_media(notas)
    maior = max(notas)
    menor = min(notas)
    
    aprovados = 0
    reprovados = 0
    recuperacao = 0
    
    for nota in notas:
        situacao = obter_situacao(nota)
        if situacao == "Aprovado":
            aprovados += 1
        elif situacao == "Recuperacao":
            recuperacao += 1
        else:
            reprovados += 1
    
    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "aprovados": aprovados,
        "reprovados": reprovados,
        "recuperacao": recuperacao
    }


def normalizar_notas(notas, nota_maxima=10):
    if nota_maxima <= 0:
        raise ValueError("Nota máxima deve ser maior que zero")
    
    if len(notas) == 0:
        return []
    
    notas_normalizadas = []
    for nota in notas:
        nota_normalizada = (nota / nota_maxima) * 10
        notas_normalizadas.append(nota_normalizada)
    
    return notas_normalizadas