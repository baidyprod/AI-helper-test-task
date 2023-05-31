from bs4 import BeautifulSoup


def advanced_scrape_locations():
    """
    'Інформація про магазини в місті Київ': [{'Назва локації': 'ТРЦ «DOMA Center» (1 поверх)', 'Адреса':
    'вул. Будівельників, 40\nст. м. «Дарниця»', 'Номер телефону': '+38 (063) 425 49 03',
    'Графік роботи': 'Пн - Пт: 10:00 - 21:30\nСб - Нд: 10:00 - 21:30'}
    """
    with open("our_shops.html", "r") as file:
        soup = BeautifulSoup(file, "html.parser")

    sections = soup.find_all("section", class_="section accordeon-section")

    result_dict = {}

    for section in sections:
        shop_city_name_div = section.find_all("div", class_="shop-city-name")
        accordeon_head_col_div = section.find_all("div", class_="accordeon_head-col")

        city_name = shop_city_name_div[0].get_text().strip()
        data_values = [div.get_text().strip() for div in accordeon_head_col_div]

        shops = []
        for i in range(0, len(data_values), 4):
            shop_dict = {
                "Назва локації": data_values[i],
                "Адреса": data_values[i + 1],
                "Номер телефону": data_values[i + 2],
                "Графік роботи": data_values[i + 3],
            }
            shops.append(shop_dict)

        result_dict[f"Інформація про магазини в місті {city_name}"] = shops

    return result_dict


def scrape_locations():
    """
    'Інформація про магазини в місті Київ': [['ТРЦ «DOMA Center» (1 поверх)', 'вул. Будівельників,
    40\nст. м. «Дарниця»', '+38 (063) 425 49 03', 'Пн - Пт: 10:00 - 21:30\nСб - Нд: 10:00 - 21:30']
    """
    with open("our_shops.html", "r") as file:
        soup = BeautifulSoup(file, "html.parser")

    sections = soup.find_all("section", class_="section accordeon-section")

    result_dict = {}

    for section in sections:
        shop_city_name_div = section.find_all("div", class_="shop-city-name")
        accordeon_head_col_div = section.find_all("div", class_="accordeon_head-col")

        city_name = shop_city_name_div[0].get_text().strip()
        data_values = [div.get_text().strip() for div in accordeon_head_col_div]

        result_dict[f"Інформація про магазини в місті {city_name}"] = [
            data_values[i: i + 4] for i in range(0, len(data_values), 4)
        ]

    return result_dict
