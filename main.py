import input
import data
import sort
import search


def main():
    data.import_dataset()
    input.welcome()

    selection = input.function_selector()
    if selection == "sort":
        num = input.sort()
        ls = sort.get_top(data.get_array(), num)
        data.display_episodes(ls)
        
    elif selection == "search":
        hashmap = search.make_hashmap()
        keyword = input.search()

        ls = "0"
        while ls == "0":
            print('''

            Sorry, there were no matches. Please try another keyword.
            
            ''')
            keyword = input.search()
            ls = search.search_description(keyword, hashmap)

        data.display_episodes(ls)

if __name__ == "__main__":
    main()