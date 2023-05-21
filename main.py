from Data_Scrapy import Scrappy
from Automation import Automation

scrapper = Scrappy()
scrapper.data_extraction()
bot = Automation()
index = 0
total_entries = len(scrapper.link)
entries_left = True

while entries_left:
    bot.fill_details(address=scrapper.address[index],
                     rent=scrapper.rent[index],
                     link=scrapper.link[index])
    index += 1
    if index == total_entries:
        entries_left = False

bot.create_google_sheet()
