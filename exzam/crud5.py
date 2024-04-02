import json
class Test:
    def add_test(self):
        with open('check.json', encoding='utf8') as f:
            lst = json.load(f)
        name = input('дайте название теста:')
        g = {
      "id": len(lst['tests'])+1,
      "name": name,
      "questions": []
    }
        lst['tests'].append(g)
        with open('check.json', 'w', encoding='utf8') as aut:
            json.dump(lst, aut, ensure_ascii=False,indent=2)
    def add_q(self):
        with open('check.json', encoding='utf8') as f:
            lst = json.load(f)
        for item in lst['tests']:print(item['id'],item['name'])
        test = int(input('выбирите тест для дополнении:'))
        question  = input('вопрос:')
        a = input('a)variant:')
        b = input('b)variant:')
        c = input('c)variant:')
        variants = [a,b,c]
        otvet = input('otvet:')
        question = {
          "id": len(lst['tests'][test-1]['questions'])+1,
          "q": question,
          "variants": variants,
          "asnwer": otvet,
          "is_correct":None
        }
        lst['tests'][test-1]['questions'].append(question)
        with open('check.json', 'w', encoding='utf8') as aut:
            json.dump(lst, aut, ensure_ascii=False,indent=2)
    def del_q(self):
        with open('check.json', encoding='utf8') as f:
            lst = json.load(f)
        for item in lst['tests']:print(item['id'],item['name'])
        test = int(input('выбирите тест для удалении:'))
        del lst['tests'][test-1]
        with open('check.json', 'w', encoding='utf8') as aut:
            json.dump(lst, aut, ensure_ascii=False,indent=2)
    def look(self):
        with open('check.json', encoding='utf8') as f:
            lst = json.load(f)
        for item in lst['tests']:print(item['id'],item['name'])
        test = int(input('выбирите тест для просмотра:'))
        for item in lst['tests'][test-1]['questions']:
            print('вопрос:',item['q'])
            print('варианты:',item['variants'])
            print('-------------------------------------------')
        print('это все)')
    def tests(self):
        with open('check.json', encoding='utf8') as f:
            lst = json.load(f)
        for item in lst['tests']:print(item['id'],item['name'])
        test = int(input('выбирите тест для прохождения:'))
        for item in lst['tests'][test-1]['questions']:
            print('вопрос:',item['q'])
            for bitem in item['variants']:
                print(str(item['variants'].index(bitem)+1)+')',bitem)
            otvet = int(input('ответ:'))
            print('-------------------------------------------')
            if item['variants'][otvet-1] == item['asnwer']:
                item['is_correct'] = True
        len_otvet = 0
        for item in lst['tests'][test-1]['questions']:
            if item['is_correct'] == True:
                len_otvet += 1
        print('кол правильных:', len_otvet)
a = Test()
while True:
    print("WElCOME to test!!!")
    d = int(input('1)пройти тест2)добавить тест 3)добавить вапрос 4)удалить тест 5)осмотр 6)exit')) 
    if d == 1:
        a.tests()
    elif d == 2:
        a.add_test()
    elif d == 3:
        a.add_q()
    elif d == 4:
        a.del_q()
    elif d == 5:
        a.look()
    elif d == 6:
        break