import pygame
import random
import os
import moviepy.video.io.ImageSequenceClip as imageio

# Initialize Pygame (without showing a window)
pygame.init()
WIDTH, HEIGHT = 1080, 1920

# Load 13 object images (hexadecimal names)
object_images = [
    pygame.image.load("\IMG\0.png"),
    pygame.image.load("\IMG\1.png"),
    pygame.image.load("\IMG\2.png"),
    pygame.image.load("\IMG\3.png"),
    pygame.image.load("\IMG\4.png"),
    pygame.image.load("\IMG\5.png"),
    pygame.image.load("\IMG\6.png"),
    pygame.image.load("\IMG\7.png"),
    pygame.image.load("\IMG\8.png"),
    pygame.image.load("\IMG\9.png"),
    pygame.image.load("\IMG\A.png"),
    pygame.image.load("\IMG\B.png"),
    pygame.image.load("\IMG\C.png"),
    pygame.image.load("\IMG\D.png"),
    pygame.image.load("\IMG\E.png"),
    pygame.image.load("\IMG\F.png"),
]

# Resize images to 100x100 pixels
object_images = [pygame.transform.scale(img, (144, 144)) for img in object_images]

# Gravity & Speed Settings
gravity = 0.7  # Stronger gravity
min_speed = 4   # Minimum initial speed
max_speed = 8  # Maximum initial speed

# Object list
objects = []

for _ in range(10):  # Keep 10 objects on screen
    x = random.randint(80, WIDTH - 280)
    y = random.randint(-10000, -10)  # Start higher
    vy = random.uniform(min_speed, max_speed)  # Increased speed
    img = random.choice(object_images)
    objects.append([x, y, vy, img])

# Create frames folder
frames_folder = "frames"
os.makedirs(frames_folder, exist_ok=True)

num_frames = 1500  # 10 seconds at 30 FPS
print("Generating frames...")

# Generate animation frames
for frame_num in range(num_frames):
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill((166, 156, 125))  # White background

    for obj in objects:
        obj[2] += gravity  # Apply gravity
        obj[1] += obj[2]  # Move down

        if obj[1] > HEIGHT:  # Reset when reaching bottom
            obj[1] = random.randint(-5000, -10)
            obj[0] = random.randint(80, WIDTH - 280)
            obj[2] = random.uniform(min_speed, max_speed)
            obj[3] = random.choice(object_images)  # Assign new random object

        surface.blit(obj[3], (obj[0], obj[1]))  # Draw object

    pygame.image.save(surface, f"{frames_folder}/frame_{frame_num:03d}.png")

# Convert Frames to Video
output_folder = "output_videos"
output_filename = "falling_objects_tiktok.mp4"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, output_filename)

print("Converting frames to video...")
fps = 30  # Frames per second
image_files = [f"{frames_folder}/frame_{i:03d}.png" for i in range(num_frames)]
clip = imageio.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(output_path, codec="libx264", fps=fps)

print(f"✅ Video saved automatically as {output_path}")
pygame.quit()
