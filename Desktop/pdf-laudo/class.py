
''' Recebe arquivo csv com genótipos de pacientes'''

class GenotiposPacientes:

   def __init__(self, gene, rsid, genotipo):
    self.gene = gene
    self.rsid = rsid
    self.genotipo = genotipo

    print("Arquivo importado com sucesso!")


class InformacoesPacientes:

    def __init__(self, dataNascimento, dataColeta, nomePaciente, protocolo):
        self.dataNascimento = dataNascimento
        self.dataColeta = dataColeta
        self.nomePaciente = nomePaciente
        self.protocolo = protocolo


class InformacoesLaudoDiet:

    def __init__(self, descricaoLonga, descricaoCurta, avisoGeral):
        self.descricaoLonga = descricaoLonga
        self.descricaoCurta = descricaoCurta
        self.avisoGeral = avisoGeral


        
