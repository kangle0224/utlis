#!/usr/bin/env python
#coding:utf-8

import logging
def get_logger(name, path, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    fh = logging.FileHandler(path)
    fh.setLevel(level)

    formatter = logging.Formatter('%(asctime)s   %(name)s   %(levelname)s   [file: %(filename)s] \
       [line: %(lineno)d]   [msg: %(message)s]')

    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

if __name__ == '__main__':
    a = get_logger('test', r'd:\\test.log', 10)
    a.info('this is a test!')
