'''The main script file'''

import os
import json
import re
import webbrowser

from jsonschema import validate
from jsonschema import exceptions

from modules.pbcolors import Pbcolors
from modules.colors import Colors


class Main:
    '''The Main class, handles as central controller and input handler of the script'''

    input_method_type = ''

    schema = ''

    def __init__(self):
        pass

    @staticmethod
    def intro():
        '''Prints the program intro to the CLI and runs the correct methods to run trough the script'''

        print('''#############################
#                           #
#  Paperback Theme Creator  #
#                           #
#############################''')

        print('\nThis program will automatically create a Paperback theme using either manual entered values or a .pbcolors/.json file.')

        print('\n1. Allowed manual input types:')
        print('  - HEX codes and alpha values')
        print('  - RGBA values')

        print(
            '\n2. Allowed file input structures (the file type must be .pbcolors or .json):')
        print('  - HEX codes and alpha values')
        print('  - RGBA values')
        print('  - sRGBA values')

        print('\nTips:')

        print('  - Type "help" into the input field bellow to see examples of the manual input types and the allowed file structures.')

        print('  - You can enter "input" to change the input method while in manual input mode.')

        print('  - Not entering a value in a manual input field will cause it to use the default color.')

        print('\n##########################')

        Main._input_method()

    @staticmethod
    def _input_method():
        '''Asks the input method and runs the according method based on it'''

        is_valid_input_method = False

        while not is_valid_input_method:
            input_method = input(
                '\nDo you have a .pbcolors or .json file (otherwise you will need to use manual input) [y/n/help]? ').lower()

            match input_method:
                case 'y':
                    is_valid_input_method = True
                    Main._file_input()

                case 'n':
                    is_valid_input_method = True

                    print(
                        '\nThe script will walk you trough all the required values now.')

                    is_valid_input_method_type = False

                    while not is_valid_input_method_type:

                        Main.input_method_type = input(
                            '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

                        match Main.input_method_type:
                            case 'hex+a':
                                is_valid_input_method_type = True

                            case 'rgba':
                                is_valid_input_method_type = True

                            case _:
                                print(
                                    '  Your input method type wasn\'t recognized, make sure to use one if the available input method types.')

                    for color, value in Colors.colors_info.items():
                        print(f'\n{color[0].upper() + color[1:]}:')
                        print(value)

                        for mode_index, mode in enumerate(Colors.modes):
                            print(f'\n  {mode.capitalize()}mode:')

                            Main._manual_input(color, mode_index)

                            while Main.input_method_type == '':
                                Main.input_method_type = input(
                                    '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

                                Main._manual_input(color, mode_index)

                    print('\n##########################')

                    Main._theme_info_input()

                case 'help':
                    print(
                        '\nExamples of the manual input types and the allowed file structures:')

                    print('\n  - Allowed manual input types:')

                    print('\n    - HEX codes and alpha values:')
                    print('      - Example hex code: #5e81ac')
                    print('      - Example alpha value: 0.3')

                    print('\n    - RGBA values:')
                    print('      - Example red, green or blue value: 173')
                    print('      - Example alpha value: 0.3')

                    print('\n  - Allowed file structures:')

                    print('\n    - HEX codes and alpha values:')
                    print('''
      {
          'accentColor': {
              'lightColor': {
                  'hexCode': '#5e81ac',
                  'alpha': 1
              },
              'darkColor': {
                  'hexCode': '#5e81ac',
                  'alpha': 1
              }
          },
          file continues...''')

                    print('\n    - RGBA values:')
                    print('''
      {
          'accentColor': {
              'lightColor': {
                  'red': 253,
                  'green': 106,
                  'blue': 104,
                  'alpha': 1
              },
              'darkColor': {
                  'red': 253,
                  'green': 106,
                  'blue': 104,
                  'alpha': 1
              }
          },
          file continues...''')

                    print('\n    - sRGBA values:')
                    print('''
      {
          'accentColor': {
              'lightColor': {
                  'red': 0.9919999837875366,
                  'green': 0.41600000858306885,
                  'blue': 0.40799999237060547,
                  'alpha': 1
              },
              'darkColor': {
                  'red': 0.9912440180778503,
                  'green': 0.41505861282348633,
                  'blue': 0.406924307346344,
                  'alpha': 1
              }
          },
          file continues...''')

                case _:
                    print(
                        '  Your input wasn\'t recognized, try again.')

    @staticmethod
    def _file_input():
        '''Asks the path to the file and loads its content'''

        print(f'\nYour current working directory: {os.getcwd()}')

        file_path = input('\nPath to the .pbcolors or .json file: ')

        while not (file_path.endswith('.pbcolors') or file_path.endswith('.json')):
            print(
                f'  "{file_path}" wasn\'t a valid path to a .pbcolors or .json file, try again.')

            file_path = input(
                '\nPath to the .pbcolors or .json file: ')

        file = {}

        while not file:
            try:
                file = json.load(open(file_path, encoding='utf8'))

                if file_path.endswith('.pbcolors'):
                    print('  Succesfully loaded the .pbcolors file.')

                elif file_path.endswith('.json'):
                    print('  Succesfully loaded the .json file.')

            except json.JSONDecodeError as e:
                print(f'  Error decoding the .pbcolors file: {
                      e}. Make sure that the file its structure is valid JSON.')

                file_path = input('\nPath to the .pbcolors or .json file: ')

            except FileNotFoundError:
                print(
                    f'  "{file_path}" wasn\'t a valid path to a .pbcolors or .json file, try again.')

                file_path = input('\nPath to the .pbcolors or .json file: ')

        print('\n##########################')

        Main._file_processing(file)

    @staticmethod
    def _file_processing(file):
        '''Processing of the file'''

        for color, value in Colors.colors_info.items():
            print(f'\n{color[0].upper() + color[1:]}:')
            print(value)

            try:
                for mode_index, mode in enumerate(Colors.modes):
                    print(f'\n  {mode.capitalize()}mode:')

                    hex_a_schema = {
                        '$schema': 'https://json-schema.org/draft/2020-12/schema',
                        'type': 'object',
                        'properties': {
                            f'{mode}Color': {
                                'type': 'object',
                                'properties': {
                                    'hexCode': {
                                        'type': 'string',
                                        'pattern': '^#?[A-Fa-f0-9]{3}([A-Fa-f0-9]{3})?$',
                                    },
                                    'alpha': {
                                        'type': 'number',
                                        'minimum': 0,
                                        'maximum': 1
                                    }
                                },
                                'required': [
                                    'hexCode', 'alpha'
                                ]
                            }
                        },
                        'required': [
                            f'{mode}Color',
                        ]
                    }

                    rgba_schema = {
                        '$schema': 'https://json-schema.org/draft/2020-12/schema',
                        'type': 'object',
                        'properties': {
                            f'{mode}Color': {
                                'type': 'object',
                                'properties': {
                                    'red': {
                                        'type': 'integer',
                                        'minimum': 0,
                                        'maximum': 255
                                    },
                                    'green': {
                                        'type': 'integer',
                                        'minimum': 0,
                                        'maximum': 255
                                    },
                                    'blue': {
                                        'type': 'integer',
                                        'minimum': 0,
                                        'maximum': 255
                                    },
                                    'alpha': {
                                        'type': 'number',
                                        'minimum': 0,
                                        'maximum': 1
                                    }
                                },
                                'required': [
                                    'red',
                                    'green',
                                    'blue',
                                    'alpha'
                                ]
                            }
                        },
                        'required': [
                            f'{mode}Color'
                        ]
                    }

                    srgba_schema = {
                        '$schema': 'https://json-schema.org/draft/2020-12/schema',
                        'type': 'object',
                        'properties': {
                            f'{mode}Color': {
                                'type': 'object',
                                'properties': {
                                    'red': {
                                        'type': 'integer',
                                        'minimum': 0,
                                        'maximum': 255
                                    },
                                    'green': {
                                        'type': 'integer',
                                        'minimum': 0,
                                        'maximum': 255
                                    },
                                    'blue': {
                                        'type': 'integer',
                                        'minimum': 0,
                                        'maximum': 255
                                    },
                                    'alpha': {
                                        'type': 'number',
                                        'minimum': 0,
                                        'maximum': 1
                                    }
                                }
                            }
                        },
                        'required': [
                            f'{mode}Color'
                        ]
                    }

                    try:
                        validate(instance=file[color],
                                 schema=hex_a_schema)

                        found_schema = 'hex_a_schema'

                        if Main.schema != found_schema:

                            Main.schema = found_schema

                            print(
                                '\n    Found schema: HEX color codes + alpha values')

                        print('\n    Found values:')
                        print(
                            f'      - Hex Code: #{file[color][mode + 'Color']['hexCode'].lstrip('#')}')
                        print(
                            f'      - Alpha: {file[color][mode + 'Color']['alpha']}')

                        match Main._replace_file_values():
                            case 'y':
                                match Main.input_method_type:
                                    case '':
                                        Main.input_method_type = input(
                                            '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

                                Main._manual_input(color, mode_index)

                                while Main.input_method_type == '':
                                    Main.input_method_type = input(
                                        '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

                                    Main._manual_input(color, mode_index)

                            case _:
                                value = Colors.colors_values[color][mode_index]

                                for index, srgb_value in enumerate(Colors.hex_to_srgb(file[color][mode +
                                                                                                  'Color']['hexCode'].lstrip('#'))):
                                    value[index] = srgb_value

                                value[-1] = float(file[color]
                                                  [mode + 'Color']['alpha'])

                                Colors.colors_values[color][mode_index] = value

                                Pbcolors.pbcolors_generation(
                                    '.temp')

                    except exceptions.ValidationError:
                        try:
                            validate(instance=file[color],
                                     schema=rgba_schema)

                            found_schema = 'rgba_schema'

                            if Main.schema != found_schema:

                                Main.schema = found_schema

                                print('\n    Found schema: RGBA values')

                            print('\n    Found values:')
                            print(
                                f'      - Red: {file[color][mode + 'Color']['red']}')
                            print(
                                f'      - Green: {file[color][mode + 'Color']['green']}')
                            print(
                                f'      - Blue: {file[color][mode + 'Color']['blue']}')
                            print(
                                f'      - Alpha: {file[color][mode + 'Color']['alpha']}')

                            match Main._replace_file_values():
                                case 'y':
                                    match Main.input_method_type:
                                        case '':
                                            Main.input_method_type = input(
                                                '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

                                    Main._manual_input(color, mode_index)

                                    while Main.input_method_type == '':
                                        Main.input_method_type = input(
                                            '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

                                        Main._manual_input(color, mode_index)

                                case _:
                                    value = Colors.colors_values[color][mode_index]

                                    for index, color in enumerate(['red', 'green', 'blue']):
                                        value[index] = file[color][mode +
                                                                   'Color'][color]

                                    value[-1] = float(file[color]
                                                      [mode + 'Color']['alpha'])

                                    Colors.colors_values[color][mode_index] = value

                                    Pbcolors.pbcolors_generation(
                                        '.temp')

                        except exceptions.ValidationError:
                            try:
                                validate(instance=file[color],
                                         schema=srgba_schema)

                                found_schema = 'srgba_schema'

                                if Main.schema != found_schema:

                                    Main.schema = found_schema

                                    print('\n    Found schema: sRGBA values')

                                print('\n    Found values:')
                                print(
                                    f'      - Red: {file[color][mode + 'Color']['red']}')
                                print(
                                    f'      - Green: {file[color][mode + 'Color']['green']}')
                                print(
                                    f'      - Blue: {file[color][mode + 'Color']['blue']}')
                                print(
                                    f'      - Alpha: {file[color][mode + 'Color']['alpha']}')

                                match Main._replace_file_values():
                                    case 'y':
                                        match Main.input_method_type:
                                            case '':
                                                Main.input_method_type = input(
                                                    '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

                                        Main._manual_input(color, mode_index)

                                        while Main.input_method_type == '':
                                            Main.input_method_type = input(
                                                '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

                                            Main._manual_input(
                                                color, mode_index)

                                    case _:
                                        value = Colors.colors_values[color][mode_index]

                                        for index, color in enumerate(['red', 'green', 'blue']):
                                            value[index] = file[color][mode +
                                                                       'Color'][color]

                                        value[-1] = float(file[color]
                                                          [mode + 'Color']['alpha'])

                                        Colors.colors_values[color][mode_index] = value

                                        Pbcolors.pbcolors_generation(
                                            '.temp')

                            except exceptions.ValidationError:
                                print('  The '' + color + '' values for ' + mode +
                                      'mode were unable to be parsed, you will need to enter them manually.')

                                Main._manual_input(color, mode_index)

            except KeyError:
                print('  The "' + color +
                      '" values were not found, you will need to enter them manually.')

                Main._manual_input(color, mode_index)

        print('\nFinished processing the provided file!')

        print('\n##########################')

        Main._theme_info_input()

    @staticmethod
    def _replace_file_values():
        '''Asks the user if they want to use the values processed by the file they provided'''

        return input(
            '\n    Do you want to replace the found values [y/N]?').lower()

    @staticmethod
    def _manual_input(color, mode_index):
        '''Asks the manual input method type and runs the according method based on it'''

        is_valid_input_method_type = False

        while not is_valid_input_method_type:

            match Main.input_method_type:
                case 'hex+a':
                    is_valid_input_method_type = True

                    Main._hex_a_input(color, mode_index)

                case 'rgba':
                    is_valid_input_method_type = True

                    Main._rgba_input(color, mode_index)

                case _:
                    print(
                        '  Your input method type wasn\'t recognized, make sure to use one if the available input method types.')

                    Main.input_method_type = input(
                        '\nWhat manual input method type do you want to use [hex+a/rgba]? ').lower()

    @staticmethod
    def _hex_a_input(color, mode_index):
        '''Asks the user for the HEX code and alpha value'''

        is_valid_hex = False

        value = Colors.colors_values[color][mode_index]

        while not is_valid_hex:
            hex_code = input(
                '\n    Enter the HEX code: ').strip('#').lower()

            match hex_code:
                case 'input':
                    Main.input_method_type = ''
                    return

                case '':
                    print('      Empty input detected, using the default value.')

                    is_valid_hex = True

                case _:
                    is_valid_hex = Colors.hex_validator(hex_code)

                    if not is_valid_hex:
                        print(
                            '      Your input wasn\'t a HEX code, please try again.')

                    else:
                        for index, srgb_value in enumerate(Colors.hex_to_srgb(hex_code)):
                            value[index] = srgb_value

        is_valid_alpha = False

        while not is_valid_alpha:
            alpha_value = input('\n    Enter the alpha value: ')

            match alpha_value:
                case 'input':
                    Main.input_method_type = ''
                    return

                case '':
                    print('      Empty input detected, using the default value.')

                    is_valid_alpha = True

                case _:
                    is_valid_alpha = Colors.alpha_validator(alpha_value)

                    if not is_valid_alpha:
                        print(
                            '      Your input wasn\'t a correct alpha value, please try again.')

                    else:
                        value[-1] = float(alpha_value)

        Colors.colors_values[color][mode_index] = value

        Pbcolors.pbcolors_generation(
            '.temp')

    @staticmethod
    def _rgba_input(color, mode_index):
        '''Asks the user for the RGBA values'''

        value = Colors.colors_values[color][mode_index]

        rgb_values = [None, None, None]

        print('\n    Enter the RGBA values: ')

        for index, rgb_color in enumerate(['red', 'green', 'blue']):
            is_valid_rgb_value = False

            while not is_valid_rgb_value:

                rgb_values[index] = input(
                    f'      - {rgb_color.capitalize()} value: ')

                match rgb_values[index]:
                    case 'input':
                        Main.input_method_type = ''
                        return

                    case '':
                        print(
                            '        Empty input detected, using the default value.')

                        is_valid_rgb_value = True

                        default_value = True

                        # FIXME: fix proper break

                    case _:
                        is_valid_rgb_value = Colors.rgb_validator(
                            rgb_values[index])

                        if not is_valid_rgb_value:
                            print(
                                '        Your input wasn\'t a valid RGB value, please try again.\n')

                        else:
                            default_value = False
            match default_value:
                case True:
                    break

                case False:
                    pass

        match default_value:
            case False:
                for index, srgb_value in enumerate(Colors.rgb_to_srgb(rgb_values)):
                    value[index] = srgb_value

            case True:
                pass

        is_valid_alpha = False

        while not is_valid_alpha:
            alpha_value = input('      - Alpha value: ')

            match alpha_value:
                case 'input':
                    Main.input_method_type = ''
                    return

                case '':
                    print('        Empty input detected, using the default value.')

                    is_valid_alpha = True

                case _:
                    is_valid_alpha = Colors.alpha_validator(alpha_value)

                    if not is_valid_alpha:
                        print(
                            '        Your input wasn\'t a correct alpha value, please try again.\n')
                    else:
                        value[-1] = float(alpha_value)

        Colors.colors_values[color][mode_index] = value

        Pbcolors.pbcolors_generation(
            '.temp')

    @staticmethod
    def _theme_info_input():
        '''Asks the user for theme info'''

        valid_input = False

        while not valid_input:

            theme_name = input(
                '\nHow do you want to name your Paperback theme (only alphanumerics, dashes and underscores are accepted, no spaces)? ')

            match bool(re.match(r'^[A-Za-z0-9-_]+$', theme_name)):
                case False:
                    print('  Not valid input, try again.')

                case True:
                    valid_input = True

        valid_input = False

        while not valid_input:

            public_theme = input(
                '\nWill this be a public theme (type \'help\' for more info) [y/n/help]? ').lower()

            match public_theme:
                case 'y':
                    public_theme = True

                    valid_input = False

                    while not valid_input:

                        creator = input(
                            '  \nWhat name would you like to go by (only alphanumerics, dashes and underscores are accepted, no spaces)? ')

                        match bool(re.match(r'^[A-Za-z0-9-_]+$', creator)):
                            case False:
                                print('    Not valid input, try again.')

                            case True:
                                valid_input = True

                    Pbcolors.pbcolors_generation(
                        theme_name, public_theme, creator)

                    os.remove('.temp.pbcolors')

                    link = print(
                        'Can this script open a link to a GitHub issue in the Celarye/paperback-themes repository in your web browser (a GitHub account is required)?\nThis issue will make it possible to review your theme and add it to the public list of themes [y/N].').lower()

                    match link:
                        case 'y':
                            print(
                                f'Openening the following link: https://github.com/Celarye/paperback-themes/issues/new?template=new-theme&title=%5BNEW%20THEME%5D%20{theme_name}')
                            webbrowser.open(
                                f'https://github.com/Celarye/paperback-themes/issues/new?template=new-theme&title=%5BNEW%20THEME%5D%20{theme_name}')

                        case _:
                            print(
                                '\nYou will need to manually open an issue in this GitHub repository: https://github.com/Celarye/paperback-themes')

                    valid_input = True

                case 'n':
                    Pbcolors.pbcolors_generation(theme_name)

                    os.remove('.temp.pbcolors')

                    valid_input = True

                case 'help':
                    print(
                        '\nPublic themes are themes which are made available to all the Paperback users through the Celarye/paperback-themes GitHub repository and the official Discord (#themes channel).')

                case _:
                    print(
                        '  Your input wasn\'t recognized, try again.')

        Main._end(False)

    @staticmethod
    def _end(public_theme=False):
        print('\nYour theme file was created, you can now share it with the Paperback app.')

        print('\nTip: You can just restart the script and choose the file input method to edit the theme you just made.')

        match public_theme:
            case True:
                print(
                    '\nIt is recommended that you make a GitHub issue in the case that you didn\'t make one yet, it is the only way for your theme to be added to the public list.')

            case _:
                pass

        input('\nPress any key to end the script...')


if __name__ == '__main__':
    Main.intro()
