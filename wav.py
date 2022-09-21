import os
import cfg
import numpy as np

wnarrow = 0.2
lengths = [10, 25, 50]
amplitd = [0.4, 0.5]

def save(fp, length, w1, w2, layer, m):

  w = round(w2 - w1, 6)
  t = np.linspace(0, 1, int(length * m) + 1)
  x = t * length
  y = 0.5 * w * np.sin(t * np.pi * 0.5)

  df = {}
  df['m'] = m
  df['x'] = x
  df['y'] = y
  df['l'] = length
  df['w1'] = w1
  df['w2'] = w2

  np.save(fp, df)

  print('seg', length, w2, layer)

  return df

def update(w1):

  obj = {}

  for length in lengths:
    for w2 in amplitd:
      for layer in ['mask', 'draft']:
        m = 1 if cfg.draft == 'draft' else 10
        i = str(length) + '_' + str(w1) + '_' + str(w2) + '_' + layer
        fp = cfg.libs + 'seg_' + i + '.npy'

        changed = False
        if os.path.isfile(fp):
          df = np.load(fp, allow_pickle=True).item()
          if df['m'] != m: changed = True
          if df['l'] != length: changed = True
          if df['w1'] != w1: changed = True
          if df['w2'] != w2: changed = True
        else: changed = True

        obj[i] = save(fp, length, w1, w2, layer, m) if changed else df
  
  return obj

def wave(layer, x, y, df, width, sign, dir):
  
  w1 = width * 0.5
  xt = df['x'] * dir
  yt = df['y'] if sign > 0 else df['y'][::-1]

  xp = x + np.append(xt, xt[::-1])
  yp = y + np.append(yt + w1, -(yt[::-1] + w1))

  data = np.array([xp, yp]).transpose()
  cfg.data.append([layer] + data.tolist())

  return x + df['l'] * dir, y

tip = update(wnarrow)