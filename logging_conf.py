import logging

# Configure logging
def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='csv_reader.log',
        filemode='a',
        encoding='utf-8'
        
    )
