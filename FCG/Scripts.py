# Checks if player is inside obj
def collision(player, obj, x_add = 0, y_add = 0):
    x_check = False
    y_check = False

    # Check for mutual X
    if (player.x + x_add < obj.x + obj.width
       and player.x + x_add + player.size > obj.x):
        x_check = True

    # Check for mutual Y
    if (player.y + y_add < obj.y + obj.height
       and player.y + y_add + player.size > obj.y):
        y_check = True

    return x_check and y_check

# Checks for collision with any object from list
def collision_all(player, obj_list, x_add = 0, y_add = 0):
    for other in obj_list:
        if collision(player, other, x_add, y_add):
            return True
    return False
