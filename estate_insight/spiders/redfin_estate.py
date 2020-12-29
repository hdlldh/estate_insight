import scrapy
import pandas as pd
from io import BytesIO

class RedfinEstateSpider(scrapy.Spider):
    name = 'redfin_estate'
    allowed_domains = ['redfin.com']

    def __init__(self):
        regions = pd.read_csv("estate_insight/resources/redfin_regions.csv")
        url_base = 'https://www.redfin.com/stingray/api/gis-csv?al=1&market=sanfrancisco&num_homes=350&ord=redfin-recommended-asc&page_number=1&region_id=%s&region_type=6&sf=1,2,3,5,6,7&sp=true&status=9&uipt=1,2,3,4,5,6&v=8'
        self.start_urls = [url_base % region_id for region_id in regions['RegionId']]

    def parse(self, response):
        data = BytesIO(response.body)
        df = pd.read_csv(data, dtype=object)
        df = df.fillna("")
        for idx, row in df.iterrows():
            # print(dict(row))
            yield dict(row)
