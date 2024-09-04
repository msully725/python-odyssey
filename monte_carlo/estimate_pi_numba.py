from numba import cuda
import numpy as np
import math

@cuda.jit
def pi_kernel(samples, out):
    idx = cuda.grid(1)
    if idx < samples.size:
        x = 2 * cuda.random.xoroshiro128p_uniform_float32(samples[idx]) - 1
        y = 2 * cuda.random.xoroshiro128p_uniform_float32(samples[idx]) - 1
        if x**2 + y**2 <= 1:
            cuda.atomic.add(out, 0, 1)

def estimate_pi_gpu(num_samples):
    samples = cuda.to_device(np.random.randint(0, 1_000_000, size=num_samples, dtype=np.uint32))
    out = cuda.to_device(np.zeros(1, dtype=np.uint32))
    threads_per_block = 256
    blocks = math.ceil(num_samples / threads_per_block)
    pi_kernel[blocks, threads_per_block](samples, out)
    result = out.copy_to_host()
    return 4 * result[0] / num_samples

# Example usage:
estimate = estimate_pi_gpu(1000000)
print(f"Estimated Pi: {estimate:.5f}")