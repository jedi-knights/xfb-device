from PIL import Image, ImageDraw, ImageFont
import pygame
import os

pygame.init()
pygame.mixer.init()

def show_status(build_system, job_name, status):
    color = (0, 255, 0) if status == 'success' else (255, 0, 0)
    sound = 'success.wav' if status == 'success' else 'fail.wav'

    # Play sound
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

    # Display image
    image = Image.new('RGB', (1024, 600), color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    draw.text((50, 250), f"{build_system}: {job_name}", fill=(0, 0, 0), font=font)

    image.save('/tmp/xfb_display.png')
    os.system("feh --fullscreen --hide-pointer --image-bg black /tmp/xfb_display.png")
