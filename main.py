import wrap,random
#переменные
x=200
y=200
random1=random.randint(50,500)

#окно игры
wrap.world.create_world(400,900,200,200)
wrap.world.set_back_color(0,0,255)

#пакмен
wrap.sprite.add("pacman",x,y,"player1")
wrap.sprite.set_size_percent(0,random1,random1)