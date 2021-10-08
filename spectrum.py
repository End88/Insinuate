# Thanks for watching this coding video
# Please do not forget to subscribe my youtube channel and like my videos, share them
# This source code will be publish under below(including the music)
# if you have any question you can comment below or contact me through every platform
# Love you guys thanks :D

import numpy
import pygame
import wave

from scipy.fftpack import dct


class Spectrum:
    def __init__(self, HEIGHT, WIDTH, DirectoryMusic):
        self.number = 60  # number of bars
        self.HEIGHT = HEIGHT  # HEIGHT of a bar 600
        self.WIDTH = WIDTH  # WIDTH of a bar 20
        self.FPS = 10

        # screen init, music playback
        self.music = DirectoryMusic

        self.screen = pygame.display.set_mode([self.number * self.WIDTH, 50 + self.HEIGHT])
        self.my_font = pygame.font.SysFont('consolas', 16)
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent()
        pygame.mixer.music.set_volume(0.2)

        # process wave data

        f = wave.open(self.music, 'rb')
        params = f.getparams()
        self.nchannels, self.sampwidth, self.framerate, self.nframes = params[:4]
        str_data = f.readframes(self.nframes)
        f.close()
        wave_data = numpy.fromstring(str_data, dtype=numpy.short)
        wave_data.shape = -1, 2
        self.wave_data = wave_data.T

        self.num = self.nframes

    def visualizer(self, nums):
        num = int(nums)
        h = abs(dct(self.wave_data[0][self.nframes - num:self.nframes - num + self.number]))
        h = [min(self.HEIGHT, int(i ** (1 / 2.5) * self.HEIGHT / 100)) for i in h]
        self.draw_bars(h)

    def vis(self):
        self.num -= self.framerate / self.FPS
        if self.num > 0:
            self.visualizer(self.num)

    def get_time(self):
        seconds = max(0, pygame.mixer.music.get_pos() / 1000)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        hms = ("%02d:%02d:%02d" % (h, m, s))
        return hms

    def draw_bars(self, h):
        bars = []
        for i in h:
            bars.append([len(bars) * self.WIDTH, 50 + self.HEIGHT - i, self.WIDTH - 1, i])
        for i in bars:
            pygame.draw.rect(self.screen, [255, 255, 255], i, 0)


pygame.init()
pygame.mixer.init()
fpsclock = pygame.time.Clock()
bars = Spectrum(400, 15, "data\\musics\\spark_of_light.wav")
close = False
while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True

    bars.screen.fill((0, 0, 0))
    fpsclock.tick(bars.FPS)
    bars.vis()
    pygame.display.update()

pygame.display.quit()