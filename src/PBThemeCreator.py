#PB theme creator

import json

class Color:

      def __init__(self, name, info):

            self.name = name
            self.info = info
            self.hex_l = 'ffffff'
            self.hex_d = 'ffffff'
            self.alpha = 1.0

      def get_pbcolors_srgb(self, ask):

            if ask:

                  self.hex_l = self._ask_hex('lightmode')
                  self.hex_d = self._ask_hex('darkmode')

                  self.alpha = self._ask_alpha()   
            
            rgbl = self._get_rgb(self.hex_l)
            rgbd = self._get_rgb(self.hex_d)

            srgbl = '"red":' + str(rgbl[0]/255) + ', "green":' + str(rgbl[1]/255) + ', "blue":' + str(rgbl[2]/255) + ', "alpha":' + str(self.alpha)

            srgbd = '"red":' + str(rgbd[0]/255) + ', "green":' + str(rgbd[1]/255) + ', "blue":' + str(rgbd[2]/255) + ', "alpha":' + str(self.alpha)
            
            srgb = '"lightColor":{' + srgbl + ' }, "darkColor":{' + srgbd + '} }'

            return '"' + color.name + '":{' + srgb

      def _get_rgb(self, hex):

            return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

      def _ask_hex(self, mode):
 
            is_valid = False

            while not is_valid:
                  
                  hex = input('Enter the ' + mode + ' hex: ').lstrip('#')
                  is_valid = self._is_valid_hex(hex)

                  if not is_valid:
                        print("Your input wasn't a hex, please try again.")

            return hex
      
      def _ask_alpha(self):
 
            is_valid = False

            while not is_valid:
                  
                  alpha = input('What is the alpha value? ')
                  is_valid = self._is_valid_alpha(alpha)

                  if not is_valid:
                        print("Your input wasn't a valid alpha value, please try again.")

            return alpha

      def _is_valid_hex(self, hex):

            is_valid = False

            if len(hex) == 6:

                  for i in range(len(hex)):

                        current_character = hex[i].lower()
                        if (current_character >= '0' and current_character <= '9') or (current_character >= 'a' and current_character <= 'f'):
                              is_valid = True

            return is_valid

      def _is_valid_alpha(self, alpha):

            is_valid = False

            try:
                  alpha = float(alpha)
                  if alpha >= 0.0 and alpha <= 1.0:
                        is_valid = True
                  return is_valid
            except:
                  return is_valid

colors = [
      Color('accentColor', 'This are all the red "boxes" in the standard theme. Recommended alpha value = 1.'), 
      Color('accentTextColor', 'This is all the text in the "accentColor" boxes. It is recommended that you use a color that makes it easy to be read. Recommended alpha value = 1.'), 
      Color('foregroundColor', 'This are all the "Boxes" which aren\'t red in the standard theme. Recommended alpha value = 1.'), 
      Color('backgroundColor', 'This is the background in the app. Recommended alpha value = 1.'), 
      Color('overlayColor', 'This is an overlay that is visible when your library or manga view is fetching updates. It is recommended that you use the same color as you used for "backgroundColor". Recommended alpha value = 0.3'), 
      Color('separatorColor', 'This are the thin seperator lines in the app. It is recommended that you use the same color as you did for "accentColor". Recommended alpha value = 1.'), 
      Color('bodyTextColor', 'This is the main text in the app. Recommended alpha value = 1.'), 
      Color('subtitleTextColor', 'This is the secondary text in the app. Recommended alpha value = 1.')
]

results = []

hexes = []

print('Paperback theme creator')

print('This program will automatically create a Paperback theme using hexes and alpha values as input.')

for color in colors:

      print(color.name + ':')

      print(color.info)

      results.append(color.get_pbcolors_srgb(ask=True))

      hexes.append(color.name + ': ' + 'lightmode: ' + color.hex_l + ', ' + 'darkmode: ' + color.hex_d)

results = "{" + ", " .join(results) + " }"

results_dict = json.loads(results)

themename = input('How would you like to call the theme? ')

with open(themename + '.pbcolors', 'w') as json_file:
  json.dump(results_dict, json_file, indent=1)

print('The .pbcolors file was created. To install the theme you will need to share this file with the Paperback app.')

publictheme = input('Is this theme meant to be a public Paperback theme (for more info check: https://github.com/Celarye/Paperback-themes#theme-creation) [y/n]? ')

if publictheme == 'y' or 'Y':

      print(hexes)

      print('Copy the above list and provide it to the theme manager together with the ".pbcolors" file.')

wait = input('Press enter to close the program.')