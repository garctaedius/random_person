from population import data_loader, sampler
from geoinfo import reverse_geocode
from geoinfo.wikipedia_info import WikiFetcher
from presentation import display

if __name__=="__main__":
    wiki_fetcher = WikiFetcher()

    wiki_page = None
    while wiki_page is None:
        place_names = None
        while place_names is None:
            data, transform = data_loader.load_population_data()
            location = sampler.sample_weighted_location(data, transform)

            place_names = reverse_geocode.get_place_name(location)

        wiki_page = wiki_fetcher.get_info(place_names)

    display.print_summary(wiki_page)