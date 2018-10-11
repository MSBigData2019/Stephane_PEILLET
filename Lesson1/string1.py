# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def donuts(count):
  if count < 10:
      return "Number of donuts: "+ str(count)
      pass
  else:
      return "Number of donuts: "+ "many"

def both_ends(s):
  if len(s) < 2:
      return ""
  else:
      return s[0:2] + s[-2::1]

def fix_start(s):
  # +++your code here+++
  if len(s) < 1:
    return s
  else:
    return s[0] + s[1::].replace(s[0], "*")

def mix_up(a, b):
  # +++your code here+++
  if ((len(a) < 2) and (len(b) < 2)):
    return a + " " + b
  else:
    return b[0:2]+a[2::] + " " + a[0:2]+b[2::]

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  print ('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print()
  print ('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')


  print()
  print ('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print()
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
