import requests
import json

def pretty_print_request(request):
    print( '\n{}\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()))
    )

def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()))
    )

    response_object = json.loads(response.text)

    if (type(response_object) == list):

        for each in response_object:
            for key, value in each.items():
                print(key, ':' , value)
            print('\n')

    elif (type(response_object) == dict):
        for key, value in response_object.items():
            print(key, ':' , value)
        print('\n')
    
           
def test_post_get_requests(method, url, payload=None):
    #url = 'https://api.github.com/users/bm2515'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    if method == "POST":

        # convert dict to json by json.dumps() for body data. 
        resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))

    elif method == "GET":

        resp = requests.get(url, headers=headers)

    
    # Validate response headers and body contents, e.g. status code.
    #assert resp.status_code == 200
    #resp_body = resp.json()
    
    
    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

if __name__ == '__main__':

    usernames = ['alpha_123', 'beta_543', 'gamma_666', 'proton_123', 'neutron_333', 'electron_999', 'garry_123',
                'ricky_23', 'morty_66', 'charles_24']

    firstnames = ['Alpha', 'Beta', 'Gamma', 'Proton', 'Neutron', 'Electron', 'Garry', 'Ricy', 'Morty', 'Charles']

    lastnames = ['Mate', 'Bar', 'Rays', 'Atoms', 'Particles', 'Atoms', 'Pint', 'Peer', 'Nass', 'Price']

    age = ['12','22','34','32','42','41','76','53','35','49']

    sex = ['Male', 'Female','Male', 'Female','Male', 'Female', 'Female', 'Male', 'Female', 'Male']

    diabetes = ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes']

    weight = ['12kg', '32kg', '54kg', '73kg', '32kg', '42kg', '65kg', '43kg', '85kg', '65kg']

    height = ['21cm', '62cm', '59cm', '93cm', '23cm', '160cm', '43cm', '180cm', '170cm', '23cm']


    #print(len(usernames), len(firstnames), len(lastnames), len(age), len(sex), len(diabetes), len(weight), len(height))

    #populate the dataBase
    POPULATE = False
    
    if POPULATE == True:

        for i in range(10):
            payload = {'username': usernames[i], 'firstname': firstnames[i], 'lastname': lastnames[i], 'age': age[i], 'sex': sex[i],
            'height': height[i], 'weight': weight[i], 'diabetes': diabetes[i]}

            print(payload)

            url = 'http://0.0.0.0:5000/users/register'

            test_post_get_requests("POST", url, payload=payload)

    #Retrieve the data
    RETRIEVE_DATA = True
    if RETRIEVE_DATA == True:

        for i in range(10):
            username = usernames[i]
            url = 'http://0.0.0.0:5000/users/' + username
            test_post_get_requests("GET", url, payload=None)


    