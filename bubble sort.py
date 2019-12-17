import pygame
import random
pygame.init()
width = 400
height = 200
win = pygame.display.set_mode((400,height))
mylist =[]
for i in range(0,200):
    mylist.append(random.randint(1,201))
random.shuffle(mylist)
print(mylist)
#initializing lines
for j in range(len(mylist)):
    pygame.draw.line(win, (255, 255, 255), (j*2, height), (j*2, height - mylist[j]))

# Bubble Sort
for k in range(0,len(mylist)):
    for l in range(len(mylist)-k-1):
        if mylist[l] > mylist[l+1]:

            mylist[l],mylist[l+1] = mylist[l+1],mylist[l]
            pygame.time.delay(2)
            pygame.draw.line(win, (0, 0, 0), (l * 2, 0), (l * 2, height))
            pygame.draw.line(win, (255, 255, 255), (l * 2, height), (l * 2, height - mylist[l]))
            pygame.time.delay(5)
            pygame.draw.line(win, (0, 0, 0), ((l + 1) * 2, 0), ((l + 1) * 2, height))
            pygame.draw.line(win, (255, 255, 255), ((l + 1) * 2, height), ((l + 1) * 2, height - mylist[l + 1]))
            pygame.time.delay(2)
            pygame.display.update()

print(mylist)



