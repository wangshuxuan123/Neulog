from neulog import gsr
# from gzp import save

import time

"""
Sample GSR experiment.

Gathers data over two phases. Use a keyboard interrupt (control-c) to end a phase.

Saves data to disk afterwards.
"""

sensor = gsr()

data = []
times = []
t0 = time.time()

print("First phase...")
pre_t = 0
while pre_t<20: #first phase (eg. 'resting')
    try:
        x = sensor.get_data(8, 1)
        t = time.time() - t0
        # print(t-pre_t, x)
        data.append(x)
        times.append(t)
        pre_t = t

    except KeyboardInterrupt:
        break

# save([data, times, breaktime], "experiment.dat")