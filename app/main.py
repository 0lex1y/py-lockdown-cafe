from .cafe import Cafe
from .errors import NotVaccinatedError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> Cafe:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            print(f"Friends can go to {cafe.name}")
        except NotVaccinatedError:
            print("All friends should be vaccinated")
        except NotWearingMaskError:
            masks_to_buy += 1

    print(f"Friends should buy {masks_to_buy} masks")
