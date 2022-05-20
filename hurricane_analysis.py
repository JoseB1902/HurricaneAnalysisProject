# names of hurricanes
from enum import unique
from itertools import count
from multiprocessing.sharedctypes import Value
from operator import itemgetter
from optparse import Values
import string
from unittest.util import sorted_list_difference


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 
'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 
'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], 
['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], 
['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], 
['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], 
['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], 
['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', 
'1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def update_damages(damage_list):    #Funcion to convert damages list to float 
    updated_list = []
    for damage in damage_list:
        if ("M" in damage):
            updated_list.append(float(damage.replace("M","")) * 1000000)        #Remove M suffix, convert to float, multiply by 1,000,000 and append to empty list
        if("B" in damage):
            updated_list.append(float(damage.replace("B","")) * 1000000000)     #Remove B suffix, convert to float, multiply by 1,000,000,000 and append to empty list
        if(damage == 'Damages not recorded'):
            updated_list.append(damage)                                         #Conserve null values in string

    return updated_list

updated_damages = update_damages(damages)





# write your construct hurricane dictionary function here:
def construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):   #Function for constructing hurricane dictionary from given lists
    dict = {}                                                                                               #Empty dictionary to pass through for loop
    indx = 0
    for name in names:
        dict.update({name: {'Name': name, 'Months': months[indx], 'Years': years[indx], 'Max Sustained Winds': max_sustained_winds[indx], 'Areas Affected': areas_affected[indx], 
        'Damages': damages[indx], 'Deaths': deaths[indx]}})                                                 #For loop itirates over the names list to pass them to the key of the dictionary, the indx value adds 1 
        indx += 1                                                                                           #to iterate through the indexes of the other list and passed as the values as a dictionary
    return dict                                


hurricane_dict = construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)





# write your construct hurricane by year dictionary function here:
def contruct_hurricane_by_year_dict(dictionary):     #Function for constructing hurricane dictionary with the year as the key
    dict = {}
    lst = []
    indx = 0
    for name in dictionary:
        yr = str(dictionary[name].get('Years'))   #Stores the 'Years' values from the dictionary into single variable 
        lst.append(yr)                            # Variable is appended into empty list
    for values in dictionary.values():            # Construct the dictionary by iterating through the indexes of the year list and attaches the values of given dictionary

        dict.update({lst[indx]: values})

        indx += 1

    return dict

hurricane_by_year_dict = contruct_hurricane_by_year_dict(hurricane_dict)


# write your count affected areas function here:
def count_affected_areas(dictionary):           #A function for giving the count of affected areas as the value and location as the key
    count = 0
    dict = {}
    area_list = []
    unique_area = []
    for name in dictionary:                     #For loop to extract the areas affected value and stores them in an empty list
        area_list.append(dictionary[name].get('Areas Affected'))

    clean_area_list = []
    for i in range(0, len(area_list)):          
        indx = 0
        while indx != len(area_list[i]):
            clean_area_list.append(area_list[i][indx])  #Loops through each list in the list and truncates it into a single list
            indx += 1
    for area in clean_area_list:                #Appends the unique areas into a list
        if area not in unique_area:
            unique_area.append(area)
        for area in unique_area:                #Gives the count by comparing if the area appears in the unique list
            count = clean_area_list.count(area)
        
            dict.update({area: count})

        
    return dict
    
    
    

affted_areas_counts = count_affected_areas(hurricane_dict)
#print(affted_areas_counts)



# write your find most affected area function here:
def areas_most_affected(dictionary):
    empty_list = []
    for area, count in dictionary.items():
        empty_list.append([area, count])
    
    sorted_list = sorted(empty_list, key=lambda x:x[1], reverse=True)
    output = "The area most affected by hurricanes is: " + sorted_list[0][0] + ", with a count of: " + str(sorted_list[0][1]) + "."

    return output


print(areas_most_affected(affted_areas_counts))
# write your greatest number of deaths function here:
def greatest_number_of_deaths(dictionary):
    empty_list = []
    for name, values in dictionary.items():
        empty_list.append([name, values['Deaths']])
    sorted_list = sorted(empty_list, key=lambda x:x[1], reverse=True)
    output = "The hurricane with the greatest number of deaths is " + sorted_list[0][0] + ", with a death count of: " + str(sorted_list[0][1]) + "."

    return output


print(greatest_number_of_deaths(hurricane_dict))

# write your catgeorize by mortality function here:
def categorize_mortality(dictionary):
    mortality_dict = {}
    scale_list = []
    name_list = []
    for name in dictionary:
        death_count = dictionary[name].get("Deaths")
        if death_count >= 10000:
            scale_list.append(4)
            name_list.append(name)
        elif death_count >= 1000:
            scale_list.append(3)
            name_list.append(name)
        elif death_count >= 500:
            scale_list.append(2)
            name_list.append(name)
        elif death_count >= 100:
            scale_list.append(1)
            name_list.append(name)
        elif death_count < 100:
            scale_list.append(0)
            name_list.append(name)  

    
    zero_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 0]
    one_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 1]
    two_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 2]
    three_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 3]
    four_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 4]

    mortality_dict = {0: zero_list, 1: one_list, 2: two_list, 3: three_list, 4: four_list}
    return mortality_dict








# write your greatest damage function here:
def most_damage(dictionary):
    damage_list= []

    for name in dictionary:
        if dictionary[name].get('Damages') != 'Damages not recorded':                     
            damage_list.append([name, dictionary[name].get('Damages')])
    
    sorted_list = sorted(damage_list, key=lambda x:x[1], reverse=True)
    output = "The hurricanes that cost the most damage is: " + sorted_list[0][0] + ", with a cost of: " + "$" + str(sorted_list[0][1]) + "."

    return output



print(most_damage(hurricane_dict))


# write your catgeorize by damage function here:
def categorize_damage(dictionary):
    mortality_dict = {}
    scale_list = []
    name_list = []
    for name in dictionary:
        if dictionary[name].get('Damages') != 'Damages not recorded':
            death_count = dictionary[name].get("Damages")
            if death_count >= 50000000000:
                scale_list.append(4)
                name_list.append(name)
            elif death_count >= 10000000000:
                scale_list.append(3)
                name_list.append(name)
            elif death_count >= 1000000000:
                scale_list.append(2)
                name_list.append(name)
            elif death_count >= 100000000:
                scale_list.append(1)
                name_list.append(name)
            elif death_count < 100000000:
                scale_list.append(0)
                name_list.append(name)  

    
    zero_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 0]
    one_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 1]
    two_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 2]
    three_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 3]
    four_list = [name_list[i] for i in range(len(scale_list)) if scale_list[i] == 4]

    mortality_dict = {0: zero_list, 1: one_list, 2: two_list, 3: three_list, 4: four_list}
    return mortality_dict


print(categorize_damage(hurricane_dict))