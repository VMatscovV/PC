# -*- coding: utf-8 -*-
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat


chat = GigaChat(
    credentials="Y2U5YTliYzMtYjJjNy00YzNhLWJmN2YtOTZlMTNiNjFiNzliOmFmMDBkNDgyLWVjMTgtNGFlMC04Y2U5LTI3ZTYwNWUyOGNlNQ==",
    verify_ssl_certs=False)


def getatt(input):
    messages = [SystemMessage(
        content="Сгенерируй яркий и провокационный слоган для стартапа не длинее 20 слов.")]
    messages.append(HumanMessage(content=input))
    res = chat(messages)
    return (res.content)


def getmarket(input):
    messages = [SystemMessage(
        content="Рассчитай объем заданного рынка в России за 2021 год. Выведи данные в следующем формате: Страна, год, сумма")]
    messages.append(HumanMessage(content=input))
    res = chat(messages)
    return (res.content)

