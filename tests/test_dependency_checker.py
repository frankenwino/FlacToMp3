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
    
    