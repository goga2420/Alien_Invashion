class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit #todo rename
        self.score = 0
        self.level = 1

    def check_high_score(self, sb):
        if self.score > self.high_score:
            self.high_score = self.score

            filename = 'historical_score.txt'
            with open(filename, 'w') as file_object:
                file_object.write(str(self.high_score))
            sb.prep_high_score()

    def read_high_score(self):
        with open('historical_score.txt') as file_object:
            highest_score = file_object.read()
            return int(highest_score)
