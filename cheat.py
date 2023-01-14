FILEPATH = r"Right click the words.txt and then copy as path and paste it in here"
AMOUNT = 15 #amount of words you want it to type out when soft cheating


cheat = int(input("1) Soft Cheat\n2) Hard Cheat\n"))






from os import system as sys



def promptCheck(prompt):
    sys("cls")
    counter = 0
    print(prompt)
    for word in words:
        if prompt in word:
            if counter < AMOUNT:
                print(word)
                counter += 1
            else:
                return prompt


def promptAI(prompt):
    for word in words:
        if prompt in word and word not in usedWords:
            usedWords.append(word)
            return word











def main():
    #Importing Modules
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC



    #open the list of words 0-7 letters of bombparty words
    global words, usedWords
    words = open(FILEPATH, "r").read().split()

    #waits in between to make sure that the browser load completly
    driver = webdriver.Chrome()
    html = driver.get("https://jklm.fun")
    wait = WebDriverWait(driver, 10)


    #switching to see the iframe to see the information of text and user's playing
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[5]")))
    while True:
        sleep(1)
        if driver.current_url.endswith("fun/"):
            continue
        break
    while True:
        sleep(1)
        if driver.find_element(By.XPATH, value="/html/body/div[2]/div[3]").get_attribute("hidden") == "true":
            break
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[4]/div[1]")))
    sleep(1)
    driver.switch_to.frame(0)


    previousP = "lol hi"
    usedWords = []
    if cheat == 2: #Hard cheat
        while True:    
            currentPlayer = driver.find_element(By.XPATH, value="/html/body/div[2]/div[3]/div[2]/div[1]")
            sleep(1)
            if currentPlayer.get_attribute("hidden") == "true":
                prompt = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[2]/div")
                textbox = driver.find_element(By.XPATH,value="/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
                textbox.send_keys(promptAI(prompt.text.lower()))
                textbox.submit()
                


    else: #soft cheat
        while True:    
            currentPlayer = driver.find_element(By.XPATH, value="/html/body/div[2]/div[3]/div[2]/div[1]")
            sleep(1)
            if currentPlayer.get_attribute("hidden") == "true":
                prompt = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[2]/div")
                if (prompt.text.lower()) != previousP:
                    previousP = promptCheck(prompt.text.lower())


if __name__ == "__main__":
    main()
