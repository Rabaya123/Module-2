# Milestone-1

For the jpeg included in this repo, it's a maze for n = 20  (20 x 20 array)

#Milestone-2

For milestone 2 I worked with my friend

Analyzing the email sent we determined the motor controls to work in conjunction with python as follows:

            [255][0][0][255] going left
            [0][255][255][0] going right
            [0][255][0][255] going forward
            
The following pseudo code was made to set up milestone 2:

facing = down
currentx = 0
currenty = 0

if position,x > currentx  (going right)
    if facing = down 
            [255][0][0][255] (turning left)
            facing = right
    if facing = left 
            [0][255][0][255] (forward)
    if facing = right
            [255][0][255][0] (reverse)
    if facing = up
            [0][255][255][0] (turning right)
            facing = right

if position,x <currentx  (going left)
    if facing = down 
        [0][255][255][0] (turn right)
        facing = left 

    if facing = LEFT
        [255][0][255][0] (reverse)

    if facing = right 
        [0][255][0][255] (forward)

    if facing = up 
        [255][0][0][255] (turning left)
        facing = left 

if position,y > currenty  (going down)
    if facing = down 
            [0][255][0][255] (forward)
    if facing = left 
            [255][0][0][255] (turning left)
            facing = down
    if facing = right
            [0][255][255][0] (turn right)
            facing = down
    if facing = up
            [255][0][255][0] (reverse)
            
if position,y < currenty  (going up)
    if facing = down 
            [255][0][255][0] (reverse)
    if facing = left 
            [0][255][255][0] (turn right)
            facing up
    if facing = right
            [255][0][0][255] (turning left)
            facing = up
    if facing = up
            [0][255][0][255] (forward)
