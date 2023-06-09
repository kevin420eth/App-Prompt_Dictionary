import os, json, random, datetime

# Add a new word
def add_new_word():
    new_word = input('\nEnter a vocabulary: ').lower()
    if new_word in data:
        print(f"\nThe word '{new_word}' has existed")
        return
    meaning = input('\nEnter its meaning: ').lower()
    synonyms = input('\nEnter its synonyms: ').lower()

    timestamp = int(datetime.datetime.now().timestamp())

    with open(f'{root}/data/data.json', 'w', encoding='utf-8') as f:
        synonyms_list = []
        if synonyms != '':
            synonyms_list.append(synonyms)
        
        data[new_word]={
            "meaning":meaning,
            "synonyms":synonyms_list,
            "add_time":timestamp
        }
        json.dump(data, f)

# Add a new property to all words
def add_property():
    target_property = input('Enter a new property:\n').lower()
    if target_property == '':
        print("Can't be empty")
        return
    else:
        for _ in data:
            if target_property in data[_]:
                print("This property has existed")
                return
            data[_][target_property]=""
    with open(f'{root}/data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

# Delete a property from all words
def delete_property():
    target_property = input('\nEnter the property you want to delete: ').lower()
    if target_property == '':
            return
    for _ in data:
        try:
            del data[_][target_property]
        except KeyError:
            print("\nThere's no this property")
            return
        except Exception as error:
            print(error)
            return
            
    with open(f'{root}/data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

    print(f"\nProperty: {target_property} has been deleted")

# Modify the value of the property of a specific word
def modify_property_value():
    target_word = input('Enter the word you want to modify:\n').lower()
    target_property = input('Enter the property you want to modify\n').lower()
    property_value = input('Enter the value you want to modify:\n').lower()
    
    if target_word not in data or target_property not in data[target_word]:
        print('Wrong input')
        return
    else:
        data[target_word][target_property] = property_value
        with open(f'{root}/data/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
        print(f'The {target_property} of {target_word} has been changed')

# Add a new synoyms
def add_new_synonyms():
    target_word = input('Enter the word you want to modify:\n').lower()
    new_synonyms = input('Enter the value you want to add:\n').lower()
    new_synonyms = new_synonyms.replace(' ','').split(',')
    if target_word not in data:
        print(f"The word '{target_word}' doesn't exist in your database")
        return
    else:
        for _ in new_synonyms:
            data[target_word]['synonyms'].append(_)
        with open(f'{root}/data/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
    print(f'New synonymses have been added')

# Check a word
def check_word():
    target_word = input('Enter a word:\n').lower()
    try:
        for _ in data[target_word]:
            print(f'\n{_}: {data[target_word][_]}')
    except KeyError:
        print("This word doesn't exist")
    except Exception as error:
        print(error)

# Review words randomly
def random_word():
    purged_data = data
    for _ in purged_data:
        del purged_data[_]['add_time']
        
    while True:
        key = random.choice(list(purged_data))
        print(f'\n{key}')
        user_input = input('').lower()
        for _ in purged_data[key]:
            print(f'{_}: {purged_data[key][_]}\n')
        user_input = input(f'-----------------------------------').lower()
        if user_input != '':
            break

# Backup the current dictionary
def backup():
    time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    try:
        with open(f'{root}/backup/{time}.json','w', encoding='utf-8') as f:
            json.dump(data, f)
    except Exception as error:
        print('\nSomething went wrong...')
    else:
        print('\nBackup is completed')

if __name__ == "__main__":
    # Read the dictionary
    base = os.path.dirname(__file__)
    root = os.path.abspath(os.path.join(base, os.pardir))

    with open(f'{root}/data/data.json','r') as f:
        data = json.load(f)
    while True:
        print(f'\n-----------------------------------')
        command = input('\nEnter a command: ').lower()
        if command == 'new':
            add_new_word()
        elif command == 'check':
            check_word()
        elif command == 'random':
            random_word()
        elif command == 'addprop':
            add_property()
        elif command == 'delprop':
            delete_property()
        elif command == 'modprop':
            modify_property_value()
        elif command == 'addsyn':
            add_new_synonyms()
        elif command == 'backup':
            backup()
        elif command == 'exit':
            break
        else:
            print("\nThe command doesn't exist")


