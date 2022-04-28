Rasbperry pi pico RP2040 MicroPython iambic morse practice keyer
touch input is on pins GP26 and GP16 (1M resistor from send pin to gnd)
pulse send pins are on GP26, GP22, gp20 and GP18 (10, 12, 15 & 17 on my breadboard).
onboard led on pin P25

____
    |
rp  |
20  |–––––––o   - GNG
40  |       |
    | _________ - touch #1
    ||      |
    |o–MMM––o   - 1M to GP26
    |       |
    |       |
    |       |
    |o–MMM––o   - 1M to GP16
    ||
    |+––––––––  - touch #2

MCU reads the touch from contact between the i/o-pin and resistor, not the most practical solution,
but it's cheap and simple.