# ECOR 1042 Lab 4 - Individual submission for test3 function

#import check module here
import check

#import load_data module here
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Emily Causi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101236902"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T055"

#==========================================#
#Do not modify the code already provided.

from load_data import character_occupation_list, character_strength_list, character_luck_list, character_weapon_list, load_data, calculate_health

def test_return_correct_dict_inside_list():
    
    #Complete the function with your test cases
    
    #test that character_occupation_list returns a correct dictionary inside the list (3 different test cases required)
    
    character_expected_first = {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}
    character_expected_second = {'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Staff'}
    character_expected_last = {'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}
    check.equal(character_occupation_list('characters-test.csv','WA')[0], character_expected_first, "First character data incorrect.")
    check.equal(character_occupation_list('characters-test.csv','WA')[1], character_expected_second, "Second character data incorrect.")
    check.equal(character_occupation_list('characters-test.csv','WA')[-1], character_expected_last, "Last character data incorrect.")
    
    #test that character_strength_list returns a correct dictionary inside the list  (3 different test cases required)
   
    strength_expected_first = {'Occupation': 'DB', 'Agility': 10, 'Stamina': 11, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'}
    strength_expected_second = {'Occupation': 'EB', 'Agility': 3, 'Stamina': 10, 'Personality': 8, 'Intelligence': 6, 'Luck': 0.5, 'Armor': 8, 'Weapon': 'Staff'}
    strength_expected_last = {'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}
    check.equal(character_strength_list('characters-test.csv',(7,10))[0], strength_expected_first, "First strength data incorrect.")
    check.equal(character_strength_list('characters-test.csv',(7,10))[1], strength_expected_second, "Second strength data incorrect.")
    check.equal(character_strength_list('characters-test.csv',(7,10))[-1], strength_expected_last, "Last strength data incorrect.")        
   
    #test that character_luck_list returns a correct dictionary inside the list  (3 different test cases required)
    
    luck_expected_first = {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'}
    luck_expected_second = {'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Club'}
    luck_expected_last = {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Armor': 11, 'Weapon': 'Spear'}
    check.equal(character_luck_list('characters-test.csv', 0.7)[0], luck_expected_first, "First luck data incorrect.")
    check.equal(character_luck_list('characters-test.csv', 0.7)[1], luck_expected_second, "Second luck data incorrect.")
    check.equal(character_luck_list('characters-test.csv', 0.7)[-1], luck_expected_last, "Last luck data incorrect.")  
    
    #test that character_weapon_list returns a correct dictionary inside the list (3 different test cases required)
    
    weapon_expected_first = {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10}
    weapon_expected_second = {'Occupation': 'EB', 'Strength': 9, 'Agility': 3, 'Stamina': 10, 'Personality': 8, 'Intelligence': 6, 'Luck': 0.5, 'Armor': 8}
    weapon_expected_last ={'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10}
    check.equal(character_weapon_list('characters-test.csv', 'Staff')[0], weapon_expected_first, "First weapon data incorrect.")
    check.equal(character_weapon_list('characters-test.csv', 'Staff')[1], weapon_expected_second, "Second weapon data incorrect.")
    check.equal(character_weapon_list('characters-test.csv', 'Staff')[-1], weapon_expected_last, "Last weapon data incorrect.")  
        
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    
    loadtuple = ('All','')
    print(load_data('characters-test.csv',loadtuple)[-1])
    load_list = load_data('characters-test.csv',loadtuple)
    
    loadlist_expected_first = {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}
    loadlist_expected_second = {'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}
    loadlist_expected_third = {'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'}
    loadlist_expected_fourth = {'Occupation': 'DB', 'Strength': 15, 'Agility': 4, 'Stamina': 10, 'Personality': 11, 'Intelligence': 3, 'Luck': 0.61, 'Armor': 9, 'Weapon': 'Club'}
    loadlist_expected_fifth = {'Occupation': 'DB', 'Strength': 10, 'Agility': 10, 'Stamina': 11, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'}
    loadlist_expected_last = {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}

    check.equal(load_data('characters-test.csv',loadtuple)[0], loadlist_expected_first, "First loadlist data incorrect.")
    check.equal(load_data('characters-test.csv',loadtuple)[1], loadlist_expected_second, "Second loadlist data incorrect.")
    check.equal(load_data('characters-test.csv',loadtuple)[2], loadlist_expected_third, "Third loadlist data incorrect.")
    check.equal(load_data('characters-test.csv',loadtuple)[3], loadlist_expected_fourth, "Fourth loadlist data incorrect.")
    check.equal(load_data('characters-test.csv',loadtuple)[4], loadlist_expected_fifth, "Fifth loadlist data incorrect.")
    check.equal(load_data('characters-test.csv',loadtuple)[-1], loadlist_expected_last, "Last loadlist data incorrect.")

    #test that calculate_health returns a correct dictionary inside the list  (3 different test cases required)
        
    health_expected_first = {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff', 'Health': 115.0}
    health_expected_second = {'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club', 'Health': 90.0}
    health_expected_last = {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear', 'Health': 119.81}
    check.equal(calculate_health(load_list)[0], health_expected_first, "First health data incorrect.")
    check.equal(calculate_health(load_list)[1], health_expected_second, "Second health data incorrect.")
    check.equal(calculate_health(load_list)[-1], health_expected_last, "Last health data incorrect.")  
           
    check.summary()


# Do NOT include a main script in your submission