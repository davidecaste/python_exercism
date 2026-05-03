
import java.util.Arrays;

class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = Arrays.copyOf(birdsPerDay, birdsPerDay.length);
    }

    public int[] getLastWeek() {
        return Arrays.copyOf(birdsPerDay, birdsPerDay.length);
    }

    public int getToday() {
        return birdsPerDay[birdsPerDay.length - 1];
    }

    public void incrementTodaysCount() {
        birdsPerDay[birdsPerDay.length - 1] += 1;
    }

    public boolean hasDayWithoutBirds() {
        return Arrays.stream(birdsPerDay).anyMatch(d -> d == 0);
    }

    public int getBusyDays() {
        return (int) Arrays.stream(birdsPerDay)
            .filter(d -> d >= 5)
            .count();
    }
    
    public int getCountForFirstDays(int numberOfDays) {
        int sum = 0;
        int limit = Math.min(numberOfDays, birdsPerDay.length);
        for (int i = 0; i < limit; i++){
            sum += birdsPerDay[i];
        }
        return sum;
    }
}
