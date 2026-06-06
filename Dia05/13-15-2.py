import logger
import time

print("Iniciando o programa...")
logger.registrar_log("Programa iniciado.")

logger.registrar_log("Iniciando a tarefa importante...")
# Simula um trabalho demorado
time.sleep(2) # Pausa por 2 segundos
print("Realizando tarefa...")
logger.registrar_log("Tarefa importante concluída com sucesso.")

logger.registrar_log("Programa finalizado.")
print("Programa finalizado. Verifique o arquivo 'log.txt'.")