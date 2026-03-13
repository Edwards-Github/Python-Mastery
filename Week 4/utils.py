import time

def execution_timer(base_fn):
	def enhanced_fn(*args, **kwargs):
		start_time = time.time()
		base_fn(*args, **kwargs)
		end_time = time.time()
		print(f'Task time: {end_time - start_time}s')
	return enhanced_fn