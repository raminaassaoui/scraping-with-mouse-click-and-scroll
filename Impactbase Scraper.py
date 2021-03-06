import time
import bs4
import pandas as pd
from selenium import webdriver
import selenium
import re

pages = [' ', 1, 2,  17] #3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
dt = pd.DataFrame()
driver = webdriver.Firefox()
#tr 21 is the attribute names row.

n = 200 # the index from which the counter will start reading rows in each page
for page in pages:

    driver.get('https://www.impactbase.org/database/targeted-search?page=' + format(str(page)))
    time.sleep(0.5)
    html = driver.execute_script('return document.documentElement.outerHTML')
    soup = bs4.BeautifulSoup(html, 'html.parser')  # type of parsing here is by tag or balise type href a p div etc..
    funds = soup.findAll(True, {'class':['even', 'odd']})
    if page == 17:
        n = 120




    for funds in soup.find_all(True, {'class':['even', 'odd']})[n:]: #in the page of index 17 use [120:]
        #    print(jobs.prettify())
        #    print("####################################")

        # retreiving the job title:
        try:
            fund_name = funds.find(class_="views-field views-field-title").text.strip()
        except Exception as e:
            fund_name = None
        print('fund_name:', fund_name)

        try:
            firm_name = funds.find(class_="views-field views-field-field-firm-ref").text.strip()
        except Exception as e:
            firm_name = None
        print('firm_name:', firm_name)

        try:
            fund_status = funds.find(class_="views-field views-field-field-fund-product-status").text.strip()
        except Exception as e:
            fund_status = None
        print('fund_status:', fund_status)

        try:
            asset_class = funds.find(class_="views-field views-field-field-asset-class").text.strip()
        except Exception as e:
            asset_class = None
        print('asset_class:', asset_class)

        try:
            target_aum = funds.find(class_="views-field views-field-field-target-fund-aum").text.strip()
        except Exception as e:
            target_aum = None
        print('target_aum:', target_aum)

        try:
            committed_capital = funds.find(class_="views-field views-field-field-fund-committed-capit").text.strip()
        except Exception as e:
            committed_capital = None
        print('committed_capital:', committed_capital)

        try:
            min_inv = funds.find(class_="views-field views-field-field-min-inv-required").text.strip()
        except Exception as e:
            min_inv = None
        print('min_inv:', min_inv)

        try:
            average_inv = funds.find(class_="views-field views-field-field-isize-avg").text.strip()
        except Exception as e:
            average_inv = None
        print('average_inv:', average_inv)




    ##################################"

        driver.find_element_by_link_text(re.sub(' +', ' ', fund_name)).click()
        print(driver.current_url)
        time.sleep(2)

        html = driver.execute_script('return document.documentElement.outerHTML')
        soupy = bs4.BeautifulSoup(html, 'html.parser')  # type of parsing here is by tag or balise type href a p div etc..

        try:
            domicile_big = soupy.find(class_='field field-name-field-fund-domiciled')
            domicile = domicile_big.find(class_='field-content').text.strip()
        except Exception as e:
            domicile = None
        print("the domocile is:", domicile)

        try:
            inception_big = soupy.find(class_='field field-name-field-fund-inception-year')
            inception = inception_big.find(class_='date-display-single').text.strip()
        except Exception as e:
            inception= None
        print("the inception is:", inception)

        try:
            vintage_big = soupy.find(class_='field field-name-field-fund-vintage-year')
            vintage = vintage_big.find(class_='date-display-single').text.strip()
        except Exception as e:
            vintage= None
        print("the Vintage year is:", inception)

        try:
            lp_big = soupy.find(class_='field field-name-field-fund-partners-investors')
            lp = lp_big.find(class_='field-content').text.strip()
        except Exception as e:
            lp = None
        print("the Limited Partners are:", lp)

        try:
            lp_preference_big = soupy.find(class_='field field-name-field-fund-investor-type')
            lp_preference = lp_preference_big.find(class_='field-content').text.strip()
        except Exception as e:
            lp_preference = None
        print("the preferred type of Limited Partners are:", lp_preference)

        try:
            target_geography_big = soupy.find(class_='field field-name-field-fund-target-geography')
            target_geography = target_geography_big.find(class_='field-content').text.strip()
        except Exception as e:
            target_geography = None
        print("the target geography:", target_geography)

        try:
            fund_website_big = soupy.find(class_='field field-name-field-fund-url')
            fund_website = fund_website_big.find(class_='field-content').text.strip()
        except Exception as e:
            fund_website = None
        print("the fund website is:", fund_website)

        try:
            firm_location_big = soupy.find(class_='class="field field-name-field-firm-country"')
            firm_location = firm_location_big.find(class_='label-inline').text.strip()
        except Exception as e:
            firm_location = None
        print("the firm location is:", firm_location)

        try:
            fund_contact_big = soupy.find(class_='field field-name-field-primary-contacts')
            fund_contact_first_name = fund_contact_big.find(class_='first-name').text.strip()
            fund_contact_last_name = fund_contact_big.find(class_='last-name').text.strip()
            fund_contact = fund_contact_first_name + " " + fund_contact_last_name
        except Exception as e:
            fund_contact = None
        print("the fund contact name is:", fund_contact)

        try:
            fund_contact_job_big = soupy.find(class_='field field-name-field-primary-contacts')
            fund_contact_job = fund_contact_job_big.find(class_='field field-name-field-contact-position').text.strip()
        except Exception as e:
            fund_contact_job = None
        print("the fund contact job is:", fund_contact_job)


        time.sleep(1)
        driver.find_element_by_link_text("Impact").click()
        html = driver.execute_script('return document.documentElement.outerHTML')
        soupy = bs4.BeautifulSoup(html, 'html.parser')
        try:
            impact_theme_big = soupy.find(class_='field field-name-field-impact-theme')
            impact_theme = impact_theme_big.find(class_='field-content').text.strip()
        except Exception as e:
            impact_theme = None
        print("the fund impact theme is:", impact_theme)


        time.sleep(1)
        driver.find_element_by_link_text("Financial").click()
        html = driver.execute_script('return document.documentElement.outerHTML')
        soupy = bs4.BeautifulSoup(html, 'html.parser')
        try:
            style_big = soupy.find(class_='field field-name-field-style-stage')
            style = style_big.find(class_='field-content').text.strip()
        except Exception as e:
            style = None
        print("the fund impact theme is:", style)

        try:
            currency_big = soupy.find(class_='field field-name-field-fund-figs-currency')
            currency = currency_big.find(class_='field-content').text.strip()
        except Exception as e:
            currency = None
        print("the fund currency:", currency)

        try:
            IRR_category_big = soupy.find(class_='field field-name-field-target-return-cat')
            IRR_category = IRR_category_big.find(class_='field-content').text.strip()
        except Exception as e:
            IRR_category = None
        print("Target rate of return:", IRR_category)

        try:
            IRR_target_big = soupy.find(class_='field field-name-field-target-irr')
            IRR_target = IRR_target_big.find(class_='field-content').text.strip()
        except Exception as e:
            IRR_target = None
        print("Target rate of return:", IRR_target)

        try:
            max_inv_big = soupy.find(class_='field field-name-field-isize-max')
            max_inv = max_inv_big.find(class_='field-content').text.strip()
        except Exception as e:
            max_inv = None
        print("maximum investment:", max_inv)

        try:
            policy_big = soupy.find(class_='field field-name-field-co-investment-policy')
            policy = policy_big.find(class_='field-content').text.strip()
        except Exception as e:
            policy = None
        print("target co-investment policy:", policy)

        try:
            fee_big = soupy.find(class_='field field-name-field-management-fee')
            fee = fee_big.find(class_='field-content').text.strip()
        except Exception as e:
            fee = None
        print("management fee is:", fee)

        try:
            interest_big = soupy.find(class_='field field-name-field-carried-interest')
            interest = interest_big.find(class_='field-content').text.strip()
        except Exception as e:
            interest = None
        print("carried interest is:", interest)

        try:
            hurdle_big = soupy.find(class_='field field-name-field-carried-interest')
            hurdle = hurdle_big.find(class_='field-content').text.strip()
        except Exception as e:
            hurdle = None
        print("hurdle rate is:", hurdle)
        driver.get('https://www.impactbase.org/database/targeted-search?page=' + format(str(page)))
        time.sleep(1.5)

        row_dt = pd.DataFrame([[fund_name, firm_name, fund_status, asset_class, target_aum, committed_capital, currency,
                                min_inv,average_inv, max_inv, domicile, inception,vintage, lp, lp_preference, target_geography,
                                impact_theme, style, policy, IRR_target, fee, interest, hurdle,
                                firm_location, fund_contact, fund_contact_job, ]])
        dt = dt.append(row_dt, ignore_index=True)
        print("#####################################################")
        time.sleep(0.5)






















dt.to_excel(r'C://Users//Administrateur//Desktop//project//indeed//impact.xlsx', index=False)




























