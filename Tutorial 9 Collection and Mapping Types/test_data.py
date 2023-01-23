import math


class TestData:
    # NOTE: All the product info from amazon.com and other websites is NOT for advertising purpose
    # The smartphones list may be read from a cache of most frequently queried data
    smartphones = [
        {'brand': 'Samsung', 'model': 'Galaxy A13 Smartphone', 'price': 297.98, 'maximum camera resolution': 50,
         'screen resolution': '1080 x 2408', 'cellular tech': '4 G', 'screen size': 6.6, 'RAM size': 4,
         'model year': 2022},
        {'brand': 'Xiaomi', 'model': 'Redmi Note 11', 'price': 329.00, 'maximum camera resolution': 50,
         'screen resolution': '1080 x 2400', 'cellular tech': '4 G', 'screen size': 6.43, 'RAM size': 6,
         'model year': 2022},
        {'brand': 'Samsung', 'model': 'Galaxy A53', 'price': 597.00, 'maximum camera resolution': 64,
         'screen resolution': '1080 x 2400', 'cellular tech': '5 G', 'screen size': 6.43, 'RAM size': 6,
         'model year': 2022},
        {'brand': 'Google', 'model': 'Pixel 6a', 'price': 475.80, 'maximum camera resolution': 12,
         'screen resolution': '1080 x 2400', 'cellular tech': '5 G', 'screen size': 6.1, 'RAM size': 6,
         'model year': 2022},
        {'brand': 'Apple', 'model': 'iPhone 12 Pro Max', 'price': 970.00, 'maximum camera resolution': 63,
         'screen resolution': '2778 x 1284', 'cellular tech': '5 G', 'screen size': 6.1, 'RAM size': 6,
         'model year': 2021},
        {'brand': 'Samsung', 'model': 'Galaxy S21 FE', 'price': 749.00, 'maximum camera resolution': 32,
         'screen resolution': '2778 x 1284', 'cellular tech': '5 G', 'screen size': 6.1, 'RAM size': 6,
         'model year': 2022},
        {'brand': 'Nokia', 'model': 'G21', 'price': 239.00, 'maximum camera resolution': 32,
         'screen resolution': '2778 x 1284', 'cellular tech': '4 G', 'screen size': 6.1, 'RAM size': 4,
         'model year': 2022},
        {'brand': 'Apple', 'model': 'iPhone 13', 'price': 1227.00, 'maximum camera resolution': 48,
         'screen resolution': '2778 x 1284', 'cellular tech': '5 G', 'screen size': 6.1, 'RAM size': 6,
         'model year': 2022},
        {'brand': 'Nokia', 'model': 'XR20', 'price': 647.99, 'maximum camera resolution': 48,
         'screen resolution': '1080 x 2400', 'cellular tech': '5 G', 'screen size': 6.67, 'RAM size': 6,
         'model year': 2021},
        {'brand': 'Google', 'model': 'Pixel 6', 'price': 1189.69, 'maximum camera resolution': 50,
         'screen resolution': '1440 x 3120', 'cellular tech': '5 G', 'screen size': 6.7, 'RAM size': 12,
         'model year': 2021},
        {'brand': 'Nokia', 'model': 'C3', 'price': 165.00, 'maximum camera resolution': 8,
         'screen resolution': '720 x 1440', 'cellular tech': '4 G', 'screen size': 5.99, 'RAM size': 2,
         'model year': 2021},
        {'brand': 'Apple', 'model': 'iPhone 14', 'price': 1379.00, 'maximum camera resolution': 63,
         'screen resolution': '2532 x 1170', 'cellular tech': '5 G', 'screen size': 6.1, 'RAM size': 6,
         'model year': 2022},
        {'brand': 'Xiaomi', 'model': 'Poco F4 GT', 'price': 873.00, 'maximum camera resolution': 64,
         'screen resolution': '1080 x 2400', 'cellular tech': '5 G', 'screen size': 6.67, 'RAM size': 12,
         'model year': 2022},
    ]

    # user inputs for tests. An empty list as the value for a key is taken for choosing all products
    # in the aspect specified by the key.
    user_inputs = [{'brands': ['Apple', 'Google'], 'price ranges': [(300, 500), (800, 1200)],
                    'camera resolution ranges': [(30, 50)], 'RAMs': [(4, 8, 12)],
                    'screen resolutions': ['1080 x 2400', '2778 x 1284', '1440 x 3120'], 'model years': [2021, 2022]},
                   {'brands': ['Google', 'Xiaomi'], 'price ranges': [(300, 500), (500, 800)],
                    'camera resolution ranges': [], 'RAMs': [(4, 8)],
                    'screen resolutions': [], 'model years': [2022]},
                   {'brands': [], 'price ranges': [(500, 800), (800, 1200)],
                    'camera resolution ranges': [(50, 70)], 'RAMs': [],
                    'screen resolutions': [], 'model years': []}
                   ]
    phone_metrics_dict = {}

    @staticmethod
    def get_range(data_set, key=None):
        """
            :param data_set: Set[Dict]
            :param key: Str default value: None
            Get the range between the minimum and maximum values in the data set
        """

        # if the key is 'price', round the values in data_set up to the nearest integer
        if key:
            data_set = [math.ceil(value) for value in data_set]

        min_value = min(data_set)
        max_value = max(data_set)

        return range(min_value, max_value + 1)

    @staticmethod
    def make_phone_dict():
        """
            Group the dictionary literals in the smart_phone list by creating a dictionary whose keys are strings
            from the 'brands' set and whose values are the dictionary literals from the 'smart_phones' list,
            like below:

            {'Apple': [{'brand': 'Apple', 'model': 'iPhone 14', 'price': 1379.00, 'maximum camera resolution': 63,
                   'screen resolution:': '2532 x 1170', 'cellular tech': '5 G', 'screen size': 6.1, 'RAM size': 6,
                   'model year': 2022}, ...],
                   'Google': [{'brand': 'Google', 'model': 'Pixel 6', 'price': 1189.69, 'maximum camera resolution': 50,
                   'screen resolution:': '1440 x 3120', 'cellular tech': '5 G', 'screen size': 6.7, 'RAM size': 12,
                   'model year': 2021}...],
            'Google': [...],
            'Nokia': [...],
            'Samsung': [...],
            'Xiaomi': [...],
            }
        """

        TestData.get_test_metrics()

        # Fill the 'phones' empty dictionary with the value for the 'brand' key in each dictionary literal
        # in the smartphone list as its keys and each dictionary literal as its values.
        phones = {}
        for brand in TestData.phone_metrics_dict['brand']:
            phones[brand] = []
            for product in TestData.smartphones:
                if brand == product['brand']:
                    phones[brand].append(product)

        return phones

    @staticmethod
    def get_test_metrics():
        """
        This method first traverse through the smartphone list and from each dictionary literal selects
        the values corresponding to the keys in the raw_data_keys frozenset.

        It then surveys the quantifiable values such as 'price', 'maximum camera resolution'
        to find the minimum and maximum and creates a range out of each pair of extrema. This range is
        then paired up with a suitable key in the phone_metric_dict dictionary.

        The phone_metric_dict also contains non-quantifiable values for such keys as 'brand',
        'screen resolution' and model year.

        :return: None
        """
        raw_data_keys = frozenset(
            {'brand', 'price', 'maximum camera resolution', 'screen resolution', 'RAM size', 'model year'})

        # Create an empty set as the initial value for each key in the raw_data_dict dictionary
        raw_data_dict = {}
        for k in raw_data_keys:
            raw_data_dict[k] = set()

        # Fill raw_data_dict with data from smartphones list for the corresponding keys from the raw_data_keys set
        for phone in TestData.smartphones:  # phone represents a dictionary in the smartphones list
            for dataKey in raw_data_keys:
                for (k, v) in phone.items():
                    # value in 'phone' under the key that equals to 'dataKey' is added to the set of values
                    if dataKey == k:
                        raw_data_dict[dataKey].add(v)

        # Fill the metrics_dict with values which are directly from or created out of the values
        # in the raw_data_dict for the corresponding keys
        for rdk in raw_data_keys:
            if rdk == 'price' or rdk == 'maximum camera resolution' or rdk == 'RAM size':
                if rdk == 'price':
                    TestData.phone_metrics_dict[rdk] = TestData.get_range(raw_data_dict[rdk], rdk)
                else:
                    TestData.phone_metrics_dict[rdk] = TestData.get_range(raw_data_dict[rdk])
            else:
                TestData.phone_metrics_dict[rdk] = raw_data_dict[rdk]
