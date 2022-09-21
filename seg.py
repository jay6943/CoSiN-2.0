import cfg
import dxf
import dev
import wav

ltip = 800
lcut = 400

xsize = cfg.size
ysize = cfg.ch

def device(x, y, lchip, sign, length, w1, w2):
  
  lext = lchip - ltip
  wext = 125

  w = [w2, 0.5, 0.8, cfg.wg]
  l = [ltip - 75, 50, 20, 5]

  if sign < 0:
    x1, _ = dxf.srect('edge', x,  y, l[0], wext)
    x2, _ = dxf.taper('core', x1, y, l[1], w[0], w[1])
    x3, _ = dxf.taper('core', x2, y, l[2], w[1], w[2])
    x4, _ = dxf.taper('core', x3, y, l[3], w[2], w[3])
    x4, _ = dxf.taper('edge', x1, y, x4 - x1, wext, cfg.eg)
    
    if lext > 0:
      x5, _ = dxf.sline('core', x4, y, lext)
      dxf.srect('edge', x4, y, x5 - x4, cfg.eg)
    else: x5 = x4

  else:

    if lext > 0:
      x1, _ = dxf.sline('core', x, y, lext)
      dxf.srect('edge', x, y, x1 - x, cfg.eg)
    else: x1 = x

    x2, _ = dxf.taper('core', x1, y, l[3], w[3], w[2])
    x3, _ = dxf.taper('core', x2, y, l[2], w[2], w[1])
    x4, _ = dxf.taper('core', x3, y, l[1], w[1], w[0])
    x4, _ = dxf.taper('edge', x1, y, x4 - x1, cfg.eg, wext)
    x5, _ = dxf.srect('edge', x4, y, l[0], wext)

  l1 = 25
  l2 = sign * (length + l1 - 6.25)
  x6 = x1 if sign < 0 else x4
  
  i = str(length) + '_' + str(w1) + '_' + str(w2) + '_' + cfg.draft
  
  x7, _ = dxf.srect('core', x6, y, l2, w2)
  x8, _ = wav.wave('core', x7, y, wav.tip[i], w1, -1, sign)

  while(x8 - l1 > x and x8 + l1 < x5):
    x9, _ = wav.wave('core', x8, y, wav.tip[i], w1,  1, sign)
    x8, _ = wav.wave('core', x9, y, wav.tip[i], w1, -1, sign)

  return x5, x4 if sign < 0 else x1

def chip(x, y, lchip, length, w1, w2):

  x1, _ = device(x, y, 0, -1, length, w1, w2)
  x2, _ = device(x1, y, lchip - x1 + x, 1, length, w1, w2)

  s = 'seg-' + str(length * 2) + '-' + str(w2)
  dev.texts(x  + ltip, y - cfg.ch * 0.5, s, 0.5, 'lc')
  dev.texts(x2 - ltip, y - cfg.ch * 0.5, s, 0.5, 'rc')
  print(s, int(x2 - x))

  return x2, y

def chips(x, y):
  
  for l in wav.lengths:
    for w in wav.amplitd:
      _, y = chip(x, y + cfg.ch, xsize, l, wav.wnarrow, w)

  return x + xsize, y

if __name__ == '__main__':

  # chip(0, 0, 3000, 50, 0.1, 0.5)

  chips(0, 0)

  dev.saveas('seg')