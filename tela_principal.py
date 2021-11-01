import PySimpleGUI as sg
from logica_gerador import Logica


class TelaPython:
    logica = Logica()
    def __init__(self):
        sg.change_look_and_feel('Dark')
        # layout
        layout = [

            [sg.Text('Nome',size=(15, 0))],
            [sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Local de Origem')],
            [sg.FileBrowse('Origem',file_types=(('Excel', '*.xlsx'),))],
            [sg.Text('Local de destino: ')],
            [sg.FolderBrowse('Destino')],
            [sg.Button('Gerar'),  sg.Cancel('Cancelar')],
            [sg.Output(key='campo',size=(50, 10))],
            [sg.Text('Desenvolvido por Felipe Santos de Santana', size=(0,0))]

        ]


        # janela


        self.janela = sg.Window("Gerador de Relatorio").layout(layout)
        # Extrair os dados da tela
        self.button, self.values = self.janela.Read()
        #Laço de validacao para os botões
        while True:
            event, values = self.janela.Read()
            if event == 'Cancelar':
                break
            elif event == sg.WIN_CLOSED:
                break
            if event == 'Gerar':
                self.logica.logica(values['nome'], values['Origem'], values['Destino'])

        self.janela.close()



Tela = TelaPython()
Tela.Iniciar()