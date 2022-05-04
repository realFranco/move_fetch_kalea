from selenium import webdriver


wd = webdriver.Firefox()

key = 'store-location'
value = {"id":"pfvswBTKMD0JMgHsvEEv","name":"Valencia"}
value = json.dumps(value)
script = f"window.localStorage.setItem('{key}', '{value}');"

def go_to_kalea(wd, script):
    key = 'store-location'
    value = {"id":"pfvswBTKMD0JMgHsvEEv","name":"Valencia"}
    value = json.dumps(value)
    script = f"window.localStorage.setItem('{key}', '{value}');"
    wd.get("https://kaleamarket.com/select-store")
    wd.execute_script(script)
    wd.get("https://kaleamarket.com/search-results?searchQuery=agua&searchType=products&category=")

# go_to_kalea(wd, script)

def quit(wd):
    wd.quit()
