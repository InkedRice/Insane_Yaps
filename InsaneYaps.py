# "insane yaps" as in mad == insane, libs == yaps

import time

print(
      '\n',
      'Welcome to Insane Yaps, a fill-in-the-blank story game!'
      )

while True:
    def mad_lib1():
        place = input('\nEnter a place: ')
        person = input("Enter a person's name: ")
        verb1 = input('Enter a past-tense verb: ')
        verb2 = input('Enter another past-tense verb: ')
        noun = input('Enter a thing: ')
        adjective = input('Enter an adjective: ')
        object1 = input('Enter an object: ')
        emotion = input('Enter an emotion: ') 
        activity = input('Enter an activity: ')

        print(
            '\n',
            ('*' * 30), '\n',
            'Dear Diary, \n',
            'Today I went to', place, 'with', (person + '.'), '\n',
            'We', verb1, 'all day long.\n',
            'After that, we', verb2, 'by the', (noun + '.'), '\n',
            'Then,', person, 'found a', adjective, (object1 + '.'), '\n',
            'Overall, today made me', (emotion + '.'), '\n',
            "Can't wait to", activity, 'again!\n',
            ('*' * 30), '\n' 
        )
     


    def mad_lib2():
        person1 = input("\nEnter a person's name: ")
        person2 = input("Enter a second person's name: ")
        creature = input('Enter a creature: ')
        place = input('Enter a place: ')
        action_verb1 = input('Enter an action verb, (-ing): ') #fixme, change var name to verb_ed
        action_verb2 = input('Enter another action verb: ')
        prof_title = input('Enter a professional title: ')
        action_verb3 = input('Enter an action verb (-ed): ') #fixme, change var name to verb_ed
        emotion = input('Enter an emotion: ')
        verb1 = input('Enter a verb: ')
        verb2 = input('Enter another verb: ')
        direction = input('Enter a direction: ')
        adjective = input('Enter an adjective: ')
        thing = input('Enter a thing: ')
        adjective2 = input('Enter another adjective: ')
        adverb = input('Enter an adverb: ')
        action_verb4 = input('Enter another action verb (-ed): ')
        

        print(
            '\n',
            ('*' * 30), '\n',
            person1, 'and', person2, 'had barely managed to escape the', (creature + '.'), '\n',
            'Now, they were headed to the', (place + '.'), '\n',
            'With the money they made from', action_verb1, 'they planned to', (action_verb2 + '.'), '\n',
            'By the time they made it to the', (place + ','), 'the', prof_title, 'had already', (action_verb3 + '.'), '\n',
            person1, 'and', person2, 'were', emotion, "and didn't know whether to", verb1, 'or', (verb2 + '!'), '\n',
            'Ultimately, they decided to', verb1, 'and headed', direction + '.', '\n',
            'On their journey, they came across a', adjective, thing, 'and made it their lunch.\n',
            'It tasted', adjective2, 'but went down', (adverb + '.'), '\n',
            "With their bellies full,", person1, 'and', person2, action_verb4, 'into the sunset...\n',
            '...knowing their adventure had just begun.\n',
            ('*' * 30), '\n'
        )

    user_select = input('\n'
                        'Please select from the following:\n'
                        '1) Dear Diary...\n'
                        "2) Adventurer's Tale\n"
                        '3) QUIT\n\n'
                        '>>> ')
    if user_select == '1':
        mad_lib1()    
    elif user_select == '2':
        mad_lib2()    
    elif user_select == '3':
        print(
            'Thanks for playing!\n'
            'These stories were written by Inkyrice & Lizard :)\n\n'
            'This window will close automatically in 3..2..1..'
            )
        time.sleep(5)
        break
    
    play_again = input('Play again? Y/N: ').upper()
    if play_again == 'N':
        print(
            'Thanks for playing!\n'
            'These stories were written by Inkyrice & Lizard :)\n\n'
            'This window will close automatically in 3..2..1..'
            )
        time.sleep(5)
        break
  
    


    