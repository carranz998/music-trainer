from data_scraping.webpage_content import WebpageContent


class BandData:
    @classmethod
    def scrap_name(cls, band_id: int | None) -> str:
        url = f'https://www.metal-archives.com/bands//{band_id}'
        soup = WebpageContent.load(url)

        band_names = [band_data.text for band_data in soup.find_all('h1', class_='band_name')]

        return band_names[0]
