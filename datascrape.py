import requests
from bs4 import BeautifulSoup

url = "https://dmarket.com/ingame-items/item-list/csgo-skins"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the container for the specific skin (replace 'your-skin-id' with the actual ID or class of the container)
    skin_container = soup.find("div", {"data-market-item-name": "★ Sport Gloves | Pandora's Box"})

    # Check if the skin container is found
    if skin_container:
        # Find the sales info section within the skin container (replace 'your-sales-info-class' with the actual class of the sales info section)
        sales_info = skin_container.find("div", class_="spiedSection ng-tns-c303-53 ng-star-inserted")

        # Check if the sales info section is found
        if sales_info:
            # Extract and print the prices, dates, and wear values
            recent_sales = sales_info.find_all("div", class_="c-salesChart ng-star-inserted")

            for sale in recent_sales:
                # Extract price (replace 'your-price-class' with the actual class of the price element)
                price = sale.find("span", class_="c-assetPreview__cell").text

                # Extract date (replace 'your-date-class' with the actual class of the date element)
                date = sale.find("span", class_="c-assetPreview__cell").text


                # Process and print the extracted data
                print(f"Price: {price}, Date: {date} ")
        else:
            print("Sales info section not found for the specified skin.")
    else:
        print("Skin container not found.")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
