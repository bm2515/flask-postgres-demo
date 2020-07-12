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
    
           
def test_post_get_requests(method, url):
    #url = 'https://api.github.com/users/bm2515'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    if method == "POST":

        payload = {'steps': '1500', 'calories': '750'}

        # convert dict to json by json.dumps() for body data. 
        resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))

    elif method == "GET":

        resp = requests.get(url, headers=headers)

    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    
    
    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/users/spencer_34/data'
    test_post_get_requests("GET", url)