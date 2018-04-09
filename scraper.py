from selenium import webdriver
import time


br = webdriver.Firefox()
base_url = "https://www.allrecipes.com/recipe/{0}"


def scrape_instructions(br):
    try:
        instructions = br.find_elements_by_class_name("recipe-directions__list--item")
        instructions = [instruct.text for instruct in instructions[:-1]]
    except:
        instructions = []
    return instructions

def main():
    url = base_url.format("8352")
    br.get(url)
    time.sleep(3)
    instructions = scrape_instructions(br)
    print(instructions)


if __name__ == '__main__':
    main()
