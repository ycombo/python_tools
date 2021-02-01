import logging
logging.basicConfig(
    filename='/tmp/application.log',
    level=logging.WARNING,
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.error("Some serious error occurred.")
logging.warning('Function you are using is deprecated.')
