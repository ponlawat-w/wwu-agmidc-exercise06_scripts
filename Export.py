for layer in map.listLayers('Valencia-20200601_*'):
  layer.visible = False

timeLabel = layout.listElements('TEXT_ELEMENT', 'TimeLabel')[0]
for i in range(0, 24):
  layer = map.listLayers('Valencia-20200601_' + str(i).zfill(2) + '00')[0]
  layer.visible = True
  timeLabel.text = str(i).zfill(2) + ':00'
  layout.exportToPNG(layer.name)
  layer.visible = False
timeLabel.text = '00:00'
