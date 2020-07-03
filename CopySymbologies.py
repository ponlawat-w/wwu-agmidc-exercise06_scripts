for i in range(0, 23):
  arcpy.management.ApplySymbologyFromLayer('Valencia-20200601_' + str(i).zfill(2) + '00',
    'Valencia-20200601_2300')
