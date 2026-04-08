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
        if (identifier == null){
            return null;
        }
        char[] asArray = identifier.toCharArray();
        StringBuilder builder = new StringBuilder();
        boolean toCapitalize = false; //see if the next char is to capitalize

        for (char c : asArray) {
            if(Character.isLetter(c)){
                builder.append(toCapitalize ? Character.toUpperCase(c) : c);
            } else if (Character.isWhitespace(c)){
                builder.append('_');
            } else if (trans_leet.containsKey(c)){
                builder.append(trans_leet.get(c));
            }
            toCapitalize = c == '-';
        }
        return builder.toString();
    }
}