public class LogLine {
    private String logLine;  

    public LogLine(String logLine) {
        this.logLine = logLine;
    }

    LogLevel getLogLevel() {
        String abbrv =
                logLine.substring(1, logLine.indexOf("]"));
        return LogLevel.fromAbbrv(abbrv);
    }

    public String getOutputForShortLog() {
        String abbr = logLine.substring(1, logLine.indexOf("]"));
        String message = logLine.split(":", 2)[1].trim();
        LogLevel level = LogLevel.fromAbbrv(abbr);
        return level.getCode() + ":" + message;
    }
}
