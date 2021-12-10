import random
import json

def generate_marks():
    with open('MOCK_DATA.json') as json_file:
        mock_data = json.load(json_file)
        for data in mock_data:
            data['mark_tia'] = generate_mark()
            data['mark_sist'] = generate_mark()
            data['mark_mining'] = generate_mark()
    with open('MOCK_DATA_MARKS.json', 'w') as outfile:
        json.dump(mock_data, outfile)


def generate_mark():
    threshold = random.randint(1,10)
    if threshold > 4:
        mark_100 = random.randrange(0,1000,5)
        if mark_100 == 0:
            return "0"
        else:
            return str(mark_100/100)
    elif threshold==1 or threshold==2:
        return None
    elif threshold==3 or threshold==4:
        return "NP"
        
if __name__ == '__main__':
    generate_marks()

