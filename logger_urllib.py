"""Создайте сопрограмму, которая получает контент с указаных ссылок и логирует ход выполнения в 
специальный файл использую стандартную библеотеку urllib. Шаги, которые должны быть залогированы:
начало запроса к адресу Хб ответ для адреса Х получен со статусом 200. Проверте ход выполенения
программы на >3"""

import logging
import urllib.error
import urllib.request

from selenium import webdriver

logging.basicConfig(level='DEBUG', filename='my_log.log', filemode='w')
logger = logging.getLogger()


def main(name):
    try:
        raw_rsp = urllib.request.urlopen(name)
        if raw_rsp.status == 200:
            logger.debug('Connection is done!')
            browser = webdriver.Chrome()
            browser.get(name)
            return browser
    except urllib.error.HTTPError as e:
        print('Status: ', e.code)
        print('Reason: ', e.reason)
        print('Url: ', e.url)


if __name__ == '__main__':
    browser1 = main('https://google.com')
    browser2 = main('https://www.youtube.com')
    browser3 = main('https://github.com')


