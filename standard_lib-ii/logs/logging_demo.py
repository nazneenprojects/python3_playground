import logging

logging.warning('Warning:Please make sure you do not enter infinity number in the list in file %s ', 'Logging.Demo')

for i in [1,22,74,76,80,104,123,174,16]:
    if (i % 2)==0:
        logging.debug(f'Debug Info:{i}')
        logging.info('Informational message: we are going to check if number satisfies even condition')
        print("its even number!")
    else :
        print("its odd number!")

logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
