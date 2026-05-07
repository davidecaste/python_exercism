class ProductionRemoteControlCar implements RemoteControlCar, Comparable<ProductionRemoteControlCar> {

    private int distance = 0;
    private int victories = 0;
    
    public void drive() {
        this.distance += 10;
    }

    public int getDistanceTravelled() {
        return this.distance;
    }

    public int getNumberOfVictories() {
        return this.victories;
    }

    public void setNumberOfVictories(int numberOfVictories) {
        this.victories = numberOfVictories;
    }

    public int compareTo(ProductionRemoteControlCar other) {
        if (other == null) {
            throw new NullPointerException("Cannot compare with null");
        }

        return Integer.compare(other.victories, this.victories);
    }
}
