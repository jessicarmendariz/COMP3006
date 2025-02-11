def cheapest(properties_dict, state):
    #Takes the property_dict and a State or Territory as Arguments
    #Returns the Property Container for the Cheapest Property
    try:
        properties = properties_dict['US States'].get(state, []) + properties_dict['Territories'].get(state, [])
        return min(
            (p for p in properties if p.price.replace('.', '', 1).isdigit()),
            key=lambda p: float(p.price),
            default=None
        )
    except ValueError:
        return None


def priciest(properties_dict, state):
    #Takes the property_dict and a State or Territory as Arguments
    #Returns the Property Container for the Priciest Property
    try:
        properties = properties_dict['US States'].get(state, []) + properties_dict['Territories'].get(state, [])
        return max(
            (p for p in properties if p.price.replace('.', '', 1).isdigit()),
            key=lambda p: float(p.price),
            default=None
        )
    except ValueError:
        return None


def dirt_cheap(properties_dict):
    #Takes the property_dict and a State or Territory as Arguments
    #Returns the Property Container for the Cheapest Property In All States
    return min(
        (prop for state in properties_dict.values() for props in state.values() for prop in props if prop.price.replace('.', '', 1).isdigit()),
        key=lambda p: float(p.price),
        default=None
    )


def best_deal(properties_dict, state, beds, baths):
    #Takes the property_dict and a State or Territory, Beds, and Baths as Arguments
    #Returns the Property Container for the Best Price Per Square Foot Property
    properties = properties_dict['US States'].get(state, []) + properties_dict['Territories'].get(state, [])
    valid_props = [
        p for p in properties
        if p.bed.isdigit() and int(p.bed) == beds
        and p.bath.replace('.', '', 1).isdigit() and float(p.bath) == baths
        and p.house_size.replace('.', '', 1).isdigit() and float(p.house_size) > 0
        and p.price.replace('.', '', 1).isdigit() and float(p.price) > 0
    ]
    return min(valid_props, key=lambda p: float(p.price) / float(p.house_size), default=None)


def budget_friendly(properties_dict, beds, baths, budget):
    #Takes the property_dict and a State or Territory, Beds, Baths, and Budget as Arguments
    #Returns the Property Container for the Best Bang For Your Buck Property
    valid_props = [
        p for state in properties_dict.values() for props in state.values() for p in props
        if p.bed.isdigit() and int(p.bed) == beds
        and p.bath.replace('.', '', 1).isdigit() and float(p.bath) == baths
        and p.price.replace('.', '', 1).isdigit() and float(p.price) <= budget
        and p.house_size.replace('.', '', 1).isdigit() and float(p.house_size) > 0
        ]
    return min(valid_props, key=lambda p: float(p.price) / float(p.house_size), default=None)
