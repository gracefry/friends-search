# "The One That I Forgot the Name Of"
I called the repo `friends-search` though.
### Try me out on [replit]()
```
                              
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
```
## Instructions
If you really want to run it just `python main.py` from the folder you downloaded.<br>
No dependencies needing to be installed. The only thing not mine is the `csv` module.
<br>Try online with [replit]()!

## Function
The program utilises a dataset of Friends episodes and has two main functions:
1) Sorting and listing the k most highly rated episodes
2) Searching for an episode using a given string

## Methodology
I parsed the dataset with the `csv` module and created an `Episode` class to group all the data into objects.
### Sort by rating
To be updated but in short max heap with heapsort algorithm.
### Search by keyword
To be updated but in short hash map with linear search algorithm.

## Acknowledgements
My thanks to:
* Codecademy for teaching me how to write the `MaxHeap` and `HashMap` modules
* Blazej Kozlowski via [ASCII Art Archive](https://www.asciiart.eu/animals/cats) for his smelly cat art
* Mohammad Reza Ghari and Moulik Dhade via [Kaggle](https://www.kaggle.com/datasets/rezaghari/friends-series-dataset) for the Friends dataset
