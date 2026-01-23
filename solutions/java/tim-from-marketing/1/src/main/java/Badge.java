class Badge {
    public String print(Integer id, String name, String department) {
        String snd = name + " - ";
        String trd = (department == null) ? "OWNER" : department.toUpperCase();
        String fst = (id == null) ? "" : "[" + id + "] - ";
        return fst + snd + trd;
    }
}