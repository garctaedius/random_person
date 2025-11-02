import wikipedia
from wikipedia import WikipediaPage

class WikiFetcher:
    def __init__(self, language="en"):
        wikipedia.set_lang(language)
        wikipedia.set_rate_limiting(True)

    def get_info(self, place_names: list[str]) -> WikipediaPage|None:
        page = None
        for place in place_names:
            try:
                page = wikipedia.page(place, preload=True)
                return page
            except:
                continue
        
        return None
