# Hier muss einmal komplett in x und in y Richtung getestet werden. Nicht pro Sprite.
class SimpleCollider():
    def collide_with_wall(self, sprite1, spritegroup):
        sprite1.rect.x = sprite1.pos.x
        for sprite2 in spritegroup:
            self.collide_with_wall_dir("x", sprite1, sprite2)
        sprite1.rect.y = sprite1.pos.y
        for sprite2 in spritegroup:
            self.collide_with_wall_dir("y", sprite1, sprite2)

    def collide_with_wall_dir(self, dir, sprite1, sprite2):
        if dir == "x":
            if sprite1.rect.colliderect(sprite2.rect):
                if sprite2.solid == True:
                    if sprite1.vel.x >= 0:
                        sprite1.pos.x = sprite2.rect.left - sprite1.rect.width
                    if sprite1.vel.x <= 0:
                        sprite1.pos.x = sprite2.rect.right
                    sprite1.vel.x = 0
                    # sprite1.acc.x = 0
                    sprite1.rect.x = sprite1.pos.x

        if dir == "y":
            if sprite1.rect.colliderect(sprite2.rect):
                if sprite2.solid == True:
                    if sprite1.vel.y >= 0:
                        sprite1.pos.y = sprite2.rect.top - sprite1.rect.height
                    if sprite1.vel.y <= 0:
                        sprite1.pos.y = sprite2.rect.bottom
                    sprite1.vel.y = 0
                    # sprite1.acc.y = 0
                    sprite1.rect.y = sprite1.pos.y
