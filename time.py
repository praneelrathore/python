from googlemaps import Client

mapService = Client('Your key here')
source = 'Kronos Solutions India Pvt Ltd'
destination = 'Gaur Grandeur'
directions = mapService.directions(source, destination)
print len(directions)
directions = directions[0]


i = 1
for leg in directions['legs']:
    duration = leg['duration']
    print duration['text']
    startAddress = leg['start_address']
    print "Start Address:", startAddress
    endAddress = leg['end_address']
    print "End Address:", endAddress
    for step in leg['steps']:
        html_instructions = step['html_instructions']
        duration = step['duration']
        i = i + 1
