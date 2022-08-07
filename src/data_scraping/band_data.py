from dynamic_web_scraper.webpage_content import WebpageContent


class BandData:
    @classmethod
    def scrap_name(cls, band_id: int | None) -> str:
        url = f'https://www.metal-archives.com/bands//{band_id}'
        soup = WebpageContent.load(url)

        found_band_names = soup.find_all('h1', class_='band_name')
        band_name = [band_data.text for band_data in found_band_names][0]

        return band_name
