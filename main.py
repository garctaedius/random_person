from population import data_loader, sampler
from geoinfo import reverse_geocode, wikipedia_info
from presentation import display

if __name__=="__main__":
    data, transform = data_loader.load_population_data()
    location = sampler.sample_weighted_location(data, transform)

    place = reverse_geocode.get_place_name(location)
    info = wikipedia_info.get_info_from_place(place)

    display.print_summary(info)