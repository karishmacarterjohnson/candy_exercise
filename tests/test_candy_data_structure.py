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
        [ "Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8
    assert new_candy_data["lollipop"] == ["Sally", "Bob"]
    # assert new_candy_data["lollipop"] 

def test_invalid_candy_name():
    # Arrange
    friend_favorites = [
        [ "Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    candy_name = "peeps"

    # Act
    candy_friends = get_friends_who_like_specific_candy(friend_favorites, candy_name)

    # Assert
    assert candy_friends == None

def test_valid_candy_name():
    friend_favorites = [
        [ "Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    candy_name = "nerds"

    # Act
    candy_friends = get_friends_who_like_specific_candy(friend_favorites, candy_name)

    # Assert
    assert candy_friends == ["Carlie"]

def test_set_of_candies():
    friend_favorites = [
        [ "Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    
    list_candies = create_candy_set(friend_favorites)


    assert type(list_candies) == set
    assert list_candies == set(["lollipop","bubble gum", "laffy taffy","milky way","licorice",\
        "chocolate bar","nerds","sour patch kids"])

