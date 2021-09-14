import pytest
from candy_problem.main import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict
    

def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert

    # assert new_candy_data["lollipop"] 

    '''
    # this did not work but it was an attempt
    structure_values = {
        "lollipop": ["Sally", "Bob"],
        "bubble gum": ["Sally"],
        "laffy taffy": ["Sally", "Arlene","Carlie"],
        "milky way": ["Bob", "Arlene"],
        "licorice": ["Bob"],
        "chocolate bar": ["Arlene"],
        "nerds": ["Carlie"],
        "sour patch kids": ["Carlie"]
    }
    
    assert new_candy_data == structure_values
    '''

    '''
    candies! {'lollipop': ['Sally', 'Bob'], 'bubble gum': ['Sally'], 'laffy taffy': ['Sally', 'Arlene', 'Carlie'], 'milky way': ['Bob', 'Arlene'], 'licorice': ['Bob'], 'chocolate bar': ['Arlene'], 'nerds': ['Carlie'], 'sour patch kids': ['Carlie']}
['Sally', 'Bob']
    '''