import platform
import subprocess

class DependencyCheck:
    def __init__(self):
        self.operating_system: str = platform.system()
        
    def supported_system(self, operating_system: str = platform.system()) -> bool:
        """supported_system checks if the operating system is supported. Currently supports MacOS and Linux.

        Args:
            operating_system (str, optional): Defaults to platform.system().

        Returns:
            bool: True if operating system is supported, False if not.
        """             
        supported_systems: list = ["darwin", "linux"]
        if operating_system.lower() in supported_systems:
            return True
        else:
            return False
        
    def dependency_check(self, dependency: str) -> bool or None:
        """dependency_check checks whether a dependency is installed.

        Args:
            dependency (str): the name of the dependency e.g. ffmpeg

        Returns:
            bool or None: True if dependency is installed, False if not and None if operating system is not supported.
        """        
        dependency_installed: bool
        if self.supported_system():
            try:
                output = subprocess.check_output(["which", dependency]).strip()
                output_split = output.decode().split("/")
                # expected_output = "/usr/bin/{}".format(dependency).encode()
                if output_split[-1] == dependency:
                    dependency_installed = True
                else:
                    dependency_installed = False
            except subprocess.CalledProcessError:
                dependency_installed = False
            
            return dependency_installed
        else:
            return None
        
    def ffmpeg_installed(self) -> bool or None:
        """ffmpeg_installed checks if ffmpeg is installed.

        Returns:
            bool or None: True if ffmpeg is installed, False if not and None if operating system is not supported.
        """        
        return self.dependency_check(dependency="ffmpeg")

    def lame_installed(self) -> bool or None:
        """lame_installed checks if lame is installed.

        Returns:
            bool or None: True if lame is installed, False if not and None if operating system is not supported.
        """        
        return self.dependency_check(dependency="lame")

    def flac_installed(self) -> bool or None:
        """flac_installed checks if flac is installed

        Returns:
            bool or None: True if flac is installed, False if not and None if operating system is not supported.
        """        
        return self.dependency_check(dependency="flac")
    
    def all_dependencies_installed(self) -> bool or None:
        ffmpeg = self.ffmpeg_installed()
        la.maketrans()

if __name__ == "__main__":
    d = DependencyCheck()
    # print(d.operating_system)
    # print(d.supported_system.__doc__)
    print(d.dependency_check("burp"))
    print(d.ffmpeg_installed())
    print(d.lame_installed())
    print(d.flac_installed())