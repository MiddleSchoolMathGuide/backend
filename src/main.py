'''
Run backend
'''

import logging
import logging.config
import os
import uvicorn

from utils.const import DEBUG_FLAG, PORT

from db.src import init


def main() -> None:
    '''Run backend'''
    init.init()
    uvicorn.run("server:app", host="0.0.0.0", port=PORT,
                reload=DEBUG_FLAG, log_config='config/logger.config.ini')


def _init_logger() -> None:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    logging.config.fileConfig('config/logger.config.ini')
    logging.info('Logging init done')


if __name__ == '__main__':
    _init_logger()
    main()
