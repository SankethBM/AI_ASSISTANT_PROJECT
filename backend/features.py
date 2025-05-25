import pygame

# Playing Assistant voice
def playAssistantSound():
    music_dir = "frontend/assets/audio/start_sound.mp3"  # Use forward slashes for cross-platform compatibility

    pygame.mixer.init()
    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Avoids high CPU usage
