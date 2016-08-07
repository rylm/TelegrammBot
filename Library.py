import requests

token = '227495190:AAEu9wUQ0lMFPHOQHs7BNuUA8tyDyVCm7wM'

url = 'https://api.telegram.org/bot' + token



def update(offsetkey):
    offsetkey = str(offsetkey)
    result = requests.get(url + '/getupdates?offset=' + offsetkey)

    result = result.json()

    return result


def send(id, text):

    requests.post(url + '/sendMessage?chat_id=' + id + '&text=' + text)



def give_text():

    text = open('Texts.txt', 'r')

    return text.read()



def send_start_message(id):

    send(id, 'Привет, не хочешь почитать анекдотов моего собсвтенного сочинения?')


def send_help_message(id):

    send(id, 'Я - бот, который пишет стихи\nНапиши мне "/get", чтобы получить анекдот!')