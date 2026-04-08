import java.util.Map;

class SqueakyClean {
    
    private static final Map<Character, Character> trans_leet = Map.of(
        '0', 'o',
        '1', 'l',
        '3', 'e',
        '4', 'a',
        '7', 't'
    );
    
    static String clean(String identifier) {
        Boolean[] toCapitalize = {false};
        
        return (identifier == null) ? null :
            identifier.chars()
                .mapToObj(c -> (char) c)
                .map(c -> {
                    
                    if (toCapitalize[0] && Character.isLetter(c)) {
                        c = Character.toUpperCase(c);
                    }

                    toCapitalize[0] = c == '-';
                
                    return trans(c);
                })
                .filter(c -> c!= null)
                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                .toString();
    }       

    private static Character trans(Character c){
        if (Character.isLetter(c)){
            return c;
        } 
        if (Character.isWhitespace(c)){
            return '_';
        }
        return trans_leet.getOrDefault(c, null);
    }
}
