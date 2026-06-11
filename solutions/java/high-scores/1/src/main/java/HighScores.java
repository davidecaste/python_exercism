import java.util.List;
import java.util.ArrayList;

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

        int best = this.scores.get(0);
        for(int score : scores){
            if (score > best){
                best = score;
            }
        }
        return best;
    }

    List<Integer> personalTopThree() {
        List<Integer> topThree = new ArrayList<>();

        for(int score : scores){
            topThree.add(score);
            topThree.sort((a,b) -> (b - a));

            if(topThree.size() > 3){
                topThree.remove(topThree.size() - 1);
            }
        }

        return topThree;
    }

    

}
