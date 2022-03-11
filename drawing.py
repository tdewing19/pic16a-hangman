# Drawing.py
# By: Arely Aguirre, Tristan Dewing

def drawing(lives):
    ''' 
      Takes in an integer and prints different
      hangman drawings depending on this value
      Arguments:
        lives: integer that determines which 
               drawing will be printed
      Returns:
          Prints hangman drawings
          Does not return anything
    '''
   
    if lives == 6:
        print('''
                ____
               |    
               |    
               |
               |
              ---''')
  
    elif lives == 5:
        print('''
                ____
               |    O
               |
               |
               |
              ---''') 
   
    elif lives == 4:
        print('''
                ____
               |    O
               |    |
               |
               |
              ---''')
        
    elif lives == 3:
        print('''
                ____
               |    O
               |   /|
               |    
               |
              ---''')
        
    elif lives == 2:
        print('''
                ___
               |   O
               |  /|\\
               |
               |
              --- 
               ''')
    
    elif lives == 1:
        print('''
                ___
               |   O
               |  /|\\
               |  /
               |
              --- 
               ''')
    
    else:
        print('''
                ___
               |   O
               |  /|\\
               |  / \\
               |
              --- 
               ''')