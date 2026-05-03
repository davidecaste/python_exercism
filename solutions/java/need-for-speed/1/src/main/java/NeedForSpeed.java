class NeedForSpeed {
    private int speed;
    private int battery = 100;
    private int batteryDrain;
    private int kilometers = 0;
    
    NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
    }

    public boolean batteryDrained() {
        return this.battery < this.batteryDrain;
    }

    public int distanceDriven() {
        return this.kilometers;
    }

    public void drive() {
        if (!batteryDrained()){
            this.kilometers += this.speed;
            this.battery -= this.batteryDrain;
        }
    }

    public static NeedForSpeed nitro() {
        return new NeedForSpeed(50, 4);
    }

    public int maxDistance() {
        return this.speed * (this.battery/this.batteryDrain);
    }
}

class RaceTrack {
    private int distance;
    RaceTrack(int distance) {
        this.distance = distance;
    }

    public boolean canFinishRace(NeedForSpeed car) {
        return car.maxDistance() >= this.distance;
    }
}
