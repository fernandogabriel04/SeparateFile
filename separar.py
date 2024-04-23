import os
from shutil import move

DIR_SERVER = "C://Users/Gabriel/Documents/EXAMES/Separar/ParaSeparar/exame"
DIR_CLIENT_PC = "C://Users/Gabriel/Documents/EXAMES/Separado/PC"
DIR_CLIENT_SPLUS = "C://Users/Gabriel/Documents/EXAMES/Separado/sPlus/exame"

for dir in os.listdir(DIR_SERVER):
    insideDirServer = os.listdir(os.path.join(DIR_SERVER, dir))

    if len(insideDirServer) != 2:
        print(f"Erro: O diretório {DIR_SERVER}/{dir} não contém exatamente dois itens.")
        continue

    pc, sPlus = insideDirServer

    try:
        # Certifique-se de que os diretórios de destino existam
        os.makedirs(os.path.join(DIR_CLIENT_PC, dir), exist_ok=True)
        os.makedirs(os.path.join(DIR_CLIENT_SPLUS, dir), exist_ok=True)

        # Mova os arquivos
        move(os.path.join(DIR_SERVER, dir, pc), os.path.join(DIR_CLIENT_PC, dir, pc))
        move(os.path.join(DIR_SERVER, dir, sPlus), os.path.join(DIR_CLIENT_SPLUS, dir, sPlus))
        print(f"Movido com sucesso: {DIR_SERVER}/{dir}/{pc} e {DIR_SERVER}/{dir}/{sPlus}")
    except Exception as e:
        print(f"Erro ao mover: {e}")
