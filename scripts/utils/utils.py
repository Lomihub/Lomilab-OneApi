from pynvml import *
import platform

def platform_system_detection() -> str:
    platform_system = platform.system().lower()
    
    if "windows" in platform_system:
        return "windows"
    elif "linux" in platform_system:
        return "linux"
    elif "wsl" in platform_system:
        return "wsl"
    elif "macos" in platform_system:
        return "macos"
    elif "ubuntu" in platform_system:
        return "ubuntu"
    else:
        raise ValueError(f"Unsupported platform system: {platform_system}")