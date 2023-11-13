import logging

logging.basicConfig(
    filename="Python Projects/Logging Warning/Arnab.txt",
    filemode='a',
    format='%(asctime)s %(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

for i in range(15):
    try:
        i /= 0
    except Exception as e:
        logging.error(e)
    # if i % 2 == 0:
    #     logging.warning("Log Warning Message")
    # elif i % 3 == 0:
    #     logging.critical("Log Critical Message")
    # else:
    #     logging.error("Log Error Message")











