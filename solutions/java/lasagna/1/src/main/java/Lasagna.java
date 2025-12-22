public class Lasagna {
    public int expectedMinutesInOven(){
        return 40;
    }
    public int remainingMinutesInOven(int x){
        return 40 - x;
    }
    public int preparationTimeInMinutes(int x){
        return 2*x;
    }

    public int totalTimeInMinutes(int layers, int minutes){
        return 2*layers + minutes;
    }
}
