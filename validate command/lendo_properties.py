
fileName = "Solution.properties"
fileObj = open(fileName)
params = {}



# Lendo Arquivo
for line in fileObj:
    line = line.strip()
    key_value = line.split('=')

    # Ignorando Comentários
    if len(key_value) == 2:
        params[key_value[0]] = key_value[1]

print(params)
print(f' {params["STOP_TIME"]} e {params["ORDER_ACCUARY"]}')

# Escrevendo ------------------------------------------------

