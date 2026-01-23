public class JedliksToyCar {
    private Integer meters = 0;
    private Integer battery = 100;
    
    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + this.meters + " meters";
    }

    public String batteryDisplay() {
        if (this.battery == 0){
            return "Battery empty";
        }
        return "Battery at " + this.battery + "%";
    }

    public void drive() {
        if (this.battery != 0){
            this.meters += 20;
            this.battery -= 1;   
        }
    }
}
