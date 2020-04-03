#
import pygame
import os


pygame.init()

FPS = 60

width = 1280
height = 720
colour = (0, 255, 255) 

window = pygame.display.set_mode((width, height ))

clock = pygame.time.Clock()



car_images = [
	pygame.image.load(os.path.join('Car/car01.png')),
	pygame.image.load(os.path.join('Car/car02.png')),
	pygame.image.load(os.path.join('Car/car03.png')),
	pygame.image.load(os.path.join('Car/car04.png'))
]


enemy_images = [ pygame.image.load(os.path.join( 'bluebat','skeleton-fly_' + str(x) + '.png')) for x in range(10)]

def get_size(image, width):
	image_size = image.get_rect().size 
	return (width, int(image_size[1] * width / image_size[0]))
	



def resize_image(image, width):
	image_size = get_size(image, width)
	return pygame.transform.scale(image, image_size)


image_width = 200 
car_images = list(map(resize_image, 
					  car_images,   
					  [ image_width for i in range(len(car_images)) ] ))	 
				 
enemy_images = list(map(resize_image, enemy_images, [ 200 for x in range(len(enemy_images)) ]))




class Base():
	def __init__(self, x, y, images):
		self.x = x
		self.y = y
		self.images = images

	def draw(self, frame):
		window.blit(self.images[frame], (self.x, self.y))


class Hero(Base):
	def __init__(self):
		super().__init__(50, int(height / 2), car_images) # x, y, hero_images
	
	def move(self, x, y):
		self.x += x
		self.y += y


class Enemy(Base):
	def __init__(self):
		super().__init__(
			int(width * 0.8),    
			int(height / 2),     
			enemy_images) 

	def move(self, x, y):
		self.x += x
		self.y += y 				

car = Hero()
enemy = Enemy()

x = width / 2
y = height / 2

vel = 3
car_x = 0
car_y = 0
car_next_tick = 100
enemy_next_tick = 50
car_frame = 0
enemy_frame = 0
ene_x = 0
ene_y = 0
while True:

	clock.tick(FPS)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				ene_x += vel
			elif event.key == pygame.K_a:
				ene_x -= vel
			elif event.key == pygame.K_w:
				ene_y -= vel
			elif event.key == pygame.K_s:
				ene_y += vel
			elif event.key == pygame.K_RIGHT:
				car_x += vel
			elif event.key == pygame.K_LEFT:
				car_x -= vel
			elif event.key == pygame.K_UP:
				car_y -= vel
			elif event.key == pygame.K_DOWN:
				car_y += vel

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				ene_x += -vel
			elif event.key == pygame.K_a:
				ene_x -= -vel
			elif event.key == pygame.K_w:
				ene_y -= -vel
			elif event.key == pygame.K_s:
				ene_y += -vel
			elif event.key == pygame.K_RIGHT:
				car_x += -vel
			elif event.key == pygame.K_LEFT:
				car_x -= -vel
			elif event.key == pygame.K_UP:
				car_y -= -vel
			elif event.key == pygame.K_DOWN:
				car_y += -vel


		

		



	
	if pygame.time.get_ticks() > car_next_tick:
		if car_x > 0:
			car_next_tick += 80
		elif car_x < 0:
			car_next_tick += 120
		else:
			car_next_tick += 100

		car_frame = (car_frame + 1) % 4

	
	if pygame.time.get_ticks() > enemy_next_tick:
		enemy_next_tick += 25
		enemy_frame = (enemy_frame + 1) % 10


	window.fill(colour)
	car.move(car_x, car_y)
	enemy.move(ene_x, ene_y)
	car.draw(car_frame)
	enemy.draw(enemy_frame)
	pygame.display.update()