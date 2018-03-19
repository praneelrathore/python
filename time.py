from googlemaps import Client

# Add you API key here
mapService = Client(key='AIzaSyDZyqHCijWTWK1j8dhisZ0ba47qH3oSFaA')

directions = mapService.directions('Disneyland', 'Universal Studios Hollywood')
directions = directions[0]

i=1
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
        #print "STEP {} {}".format(i ,html_instructions)
        i = i+1
