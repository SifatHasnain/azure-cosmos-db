import uuid

import names
from random import sample
import pandas as pd
import random
import time

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

def get_people_name():
    return names.get_full_name()

def get_ABN_numbers():
    return random.randint(10000000000,20000000000)
