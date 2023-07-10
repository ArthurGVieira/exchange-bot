import time
import telebot
from api_request import *


class Bot(telebot.TeleBot):
    def __init__(self):
        # Token de acesso ao bot
        self.token = '6308958806:AAH-p0NBltpmxiQkmjisUz7pDMPX0jctDxQ'
        self.chat_id = None
        # Dicionário com as informações obtidas da API
        self.data = api_request()

        super().__init__(self.token)
        self.run()

    def set_chat_id(self, new_id):
        self.chat_id = new_id

    # Retorna o valor da moeda selecionada dividido pelo valor do real brasileiro, para resultar na cotação baseada
    # no real brasileiro
    def cotacao(self, moeda):
        valor = self.data['rates'][moeda]
        return round(self.data['rates']['BRL'] / valor, 2)

    # Envia uma resposta no chat do usuário informando a cotação atual de acordo com a moeda escolhida
    def resposta(self, moeda):
        self.send_message(self.chat_id, 'A cotação atual do {MOEDA} é R${VALOR}'.format(MOEDA=moeda,
                                                                                      VALOR=self.cotacao(moeda)))
        time.sleep(2)
        self.keyboard()

    # Função para lidar com o conteúdo da mensagem recebida no chat do bot
    def handle_text(self, message):
        match message.text:
            case '/start':
                self.set_chat_id(message.chat.id)
                self.keyboard()
            case 'Dólar americano':
                self.resposta('USD')
            case 'Dólar australiano':
                self.resposta('AUD')
            case 'Dólar canadense':
                self.resposta('CAD')
            case 'Zloty polonês':
                self.resposta('PLN')
            case 'Peso mexicano':
                self.resposta('MXN')
            case 'Peso argentino':
                self.resposta('ARS')

    # Cria botões interativos no chat do usuário para escolha da opção
    def keyboard(self):
        b1 = telebot.types.KeyboardButton('Dólar americano')
        b2 = telebot.types.KeyboardButton('Dólar australiano')
        b3 = telebot.types.KeyboardButton('Dólar canadense')
        b4 = telebot.types.KeyboardButton('Zloty polonês')
        b5 = telebot.types.KeyboardButton('Peso mexicano')
        b6 = telebot.types.KeyboardButton('Peso argentino')

        keyboard = telebot.types.ReplyKeyboardMarkup()
        keyboard.add(b1, b2, b3, b4, b5, b6)

        self.send_message(self.chat_id, 'Escolha uma moeda para ver sua cotação atual com base no REAL BRASILEIRO',
                          reply_markup=keyboard)

    def run(self):
        self.message_handler()(self.handle_text)
        self.infinity_polling()
