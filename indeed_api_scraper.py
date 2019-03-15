# verifying indeed publisher number 
from indeed import IndeedClient 
client = IndeedClient(publisher = 'publisher_number')

params = {
        'q' : "software engineer",
        'l' : "Chicago",
        'sort' : "date",
        'fromage' : "5",
        'limit' : "50",
        'filter' : "1",
        'userip' : "ip_address",
        'useragent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }

# main search function 
def get_offers(params):
    search_results = client.search(**params) #perform search 
    for elm in search_results['results']:
         offer = (elm['jobtitle'], #parsing the offer 
                 elm['formattedLocation'],
                 elm['formattedLocation'],
                 elm['snippet'], 
                 elm['url'],
                 elm['indeedApply'],
                 elm['jobkey'],
                 elm['date'])
        
                 
