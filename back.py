import kivy
kivy.require('2.0.0') # Substitua pela sua versão do Kivy
# Imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import pandas as pd
import openpyxl
import sys
import time
pd.read_excel('paises_pro.xlsx')
pd.read_excel('paises.xlsx')
class PaisGenerator(App):
    def build(self):
        self.paises = self.carregar_dados('paises.xlsx')
        self.paises_pro = self.carregar_dados('paises_pro.xlsx')
        self.dados_paises = {
            'brasil': {'nome': 'Brasil', 'pib': "2,174 trilhões USD (2023)", 'surgiuem': '1500', 'populacao': '212,6 milhões de habitantes (2024)'},
            'usa': {'nome': 'Estados Unidos', 'pib': '27,72 trilhões USD (2023)', 'surgiuem': 'Surgiu em 1776', 'populacao': '340,1 milhões de habitantes (2024)'},
            'estados unidos': {'nome': 'Estados Unidos', 'pib': '27,72 trilhões USD (2023)', 'surgiuem': 'Surgiu em 1776', 'populacao': '340,1 milhões de habitantes (2024)'},
            'estadosunidos': {'nome': 'Estados Unidos', 'pib': '27,72 trilhões USD (2023)', 'surgiuem': 'Surgiu em 1776', 'populacao': '340,1 milhões de habitantes (2024)'},
            'estados-unidos': {'nome': 'Estados Unidos', 'pib': '27,72 trilhões USD (2023)', 'surgiuem': 'Surgiu em 1776', 'populacao': '340,1 milhões de habitantes (2024)'}
        }
        self.tokens = ['MigRDEV', 'Joao', 'a2r@#HsDj9kY354fBFSacs']
        self.internet = ['Joao']
        self.tokens_o = [token for token in self.tokens if token not in self.internet]

        self.layout = BoxLayout(orientation='vertical', padding=10)

        self.label_intro = Label(text="Bem Vindo ao Gerador de Países!\nComplete as informações e terá seu país criado! \nFeito por: MigRDEV -- Contato: Discord")
        self.layout.add_widget(self.label_intro)

        self.button_pro = Button(text="Ativar PRO+")
        self.button_pro.bind(on_press=self.ativar_pro)
        self.layout.add_widget(self.button_pro)

        self.button_gerar = Button(text="Gerar País")
        self.button_gerar.bind(on_press=self.gerar_pais)
        self.layout.add_widget(self.button_gerar)

        self.button_pesquisar = Button(text="Pesquisar País")
        self.button_pesquisar.bind(on_press=self.pesquisar_pais)
        self.layout.add_widget(self.button_pesquisar)

        return self.layout

    def carregar_dados(self, excel):
        try:
            return pd.read_excel('paises_pro.xlsx')
        except FileNotFoundError:
            return pd.DataFrame(columns=['Nome Do Pais', 'Descricao', 'PIB', 'Estados 1', 'Estados 2', 'Estados 3', 'Estados 4', 'Estados 5', 'Surgiu Em'])

    def ativar_pro(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Digite o token:"))
        self.token_input = TextInput(multiline=False)
        self.layout.add_widget(self.token_input)
        self.layout.add_widget(Button(text="Confirmar", on_press=self.confirmar_token))

    def confirmar_token(self, instance):
        
        token = self.token_input.text
        if token in self.tokens_o:
            self.layout.clear_widgets()
            self.layout.add_widget(Label(text="PRO+ ativado!"))
            self.layout.add_widget(Button(text="Criar País PRO+", on_press=self.criar_pais_pro))
        else:
            self.layout.clear_widgets()
            self.layout.add_widget(Label(text=f"O token {token} não foi encontrado!"))

    def criar_pais_pro(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Digite o nome do país:"))
        self.nome_input = TextInput(multiline=False)
        self.layout.add_widget(self.nome_input)

        self.layout.add_widget(Label(text="Digite a descrição do país:"))
        self.descricao_input = TextInput(multiline=False)
        self.layout.add_widget(self.descricao_input)

        self.layout.add_widget(Label(text='Qual o PIB (Produto interno bruto) do seu país: '))
        self.pib_input = (TextInput(multiline=False))
        self.layout.add_widget(self.pib_input)

        self.layout.add_widget(Label(text='Qual o número de Soldados em seu país: '))
        self.soldados_input = TextInput(multiline=False)
        self.layout.add_widget(self.soldados_input)
        self.layout.add_widget(Button(text='Continuar',on_press=self.estados_pro))


    def estados_pro(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='Qual o primeiro estado em seu país: '))
        self.estado1_input = TextInput(multiline=False)
        self.layout.add_widget(self.estado1_input)

        self.layout.add_widget(Label(text='Qual o segundo estado em seu país: '))
        self.estado2_input = TextInput(multiline=False)
        self.layout.add_widget(self.estado2_input)

        self.layout.add_widget(Label(text='Qual o terceiro estado em seu país: '))
        self.estado3_input = TextInput(multiline=False)
        self.layout.add_widget(self.estado3_input)

        self.layout.add_widget(Label(text='Qual o quarto estado em seu país: '))
        self.estado4_input = TextInput(multiline=False)
        self.layout.add_widget(self.estado4_input)

        self.layout.add_widget(Label(text='Qual o quinto(último) estado em seu país: '))
        self.estado5_input = TextInput(multiline=False)
        self.layout.add_widget(self.estado5_input)
            # Adicione outros campos de entrada para os dados do país

        self.layout.add_widget(Button(text="Continuar", on_press=self.confirmar_criar_pais_pro))
    def confirmar_criar_pais_pro(self, instance):
        self.layout.clear_widgets()
        nome_pais = self.nome_input.text
        self.layout.add_widget(Label(text=f'Deseja criar o país {nome_pais}?'))
        criarpaiss = self.layout.add_widget(Button(text='SIM',on_press=self.salvar_pais_pro))
        criarpaisn = self.layout.add_widget(Button(text='Não',on_press=self.erro404))
    def erro404(self, instance):
        self.layout.clear_widgets()
        nome_pais = self.nome_input.text
        self.layout.add_widget(Label(text=f'O País {nome_pais} não foi criado! -- Tente Novamente!'))
        self.layout.add_widget(Label(text=f'Deseja ver o país {nome_pais}!'))
        
        self.layout.add_widget(Label(text=f'Se Deseja criar ele, tente novamente!'))
    def salvar_pais_pro(self, instance):

        nome_pais = self.nome_input.text

        descricao = self.descricao_input.text
        pib = self.pib_input.text
        estados=[]
        estado1=self.estado1_input.text
        estado2=self.estado2_input.text
        estado3=self.estado3_input.text
        estado4=self.estado4_input.text
        estado5=self.estado5_input.text
        # Obtenha os outros dados dos campos de entrada
        # ...
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=f"País {nome_pais} criado com sucesso!"))
        self.layout.add_widget(Label(text=f'Deseja ver o país {nome_pais}?:'))
        self.layout.add_widget(Button(text=f'Sim',on_press=self.ver_pais_info))
        self.layout.add_widget(Button(text=f'Não',on_press=sys.exit()))
        dados_pro={
            'Descrição': [descricao],
            'PIB':[pib],
            'Estado 1':[estado1],
            'Estado 2':[estado2],
            'Estado 3':[estado3],
            'Estado 4':[estado4],
            'Estado 5':[estado5],
        }
        df_df = pd.DataFrame(dados_pro)

        try:
            # Tenta ler o arquivo Excel existente
            df_existente = pd.read_excel('paises_pro.xlsx')
            df = pd.concat([df_existente, df_df], ignore_index=True)
            
        except FileNotFoundError:
            # Se o arquivo não existir, cria um DataFrame vazio com as colunas desejadas
            colunas = ['Nome', 'Descrição', 'PIB','N-Soldados','Estado 1','Estado 2','Estado 3','Estado 4','Estado 5']  # Adicione outras colunas, se necessário
            df = pd.DataFrame(columns=colunas)
            df = pd.concat([df, df_df], ignore_index=True)
              # Se o arquivo não existir, cria um novo
        df.to_excel('paises_pro.xlsx', index=False)
        
        # ...


    def ver_pais_pro(self, instance):
        self.layout.clear_widgets()
        nome_pais = self.nome_input
        self.layout.add_widget(Label(f'Deseja ver seu país {nome_pais}?'))
        self.layout.add_widget(Button("Sim", on_press=self.ver_pais_info))
        self.layout.add_widget(Button('Não'))
    def ver_pais_info(self , instance):
        self.layout.clear_widgets()
        nome_pais = self.nome_input
        self.layout.add_widget(Label(f"O nome do seu País é {nome_pais}, a descrição é {self.descricao_input}, o pib é {self.pib_input}, o primeiro estado é {self.estado1_input}, o segundo é {self.estado2_input}, o terceiro estado é {self.estado3_input}, o quarto estado é {self.estado4_input} e o quinto(último) estado é {self.estado5_input}."))
    def gerar_pais(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Digite o nome do país:"))
        self.nome_g_input = TextInput(multiline=False)
        self.layout.add_widget(self.nome_input)

        self.layout.add_widget(Label(text="Digite a descrição do país:"))
        self.descricao_g_input = TextInput(multiline=False)
        self.layout.add_widget(self.descricao_input)

        self.layout.add_widget(Label(text='Qual o PIB (Produto interno bruto) do seu país: '))
        self.pib_g_input = (TextInput(multiline=False))
        self.layout.add_widget(self.pib_input)

        self.layout.add_widget(Label(text='Qual o número de Soldados em seu país: '))
        self.soldados_g_input = TextInput(multiline=False)
        self.layout.add_widget(self.soldados_input)
        self.layout.add_widget(Button(text='Continuar',on_press=self.estados))
        # Adicione outros campos de entrada para os dados do país

        self.layout.add_widget(Button(text="Criar", on_press=self.estados))
    def estados(self,instance):
        self.estado1_input = TextInput(multiline=False)
        self.layout.add_widget(self.estado1_input)

        self.layout.add_widget(Label(text="Digite a descrição do país:"))
        self.estado2_input = TextInput(multiline=False)
        self.layout.add_widget(self.descricao_input)

        self.layout.add_widget(Label(text='Qual o PIB (Produto interno bruto) do seu país: '))
        self.pib_input = (TextInput(multiline=False))
        self.layout.add_widget(self.pib_input)

        self.layout.add_widget(Label(text='Qual o número de Soldados em seu país: '))
        self.soldados_input = TextInput(multiline=False)
        self.layout.add_widget(self.soldados_input)
        self.layout.add_widget(Button(text='Continuar',on_press=self.estados))
    def salvar_pais(self, instance):
        nome_pais = self.nome_input.text
        # Obtenha os outros dados dos campos de entrada
        # ...

        # Salve os dados no arquivo Excel
        # ...

        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=f"País {nome_pais} criado com sucesso!"))

    def pesquisar_pais(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Digite o nome do país para pesquisar:"))
        self.pesquisa_input = TextInput(multiline=False)
        self.layout.add_widget(self.pesquisa_input)
        self.layout.add_widget(Button(text="Pesquisar", on_press=self.exibir_dados_pais))

    def exibir_dados_pais(self, instance):
        nome_pais = self.pesquisa_input.text.lower()
        if nome_pais in self.dados_paises:
            dadospais_usuario = self.dados_paises[nome_pais]
            resultado = f"Nome do país: {dadospais_usuario['nome']}\nPIB: {dadospais_usuario['pib']}\nSurgiu em: {dadospais_usuario['surgiuem']}\nPopulação: {dadospais_usuario['populacao']}"
            self.layout.clear_widgets()
            self.layout.add_widget(Label(text=resultado))
        else:
            self.layout.clear_widgets()
            self.layout.add_widget(Label(text=f"O país {nome_pais} não foi encontrado!"))

if __name__ == '__main__':
    PaisGenerator().run()