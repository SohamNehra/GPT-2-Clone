import torch
print(torch.cuda.get_device_properties(0).multi_processor_count)