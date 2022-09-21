import cfg
import dxf
import dev

ltip = 800
lcut = 400

xsize = cfg.size
ysize = cfg.ch

def device(x, y, lchip, length, sign):
  
  lext = lchip - ltip
  wext = 125

  w = [0.1, 0.5, 0.8, cfg.wg]
  l = [50, 25]
  t = sum(l)
  l.insert(0, ltip - t)

  if sign > 0: idev = len(cfg.data)

  x1, y = dxf.srect('edge', x,  y, l[0], wext)
  x1, y = dxf.srect('sio2', x,  y, l[0], 6)
  x4, y = dxf.taper('edge', x1, y, t, wext, cfg.eg)
  x4, y = dxf.taper('sio2', x1, y, t, 6, 0.1)
  x2, y = dxf.taper('core', x4, y, -l[2], w[3], w[2])
  x3, y = dxf.taper('core', x2, y, -l[1], w[2], w[1])
  if lext > 0: x5, y = dev.sline(x4, y, lext)
  else: x5 = x4

  dxf.taper('core', x3, y, -length, w[1], w[0])

  if sign > 0: dxf.xreverse(idev, x, y, x + lchip)

  return x5, x4 if sign < 0 else x1

def fiber(x, y, lchip, sign):

  return device(x, y, lchip, 400, sign)

def pd(x, y, lchip, sign):

  return device(x, y, lchip, 400, sign)

def chip(x, y, lchip, length):

  x1, _ = device(x, y, 0, length, -1)
  x2, _ = device(x1, y, lchip - x1 + x, length, 1)

  s = 'sio-' + str(int(length))
  dev.texts(x  + ltip, y - cfg.ch * 0.5, s, 0.5, 'lc')
  dev.texts(x2 - ltip, y - cfg.ch * 0.5, s, 0.5, 'rc')
  print(s, int(x2 - x))

  return x2, y

def chips(x, y, start, stop, step):
  
  width = dev.arange(start, stop, step)
  
  for w in width: x1, y = chip(x, y + cfg.ch, xsize, w)

  return x1, y

if __name__ == '__main__':

  # chip(0, 0, 0)

  chips(0, 0, 200, 600, 200)

  dev.saveas('sio')