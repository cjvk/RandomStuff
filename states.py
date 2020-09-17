#!/usr/bin/python

ALL_STATES = (
    ('Alabama', 'AL'), ('Alaska', 'AK'), ('Arizona', 'AZ'), ('Arkansas', 'AR'), ('California', 'CA'),
    ('Colorado', 'CO'), ('Connecticut', 'CT'), ('Delaware', 'DE'), ('Florida', 'FL'), ('Georgia', 'GA'),
    ('Hawaii', 'HI'), ('Idaho', 'ID'), ('Illinois', 'IL'), ('Indiana', 'IN'), ('Iowa', 'IA'),
    ('Kansas', 'KS'), ('Kentucky', 'KY'), ('Louisiana', 'LA'), ('Maine', 'ME'), ('Maryland', 'MD'),
    ('Massachusetts', 'MA'), ('Michegan', 'MI'), ('Minnesota', 'MN'), ('Mississippi', 'MS'), ('Missouri', 'MO'),
    ('Montana', 'MT'), ('Nebraska', 'NE'), ('Nevada', 'NV'), ('New Hampshire', 'NH'), ('New Jersey', 'NJ'),
    ('New Mexico', 'NM'), ('New York', 'NY'), ('North Carolina', 'NC'), ('North Dakota', 'ND'), ('Ohio', 'OH'),
    ('Oklahoma', 'OK'), ('Oregon', 'OR'), ('Pennsylvania', 'PA'), ('Rhode Island', 'RI'), ('South Carolina', 'SC'),
    ('South Dakota', 'SD'), ('Tennessee', 'TN'), ('Texas', 'TX'), ('Utah', 'UT'), ('Vermont', 'VT'),
    ('Virginia', 'VA'), ('Washington', 'WA'), ('West Virginia', 'WV'), ('Wisconsin', 'WI'), ('Wyoming', 'WY'),
)

STATES_BY_NAME = {}
STATES_BY_ABBR = {}
STATES_UNGUESSED = {}

def initialize():
    for state_tuple in ALL_STATES:
        name = state_tuple[0]
        abbr = state_tuple[1]
        STATES_BY_NAME[name] = abbr
        STATES_BY_ABBR[abbr] = name
        STATES_UNGUESSED[name] = ''
    pass

def process_next_guess():
    # return True if exit is indicated
    user_input = raw_input('make a guess please (\'exit\' to exit)\n==> ')
    if user_input in STATES_BY_ABBR:
        user_input = STATES_BY_ABBR[user_input]
    if user_input in STATES_UNGUESSED:
        del STATES_UNGUESSED[user_input]
        print 'correct'
    else:
        print 'incorrect'
    return user_input == 'exit'

def is_finished():
    return len(STATES_UNGUESSED) == 0

def final_processing():
    number_correct = 50 - len(STATES_UNGUESSED)
    print('You got ' + str(number_correct) + ' correct out of 50')

def main():
    print 'hello world'
    initialize()
    while True:
        should_exit = process_next_guess()
        if should_exit or len(STATES_UNGUESSED) == 0:
            break
    final_processing()

main()
    
