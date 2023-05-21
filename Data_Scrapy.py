from bs4 import BeautifulSoup
import requests
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
      "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122" \
      ".30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22" \
      "%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D" \
      "%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price" \
      "%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom" \
      "%22%3A12%7D"


class Scrappy:

    def __init__(self):
        self.html_file = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                                                  "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                                                                  "Version/15.6.1 Safari/605.1.15"}).text
        self.soup = BeautifulSoup(self.html_file, "html.parser")
        self.address = []
        self.rent = []
        self.link = []

    def data_extraction(self):
        listing = self.soup.find_all("li")
        for index, item in enumerate(listing):
            try:
                list_item = item.find("a", {"data-test": "property-card-link"})
                list_links = list_item.get("href")
                list_address = list_item.address
                try:
                    if "https://" not in list_links:
                        list_link = f'https://www.zillow.com{list_links}'
                    else:
                        list_link = list_links
                    self.link.append(list_link)
                    address = list_address.text
                    self.address.append(address)
                    price = list_item.find_next("span", {"data-test": "property-card-price"}).text
                    if "/mo" in price or "+/mo" in price:
                        rent = price.strip("+/mo")
                    else:
                        rent = price.split("+")[0]
                    self.rent.append(rent)
                except AttributeError:
                    pass
            except AttributeError:
                pass
