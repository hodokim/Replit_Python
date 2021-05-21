import os
import requests



def end():
  ans = input("Do you want to start over? y/n").lower()
  if ans =='y':
    start()
  elif ans=='n':
    print("program terminated")
  else:
    print("please press 'y' or 'n' only")
    end()


def start():
  os.system('clear')
  print("Welcome to IsItDown.py!\
  \nPlease write a URL or URLs you want to check. (separated by comma)")
  urls = input().lower().replace(" ","").split(",")
  for url in urls:
    if "." not in url:
      print(f"{url} is not the correct URL format.")
      continue
    elif "http://" not in url and "https://" not in url:
      url = f"http://{url}"
    try:
      request = requests.get(url)
      if request.status_code == 200:
        print(f"{url} is up!")
      else:
        print(f"{url} is down!")
    except:
      print(f"{url} is down!")
    
  end()



start()
