'''
DIRECTIONS
==========

1. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    [ "Sally", [ "lollipop", "bubble gum", "laffy taffy" ]],
    [ "Bob", [ "milky way", "licorice", "lollipop" ]],
	[ "Arlene", [ "chocolate bar", "milky way", "laffy taffy" ]],
	[ "Carlie", [ "nerds", "sour patch kids", "laffy taffy" ]]
]

2. In `get_friends_who_like_specific_candy()`, return friends who like lollipops.

3. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

4. Write tests for all of the functions in this exercise.

'''


def create_new_candy_data_structure(data):
    candy_favoriters = {}
    for friend in data:
        for candy in friend[1]:
            if candy in candy_favoriters:
                candy_favoriters[candy].append(friend[0])
            else:
                candy_favoriters[candy] = [friend[0]]
    print("candies!", candy_favoriters)
    return candy_favoriters

friend_favorites = [
    [ "Sally", [ "lollipop", "bubble gum", "laffy taffy" ]],
    [ "Bob", [ "milky way", "licorice", "lollipop" ]],
	[ "Arlene", [ "chocolate bar", "milky way", "laffy taffy" ]],
	[ "Carlie", [ "nerds", "sour patch kids", "laffy taffy" ]]
]

create_new_candy_data_structure(friend_favorites)

def get_friends_who_like_specific_candy(data, candy_name):
    pass


def create_candy_set(data):
    pass 
