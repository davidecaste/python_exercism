public enum LogLevel {
    TRACE("TRC", 1),
    DEBUG("DBG", 2),
    INFO("INF", 4),
    WARNING("WRN", 5),
    ERROR("ERR", 6),
    FATAL("FTL", 42),
    UNKNOWN("", 0);

    private String abbrv;
    private int code;
    LogLevel(String abbrv, int code) {
        this.abbrv = abbrv;
        this.code = code;
    }
    
    public String getAbbrv(){
        return this.abbrv;
    }


    public int getCode(){
        return this.code;
    }
    
    static LogLevel fromAbbrv(String abbrv) {
        for (LogLevel level : values()) {
            if (level.abbrv.equals(abbrv)) {
                return level;
            }
        }
        return UNKNOWN;
    }
}
