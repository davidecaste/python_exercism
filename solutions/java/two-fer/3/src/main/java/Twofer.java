public class Twofer {
    public String twofer(String name) {
        return "One for " + (name == null || "".equals(name) ? "you" : name) + ", one for me.";
    }
}
