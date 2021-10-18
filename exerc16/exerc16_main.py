'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço
em disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários e
identificar os usuários com maior espaço ocupado. Através de um programa, baixado
da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
'''
from exerc16_mod import *

def main():
    #Definindo variáveis
    usuarioAtual = str("") #Dados voláteis
    bytesAtual = int(0) #Dados voláteis
    nomeDoArquivo = "relatorio"
    
    espacoTotal = int(0)
    espacoMedio = int(0)
    
    #Definindo listas/tuplas
    usuarios = []
    espacoUsuarios = []
    
   
    #Recebendo entradas
    usuarioAtual = str(input("Usuário: "))

    #Processando dados
    while usuarioAtual != "":
        bytesAtual = int(input(f"Espaço utilizado pelo {usuarioAtual}: "))
        usuarios.append(usuarioAtual)
        espacoUsuarios.append(bytesAtual)
        espacoTotal += bytesAtual
        
        print("Cadastrando novo usuario, para cancelar de ENTER")
        usuarioAtual = str(input("Usuário: "))
        
    
    #Gerando arquivo de saída
    with open(f'{nomeDoArquivo}.txt', 'w') as saida:
        saida.write(f"ACME Inc.     Uso do espaco em disco pelos  usuarios")
        saida.write(f"\n----------------------------------------------------")
        saida.write(f"\nNr.     Usuario         Espaco utilizado    % do uso")
        saida.write(f"\n----------------------------------------------------")
        
        #Gerando linha para cada usuário
        for pos, usuario in enumerate(usuarios):
            num = pos + 1
            saidaUser = saidaUsuario(usuario)
            espacoUtilizado = byteToMegabyte(espacoUsuarios[pos])
            saidaSpace = saidaConvert(espacoUtilizado, 14)
            percentUso = (espacoUtilizado * 100)/byteToMegabyte(espacoTotal)
            saidaPercent = saidaConvert(percentUso, 9)
            
            saida.write(f"\n{num:03}     {saidaUser} {saidaSpace}MB  {saidaPercent}%")
        
        saida.write(f"\n----------------------------------------------------\n")
        espacoTotalMB = byteToMegabyte(espacoTotal)
        espacoMedio = calcMedia(espacoTotal, len(espacoUsuarios))
        espacoMedioMB = byteToMegabyte(espacoMedio)
        saida.write(f"\nEspaco total ocupado: {espacoTotalMB:.2f} MB")
        saida.write(f"\nEspaco medio ocupado: {espacoMedioMB:.2f} MB")

if __name__ == "__main__":
    main()