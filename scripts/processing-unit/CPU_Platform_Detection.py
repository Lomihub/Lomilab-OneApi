from psutil import cpu_count, cpu_info, virtual_memory

class CPUPlatformDetection():
    def __init__(self):
        """
        Initialize CPUPlatformDetection class
        """
        self.cpu_count = None
        self.cpu_physical_count = None
        self.cpu_name = None
        self.cpu_memory_info = None
        
    def get_cpu_count(self) -> int:
        """
        Get CPU count
        Returns:
            cpu_count (int): Number of CPUs
        """
        try:
            self.cpu_count = cpu_count()
            return self.cpu_count
        except Exception as error:
            raise Exception("Unable to get CPU count. Error: " % error)
    
    def get_cpu_physical_count(self) -> int:
        """
        Get CPU physical count
        Returns:
            cpu_physical_count (int): Number of physical CPUs
        """
        try:
            self.cpu_physical_count = cpu_count(logical=False)
            return self.cpu_physical_count
        except Exception as error:
            raise Exception("Unable to get CPU physical count. Error: " % error)
        
    def get_cpu_name(self) -> str:
        """
        Get CPU name
        Returns:
            cpu_name (str): Name of CPU
        """
        try:
            self.cpu_name = cpu_info()[0]['brand_raw']
            return self.cpu_name
        except Exception as error:
            raise Exception("Unable to get CPU name. Error: " % error)
        
    def get_cpu_memory_info(self) -> dict:
        """
        Get CPU memory information
        Returns:
            cpu_memory_info (dict): CPU memory information
        """
        try:
            self.cpu_memory_info = {}
            self.cpu_memory_info['total'] = virtual_memory().total
            self.cpu_memory_info['available'] = virtual_memory().available
            self.cpu_memory_info['used'] = virtual_memory().used
            self.cpu_memory_info['free'] = virtual_memory().free
            return self.cpu_memory_info
        except Exception as error:
            raise Exception("Unable to get CPU memory information. Error: " % error)
        
    def get_cpu_platform_info(self) -> dict:
        """
        Get CPU platform information
        Returns:
            cpu_platform_info (dict): CPU platform information
        """
        cpu_platform_info = {}
        cpu_platform_info['cpu_count'] = self.get_cpu_count()
        cpu_platform_info['cpu_physical_count'] = self.get_cpu_physical_count()
        cpu_platform_info['cpu_name'] = self.get_cpu_name()
        cpu_platform_info['cpu_memory_info'] = self.get_cpu_memory_info()
        return cpu_platform_info
    
    def __repr__(self) -> str:
        """
        Get CPU platform information
        Returns:
            res (str): CPU platform information
        """
        res = ""
        res += "CPU Platform Information\n"
        res += "------------------------\n"
        cpu_platform_info = self.get_cpu_platform_info()
        for key, value in cpu_platform_info.items():
            res += key + ": " + str(value) + "\n"
        return res
    
if __name__ == "__main__":
    cpu = CPUPlatformDetection()
    print(cpu)