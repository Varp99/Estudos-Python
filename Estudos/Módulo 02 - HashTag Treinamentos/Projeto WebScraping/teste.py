#Importa o Webdriver que é o que usamos para criar o navegador
from selenium import webdriver   
from selenium.webdriver.common.by import By 

#Abrir em tela cheia
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
#Cria o seu navegador e abre em tela cheia para ser controlado pelo Selenium
navegador = webdriver.Chrome(options=options)
#Permite abrir uma página específica do navegador
navegador.get("https://www.hashtagtreinamentos.com/")

#Localiza os elementos pelo ID e armazena numa variavel (pegar o ID usando o inspecionar elemento na página)
campo_nome = navegador.find_element(By.ID, 'firstname')
campo_nome.send_keys("Vinicius")

campo_email = navegador.find_element(By.ID, 'email')
campo_email.send_keys("vini.arpini99@hotmail.com")

botao_enviar = navegador.find_element(By.ID, '')