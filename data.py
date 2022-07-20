import uuid

import names
from random import sample
# import pandas as pd
import random
import time
import nltk
from nltk.corpus import words

nltk.download('words')

def get_andersen_family_item():
    andersen_item = {
    'id': 'Andersen_' + str(uuid.uuid4()),
    'lastName': 'Andersen',
    'district': 'WA5',
    'parents': [
        {
            'familyName': None,
            'firstName': 'Thomas'
        },
        {
            'familyName': None,
            'firstName': 'Mary Kay'
        }
    ],
    'children': None,
    'address': {
        'state': 'WA',
        'county': 'King',
        'city': 'Seattle'
    },
    'registered': True
}
    return andersen_item

def get_wakefield_family_item():
    wakefield_item = {
        'id': 'Wakefield_' + str(uuid.uuid4()),
        'lastName': 'Wakefield',
        'district': 'NY23',
        'parents': [
            {
                'familyName': 'Wakefield',
                'firstName': 'Robin'
            },
            {
                'familyName': 'Miller',
                'firstName': 'Ben'
            }
        ],
        'children': [
            {
                'familyName': 'Merriam',
                'firstName': 'Jesse',
                'gender': None,
                'grade': 8,
                'pets': [
                    {
                        'givenName': 'Goofy'
                    },
                    {
                        'givenName': 'Shadow'
                    }
                ]
            },
            {
                'familyName': 'Miller',
                'firstName': 'Lisa',
                'gender': 'female',
                'grade': 1,
                'pets': None
            }
        ],
        'address': {
            'state': 'NY',
            'county': 'Manhattan',
            'city': 'NY'
        },
        'registered': True
    }
    return wakefield_item

def get_smith_family_item():
    smith_item = {
    'id': 'Johnson_' + str(uuid.uuid4()),
    'lastName': 'Johnson',
    'district': None,
    'registered': False
    }
    return smith_item

def get_johnson_family_item():
    johnson_item = {
    'id': 'Smith_' + str(uuid.uuid4()),
    'lastName': 'Smith',
    'parents': None,
    'children': None,
    'address': {
        'state': 'WA',
        'city': 'Redmond'
    },   
    'registered': True
    }
    return johnson_item

# Entity name & Business name
def get_people_name():
    word_len = random.randint(3, 5)
    return ' '.join(sample(words.words(), word_len))

def get_ABN_numbers():
    return random.randint(10000000000,20000000000)

# Trading Name
def get_trading_name():
    word_len = random.randint(2, 4)
    return ' '.join(sample(words.words(), word_len))

def get_post_code():
    return random.randint(800, 7999)

def get_business_name():
    start = time.time()
    business_name = ""
    business_cnt = random.randint(1, 200)
    for _ in range(business_cnt):
        word_len = random.randint(1, 2)
        business_name += ' '.join(sample(words.words(), word_len))

    # print("Time took to generate business name: {}".format(time.time() - start))
    return business_name

# trading_name = get_trading_name()

# print("Trading name:", trading_name)
# print("Entity name:", get_people_name())
# print("Business name:", get_business_name())