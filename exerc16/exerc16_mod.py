def byteToMegabyte(byte):
    return (byte/1024)/1024

def saidaUsuario(usuario):
    if len(usuario) < 15:
        for x in range(0, (15-len(usuario))):
            usuario +=" "
        return usuario
    
    else:
        return usuario

def saidaConvert(string, num):
    strSaida = (f"{string:.2f}")
    if len(strSaida) < num:
        for x in range(0, (num-len(strSaida))):
            strSaida = " " + strSaida
        return strSaida
    
    else:
        return strSaida
    
def calcMedia(total, quantidade):
    return (total/quantidade)