import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;

class HighScores {
    private List<Integer> scores;

    public HighScores(List<Integer> highScores) {
        this.scores = highScores;
    }

    List<Integer> scores() {
        return this.scores;
    }

    Integer latest() {
        int length = this.scores.size();
        return this.scores.get(length - 1);
    }

    Integer personalBest() {
        if (this.scores.isEmpty()){
            return null;
        }
        return personalTopThree().get(0);
    }

    List<Integer> personalTopThree() {
        return scores.stream()
                .sorted(Comparator.reverseOrder())
                .limit(3)
                .toList();
    }
}
