from selenium import webdriver
import time


br = webdriver.Firefox()
base_url = "https://www.allrecipes.com/recipe/{0}"
directions_and_author = []

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
    directions_and_author.append((instructions, author))
    print(directions_and_author)


if __name__ == '__main__':
    main()
