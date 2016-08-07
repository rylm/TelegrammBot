import Library



update_id = Library.update(1)['result'][0]['update_id']
a = update_id

while 1:

    update = Library.update(-1)
    if a != update['result'][0]['update_id']:
        print(update['result'][0]['update_id'])
        if update['result'][0]['update_id'] - a != 1:
            print('loss:', update['result'][0]['update_id'] - a - 1)
        a = update['result'][0]['update_id']

    if update_id != update['result'][0]['update_id']:

        chat_id = update['result'][0]['message']['chat']['id']
        chat_id = str(chat_id)


        #start
        if update['result'][0]['message']['text'] == '/start':
            Library.send_start_message(chat_id)
            update_id = update['result'][0]['update_id']
            continue


        #help
        if update['result'][0]['message']['text'] == '/help':
            Library.send_help_message(chat_id)
            update_id = update['result'][0]['update_id']
            continue

        #get
        if update['result'][0]['message']['text'] == '/get':
            message = Library.give_text()
            Library.send(chat_id, message)
            update_id = update['result'][0]['update_id']
            continue

        Library.send(chat_id, 'Напиши мне "/get", чтобы получить анекдот!')



    #print(requests.get(url + '/getupdates?offset=-1'))
    #print(Library.update())
    #print(Library.update(1)['result'][0])
    #Library.post(chat_id, 'Hello')
    #print(update['result'][0]['message']['text'])