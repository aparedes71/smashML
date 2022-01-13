import csv
import urllib3
from bs4 import BeautifulSoup
from frameDataUtils import get_moves
from os.path import basename

http = urllib3.PoolManager()

#global url to get smash characters data
main_url = "https://ultimateframedata.com"

#function to use  REST GET operation to retrieve the response which is in html format
def get_html (url):
    r = http.request('GET', url)
    print(f'Url : {url} , Status : {r.status}')
    return r

#function to use html format of the mian page in order to find all the links for every individual character
def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    data_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if(href[0] == '/'):
            print(href)
            data_links.append(main_url+href)
    print()
    return data_links

# This function return a list of dictionary items each pertaining to a move for the character
def get_frame_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    moves = soup.find_all("div", {"class": "movecontainer"})
    return get_moves(moves)



if __name__ == "__main__":
    
    r = get_html(main_url)

    if(r.status == 200):
        print("Site succesfully responded")
        print()
        print()
        html = r.data
        char_links = get_links(html)
        print()
        print()
        csv_data = []
        for link in char_links:
            if link != 'https://ultimateframedata.com/stats':       
                r2 = get_html(link)
                charname = basename(link)
                print(charname) 
                move_list = get_frame_data(r2.data) 
                move_list.insert(0,charname) 
                csv_data.append(move_list)     
        with open("frameData.csv",'w+') as csvfile:
            writer = csv.writer(csvfile, dialect='unix')
            for entry in csv_data:
                writer.writerow(entry)  
    else:
        print("Site did not respond")
