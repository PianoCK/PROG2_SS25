import pygame as pg
vec = pg.Vector2

class Collider:

    def __init__(self):
        self.contact_normal = vec(0, 0)
        self.contact_point = vec(0, 0)
        self.contact_time = 0
        self.t_hit_near = 0
        self.t_hit_far = 0

    '''
        Collision Point and Rect vs Rect
    '''

    def PointVsRect(self, point, rect):
        # Test if a point is colliding with a rect
        # returns True or False
        return point.x >= rect.x and point.y >= rect.y and point.x < rect.x + rect.width and point.y < rect.y + rect.height

    def RectVsRect(self, rect1, rect2):
        # Test if rect1 is colliding with rect2
        # returns True or False
        return rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and rect1.y < rect2.y + rect2.height and rect1.y + rect1.height > rect2.y

    '''
        Collision Detection AABB method
    '''

    def getAABBHits(self, sprite, obstacles):
        hits = []
        for obstacle in obstacles:
            if self.RectVsRect(sprite.rect, obstacle.rect):
                hits.append(obstacle)
        return hits

    def checkAABBx(self, sprite, obstacles):
        sprite.pos.x += sprite.vel.x
        sprite.rect.topleft = sprite.pos
        hits = self.getAABBHits(sprite, obstacles)
        collisions = []
        for hit in hits:
            if sprite.vel.x > 0:  # Hit moving right
                collisions.append({"contact_time": 0,
                                   "contact_normal": vec(-1, 0), "object": hit})
            elif sprite.vel.x < 0:  # Hit moving left
                collisions.append({"contact_time": 0,
                                   "contact_normal": vec(1, 0), "object": hit})
        sprite.pos.x -= sprite.vel.x
        sprite.rect.topleft = sprite.pos
        return collisions

    def checkAABBy(self, sprite, obstacles):
        sprite.pos.y += sprite.vel.y
        sprite.rect.topleft = sprite.pos
        hits = self.getAABBHits(sprite, obstacles)
        collisions = []
        for hit in hits:
            if sprite.vel.y > 0:  # Hit moving bottom
                collisions.append({"contact_time": 0,
                                   "contact_normal": vec(0, -1), "object": hit})
            elif sprite.vel.y < 0:  # Hit moving top
                collisions.append({"contact_time": 0,
                                   "contact_normal": vec(0, 1), "object": hit})
        sprite.pos.y -= sprite.vel.y
        sprite.rect.topleft = sprite.pos
        return collisions

    def collideAABB(self, sprite, obstacles):
        collisions = []
        collisions.extend(self.checkAABBx(sprite, obstacles))
        collisions.extend(self.checkAABBy(sprite, obstacles))
        return collisions

    def resolveAABB(self, sprite, collisions):
        sprite.pos += sprite.vel
        for hit in collisions:
            if hit["contact_normal"] == vec(-1, 0):  # Hit moving right
                sprite.pos.x = hit["object"].rect.left - sprite.rect.width
                sprite.vel.x = 0
            elif hit["contact_normal"] == vec(1, 0):  # Hit moving left
                sprite.pos.x = hit["object"].rect.right
                sprite.vel.x = 0
            elif hit["contact_normal"] == vec(0, -1):  # Hit moving bottom
                sprite.pos.y = hit["object"].rect.top - sprite.rect.height
                sprite.vel.y = 0
            elif hit["contact_normal"] == vec(0, 1):  # Hit moving top
                sprite.pos.y = hit["object"].rect.bottom
                sprite.vel.y = 0
            else:
                return False
        sprite.rect.topleft = sprite.pos
        return True
