import math
from typing import Set, Dict, Any, List, AnyStr

from smart_phone import SmartPhone
from test_data import TestData


def make_phones_set(selected_phones_dict):
    """
    This method iterates on the 'selected_phones_dict' parameter to feed the phone dictionary literals
    in its values to the initializer for the SmartPhone class to create SmartPhone instances.
    These instances are then added to the 'selected_brands_set' which is the return value of the method.

    :param selected_phones_dict: Dict[Str, List]
    :return: selected_brands_set: Set[SmartPhone]
    """
    selected_brands_set: Set[SmartPhone] = set()
    for phones in selected_phones_dict.values():
        for phone in phones:
            selected_brand = SmartPhone(phone)
            selected_brands_set.add(selected_brand)

    return selected_brands_set


def select_phones_of_brands(selected_phone_brands: List[AnyStr]):
    """
    This method selects from the 'phone_dict' dictionary the phone dictionary literals for the
    keys stored in the 'selected_phones_brands' list.
    :return: a Set[SmartPhone] returned by the 'make_phones_set' method.
    """
    phone_dict: Dict[Any, List] = TestData.make_phone_dict()
    selected_phones_of_brands_dict: Dict[Any, List[Any]] = {}
    # If the 'selected_phone_brands' list is not empty, selects the phones whose brands match any brand string
    # in the 'selected_phone_brands' list and populate the 'selected_phones_of_brands_dict' dictionary with
    # the selected phones.
    if len(selected_phone_brands) > 0:
        for phone_brand in selected_phone_brands:
            selected_phones_of_brands_dict[phone_brand] = phone_dict[phone_brand]
    else:  # If the list is empty, the whole phone_dict is returned
        selected_phones_of_brands_dict = phone_dict

    return make_phones_set(selected_phones_of_brands_dict)


def select_phones_in_ranges(ranges: List[Any], key: AnyStr) -> Set[SmartPhone]:
    """
    This method selects from the 'smartphone' list the phones whose quantifiable attributes fall into the given ranges.
    :param ranges: List[Any], a list of ranges which is the value of a dictionary in the 'user_inputs' list
                    for the 'key' parameter
    :param key: AnyStr, the key to retrieve values from the 'smartphones' list based on the calculated range
    :return: selected_phones_set: Set[SmartPhone], a set of phones selected from the 'smartphones' list
    """
    selected_phones_set: set[SmartPhone] = set()

    # Get the minimum and maximum values from the list of ranges passed in by the 'ranges' parameter
    if len(ranges) > 0:
        max_range = max(ranges)
        min_range = min(ranges)
        max_value = max(max_range)
        min_value = min(min_range)
    else:  # if the list of ranges is empty, use the maximum and minimum values from the phone_metrics_dict,
        # i.e. all the available ranges
        max_value = max(TestData.phone_metrics_dict[key])
        min_value = min(TestData.phone_metrics_dict[key])

    # create a range out of the minimum and maximum values obtained in the above if-else block
    the_range = range(min_value, max_value + 1)

    # Select the 'phone' dictionary literals from the smartphones list if their values fall within the above
    # computed range. And feed the selected 'phone' dictionary literals to the initializer of the SmartPhone class
    # to create instances of the SmartPhone class, which are then added to the selected_phones_set.
    for phone in TestData.smartphones:
        if (key == 'price' and math.ceil(phone[key]) in the_range) or \
                (phone[key] in the_range):
            selected_phone = SmartPhone(phone)
            selected_phones_set.add(selected_phone)

    return selected_phones_set


def select_phones_of_attributes(attributes: List[Any], key: AnyStr) -> object:
    """
    This method selects from the 'smartphone' list the phones whose non-quantifiable attributes meet the attributes
    in the 'attributes' parameter.
    :param attributes: List[Any], a list of non-quantifiable attributes of the smartphones in the 'smartphones' list
    :param key: AnyStr, the key to retrieve values from the 'smartphones' list based on the given attributes
    :return: selected_phones_set: Set[SmartPhone], a set of phones selected from the 'smartphones' list
    """
    selected_phones_set: Set[SmartPhone] = set()

    # If the 'attributes' list is not empty, select the 'phone' dictionary literals whose values are found
    # equal to the elements in the 'attribute' list.
    # And it does the same thing the above 'select_phones_in_ranges' method does to the selected objets.
    if len(attributes) > 0:
        for attrib in attributes:
            for phone in TestData.smartphones:
                if attrib == phone[key]:
                    selected_phone = SmartPhone(phone)
                    selected_phones_set.add(selected_phone)
    else:  # If the 'attributes' list is empty, then all the phones in the 'smartphones' list are selected.
        for phone in TestData.smartphones:
            selected_phone = SmartPhone(phone)
            selected_phones_set.add(selected_phone)

    return selected_phones_set


def print_phone_set(phone_set: Set[SmartPhone]):
    """
    This method prints the profile of the list of phones passed in by the 'phone_set' parameter
    :type phone_set: Set[SmartPhone]
    """
    for phone in phone_set:
        print(phone)


def test_input(user_input: Dict[Any, List]) -> object:
    """
    The method invokes various other methods in this module using the keys and values in the dictionary
    passed in by the 'user_input' parameter. Each of those other methods select the phones from the 'smartphone'
    list according to provided product ranges or attributes. The selected phones are returned by each method
    and are put in an empty set declared below. These filled sets are then intersected to obtain the phones
    that matches all the selection criteria. If the result of the set intersection contains phones, the info
    about the phone will be printed. Otherwise, a message will be printed to tell the user search found 0 results.
    :param user_input: Dict[Any, List]
    """
    phones_at_prices: set[Any] = set()
    phones_of_cam_res: set[Any] = set()
    phones_of_ram_sz: set[Any] = set()
    phones_of_year: set[Any] = set()

    for (k, v) in user_input.items():
        if k == 'brands':
            phones_of_brands = select_phones_of_brands(v)
        if k == 'price ranges':
            phones_at_prices = select_phones_in_ranges(v, 'price')
        if k == 'camera resolution ranges':
            phones_of_cam_res = select_phones_in_ranges(v, 'maximum camera resolution')
        if k == 'RAMs':
            phones_of_ram_sz = select_phones_in_ranges(v, 'RAM size')
        if k == 'screen resolutions':
            phones_of_scrn_res = select_phones_of_attributes(v, 'screen resolution')
        if k == 'model years':
            phones_of_year = select_phones_of_attributes(v, 'model year')

    # The '__eq__(self)' and '__hash__(self)' are called when the following set intersection
    # operation is carried out to single out the common elements of the participating sets.
    selected_phones = phones_of_brands & phones_at_prices & phones_of_cam_res \
                      & phones_of_ram_sz & phones_of_scrn_res & phones_of_year

    if len(selected_phones) > 0:
        print(f'Search found {len(selected_phones)} results.')
        print_phone_set(selected_phones)
    else:
        print('Search found 0 results.')


def test_user_inputs() -> object:
    """
    This method serves as the driver to test the program's logic by invoking the 'test_input' method
    with the 'user_input' dictionary as the parameter.
    :rtype: None
    """
    counter = 0

    for user_input in TestData.user_inputs:
        print(f'Testing user input #{counter}:')
        test_input(user_input)
        counter += 1


test_user_inputs()
