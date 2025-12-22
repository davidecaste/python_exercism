public class Lasagna {
    private static int MINUTESINOVEN = 40;
    private static int MINUTESFORLAYER = 2;

    public int expectedMinutesInOven(){
        return MINUTESINOVEN;
    }
    public int remainingMinutesInOven(int x){
        return expectedMinutesInOven() - x;
    }
    public int preparationTimeInMinutes(int x){
        return MINUTESFORLAYER*x;
    }

    public int totalTimeInMinutes(int layers, int minutes){
        return preparationTimeInMinutes(layers) + minutes;
    }
}
