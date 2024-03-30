from graphics import Canvas
# import os
# os.system('pip install Pillow')
import random
import time

canvas_size_x = 910
canvas_size_y = 480
max_meteor = 90
min_meteor = 30
size_meteor = random.randint(min_meteor, max_meteor)
location_meteor_y = random.randint(0, canvas_size_y - size_meteor)
max_speed = 35
min_speed = 15
speed_meteor = random.randint(min_speed, max_speed)
bullet_speed = 50
bullet_size_x = 60
bullet_size_y = 60
yoda_speed = 10
health = 5
score = 0
meteors = []
bullets = []

canvas = Canvas(canvas_size_x, canvas_size_y)
canvas.set_canvas_title("Save Yoda")
background = canvas.create_image_with_size(0, 0, canvas_size_x, canvas_size_y, "background.jpg")
spaceship = canvas.create_image_with_size(90, 205,70 , 70, "zyro.png")
yoda = canvas.create_image_with_size(20, 218 , 55, 55, "yoda.png")
table = canvas.create_text(800 ,18, "Health :"+str(health))
canvas.set_font(table, "Courier", 20)
canvas.set_color(table, "red")
score_table = canvas.create_text(800 ,430, "Score :"+str(score))
canvas.set_font(score_table, "Courier", 20)
canvas.set_color(score_table, "red")

 
def create_table(health):
    table = canvas.create_text(800,18, "Health :"+str(health))
    canvas.set_font(table, "Courier", 20)
    canvas.set_color(table, "red")
    return table

def create_score_table(score):
    score_table = canvas.create_text(800 ,440, "Score :"+str(score))
    canvas.set_font(score_table, "Courier", 20)
    canvas.set_color(score_table, "red")
    return score_table

def create_meteor():
    meteor = canvas.create_image_with_size(910-size_meteor, location_meteor_y, size_meteor, size_meteor, "meteor.png")
    meteors.append(meteor)
    return meteor

def create_bullet():
    bullet = canvas.create_image_with_size(110, mouse_y-45, bullet_size_x, bullet_size_y, "bullet.png")
    bullets.append(bullet)
    return bullet

def check_collisions_yoda(canvas, yoda, background, spaceship, health, table, score, score_table): 
    yoda_coords = canvas.coords(yoda)
    yoda_x_left = yoda_coords[0]
    yoda_y_top = yoda_coords[1]    
    colliding_list = canvas.find_overlapping(yoda_x_left+10,yoda_y_top+10,yoda_x_left+40,yoda_y_top+40)
    for collider in colliding_list:
        if collider != background and collider != yoda:
            canvas.delete(yoda)
            time.sleep(1.5)
            canvas.delete_all()
            background = canvas.create_image_with_size(0, 0, canvas_size_x, canvas_size_y, "background.jpg")
            game_over = canvas.create_text(450, 200,'Game Over')
            canvas.set_font(game_over, "Courier", 50)
            canvas.set_color(game_over, "red")
            show_score = canvas.create_text(460, 250, 'Your Score :'+str(score))
            canvas.set_font(show_score, "Courier", 25)
            canvas.set_color(show_score, "red")
            canvas.wait_for_click() 
            canvas.delete(game_over)
            canvas.delete(show_score) 
            canvas.delete(game_over)
            spaceship = canvas.create_image_with_size(90, 205,70 , 70, "zyro.png")
            yoda = canvas.create_image_with_size(20, 218 , 55, 55, "yoda.png")
            health = 5
            score = 0
            score_table = create_score_table(score)
            table = canvas.create_text(800,18, "Health :"+str(health))
            canvas.set_font(table, "Courier", 20)
            canvas.set_color(table, "red")
    return background, spaceship, yoda, health, table, score, score_table

