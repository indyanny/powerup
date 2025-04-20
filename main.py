import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(1)

def acessar_site(url):
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(3)

def esperar_e_clicar(imagem, timeout=10):
    """
    Espera a imagem aparecer na tela e clica nela.
    """
    inicio = time.time()
    while time.time() - inicio < timeout:
        posicao = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
        if posicao:
            pyautogui.click(posicao)
            return True
        time.sleep(0.5)
    raise Exception(f"Imagem '{imagem}' não encontrada na tela.")

def fazer_login(email, senha):
    esperar_e_clicar('campo_email.png')
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

def cadastrar_produtos(tabela):
    for _, produto in tabela.iterrows():
        print(f"Cadastrando produto: {produto['codigo']}")
        esperar_e_clicar('campo_codigo.png')

        pyautogui.write(str(produto["codigo"])); pyautogui.press("tab")
        pyautogui.write(str(produto["marca"])); pyautogui.press("tab")
        pyautogui.write(str(produto["tipo"])); pyautogui.press("tab")
        pyautogui.write(str(produto["categoria"])); pyautogui.press("tab")
        pyautogui.write(str(produto["preco_unitario"])); pyautogui.press("tab")
        pyautogui.write(str(produto["custo"])); pyautogui.press("tab")

        obs = str(produto["obs"]).strip()
        if obs.lower() != "nan":
            pyautogui.write(obs)
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)

def main():
    email = "seu email"
    senha = "sua senha"
    url = "url desejado"

    abrir_navegador()
    acessar_site(url)
    fazer_login(email, senha)

    try:
        tabela = pd.read_csv("produtos.csv")
        print("Tabela carregada com sucesso!")
        cadastrar_produtos(tabela)
    except FileNotFoundError:
        print("Erro: Arquivo 'produtos.csv' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
