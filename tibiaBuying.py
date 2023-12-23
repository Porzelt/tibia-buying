import pyautogui
from time import sleep


# Função para rolar o scroll
def scrolldown():
    for i in range(7):
        pyautogui.scroll(-1)
        sleep(0.5)


# Esta função aciona uma hotkey do jogo com texto, para falar com o NPC e
# efetua os cliques nos locais corretos para realizar a compra dos itens (
# Stone Skin Amulet).
def buyssa():
    for i in range(2):
        pyautogui.press('f12')
        sleep(1)
    pyautogui.moveTo(1819, 641)
    scrolldown()
    pyautogui.leftClick()
    pyautogui.moveTo(1852, 692)
    pyautogui.leftClick()
    pyautogui.moveTo(1889, 731)
    for i in range(5):
        pyautogui.leftClick()
        sleep(2)


# Esta função também realiza a compra de itens no NPC (Brown Mushroom).
def buymush():
    for i in range(2):
        pyautogui.press('f12')
        sleep(1)
    pyautogui.moveTo(1819, 534)
    pyautogui.leftClick()
    pyautogui.moveTo(1852, 692)
    pyautogui.leftClick()
    pyautogui.moveTo(1889, 731)
    for i in range(2):
        pyautogui.leftClick()
        sleep(2)


# Esta função efetua cliques no mapa do jogo para movimentar o personagem até
# o depot (estoque).
def movetodepot():
    pyautogui.moveTo(1853, 16)
    pyautogui.leftClick()
    pyautogui.moveTo(841, 451)
    sleep(18)
    pyautogui.rightClick()
    pyautogui.moveTo(1816, 77)
    pyautogui.leftClick()
    pyautogui.moveTo(966, 437)
    sleep(6)
    pyautogui.rightClick()


# Esta função faz com que os mushroons sejam depositados no depot.
def dropmush():
    openclosebp()
    pyautogui.moveTo(1775, 523)
    pyautogui.keyDown('ctrl')
    pyautogui.click(button='right')
    pyautogui.keyUp('ctrl')
    sleep(0.5)
    pyautogui.moveTo(1640, 709)
    pyautogui.leftClick()
    sleep(0.5)
    openclosebp()


# Função criada para abrir e fechar a mochila do personagem
def openclosebp():
    pyautogui.moveTo(1838, 147)
    pyautogui.rightClick()


# Esta função realiza a sequência de ações para a criação de uma oferta de
# venda do item SSA na casa de leilões.
def sellssa():
    pyautogui.moveTo(1769, 457)
    pyautogui.rightClick()
    sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.click(button='right')
    pyautogui.keyUp('ctrl')
    sleep(0.5)
    pyautogui.moveTo(1662, 589)
    pyautogui.leftClick()
    pyautogui.moveTo(1013, 721)
    pyautogui.leftClick()
    pyautogui.typewrite("5980")
    pyautogui.moveTo(1091, 701)
    pyautogui.leftClick()
    pyautogui.moveTo(1188, 745)
    pyautogui.leftClick()
    pyautogui.moveTo(1298, 744)
    pyautogui.leftClick()
    pyautogui.moveTo(1275, 787)
    pyautogui.leftClick()


# Esta função arrasta a mochila de volta para o personagem.
def dragbpback():
    pyautogui.moveTo(1885, 427)
    pyautogui.leftClick()
    pyautogui.moveTo(1767, 455)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1838, 147)
    pyautogui.mouseUp(button='left')


# Esta função arrasta a mochila do personagem para o depot.
def dragbptodepot():
    pyautogui.moveTo(1769, 457)
    pyautogui.rightClick()
    sleep(0.5)
    pyautogui.rightClick()
    pyautogui.moveTo(1838, 147)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1770, 453)
    pyautogui.mouseUp(button='left')


# Esta função leva o personagem até o vendedor.
def movetoseller():
    pyautogui.moveTo(1796, 38)
    pyautogui.leftClick()
    sleep(6)
    pyautogui.moveTo(1756, 109)
    pyautogui.leftClick()
    sleep(18)


# Esta função executa a sequência de ações completa de compra do item SSA,
# venda na casa de leilões e retorno ao NPC para recomeçar o ciclo. O
# parâmetro (laps) significa a quantidade de ciclos completos a serem
# realizados.
def startssa(laps):
    for i in range(laps):
        print(f"Volta {i + 1}/{laps}")
        buyssa()
        movetodepot()
        dragbptodepot()
        sellssa()
        dragbpback()
        movetoseller()



# Esta função executa a sequência completa de ações de compra do item
# Mushroom, deposito no depot e retorno ao NPC para recomeço do ciclo. O
# parâmetro (laps) diz respeito à quantidade de ciclos completos a serem
# realizados.
def startmush(laps):
    for i in range(laps):
        print(f"Volta {i + 1}/{laps}")
        buymush()
        movetodepot()
        dropmush()
        movetoseller()



sleep(3)
startssa(3)
