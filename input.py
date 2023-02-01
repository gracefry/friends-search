def welcome():
    print('''                                                                                                                                           
                                  
          \`*-.                    
           )  _`-.                                < smelly cat >
          .  : `. .                                     
          : _   '  \               
          ; *` _.   `*-._               "The One That I Forgot the Name Of"
          `-.-'          `-.               
            ;       `       `.     
            :.       .        \          Use this tool to search and sort
            . \  .   :   .-'   .       through a dataset of Friends episodes
            '  `+.;  ;  '      :        and finally remember which one you
            :  '  |    ;       ;-.      were trying to remember the name of
            ; '   : :`-:     _.`* ;
   [bug] .*' /  .*' ; .*`- +'  `*' 
         `*-*   `*-*  `*-*'
    ''')

def function_selector():
    print('''
    This program has several functions you can choose from:
        
        1) List the top rated episodes
        2) Search for an episode using a keyword

    Please make your selection by entering the corresponding number:
    ''')

    while True:
        
        response = input("What would you like to do?: ")
    
        if response == "1":
            return "sort"
        elif response == "2":
            return "search"
        else:
            print('''
            Please enter [1] or [2].
            ''')

def search():
    print('''
    This tool will allow you search through the titles and descriptions
    of the 236 Friends episodes using a key word or phrase.

    Some suggestions: 
        [wedding] [turkey] [smelly cat] [janice]
    ''')

    keyword = input("Enter a keyword: ")

    return keyword

def sort():
    print('''
    This tool will allow you to rank the 236 Friends episodes by the iMDB star
    rating. You could look for the Top 3, Top 10, Top 100... it's up to you.
    ''')

    while True:

        num = input("How many episodes do you wish to rank?: ")

        # Check if number
        try:
            isInt = float(num).is_integer()
        except:
            print('''
            Please input a valid number.
            ''')
            continue
        
        # Check if integer
        if isInt == True:
            num = int(num)
        else:
            print('''
            Please input a valid integer between 0 and 236.
            ''')
            continue

        # Check integer size
        if num > 236:
            print('''
            You can't rank more episodes than there are in existence! 
            Choose a smaller number.
            ''')
            continue
        elif num < 0:
            print('''
            Why would you put in a negative number? Are you trying to break me?
            Choose a positive integer.
            ''')
            continue
        elif num == 0:
            print('''
            I can't rank the Top 0 episodes... please put in a larger number.
            ''')
            continue

        return num