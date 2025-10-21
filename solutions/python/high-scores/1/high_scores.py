class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1] if len(self.scores) != 0 else None

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse = True)[:3]