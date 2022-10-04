import pygame


class Debug:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.display_surf = pygame.display.get_surface()
        self.debug_surf = None
        self.debug_rect = None

    def show_debug(self, *i, y=10, x=10):
        info = ' '.join(x.__str__() for x in i)

        self.debug_surf = self.font.render(info, True, 'Black')
        self.debug_rect = self.debug_surf.get_rect(topleft=(x, y))

        self.display_surf.blit(self.debug_surf, self.debug_rect)
