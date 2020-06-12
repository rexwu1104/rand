import time

def l():
  before = time.time()
  for i in range(10000):
    continue

  after = time.time()
  return after - before

class rand():
  def __init__(self, modmax=None):
    self.seed_out = int(l() * 10000)
    if modmax is not None:
      self.max = modmax
    else:
      self.max = 65536

  def rand(self, times : int):
    num = []
    seed = self.seed_out
    if times > self.max:
      limit = times // self.max 
      nums = times % self.max
    else:
      limit = 1
      nums = times
    for i in range(times):
      seed = (seed * (2 ** 127 - 1) // int(l() * 10000)) % self.max + 1
      while True:
        if seed not in num and limit != 0:
          num.append(seed)
          break
        elif len(num) == self.max and limit != 0:
          limit -= 1
          num = []
        elif limit == 0 and len(num) != nums and seed not in num:
          num.append(seed)
          break
        else:
          seed = seed * (2 ** int(l() * 1000)) * int(l() * 10000) % self.max + 1
      yield seed
  
  def setup(self, max : int):
    self.max = max
