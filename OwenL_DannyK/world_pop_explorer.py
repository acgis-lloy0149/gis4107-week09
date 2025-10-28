#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
# Last update: 31/10/2022
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_pop

# Key = country name and 
# Value = population as a number (i.e. not text containing commas)
#
country_to_pop = dict()


def get_country_count():
    return len(country_pop.splitlines())-1
    

def conv_num_with_commas(number_text):
    number_text=number_text.replace(",","")
    return float(number_text)
        



def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    country_list=[]
    global country_pop
    country_pop_split=country_pop.split("\n")
    for cntr in country_pop_split:
        split_cntr=cntr.split("\t")
        country_list.append(split_cntr[1])
    return country_list[1:6]

    return country_pop.split('\t')


def set_country_to_pop():
    """Sets the global country_to_pop dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """
    global country_pop
    global country_to_pop
    country_pop_split=country_pop.split("\n")
    for cntr in country_pop_split:
        split_cntr=cntr.split("\t")  
        if split_cntr[0]=="Rank":
            continue     
        country_to_pop.update({split_cntr[1]:(int(conv_num_with_commas(split_cntr[5])),float(split_cntr[6][1:len(split_cntr[6])-1]))})
        



def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
       from country_to_pop.  If the country_to_pop is
       empty (i.e. no keys or values), then run set_country_to_pop
       to initialize it."""
    global country_to_pop
    if country_to_pop=={}:
        set_country_to_pop()
    return country_to_pop[country_name][0]


def get_continents():
    """Return the list of continents"""
    global country_pop
    continent_list=[]
    country_pop_split=country_pop.split("\n")
    for cntr in country_pop_split:
        split_cntr=cntr.split("\t")  
        if split_cntr[0]=="Rank":
            continue 
        else:
            if not continent_list.__contains__(split_cntr[2]):
                continent_list.append(split_cntr[2])
    
    continent_list.sort()
    return continent_list





def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total population of all countries on that continent"""
    cont_pop=dict()
    global country_pop
    continent_list=[]
    country_pop_split=country_pop.split("\n")
    for cntr in country_pop_split:
        split_cntr=cntr.split("\t")  
        if split_cntr[0]=="Rank":
            continue 
        else:
            if not split_cntr[2] in list(cont_pop.keys()):
                cont_pop.update({split_cntr[2]:conv_num_with_commas(split_cntr[5])})
            else:
                new_pop=cont_pop[split_cntr[2]]+conv_num_with_commas(split_cntr[5])
                cont_pop.update({split_cntr[2]:new_pop})  
    return cont_pop