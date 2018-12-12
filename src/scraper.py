from selenium import webdriver
import time
import json

br = webdriver.Firefox()
base_url = "https://www.allrecipes.com/recipe/{0}"
directions_and_author = []
recipe_numbers = [222733, 218786, 218785, 216388, 220100, 214192, 214182, 214187, 214193, 62804433, 261588, 255587, 255019, 238312, 228372, 244944, 228272, 238263, 219113, 237139, 233394, 233393, 63913337, 63318646, 63866594, 62898848, 62874161, 62805863, 62860298, 62892448, 220165, 219715, 220090, 242118, 242117, 241875, 63297481, 62170189, 63244504, 63313968, 161178, 62875492, 62124424, 62069364, 62124421, 62123930, 62124420, 62127910, 62127907, 62127724, 69843, 70208, 258666, 93037, 83033, 70907, 72471, 72992, 147346, 220689, 214935, 62223580, 63810172, 62787170, 64387395, 64395749, 64460595, 64387717, 64037838, 64390159, 233546, 256543, 222010, 189460, 238147, 64205813, 63659666, 62448041, 64393422, 63688749, 245659, 237447, 240557, 63988609, 63717885, 64119189, 64233783, 63748984, 64241558, 64437383, 62420218, 62320993, 62320738, 62320355, 62318986, 62317605, 62317495, 62317572, 62317439, 62316518]

def scrape_instructions(br):
    try:
        instructions = br.find_elements_by_class_name("recipe-directions__list--item")
        instructions = [instruct.text for instruct in instructions[:-1]]
    except:
        instructions = []
    return instructions

def scrape_author(br):
    try:
        author = br.find_element_by_class_name("submitter__name")
        author = [author.text]
    except:
        author = ["exception"]
    return author

def main(url_number):
    url = base_url.format(url_number)
    br.get(url)
    time.sleep(3)
    instructions = scrape_instructions(br)
    author = scrape_author(br)
    recipe_mapping = {
        "Author": author,
        "Instructions": " ".join(instructions)
    }
    directions_and_author.append(recipe_mapping)
    #print(directions_and_author)

for i in recipe_numbers:
    main(i)

with open('all_recipe_data.json', 'w') as outfile:
    json.dump(directions_and_author, outfile)
