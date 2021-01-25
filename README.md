# Advent-of-Code-2020

## Benchmarks
pypy3 is was used on longer problems where the speedup is notable.
```
     Day 1:   0.146974
     Day 2:   0.172626
     Day 3:   0.189994
     Day 4:   0.196646
     Day 5:   0.192404
     Day 6:   0.185958
     Day 7:   0.213869
     Day 8:   0.171903
     Day 9:   0.144384
    Day 10:   0.164560
    Day 11:   0.429212
    Day 12:   0.182695
    Day 13:   0.171555
    Day 14:   0.544596
    Day 15:   7.474768 (pypy3)
    Day 16:   0.255753
    Day 17:   1.112069
    Day 18:   0.153736
    Day 19:   1.892090 (pypy3)
    Day 20:   0.294954
    Day 21:   0.201398
    Day 22:   1.490760
    Day 23:   1.085218 (pypy3)
    Day 24:   1.457711
    Day 25:   0.523313
Total time: 19.04914402961731
```
## Notes
### Day 13
Day 13 had a very interesting optimization that is not apparent until you see a visualization. Essentially, given all seats start empty: once a seat doesn't change during a round, it will never change again. Therefore you only have to check the neighbors to these *crystalized* seats. This lets you iterate over a 2d boundary of seats instead of the whole 2d area.
