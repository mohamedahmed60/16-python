
'''
def multiplication_table(start,end):
    for x in range(start,end+1):
        for y in range(1,11):
            print(f"{x} X {y} = {x*y}")
        print('-----------')
multiplication_table(5,10)

'''

'''

def count_words(self,sentence):
    word_count = len(sentence.split())
    return word_count


'''

class Game:
    def __init__(self):
        while True:
            print('''
    Welcom In Our Game
        1 : Multiplication Table Game
        2 : World Count Game
        3 : press X to exit
        ''')
            user_choice =(input('Enter Your Choice :  '))
            if user_choice =='X':
                break
            
            if int(user_choice) == 1:
                start = int(input('Enter Start: '))
                end = int(input('Enter End: '))
                self.multiplication_table(start,end)

            elif int(user_choice) == 2:
                mysentence = input('Enter Sentence: ')
                count = self.count_words(mysentence)
                print(count)
            play_again = input('press any key to play Again , N for exit :')
            if play_again == 'N':
                break

            
    def multiplication_table(self,start,end):
        for x in range(start,end+1):
            for y in range(1,11):
                print(f"{x} X {y} = {x*y}")
            print('-----------')

    def count_words(self,sentence):
        word_count = len(sentence.split())
        return word_count
    
g1 = Game()

