import platform
import subprocess


class DependencyCheck:
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
            dependency (str): the name of the dependency e.g. ffmpeg.

        Returns:
            bool or None: True if dependency is installed, False if not and None if operating system is not supported.
        """
        dependency_installed: bool
        if self.supported_system():
            try:
                output = subprocess.check_output(["which", dependency]).decode().strip()
                output_split = output.split("/")
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
        """flac_installed checks if flac is installed.

        Returns:
            bool or None: True if flac is installed, False if not and None if operating system is not supported.
        """
        return self.dependency_check(dependency="flac")
    
    def cuetools_installed(self) -> bool or None:
        """cuetools_installed checks if cuetools is installed.

        Returns:
            bool or None: True if cuetools is installed, False if not and None if operating system is not supported.
        """
        return self.dependency_check(dependency="cuebreakpoints")
    
    def shntool_installed(self) -> bool or None:
        """shntool_installed checks if shntool is installed.

        Returns:
            bool or None: True if shntool is installed, False if not and None if operating system is not supported.
        """
        return self.dependency_check(dependency="shntool")

    def all_dependencies_installed(self) -> bool:
        """all_dependencies_installed checks if all dependencies are installed.

        Returns:
            bool: True if all dependencies are installed, False if not.
        """
        all_installed: bool
        dep_dict = {
            "ffmpeg": {"installed": self.ffmpeg_installed()},
            "lame": {"installed": self.lame_installed()},
            "flac": {"installed": self.flac_installed()},
            "cuetools": {"installed": self.cuetools_installed()},
            "shntool": {"installed": self.shntool_installed()}
        }
        dep_total = len(dep_dict)
        dep_count = 0

        for dep, dep_info in dep_dict.items():
            # print(f"{dep} installed: {dep_info['installed']}")
            if dep_info["installed"]:
                dep_count += 1

        if dep_count == dep_total:
            all_installed = True
        else:
            all_installed = False

        return all_installed


if __name__ == "__main__":
    d = DependencyCheck()
    print(f"OS: {platform.system()}")
    print(f"Supported OS: {d.supported_system()}")
    print(f"Ffmpeg installed: {d.ffmpeg_installed()}")
    print(f"Lame installed: {d.lame_installed()}")
    print(f"Flac installed: {d.flac_installed()}")
    print(f"Cuetools installed: {d.cuetools_installed()}")
    print(f"Shntool installed: {d.shntool_installed()}")
    print(f"All installed: {d.all_dependencies_installed()}")
