import requests

rover_url = 'enter link here'
def get_mars_photos(sol):
    request_params = { 'sol' : sol, 'api_key' : 'DEMO_KEY'}
    response = requests.get(rover_url, params= request)
    mars_data = response.json()

    photo = mars_data['photos']
