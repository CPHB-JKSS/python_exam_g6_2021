# Imports
import bs4 
import requests
import re
import urllib.request
import csv
import shutil

# Henter en url og bruger requests til at fejl finde eller raise en fejl.
# BeautifulSoup parser html og laver det til læseligt tekst.
url = "https://www.kongehuset.dk/monarkiet-i-danmark/nytarstaler/hendes-majestat-dronningens-nytarstaler"
r_url = requests.get(url)
r_url.raise_for_status()
soup = bs4.BeautifulSoup(r_url.text, 'html.parser')

# Hent a href links og skriver indholdet til csv filer som en liste.


def get_links_and_write_to_csv(output_file):
    list_of_links = []

    # Henter alle a href links og adder det til en liste.
    for link in soup.findAll('a', attrs={'href': re.compile("https://www.kongehuset.dk")}):
        list_of_links.append(link.get('href'))
        # print(link.get('href'))

    # Skriv indholdet af linksnes tekst til en csv fil.
    with open(output_file, 'w') as file_object:
        write_to = csv.writer(file_object, delimiter=',')
        write_to.writerow(list_of_links)
    return list_of_links


# Tager en fil og add'er indholdet af filen til en liste, som den returnere.
def read_csv_and_add_to_list(input_file):
    list_of_urls = []
    with open(input_file, 'r') as file_object:
        read_it = csv.reader(file_object, delimiter=',')
        for row in read_it:
            list_of_urls.append(row)
    return(list_of_urls)


# Funktion til at fiske årstallet ud af en streng og returne et ensrettet string-navn.
def nameFile(str):
    char_count = 0
    year = ""
    counter = -1

    for character in str:
        counter += 1

        if counter+3 == len(str):
            break
        if str[counter].isdigit() and str[counter+1].isdigit() and str[counter+2].isdigit() and str[counter+3].isdigit():
            year = str[counter]+str[counter+1]+str[counter+2]+str[counter+3]
        if len(year) == 4:
            return "data/Nytårstalen "+year

    return "Nytårstalen (årstal mangler)"


# Rekursiv metode til gennemløbning af HTML elementer.
def get_last_child(elements):
    result = ""
    for element in elements:
        if "GUD BEVARE DANMARK" in element.text:
            children = element.findChildren('div', recursive=False)
            if len(children) > 0:
                get_last_child(children)
            elif len(children) == 0:
                result = element.text
    return result


# Åbner links og læser indholdet på de links og skriver indholdet til filer, lokalt.
def write_data_to_files_from_links(links):
    for link in links:
        stringified_link = link
        for new_string in stringified_link:
            response = urllib.request.urlopen(new_string)

            # Decoder og læser response fra url'en.
            res = response.read().decode('utf-8')

            # Gennemløber responsen med bs4
            soup = bs4.BeautifulSoup(res, 'html.parser')
            # Finder den nederste <div> hvor talen ligger i.
            speech = get_last_child(soup.findAll('div'))

            # Alternativ/komplimentær løsning:
            # Gennemløb filer for indhold der indrammer talerne på alle siderne.
            # Fx.: "Hendes Majestæt Dronningens" & "GUD BEVARE DANMARK"
            #speech = res.split('Hendes Majestæt Dronningens')[0]

            file_name = nameFile(new_string)
            print(file_name)

            f = open(file_name, 'w')
            f.write(speech)
            f.close


