
# API calls can be found here: https://console.tethersecurity.com/api/v1/docs/

import requests

data = []

#Token appears to work...
def post_token_obtain():
    url = 'https://console.tethersecurity.com/api/v1/token/'
    credentials = {'username' : 'PUT USERNAME HERE', 'password' : 'PUT PASSWORD HERE'}

    result = requests.post(url, json = credentials)

    access_token = result.json()['access']
    #For testing:  print(access_token)

    print(result.text)

    return access_token

def get_assets(num_page, num_items, myToken):

    url = 'https://console.tethersecurity.com/api/v1/assets/'
    p = {"page" : num_page , "page_size" : num_items}

    print("This is the token.")
    print(myToken)

    head = {'Authorization': 'token {}'.format(myToken)}

    try:
        response = requests.get(url, headers = head, json = p)

        if response.status_code == 200:
            posts = response.json()
            return posts
        
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def del_assets(dups):
    url = 'https://console.tethersecurity.com/api/v1/assets/delete/'

    parameters = {
        "uninstall" : True,
        "disable_encryption" : True,
        "disable_bootlock" : True,
        "disable_efs" : True,
        "decrypt_bitlocker_drives" : True,
        "disable_bitlocker_tpm" : True,
        "disable_diskvault" : True,
        "disable_sed" : True,
        "disable_mobile_password_protection" : True,
        "assets_ids" : 
            [
                dups
            ]
        
     } #end parameters

    r = requests.patch(url, data = parameters)

    #check status code for response received
    #success code - 200
    print(r)

    #print content of request
    print(r.content)

def main():
    #During testing, this part will be rather fluid. I will adjust as time goes on for a consistent experience
    r = "spaceholder"
    
    #Token can be officially obtained.
    myToken = post_token_obtain() 

    get_assets(1, 100, myToken)

    #REMEMBER TO EDIT IN AND OUT YOUR CREDENTIALS WHEN NOT ACTIVELY TESTING THE PROGRAM!!!!!

if __name__ == '__main__':
    main()

















