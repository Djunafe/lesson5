"""Создайте сопрограмму, которая получает контент с указаных ссылок и логирует ход выполнения в 
специальный файл использую стандартную библеотеку aiohttp. Шаги, которые должны быть залогированы:
начало запроса к адресу Хб ответ для адреса Х получен со статусом 200. Проверте ход выполенения
программы на >3"""

import logging
import asyncio
import aiohttp
from selenium import webdriver


logging.basicConfig(level=0, filename='my_log2.log', filemode='w')
logger = logging.getLogger()


async def url_status(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                logger.debug('Connection is done!')
                browser = webdriver.Chrome()
                browser.get(url)
                return browser

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    browser1 = loop.run_until_complete(url_status('https://google.com'))
    browser2 = loop.run_until_complete(url_status('https://www.youtube.com'))
    browser3 = loop.run_until_complete(url_status('https://github.com'))
