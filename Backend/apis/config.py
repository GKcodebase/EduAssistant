import os
class APIConfig:
    LLAVA_TOKEN = os.getenv('LLAVA_TOKEN', '')
    PHI3_TOKEN = os.getenv('PHI3_TOKEN', '')
    FLUX_TOKEN = os.getenv('FLUX_TOKEN', '')
    SDXL_TOKEN = os.getenv('SDXL_TOKEN', '')