import java.util.Map;
import java.util.HashMap;

public class DialingCodes {
    private Map<Integer, String> codes;

    public DialingCodes(){
        this.codes = new HashMap<>();
    }
    
    public Map<Integer, String> getCodes() {
        return this.codes;
    }

    public void setDialingCode(Integer code, String country) {
        this.codes.put(code, country);
    }

    public String getCountry(Integer code) {
        return this.codes.get(code);
    }

    public void addNewDialingCode(Integer code, String country) {
        if (!this.codes.containsKey(code) && !this.codes.containsValue(country)) {
            this.codes.put(code, country);    
        }
        return;
    }

    public Integer findDialingCode(String country) {
        for (Map.Entry<Integer, String> entry : this.codes.entrySet()) {
            if (entry.getValue().equals(country)) {
                return entry.getKey();
            }
        }
    return null;
    }

    public void updateCountryDialingCode(Integer code, String country) {
        Integer existingCode = null;

        for (Map.Entry<Integer, String> entry : this.codes.entrySet()) {
            if (entry.getValue().equals(country)) {
                existingCode = entry.getKey();
                break;
            }
        }

        if (existingCode == null) {
            return; 
        }

        this.codes.remove(existingCode);
        this.codes.put(code, country);
    }
}
