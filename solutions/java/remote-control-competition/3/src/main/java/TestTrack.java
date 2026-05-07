import java.util.List;

public class TestTrack {

    public static void race(RemoteControlCar car) {
        car.drive();
    }

    public static List<ProductionRemoteControlCar> getRankedCars(List<ProductionRemoteControlCar> cars) {
        for (int i = 0; i < cars.size() - 1; i++) {
            for (int j = 0; j < cars.size() - 1 - i; j++) {
                ProductionRemoteControlCar current = cars.get(j);
                ProductionRemoteControlCar next = cars.get(j + 1);
                if (current.compareTo(next) > 0) {
                    cars.set(j, next);
                    cars.set(j + 1, current);
                }
            }
        }
        return cars;
    }
}