def check_collisions_spaceship(canvas, background, spaceship, yoda, health, table, score, score_table):
    spaceship_coords = canvas.coords(spaceship)
    spaceship_x_left = spaceship_coords[0]
    spaceship_y_top = spaceship_coords[1]
    colliding_list = canvas.find_overlapping(spaceship_x_left+10,spaceship_y_top+10,spaceship_x_left+50,spaceship_y_top+50)
    for collider in colliding_list:
        if collider != background and collider != spaceship:
            canvas.delete(collider)
            health -= 1
            canvas.delete(table)            
            table = create_table(health)             
            if health == 0:
                canvas.delete(table)            
                table = create_table("0")
                time.sleep(1.5)
                canvas.delete_all()
                background = canvas.create_image_with_size(0, 0, canvas_size_x, canvas_size_y, "background.jpg")
                game_over = canvas.create_text(450, 200,'Game Over')
                canvas.set_font(game_over, "Courier", 50)
                canvas.set_color(game_over, "red")
                show_score = canvas.create_text(460, 250, 'Your Score :'+str(score))
                canvas.set_font(show_score, "Courier", 25)
                canvas.set_color(show_score, "red")
                canvas.wait_for_click() 
                canvas.delete(game_over)
                canvas.delete(show_score)
                spaceship = canvas.create_image_with_size(90, 205,70 , 70, "zyro.png")
                yoda = canvas.create_image_with_size(20, 218 , 55, 55, "yoda.png")
                health = 5 
                score = 0
                score_table = create_score_table(score)
                table = canvas.create_text(800,18, "Health :"+str(health))
                canvas.set_font(table, "Courier", 20)
                canvas.set_color(table, "red")                    
    return background, spaceship, yoda, health, table, score, score_table

def check_collisions_bullet(bullet, score, score_table):
    if len(canvas.coords(bullet))> 0:
        bullet_coords = canvas.coords(bullet)
        bullet_x_left = bullet_coords[0]
        bullet_y_top = bullet_coords[1]
        colliding_list = canvas.find_overlapping(bullet_x_left,bullet_y_top,bullet_x_left+35,bullet_y_top+35)
        for collider in colliding_list:
            if collider != background and collider != bullet and collider != table and collider != score_table:
                canvas.delete(collider)
                canvas.delete(bullet)
                canvas.delete(score_table)
                score += 5
                score_table = create_score_table(score)
    return score, score_table

canvas.wait_for_click()

while True:
    
    if canvas.get_top_y(yoda) < 5 or canvas.get_top_y(yoda) > 420:
        yoda_speed = - yoda_speed       
    canvas.move(yoda, 0, yoda_speed)
         
    if  canvas.get_top_y(yoda) >= 420 or canvas.get_top_y(yoda) <= 5 :
        for i in range(4):
            size_meteor = random.randint(min_meteor, max_meteor)
            location_meteor_y = random.randint(0, canvas_size_y - size_meteor)
            speed_meteor = random.randint(min_speed, max_speed)
            meteor = create_meteor()            
        
    if len(meteors) == 0:
        size_meteor = random.randint(min_meteor, max_meteor)
        location_meteor_y = random.randint(0, canvas_size_y - size_meteor)
        speed_meteor = random.randint(min_speed, max_speed)
        meteor = create_meteor()         

    mouse_y = canvas.get_mouse_y()
    y = min(max(mouse_y -50,0),canvas_size_y-70)    
    canvas.moveto(spaceship, 90, y) 
    
    for i in range(len(meteors)):
        canvas.move(meteors[i], -speed_meteor, 0)
             
    clicks = canvas.get_new_mouse_clicks()    
    if clicks:
        bullet = create_bullet() 
        
    if int(len(bullets)) > 0:
        for bullet in bullets:
            canvas.move(bullet, bullet_speed, 0)
            score, score_table = check_collisions_bullet(bullet, score, score_table)
          
    background, spaceship, yoda, health, table, score, score_table = check_collisions_yoda(canvas, yoda, background, spaceship, health, table, score, score_table)
    background, spaceship, yoda, health, table, score, score_table = check_collisions_spaceship(canvas, background, spaceship, yoda, health, table, score, score_table)    
    
    time.sleep(0.06)
    canvas.update()
    
canvas.mainloop()