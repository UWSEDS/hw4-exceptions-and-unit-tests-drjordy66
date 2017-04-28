# Code to download files

import os
import urllib3
import numpy as np

urllib3.disable_warnings()
http = urllib3.PoolManager()

def get_data(url):
    """
    Download data if not present locally
    If the data are already present, take no action
    Throw exception if the URL does not exist
    """
    filename = os.path.basename(url)
    try:
        response = http.request('GET', url)
    except:
        return('Sorry! You have entered an invalid URL.')
    if np.floor(response.status/100 == 2) and os.path.exists(filename):
        return('Data exists locally. No action was taken.')
    elif np.floor(response.status/100 == 2):
        with open(filename, 'wb') as f:
            f.write(response.data)
        response.release_conn()
        return('Data downloaded successfully!')
    elif np.floor(response.status/100 != 2):
        return('Sorry! You have entered an invalid URL.')
    else:
        return('How did I get here???')

def delete_data(url):
    """
    Removes data if it is present locally
    """
    filename = os.path.basename(url)
    response = http.request('GET', url)
    if np.floor(response.status/100 == 2) and os.path.exists(filename):
        os.remove(filename)
        return('Data has been removed locally.')
    elif np.floor(response.status/100 != 2):
    	return('Sorry! You have entered an invalid URL.')
    else:
        return('Data not found locally. No file was removed.')

# Run the following code if the file is run at the command line
if __name__ == "__main__":
    i = 0
    max_iter = 5
    while (i < max_iter):
        if i == 0:
            decision = str(input("Would you like to get data or delete data? Enter 'get' or 'del' or 'exit' to quit: "))
        else:
        	decision = str(input("Invalid entry. Please enter either 'get', 'del', or 'exit': "))
        if decision == 'get':
            url = str(input("Enter a URL to download a file from: "))
            result = get_data(url)
            print(result)
            break
        elif decision == 'del':
            url = str(input("Enter the URL that the file you wish to delete was obtained from: "))
            result = delete_data(url)
            print(result)
            break
        elif decision == 'exit':
            print('Thanks for trying it out! Bye!')
            break
        elif i == max_iter - 1:
            print('Sorry, you have reached your maximum number of attempts (5).')
        else:
            pass
        i += 1