from flac_to_mp3.dependency_checker import DependencyCheck


def test_supported_system_windows(): 
    # Arrange
    d = DependencyCheck()
    
    # Act
    supported_system = d.supported_system(operating_system="Windows")
    
    #Assert
    assert supported_system is False
    
def test_supported_system_linux(): 
    # Arrange
    d = DependencyCheck()
    
    # Act
    supported_system = d.supported_system(operating_system="Linux")
    
    #Assert
    assert supported_system is True


def test_supported_system_macos(): 
    # Arrange
    d = DependencyCheck()
    
    # Act
    supported_system = d.supported_system(operating_system="Darwin")
    
    #Assert
    assert supported_system is True
    

def test_ffmpeg_installed():
    # Arrange
    d = DependencyCheck()
    
    # Act
    installed = d.ffmpeg_installed()
    
    # Assert
    assert installed is True

def test_lame_installed():
    # Arrange
    d = DependencyCheck()
    
    # Act
    installed = d.lame_installed()
    
    # Assert
    assert installed is True
    
def test_flac_installed():
    # Arrange
    d = DependencyCheck()
    
    # Act
    installed = d.flac_installed()
    
    # Assert
    assert installed is True

def test_all_dependencies_installed():
    # Arrange
    d = DependencyCheck()
    
    # Act
    all_deps_installed = d.all_dependencies_installed()
    
    # Assert
    assert all_deps_installed is True
    
    