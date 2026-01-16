public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        double prod = 0.0;
        if (1 <= speed && speed <= 4){
            prod = 1.0 * speed * 221;
        }
        if (5 <= speed && speed <= 8){
            prod = 0.9 * speed * 221;
        }
        if (speed == 9){
            prod = 0.8 * speed * 221;
        }
        if (speed == 10){
            prod = 0.77 * speed * 221;
        }
        return prod;
    }

    public int workingItemsPerMinute(int speed) {
        return (int) productionRatePerHour(speed) / 60;
    }
}
