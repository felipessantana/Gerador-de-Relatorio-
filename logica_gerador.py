import pandas as pd
import datetime

class Logica:
    def logica(self,nome,origem,destino):
        # data = pd.read_excel('./Acesso.xlsx', dtype=str)
        data = pd.read_excel(origem, dtype=str)
        df = pd.DataFrame(data)
        count = 0

        for index, row in df.iterrows():
            # Formatando o campo de horario de acesso
            date_time_obj = datetime.datetime.strptime(row["dthr_acesso"], '%Y-%m-%d %H:%M:%S.%f').strftime(
                '%d/%m/%y %H:%M:%S')
            print(date_time_obj)
            # Df seria data frame, este caso ele vai percorrer a coluna dthr e transformar em string e passar para a variavel data_time_obj
            df.at[count, 'dthr_acesso'] = str(date_time_obj)
            count += 1
        print('Operação Concluida')
        # Apagando as colunas
        excel = df.drop(["idacesso", "idacesso_log", "idpessoa", "tipo_veiculo", "idevento", "extra", "documento"],
                        axis=1)
        # Renomendo o titulo das colunas
        mapping = excel.rename({'codigo_lido': 'Codigo', 'nome_variavel': 'Mensagem',
                                'dthr_acesso': 'Horario de Acesso', 'idacesso_tipo': 'Tipo de Acesso',
                                'idsetor': 'Descricao do Portao',
                                'iddispositivo': 'Dispositivo', 'nome_evento': 'Nome do Evento',
                                'nome_pessoa': 'Nome da Pessoa'
                                }, axis=1)
        # Organizando as colunas
        excel1 = mapping[
            ['Descricao do Portao', 'Dispositivo', 'Tipo de Acesso', 'Codigo', 'Horario de Acesso', 'Mensagem',
             'Nome do Evento', 'Nome da Pessoa']]

        # Exportando o arquivo tratado para excel
        excel1.to_excel(""+destino+"/"+nome+".xlsx")