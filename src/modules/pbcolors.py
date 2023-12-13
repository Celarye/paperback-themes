'''The Pbcolors class file'''

import json

from modules.colors import Colors


class Pbcolors:
    '''The Pbcolors class, handles .pbcolors file creation'''

    def __init__(self):
        pass

    @staticmethod
    def pbcolors_generation(theme_name='theme', public_theme=False, creator=''):
        '''Takes the sRGBA color values from the Colors class and creates a .pbcolors file'''

        pbcolors = {}

        if public_theme:
            pbcolors['creator'] = creator

        for color, values in Colors().colors_values.items():
            pbcolors[color] = {}

            for mode_index, mode in enumerate(Colors().modes):
                pbcolors[color][mode + 'Color'] = {}

                for value_index, value in enumerate(['red', 'green', 'blue', 'alpha']):
                    pbcolors[color][mode +
                                    'Color'][value] = values[mode_index][value_index]

        with open(theme_name + '.pbcolors', 'w', encoding='utf-8') as json_file:
            json.dump(pbcolors, json_file, indent=1)
