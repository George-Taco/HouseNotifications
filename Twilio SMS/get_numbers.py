# Gets Numbers from a Google Spreadsheet that is connected
import pandas as pd


def import_numbers():
    url = "spreadsheet_url"
    df = pd.read_csv(url)

    #print(df.get('Phone Number'))

    numbers = df.get('Phone Number')

    number_list_for_text_file = ""

    f = open("phonenumbers.txt", "w")
    for number in numbers:
        number_list_for_text_file += (str(number)+",")
    number_list_for_text_file = number_list_for_text_file.rstrip(',')
    f.write(number_list_for_text_file)
    f.close()