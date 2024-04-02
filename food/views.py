import json

def create():
    with open('chikds.json', 'r+', encoding='utf-8') as file:
        existing_data = json.load(file)
        max_id = existing_data[0]["id"]
        for i in existing_data:
            if max_id<i['id']:
                max_id=i['id']
  
        add_name = input("Enter name:    ")
        add_bd = int(input("Enter price:    "))
        next_id = max_id+1
        new_data = {'id': next_id, 'name': add_name, 'price': add_bd}
        existing_data.append(new_data)
        file.seek(0)
        json.dump(existing_data, file, indent=4,ensure_ascii=False)


# delete

def delete():
    with open ('chikds.json', 'r',encoding='utf-8') as file:
        take_json = json.load(file)
        print(take_json)
        del_id = int(input("Which id do you want to delete?    "))

        for count,i in enumerate(take_json):
                if i['id'] == del_id:
                        del take_json[count]
                with open('chikds.json', 'w', encoding='utf-8') as outfile:
                        json.dump(take_json,outfile,ensure_ascii=False,indent=4)
        print("unkown")


# change

def change():
    with open('chikds.json', 'r', encoding='utf-8') as file:
        take_json = json.load(file)
        print(take_json)
        id_food=int(input("Select id: "))

        for count, i in enumerate(take_json):
                if i['id'] == id_food:
                        # print(take_json[count])
                        take_json[count]['name']=input("Select name    ")
                        take_json[count]['price']=input("Select price    ")
                with open ('chikds.json', 'w', encoding='utf-8') as outfile:
                        json.dump(take_json, outfile, ensure_ascii=False, indent=4 )


# list


def list():
    with open('chikds.json', 'r', encoding='utf-8') as file:
        take_json = json.load(file)
        print(take_json)
        id_food = int(input('Select id:    '))
        for count, i in enumerate(take_json):
                if i['id'] == id_food:
                        print(take_json[count])
                with open('chikds.json', 'w', encoding='utf-8') as outfile:
                        json.dump(take_json, outfile, ensure_ascii=False, indent=4)
