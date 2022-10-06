#PB theme creator

class Color:

      def __init__(self, name, info):

            self.name = name
            self.info = info
            self.hex_l = 'ffffff'
            self.hex_d = 'ffffff'
            self.alpha = 1.0

      def get_pbcolors_srgb(self, ask):

            if ask:
                  self.hex_l = input('Enter the lightmode hex: ').lstrip('#')
                  
                  self.hex_d = input('Enter the darkmode hex: ').lstrip('#')

                  self.alpha = input('What is the alpha value? ')            
            
            rgbl = self._get_hex(self.hex_l)
            rgbd = self._get_hex(self.hex_d)

            srgbl = '"red": ' + str(rgbl[0]/255) + ', "green": ' + str(rgbl[1]/255) + ', "blue": ' + str(rgbl[2]/255) + ', "alpha": ' + str(self.alpha) + ''

            srgbd = '"red": ' + str(rgbd[0]/255) + ', "green": ' + str(rgbd[1]/255) + ', "blue": ' + str(rgbd[2]/255) + ', "alpha": ' + str(self.alpha) + ''
            
            srgb = '"lightColor":{ ' + srgbl + ' }, "darkColor":{ ' + srgbd + ' } }'

            return '"' + color.name + '":{ ' + srgb

      def _get_hex(self, hex):

            return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

colors = [
      Color('accentColor', 'This are all the red "boxes" in the standard theme.'), 
      Color('accentTextColor', 'This is all the text in the "accentColor" boxes. It is recommended that you use a color that makes it easy to be read.'), 
      Color('foregroundColor', 'This are all the "Boxes" which aren\'t red in the standard theme.'), 
      Color('backgroundColor', 'This is the background in the app.'), 
      Color('overlayColor', 'This is an overlay that is visible when your library or manga view is fetching updates. It is recommended that you use the same color as you used for "backgroundColor".'), 
      Color('separatorColor', 'This are the thin seperator lines in the app. It is recommended that you use the same color as you did for "accentColor".'), 
      Color('bodyTextColor', 'This is the main text in the app.'), 
      Color('subtitleTextColor', 'this is the secondary text in the app.')
]

Results = []

Hexes = []

for color in colors:

      print(color.name + ':')

      print(color.info)

      Results.append(color.get_pbcolors_srgb(ask=True))

      Hexes.append(color.hex_l + ' - ' + color.hex_d)

print('{')

for index, Result in enumerate(Results):
      print(Result + (',' if (index < len(Results) - 1) else ''))

print('}')

print('Copy the above text and put it in a ".pbcolors" file.')

publictheme = input('Is this theme meant to be a public Paperback theme (for more info check: https://github.com/Celarye/Paperback-themes#theme-creation)? Type "Yes" if it is, otherwise any input will do.')

if publictheme == 'Yes':
      print(Hexes)
      print('Copy the above and provide it to the theme manager together with the ".pbcolors" file.')

wait = input('Press enter to close the program. WARNING: ALL DATA CREATED IN THIS PROGRAM WILL BE LOST!')