import psutil

def get_storage_size():
    """
    Get the total storage size of the current device.
    
    Returns:
    - storage_size (float): Total storage size in gigabytes.
    """
    disk_usage = psutil.disk_usage('/')
    storage_size_gb = disk_usage.total / (1024 ** 3)  # Convert bytes to gigabytes
    return storage_size_gb

# Example usage
storage_size = get_storage_size()
print(f"The total storage size of the current device is approximately {storage_size:.2f} GB.")
