from dino_runner.utils.constants import BIRD

class bird:
    def __init__(self) -> None:
        pass
    def fly (self):
        
        self.image = BIRD[0] if self.index < 5 else BIRD[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1
