import json
def opening():
    with open('smth.json', 'r', encoding='utf-8') as date:
        file = json.load(date)
    return file


def add(key, value):
    with open('smth.json', 'r', encoding='utf-8') as data:
        file_ch = json.load(data)
    file_ch[key] = value
    with open('smth.json', 'w', encoding='utf-8') as data:
        json.dump(file_ch, data, ensure_ascii=False)


def delete(key):
    with open('smth.json', 'r', encoding='utf-8') as data:
        file_ch = json.load(data)
    del file_ch[key]
    with open('smth.json', 'w', encoding='utf-8') as data:
        json.dump(file_ch, data, ensure_ascii=False)
