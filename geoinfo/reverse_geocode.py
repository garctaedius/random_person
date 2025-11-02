from geopy.geocoders import Nominatim
from geopy.location import Location as GeopyLoc

from util.named_types import Location

def get_place_name(location: Location) -> list[str]|None:
    geolocator = Nominatim(user_agent="random_person_selection")
    loc = geolocator.reverse((location.latitude, location.longitude), exactly_one=True, addressdetails=True)
    if not isinstance(loc, GeopyLoc) or "address" not in loc.raw:
        return None
    
    address = loc.raw["address"]

    # Get name of place from address, trying to find a name, going from small to large
    # (every address has a country tag, so that is the fallback)
    place_names = [address.get("town"), address.get("city"), address.get("county"), address.get("state"), address.get("region"), address.get("country")]
    place_names = [name for name in place_names if isinstance(name, str)]

    return place_names