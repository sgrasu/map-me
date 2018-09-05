import requests
import re
from server import db
from server import Brewery
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.brewersassociation.org/directories/breweries/')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
country_list = soup.find(id='country_select')
# Pull text from all instances of <a> tag within BodyText div
country_list_items = country_list.find_all("li")
db.create_all()
for country in country_list_items:
    print(country['data-country-id'])
    country_page = requests.post('https://www.brewersassociation.org/wp-admin/admin-ajax.php',
    data ={'action':'get_breweries','_id':country,'search_by':'country'})
    country_breweries_soup = BeautifulSoup(country_page.text,'html.parser')

    breweries = country_breweries_soup.find_all('ul',class_="brewery-info")

    for brewery in breweries:
        ids = ['name','telephone','state']
        props = {k: brewery.find(class_=k).text if \
        brewery.find(class_=k) is not None else '' for k in ids }
        props['telephone'] = re.sub('[^0-9+]',"",props['telephone'])
        props['address'] = ''
        address1 = brewery.find(class_='address')
        if address1 is not None:
            props['address'] = address1.text
            address2 = address1.find_next_sibling('li')
            if address2 is not None:
                props['address'] = address1.text +' '+ address2.text
        props['country'] = country['data-country-id']
        db_brewery = Brewery(**props)
        db.session.add(db_brewery)
        db.session.commit()
    db.session.commit()


