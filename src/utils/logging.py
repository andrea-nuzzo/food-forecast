import logging

def setup_logging():
    # Crea un logger di livello più alto
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Imposta il livello minimo di log a DEBUG

    # Se non ci sono handler, configura il logging
    if not logger.handlers:
        # Formato per i messaggi di log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Crea un StreamHandler per stampare i log nel terminale
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.DEBUG)  # Imposta il livello per il terminale

        # Aggiungi il StreamHandler al logger
        logger.addHandler(stream_handler)

    # # Crea un FileHandler per scrivere i log in un file
    # file_handler = logging.FileHandler('app.log')
    # file_handler.setFormatter(formatter)
    # file_handler.setLevel(logging.WARNING)  # Imposta un livello di log più alto per il file

    # # Aggiungi il FileHandler al logger
    # logger.addHandler(file_handler)