import pygame
import os
from pygame import mixer

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.init()
        mixer.init()
        self.music_folder = music_folder
        self.music_files = [file for file in os.listdir(music_folder) if file.endswith(('.mp3', '.wav'))]
        self.current_track = 0
        self.playing = False

    def LM(self):
        pygame.mixer.music.load(os.path.join(self.music_folder, self.music_files[self.current_track]))

    def PM(self):
        pygame.mixer.music.play()

    def SM(self):
        pygame.mixer.music.stop()

    def NT(self):
        self.current_track = (self.current_track + 1) % len(self.music_files)
        self.LM()
        if self.playing:
            self.PM()

    def PT(self):
        self.current_track = (self.current_track - 1) % len(self.music_files)
        self.LM()
        if self.playing:
            self.PM()

    def run(self):
        self.LM()

        while True:
            query = input('  ')
                
            if query == 's':
                self.SM()
            elif query == ' ':
                self.PM()
                self.playing = True
            elif query == 'n':
                self.NT()
            elif query == 'p':
                self.PT()
            elif query == 'q':
                pygame.quit()
                exit()

if __name__ == "__main__":
    function = MusicPlayer("C:\\Users\\ramazan\\Desktop\\pp2\\music")
    function.run()
    
    pygame.quit()
    exit()
