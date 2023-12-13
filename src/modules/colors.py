'''The Colors class file'''


class Colors:
    '''The Colors class'''

    colors_info = {
        'accentColor':
            '  This is for all the non transparent red "boxes" in the standard theme.\n  Recommended alpha value = 1.',

            'accentTextColor':
            '  This is for all the text in those boxes.\n  It is recommended that you use a color that makes it easy to be read.\n  Recommended alpha value = 1.',

            'foregroundColor':
            '  This is for all the "boxes" which aren\'t red in the standard theme.\n  Recommended alpha value = 1.',

            'backgroundColor':
            '  This is for the background in the app.\n  Recommended alpha value = 1.',

            'overlayColor':
            '  This is for an overlay that is visible when your library or manga view is fetching updates.\n  It is recommended that you use the same color as you used for "backgroundColor".\n  Recommended alpha value = 0.3',

            'separatorColor':
            '  This is for all the thin seperator lines in the app.\n  It is recommended that you use the same color as you did for "accentColor".\n  Recommended alpha value = 1.',

            'bodyTextColor':
            '  This is for all the main text in the app.\n  Recommended alpha value = 1.',

            'subtitleTextColor':
            '  This is for all the secondary text in the app.\n  Recommended alpha value = 1.',

            'buttonNormalBackgroundColor':
            '  This is for all the semi-transparent red refresh buttons in the standard theme.\n  Recommended alpha value = 0.3',

            'buttonNormalTextColor':
            '  This is for all the refresh icons in those boxes.\n  It is recommended that you use a color that makes it easy to be read.\n  Recommended alpha value = 0.3.'
    }
    modes = ['light', 'dark']
    colors_values = {
        'accentColor': [
            [0.9919999837875366, 0.41600000858306885, 0.40799999237060547, 1],
            [0.9912440180778503, 0.41505861282348633, 0.406924307346344, 1]
        ],

        'accentTextColor': [
            [1, 1, 1, 1],
            [0.9210000038146973, 0.9210000038146973, 0.9210000038146973, 1]
        ],

        'foregroundColor': [
            [0.987731397151947, 1, 1, 1],
            [0.09000000357627869, 0.09000000357627869, 0.09000000357627869, 1]
        ],

        'backgroundColor': [
            [0.949999988079071, 0.949999988079071, 0.949999988079071, 1],
            [0, 0, 0, 1]
        ],

        'overlayColor': [
            [0.949999988079071, 0.949999988079071, 0.949999988079071, 0.3],
            [0, 0, 0, 0.3]
        ],

        'separatorColor': [
            [0.23529411764705882, 0.23529411764705882, 0.2627450980392157, 0.3],
            [0.32941176470588235, 0.32941176470588235, 0.34509803921568627, 0.3]
        ],

        'bodyTextColor': [
            [0.12999999523162842, 0.12999999523162842, 0.12999999523162842, 1],
            [0.9210000038146973, 0.9210000038146973, 0.9210000038146973, 1]
        ],

        'subtitleTextColor': [
            [0.3709999918937683, 0.3709999918937683, 0.3709999918937683, 1],
            [0.7540000081062317, 0.7540000081062317, 0.7540000081062317, 1]
        ],

        'buttonNormalBackgroundColor': [
            [0.9919999837875366, 0.41600000858306885, 0.40799999237060547, 0.3],
            [0.9912440180778503, 0.41505861282348633, 0.406924307346344, 0.3]
        ],

        'buttonNormalTextColor': [
            [0.12999999523162842, 0.12999999523162842, 0.12999999523162842, 1],
            [0.9210000038146973, 0.9210000038146973, 0.9210000038146973, 1]
        ]
    }

    def __init__(self):
        pass

    @staticmethod
    def hex_validator(hex_code):
        '''Validates the manual HEX code input'''

        is_valid = False

        if len(hex_code) == 6 or len(hex_code) == 3:

            for current_character in hex_code:
                is_valid = (current_character >= '0' and current_character <= '9') or (
                    current_character >= 'a' and current_character <= 'f')

        return is_valid

    @staticmethod
    def hex_to_srgb(hex_code):
        '''Takes the valid HEX code and returns sRGB values'''

        match len(hex_code):
            case 3:
                return [value/255 for value in tuple(int(2 * hex_code[i], 16)
                                                     for i in (0, 1, 2))]

            case 6:
                return [value/255 for value in tuple(int(hex_code[i:i+2], 16)
                                                     for i in (0, 2, 4))]

    @staticmethod
    def rgb_validator(rgb_value):
        '''Validates the manual RGB value input one by one'''

        is_valid = False

        try:
            rgb_value = float(rgb_value)

            if rgb_value.is_integer():
                is_valid = rgb_value <= 255 and rgb_value >= 0

        except ValueError:
            pass

        return is_valid

    @staticmethod
    def rgb_to_srgb(rgb_values):
        '''Takes the valid RGB values and returns sRGB values'''

        return [int(value)/255 for value in rgb_values]

    @staticmethod
    def alpha_validator(alpha_value):
        '''Validates the manual alpha value input'''

        is_valid = False

        try:
            alpha_value = float(alpha_value)

            is_valid = alpha_value <= 1 and alpha_value >= 0

        except ValueError:
            pass

        return is_valid
