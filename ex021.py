print('Faça um programa em PYTHON que abra e reproduza um arquivo e áudio MP3.')
import pygame
pygame.init()
pygame.mixer.music.load('ex021a.mp3')
pygame.mixer.music.play()
pygame.event.wait()



