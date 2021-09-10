def process_tile(tile_soup):
    # 1. do click into read more...
    # 2. scrape all relevant page fields
    # 3. put into dictionary like example


def process_page(page_soup):
    # get a list of job-tiles from the page soup
    tiles = page_soup.find_all("#job-tile")

    rows = []

    # loop thorugh job-tiles
    for each job-tile in tiles:
        # take in tile soup and return dictionary with fields
        job_df = process_tile(tile)

        # eg = {'job_title' : ["Backend Dev"], 'job_category' : ["Technology"]}

        df = pd.DataFrame(job_df)
        rows.append(df)

    # combine rows into df
    page_df = pd.concat(rows)

    return page_df


def call_scraper:

    offset = 0
    failed = False
    page_dfs = []

    while not failed:
        try:
            # get the soup for one page
            result = request.get(..) # the soup
            # ...

            # take the soup, process it to return DF with desired page fields
            page_df = process_page(result)

            # append the page df to our list
            page_dfs.append(df)

            offset += 10
        except:
            failed = True

    # combine all page dfs and write to file
    all_listings = pd.concat(page_dfs, axis=0)
    all_listings.to_csv("...")


main:
    call_scraper
