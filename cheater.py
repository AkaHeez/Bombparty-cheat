code = input("what is the code? ").upper()
PATH = f"https://jklm.fun/{code}"


USER = "Username here, anything works"
FILEPATH = r"Right click the words.txt and then copy as path and paste it in here"







from os import system as sys



def promptCheck(words, prompt):
    sys("cls")
    counter = 0
    print(prompt)
    for word in words:
        if prompt in word:
            if counter < 15:
                print(word)
                counter += 1
            else:
                return prompt


def main():
    #Importing Modules
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException



    #open the list of words 0-7 letters of bombparty words
    words = open(FILEPATH, "r").read().split()

    #waits in between to make sure that the browser load completly
    driver = webdriver.Chrome()
    html = driver.get(PATH)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/input")))
    sleep(1)
    driver.find_element(By.XPATH,value="/html/body/div[2]/div[3]/form/div[2]/input").send_keys(USER)
    driver.find_element(By.XPATH,value="/html/body/div[2]/div[3]/form/div[2]/button").click()
    #switching to see the iframe to see the information of text and user's playing
    sleep(10)
    driver.switch_to.frame(0)
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/button")))
    sleep(1)
    driver.find_element(By.XPATH,value="/html/body/div[2]/div[3]/div[1]/div[1]/button").click()
    #looping the process of if the user is me and if it is, it prints out the words usuable in the console, up to 15
    previousP = "lol hi"
    while True:    
        currentPlayer = driver.find_element(By.XPATH, value='/html/body/div[2]/div[3]/div[2]/div[1]')
        sleep(1)
        if currentPlayer.get_attribute("hidden") == "true":
            prompt = driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/div[2]/div[2]/div')
            if (prompt.text.lower()) != previousP:
                previousP = promptCheck(words, prompt.text.lower())
if __name__ == "__main__":
    main()