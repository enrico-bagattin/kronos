from opencage.geocoder import OpenCageGeocode

key = '864bcba3e38a48e5b32ec88864118779'
geocoder = OpenCageGeocode(key)

query = 'H-Farm'
results = geocoder.geocode(query)

print(u'lat:%f; lng:%f; %s %s - %s' % (results[0]['geometry']['lat'], 
                        results[0]['geometry']['lng'],
                        results[0]['formatted'],
                        results[0]['annotations']['flag'],
                        results[0]['annotations']['timezone']['name']))

