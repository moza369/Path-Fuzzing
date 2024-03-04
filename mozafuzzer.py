import requests
import sys

class colors:
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    RED = '\033[91m'
    RESET = '\033[0m'


def banner():
    bann = """

        #   #   ###   #####    #       #####  #   #  #####  #####  #####  ####   
        ## ##  #   #     #    # #      #      #   #     #      #   #      #   #  
        # # #  #   #    #    #   #     #####  #   #    #      #    #####  ####   
        #   #  #   #   #     #####     #      #   #   #      #     #      #  #   
        #   #   ###   #####  #   #     #       ###   #####  #####  #####  #   # 
          
          """
    
    print(bann)

def pathfuzzing(url, wordlist):

    for word in wordlist:
        word = word.strip()

        full_url = url.rstrip('/') + '/' + word
        try:
            response = requests.get(full_url)
            
            
            if response.status_code == 200:
                 print(colors.GREEN + "[+]Found:" + colors.RESET, {full_url}, response.status_code)
            else:
                print(colors.PURPLE + "[+]Other:" + colors.RESET, {full_url}, response.status_code)
        
        except requests.RequestException as e:
            print(colors.RED + "Error accessing" + colors.RESET, full_url, ":", e)
        


def main():  
    if len(sys.argv) != 3:
        print("How to run script: python3 script.py 'url' 'path_to_wordlist' ")
        sys.exit(1)
    
    url = sys.argv[1]
    file_path = sys.argv[2]
    
    banner()
    
    try:
        with open(file_path, "r") as wordlst:
            pathfuzzing(url, wordlst)
            
    except FileNotFoundError:
        print("Wordlist Not Found : ", file_path)
        sys.exit(1)

    
if __name__ == "__main__":
    main()