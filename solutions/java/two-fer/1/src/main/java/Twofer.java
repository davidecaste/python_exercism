public class Twofer {
    public String twofer(String name) {
        String forWho = ("".equals(name) || name == null) ? "you" : name;
        return "One for " + forWho + ", one for me.";
    }
}
