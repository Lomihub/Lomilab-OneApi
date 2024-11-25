from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetName, nvmlSystemGetDriverVersion, nvmlDeviceGetCount, nvmlDeviceGetCudaComputeCapability, nvmlShutdown, NVMLError

class NVIDIAPlatformDetection(): 
    
    def __init__(self) -> None:
        """ 
        Constructor for NVIDIAPlatformDetection class
        Run NVML initialization
        If not connection to NVIDIA GPU, raise NVMLError
        """
        try: 
            nvmlInit()      
        except NVMLError as error:
            raise NVMLError("Unable to connect to NVIDIA GPU. Error: " % error)

        self.gpu_names = None
        self.nvidia_driver_version = None
        self.nvidia_device_count = None
        self.nvidia_device_name = None
        self.nvidia_cuda_version = None
    
    def get_gpu_names(self) -> list:
        """
        Get GPU names
        Returns:
            gpu_names (list): List of GPU names
        """
        try: 
            self.gpu_names = []
            for i in range(self.get_nvidia_device_count()):
                handle = nvmlDeviceGetHandleByIndex(i)
                gpu_name = nvmlDeviceGetName(handle)
                self.gpu_names.append(gpu_name)
            return self.gpu_names
        except NVMLError as error:
            raise NVMLError("Unable to get GPU names. Error: " % error)
    
    def get_nvidia_driver_version(self) -> str:
        """
        Get NVIDIA driver version
        Returns:
            nvidia_driver_version (str): NVIDIA driver version
        """
        try: 
            self.nvidia_driver_version = nvmlSystemGetDriverVersion()
            return self.nvidia_driver_version
        except NVMLError as error:
            raise NVMLError("Unable to get NVIDIA driver version. Error: " % error)
        
    def get_nvidia_device_count(self) -> int:
        """
        Get NVIDIA device count
        Returns:
            nvidia_device_count (int): Number of NVIDIA devices
        """
        try: 
            self.nvidia_device_count = nvmlDeviceGetCount()
            return self.nvidia_device_count
        except NVMLError as error:
            raise NVMLError("Unable to get NVIDIA device count. Error: " % error)
    
    def get_nvidia_device_name(self) -> str:
        """
        Get NVIDIA device name
        Returns:
            nvidia_device_name (str): Name of NVIDIA device
        """
        try: 
            self.nvidia_device_name = nvmlDeviceGetName(nvmlDeviceGetHandleByIndex(0))
            return self.nvidia_device_name
        except NVMLError as error:
            raise NVMLError("Unable to get NVIDIA device name. Error: " % error)
        
    def get_nvidia_cuda_version(self) -> list:
        """
        Get NVIDIA CUDA version
        Returns:
            nvidia_cuda_version (str): NVIDIA CUDA version
        """
        try: 
            self.nvidia_cuda_version = []
            for i in range(self.nvidia_device_count):
                self.nvidia_cuda_version.append(nvmlDeviceGetCudaComputeCapability(nvmlDeviceGetHandleByIndex(i)))
            return self.nvidia_cuda_version
        except NVMLError as error:
            raise NVMLError("Unable to get NVIDIA CUDA version. Error: " % error)
    
    def get_nvidia_platform_info(self) -> dict:
        """
        Get NVIDIA platform information
        Returns:
            nvidia_platform_info (dict): NVIDIA platform information
        """
        nvidia_platform_info = {}
        nvidia_platform_info['nvidia_driver_version'] = self.get_nvidia_driver_version()
        nvidia_platform_info['nvidia_device_count'] = self.get_nvidia_device_count()
        nvidia_platform_info['nvidia_device_name'] = self.get_nvidia_device_name()
        nvidia_platform_info['nvidia_cuda_version'] = self.get_nvidia_cuda_version()
        return nvidia_platform_info
    
    def __repr__(self) -> str:
        """
        Representation for NVIDIAPlatformDetection class
        Returns:
            res (str): NVIDIA platform information
        """
        nvidia = self.get_nvidia_platform_info()
        res = ""
        res += "NVIDIA Platform Information\n"
        res += "---------------------------\n"
        for key, value in nvidia.items():
            res += f"{key}: {value}\n"
        return res
        
    def __del__(self):
        """
        Destructor for NVIDIAPlatformDetection class
        Run NVML shutdown
        """
        nvmlShutdown()