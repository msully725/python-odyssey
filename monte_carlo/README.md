# Monte Carlo

Experiment with a simple Monte Carlo sim in python. In this case, computing an estimate of pi by running many random indepdent samples. 

At the current iteration there are 4 examples:
* `estimate_pi.py`
  * Simplest implementation. 
* `estimate_pi_numba.py`
  * Utilize CUDA for a performance boost.
  * Not yet tested, need to run on NVIDIA rig.
* `estimate_pi_concurrent_futures_slow.py`
  * Originally this was not `_slow`, but after running it, it was renamed.
  * Although this ulitizes concurrency to run multiple operations simultaneously which should improve throughput and reduce run time, python's Process Pool for concurrency requires careful consideration to see such gains.
  * In this implementation, `points_in_circle` is a shared value with a lock around it when updating. 
    * Without the lock, the estimates are terrible as it is losing many of the "in circle" samples due to race conditions.
  * The leading thought is synchronization overhead between many processes negates the speed up. 
    * Still want to dig into this more to solidly understand the exact cause of the slow down.

* `estimate_pi_concurrent_futures_fast.py`
  * An alternative concurrent implementation that is more carefully designed to avoid inter-processs communication slow downs. 
  * Since each 'run' is completely independent (aka embarrassingly parrallel), we instead divide the number of runs by `desired_workers` and allow each process to run continously, uninterrupted by locks/waits.
  * This results in the speed up we expect - about x4 when split across 4 "workers".


## Example Results

| | Approach | Execution Time | Speedup |
|-|-|-|-|
| estimate_pi | Single-threaded | 7.106 sec | x1 |
| estimate_pi_concurrent_futures_slow | Multi-process, shared locks | 306.787 sec | -43x |
| estimate_pi_concurrent_futures_fast | Multi-process, lock-free | 1.766 sec | x4 |


### estimate_pi.py
```sh
Sample size: 10000. Pi estimate: 3.15120
Sample size: 173205. Pi estimate: 3.13989
Sample size: 3000000. Pi estimate: 3.14104

Total Execution Time: 7.105914003001089 seconds
```

### estimate_pi_concurrent_futures_slow.py
```sh
Sample size: 10000. Pi estimate: 3.15200
Sample size: 173205. Pi estimate: 3.14317
Sample size: 3000000. Pi estimate: 3.14167

Total Execution Time: 306.7871647219981 seconds
```

### estimate_pi_concurrent_futures_fast.py
```sh
Sample size: 10000. Pi estimate: 3.14680
Sample size: 173205. Pi estimate: 3.14009
Sample size: 3000000. Pi estimate: 3.14011

Total Execution Time: 1.7655968760009273 seconds
```