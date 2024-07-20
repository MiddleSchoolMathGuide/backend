'''
Run backend
'''

import logging
import logging.config
import os
import uvicorn

from const import DEBUG_FLAG, PORT
from filter import LogFilter


def main() -> None:
    '''Run backend'''
    uvicorn.run(
        'server:app',
        host='0.0.0.0',
        port=PORT,
        reload=DEBUG_FLAG,
        log_config='config/logger.config.ini',
        reload_excludes=['*.log'],
    )


def _init_logger() -> None:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    logging.config.fileConfig('config/logger.config.ini')

    # Ignore watchfiles
    logging.getLogger('watchfiles.main').addFilter(
        LogFilter(r'^\d+ change detected: .+$')
    )
    logging.info('Logging init done')


if __name__ == '__main__':
    _init_logger()
    main()
